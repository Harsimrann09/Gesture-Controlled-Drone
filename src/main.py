import cv2
import mediapipe as mp

from gesture_detector import GestureDetector
from airsim_controller import DroneController



drone = DroneController()

gesture = GestureDetector()



mp_hands = mp.solutions.hands


hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


draw = mp.solutions.drawing_utils



cap=cv2.VideoCapture(0)



last_command=""



while True:


    ret,frame=cap.read()


    if not ret:
        break



    frame=cv2.flip(frame,1)



    rgb=cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )



    result=hands.process(rgb)



    command="NONE"



    if result.multi_hand_landmarks:


        hand=result.multi_hand_landmarks[0]


        draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )


        command=gesture.detect(
            hand.landmark

        )
        print(command)





        if command != last_command:


            print(command)



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


            elif command=="FORWARD":
                drone.forward()


            elif command=="BACKWARD":
                drone.backward()


            elif command=="HOVER":
                drone.hover()



            last_command=command



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
        "Gesture AirSim Drone",
        frame
    )


    if cv2.waitKey(1)==ord('q'):
        break



cap.release()
cv2.destroyAllWindows()