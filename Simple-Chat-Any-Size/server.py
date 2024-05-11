from socket import *

try:
    host = "127.0.0.1"
    port = 5000
    server_socket = socket(AF_INET, SOCK_STREAM)

    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server listening on {}:{}".format(host, port))
    client_socket, client_address = server_socket.accept()
    print("Connection to: ", client_address[0])

    while True:
        recv_data = b""
        while True:
            chunk = client_socket.recv(4096)
            if not chunk:
                break
            recv_data += chunk

        recv_data = recv_data.decode("utf-8")

        if not recv_data:
            break

        if recv_data.lower() == 'exit':
            break

        print(f"Client: {recv_data}")

        sent_data = input("Server: ")
        if sent_data.lower() == 'exit':
            client_socket.send(sent_data.encode("utf-8"))
            break

        client_socket.send(sent_data.encode("utf-8"))

    server_socket.close()

except error:
    print(error)
except KeyboardInterrupt:
    print("\n\nServer Stopped")
