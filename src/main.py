import cv2
import mediapipe as mp

from gesture_detector import GestureDetector
from airsim_controller import DroneController



# -----------------
# Initialize
# -----------------

drone = DroneController()

gesture = GestureDetector()


mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)


mp_draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)



# -----------------
# Main Loop
# -----------------

while True:


    ret, frame = cap.read()

    if not ret:
        break


    frame = cv2.flip(frame,1)


    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    results = hands.process(rgb)


    command="NONE"



    if results.multi_hand_landmarks:


        for hand in results.multi_hand_landmarks:


            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )


            command = gesture.detect(
                hand.landmark
            )


            print(command)



            # Drone control

            if command=="TAKEOFF":
                drone.takeoff()


            elif command=="LAND":
                drone.land()


            elif command=="UP":
                drone.up()


            elif command=="DOWN":
                drone.down()


            elif command=="LEFT":
                drone.left()


            elif command=="RIGHT":
                drone.right()


            elif command=="HOVER":
                drone.hover()



    cv2.putText(
        frame,
        command,
        (40,60),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (0,255,0),
        3
    )


    cv2.imshow(
        "Gesture Drone Control",
        frame
    )


    if cv2.waitKey(1)&0xff==ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
