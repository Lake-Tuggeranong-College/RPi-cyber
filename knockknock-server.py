import socket

def server_program():
    host = "192.168.1.14"
    port = 1313

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        try:
                message = client_socket.recv(1024).decode()
        except:
                continue
        print(f"Received message: {message}")

        if message.lower().strip() == "quit":
            break  # Terminate the server if the client sends "quit"

        if message.lower().strip() == "code":
            # Correct Code
            response = f"Code for next step is: 1234"
        else:
            response = f"Your command was: {message.upper()}"

        client_socket.send(response.encode())
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    server_program()
