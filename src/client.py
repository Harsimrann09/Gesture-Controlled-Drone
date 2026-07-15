import socket

SERVER_IP = "10.221.29.57"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("Connected to AirSim Server")


def send_command(command):

    try:
        client.send(command.encode())
        print("Sent:", command)

    except Exception as e:
        print(e)