import cv2
import mediapipe as mp

from gesture_detector import GestureDetector


# -----------------------------
# MediaPipe setup
# -----------------------------

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


# Gesture detector object
gesture_detector = GestureDetector()


# -----------------------------
# Camera setup
# -----------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found")
    exit()


# -----------------------------
# Main loop
# -----------------------------

while True:

    success, frame = cap.read()

    if not success:
        break


    # Mirror image
    frame = cv2.flip(frame, 1)


    # Convert BGR to RGB
    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # Detect hand
    results = hands.process(rgb)


    command = "NONE"


    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:


            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )


            # Get landmarks list
            landmarks = hand_landmarks.landmark


            # Detect gesture
            command = gesture_detector.detect(
                landmarks
            )


            # Display command
            cv2.putText(
                frame,
                "Command: " + command,
                (30,60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (0,255,0),
                3
            )


            # Display finger coordinates (debug)
            cv2.putText(
                frame,
                "Hand Detected",
                (30,110),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255,0,0),
                2
            )


    else:

        cv2.putText(
            frame,
            "No Hand",
            (30,60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (0,0,255),
            3
        )


    # Show camera
    cv2.imshow(
        "Gesture Controller",
        frame
    )


    # Quit with q
    if cv2.waitKey(1) & 0xff == ord('q'):
        break



# Cleanup
cap.release()
cv2.destroyAllWindows()
hands.close()