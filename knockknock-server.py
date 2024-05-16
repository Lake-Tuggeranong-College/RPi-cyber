import socket

def server_program():
    host = "192.168.1.43"
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

        if message.lower().strip() == "ahsoka":
            # Correct Code
            response = f"\n\nSome things are not what they seem.\n{message}, assume nothing. \nA K2 droid has infiltrated the base, pretending to a rebel terminal. \nFind it. \nThe empire installed a backdoor on their K2 droids \nHNFGONLNHYQWWVSSIBIF4VRRHBHVCXJ2HFIEQZ3TIBIF6IZFIBZDKNCZIBIF6JRRHBHWWZDAIBJHIOKJIA3U4PRFHYRVEN2A.....\n\n"
        else:
            response = f"Name provided: {message.upper()}. I was expecting Lady Tano. Try again."

        client_socket.send(response.encode())
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    server_program()
