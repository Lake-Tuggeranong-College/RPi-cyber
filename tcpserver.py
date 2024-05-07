import socket

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")

        if message.lower().strip() == "quit":
            break  # Terminate the server if the client sends "quit"

        # Process the command and generate a response
        response = f"Your command was: {message.upper()}"

        client_socket.send(response.encode())
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    server_program()
