import socket
import threading

HOST = '0.0.0.0'
PORT = 5003

def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in 'aeiou')

def get_response(vowel_count):
    if vowel_count == 0:
        return "Not enough vowels"
    elif vowel_count <= 2:
        return "Enough vowels I guess"
    else:
        return "Too many vowels"

def handle_client(conn, addr):
    with conn:
        print(f"[CONNECTION] {addr}")
        data = conn.recv(1024).decode()
        if data:
            vowels = count_vowels(data)
            print(f"[{addr}] Message: '{data}' | Vowels: {vowels}")
            response = get_response(vowels)
            conn.sendall(response.encode())
    print(f"[DISCONNECTED] {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Multi-threaded server listening on port {PORT}...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
