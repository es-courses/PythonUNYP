
from socket import socket, AF_INET, SOCK_STREAM

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8001))

server_socket.listen()
print("Server started on port 8001")

while True:
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    msg_bytes = conn.recv(1024)
    msg = msg_bytes.decode('utf-8')

    msg = "Hello " + msg
    msg_bytes = msg.encode()

    conn.send(msg_bytes)




