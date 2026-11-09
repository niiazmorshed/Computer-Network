import socket

HOST = '0.0.0.0'
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on port {PORT}...")

while True:
    conn, addr = server.accept()
    with conn:
        data = conn.recv(1024).decode()
        if data:
            print(f"[CONNECTION] Client IP: {addr[0]}, Device Name: {data}")
