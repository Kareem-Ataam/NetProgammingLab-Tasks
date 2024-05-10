from socket import *

host = "127.0.0.1"
port = 5000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))
print("Connected to the server.")

while True:
    sent_data = input("Client:")
    if sent_data.lower() == 'exit':
        client_socket.send(sent_data.encode("utf-8"))
        break
    client_socket.send(sent_data.encode("utf-8"))

    recv_data = b''
    while True:
        chunk = client_socket.recv(2048)
        if not chunk:
            break
        recv_data += chunk

    if recv_data.decode("utf-8").lower() == 'exit':
        break
    print("Server:", recv_data.decode("utf-8"))

client_socket.close()