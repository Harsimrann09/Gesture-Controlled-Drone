import airsim
import time


client = airsim.MultirotorClient()

client.confirmConnection()

print("Connected to AirSim")


client.enableApiControl(True)

client.armDisarm(True)

print("Drone armed")


client.takeoffAsync().join()

print("Drone is flying")


time.sleep(5)


client.landAsync().join()

print("Drone landed")


client.armDisarm(False)

client.enableApiControl(False)

print("Test completed")
