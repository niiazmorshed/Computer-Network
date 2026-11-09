import socket

HOST = '127.0.0.1'
PORT = 5001

device_name = socket.gethostname()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(device_name.encode())
print(f"Sent device name '{device_name}' to server.")
client.close()
