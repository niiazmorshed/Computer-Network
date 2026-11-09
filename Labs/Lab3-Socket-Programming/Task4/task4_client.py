import socket

HOST = '127.0.0.1'
PORT = 5004

hours = input("Enter the number of hours worked: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(hours.encode())
response = client.recv(1024).decode()
print(f"Server response: {response}")
client.close()
