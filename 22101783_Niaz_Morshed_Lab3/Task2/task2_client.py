import socket

HOST = '127.0.0.1'
PORT = 5002

message = input("Enter a message to send to the server: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(message.encode())
response = client.recv(1024).decode()
print(f"Server response: {response}")
client.close()
