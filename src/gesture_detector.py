class GestureDetector:


    def get_fingers(self, lm):

        fingers = []


        # Thumb
        if lm[4].x < lm[3].x:
            fingers.append(1)
        else:
            fingers.append(0)


        # Index
        if lm[8].y < lm[6].y:
            fingers.append(1)
        else:
            fingers.append(0)


        # Middle
        if lm[12].y < lm[10].y:
            fingers.append(1)
        else:
            fingers.append(0)


        # Ring
        if lm[16].y < lm[14].y:
            fingers.append(1)
        else:
            fingers.append(0)


        # Pinky
        if lm[20].y < lm[18].y:
            fingers.append(1)
        else:
            fingers.append(0)


        return fingers



    def detect(self, lm):


        thumb,index,middle,ring,pinky = self.get_fingers(lm)


        fingers=[
            thumb,
            index,
            middle,
            ring,
            pinky
        ]


        print(fingers)



        # ------------------
        # LAND
        # ------------------

        if fingers == [0,0,0,0,0]:
            return "LAND"



        # ------------------
        # HOVER
        # ------------------

        if fingers == [1,1,1,1,1]:
            return "HOVER"



        # ------------------
        # TAKEOFF
        # Victory
        # ------------------

        if fingers == [0,1,1,0,0]:
            return "TAKEOFF"



        # ------------------
        # UP
        # Index only
        # ------------------

        if fingers == [0,1,0,0,0]:
            return "UP"



        # ------------------
        # DOWN
        # Thumb only
        # ------------------

        if fingers == [1,0,0,0,0]:
            return "DOWN"



        # ------------------
        # RIGHT
        # Pinky only
        # ------------------

        if fingers == [0,0,0,0,1]:
            return "RIGHT"



        # ------------------
        # LEFT
        # Thumb + Pinky
        # ------------------

        if fingers == [1,0,0,0,1]:
            return "LEFT"



        # ------------------
        # FORWARD
        # Index + Middle + Pinky
        # 🤟
        # ------------------

        if fingers == [0,1,1,0,1]:
            return "FORWARD"



        # ------------------
        # BACKWARD
        # Middle + Ring + Pinky
        # 🤘
        # ------------------

        if fingers == [0,0,1,1,1]:
            return "BACKWARD"



        return "NONE"