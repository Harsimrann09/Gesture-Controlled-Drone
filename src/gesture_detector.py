class GestureDetector:


    def get_fingers(self, landmarks):

        fingers = []


        # Thumb
        if landmarks[4].x < landmarks[3].x:
            fingers.append(1)
        else:
            fingers.append(0)


        # Index
        if landmarks[8].y < landmarks[6].y:
            fingers.append(1)
        else:
            fingers.append(0)


        # Middle
        if landmarks[12].y < landmarks[10].y:
            fingers.append(1)
        else:
            fingers.append(0)


        # Ring
        if landmarks[16].y < landmarks[14].y:
            fingers.append(1)
        else:
            fingers.append(0)


        # Pinky
        if landmarks[20].y < landmarks[18].y:
            fingers.append(1)
        else:
            fingers.append(0)


        return fingers



    def detect(self, landmarks):

        thumb,index,middle,ring,pinky = self.get_fingers(landmarks)



        # ------------------
        # LAND - FIST
        # ------------------
        if [thumb,index,middle,ring,pinky] == [0,0,0,0,0]:
            return "LAND"



        # ------------------
        # TAKEOFF - VICTORY
        # ------------------
        if (
            index == 1 and
            middle == 1 and
            ring == 0 and
            pinky == 0
        ):
            return "TAKEOFF"



        # ------------------
        # HOVER - OPEN PALM
        # ------------------
        if [thumb,index,middle,ring,pinky] == [1,1,1,1,1]:
            return "HOVER"



        # ------------------
        # UP - INDEX ONLY
        # ------------------
        if (
            index == 1 and
            thumb == 0 and
            middle == 0 and
            ring == 0 and
            pinky == 0
        ):
            return "UP"



        # ------------------
        # DOWN - THUMB DOWN
        # ------------------
        if (
            thumb == 1 and
            index == 0 and
            middle == 0 and
            ring == 0 and
            pinky == 0
        ):
            if landmarks[4].y > landmarks[3].y:
                return "DOWN"



        # ------------------
        # RIGHT - PINKY ONLY
        # ------------------
        if (
            pinky == 1 and
            thumb == 0 and
            index == 0 and
            middle == 0 and
            ring == 0
        ):
            return "RIGHT"



        # ------------------
        # LEFT - CALL SIGN
        # Thumb + Pinky
        # ------------------
        if (
            thumb == 1 and
            pinky == 1 and
            index == 0 and
            middle == 0 and
            ring == 0
        ):
            return "LEFT"



        return "NONE"
    