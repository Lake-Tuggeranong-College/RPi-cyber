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
        print(f"Received name: {message}")

        if message.lower().strip() == "quit":
            break  # Terminate the server if the client sends "quit"

        if message.lower().strip() == "Ahsoka":
            # Correct Code
            response = f"Some things are not what they seem./n{message}, assume nothing. A K2 droid has infiltrated the base, pretending to a rebel terminal. Find it. The empire installed a backdoor on their K2 droids HNFGONLNHYQWWVSSIBIF4VRRHBHVCXJ2HFIEQZ3TIBIF6IZFIBZDKNCZIBIF6JRRHBHWWZDAIBJHIOKJIA3U4PRFHYRVEN2A....."
        else:
            response = f"Your name was: {message.upper()}. I was expecting Lady Tano. Try again."

        client_socket.send(response.encode())
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    server_program()
