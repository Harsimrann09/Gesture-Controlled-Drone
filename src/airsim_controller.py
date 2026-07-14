import airsim



class DroneController:


    def __init__(self):

        self.client = airsim.MultirotorClient()

        self.client.confirmConnection()

        self.client.enableApiControl(True)

        self.client.armDisarm(True)

        print("AirSim Drone Connected")



    def takeoff(self):

        print("TAKEOFF")

        self.client.takeoffAsync().join()



    def land(self):

        print("LAND")

        self.client.landAsync().join()



    def up(self):

        print("UP")

        self.client.moveByVelocityAsync(
            0,0,-2,1
        )



    def down(self):

        print("DOWN")

        self.client.moveByVelocityAsync(
            0,0,2,1
        )



    def left(self):

        print("LEFT")

        self.client.moveByVelocityAsync(
            0,-2,0,1
        )



    def right(self):

        print("RIGHT")

        self.client.moveByVelocityAsync(
            0,2,0,1
        )



    def forward(self):

        print("FORWARD")

        self.client.moveByVelocityAsync(
            2,0,0,1
        )



    def backward(self):

        print("BACKWARD")

        self.client.moveByVelocityAsync(
            -2,0,0,1
        )



    def hover(self):

        print("HOVER")

        self.client.hoverAsync()