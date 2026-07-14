import airsim
import time


class DroneController:


    def __init__(self):

        self.client = airsim.MultirotorClient()

        self.client.confirmConnection()

        self.client.enableApiControl(True)

        self.client.armDisarm(True)


    def takeoff(self):

        print("Taking off")

        self.client.takeoffAsync().join()



    def land(self):

        print("Landing")

        self.client.landAsync().join()



    def up(self):

        print("Moving Up")

        self.client.moveByVelocityAsync(
            0,0,-2,2
        ).join()



    def down(self):

        print("Moving Down")

        self.client.moveByVelocityAsync(
            0,0,2,2
        ).join()



    def left(self):

        print("Moving Left")

        self.client.moveByVelocityAsync(
            0,-2,0,2
        ).join()



    def right(self):

        print("Moving Right")

        self.client.moveByVelocityAsync(
            0,2,0,2
        ).join()



    def hover(self):

        print("Hover")

        self.client.hoverAsync().join()



    def stop(self):

        self.client.hoverAsync().join()
        