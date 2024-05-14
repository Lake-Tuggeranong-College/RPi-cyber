import socket

def send_command_to_server(command):
    host = "192.168.1.14"  # Change this to the server's hostname or IP address
    port = 1313  # Use the same port number as the server

    client_socket = socket.socket()
    client_socket.connect((host, port))  # Connect to the server

    client_socket.send(command.encode())  # Send the command to the server
    response = client_socket.recv(1024).decode()  # Receive the response

    print(f"Server response: {response}")

    client_socket.close()  # Close the connection

if __name__ == "__main__":
    user_command = input("Enter a command to send to the server: ")
    send_command_to_server(user_command)
