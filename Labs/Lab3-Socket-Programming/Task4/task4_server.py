import socket

HOST = '0.0.0.0'
PORT = 5004

def calculate_salary(hours):
    if hours <= 40:
        return hours * 200
    else:
        return 8000 + (hours - 40) * 300

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on port {PORT}...")

while True:
    conn, addr = server.accept()
    with conn:
        print(f"[CONNECTION] {addr}")
        data = conn.recv(1024).decode()
        if data:
            try:
                hours = float(data)
                salary = calculate_salary(hours)
                response = f"Salary for {hours} hours worked: Tk {salary}"
            except ValueError:
                response = "Invalid input. Please send a numeric value."
            print(f"Hours: {data} | Response: {response}")
            conn.sendall(response.encode())
