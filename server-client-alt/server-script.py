import socket, time, random
port = random.randint(1,12345)
# Create a socket object
file = open("server-logs.txt", "a")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file.write(f"\n{time.asctime(time.localtime())}: server-script launched.")

# Bind the socket to a host and port
print("Would you like to host the server on localhost?")
question = input("[Y] or [N]: ").lower()
if "n" in question:
    print(f"This machine's IP address is {socket.gethostbyname(socket.gethostname())}")
    server_socket.bind(('', port))
elif "y" in question:
    server_socket.bind(('localhost', port))
else:
    print("Invalid answer. Try again.")
    quit()

print(f"The server is being hosted on port {port}.")
file.write(f"\n{time.asctime(time.localtime())}: Socket bound.")

# Start listening for incoming connections
server_socket.listen(1)
file.write(f"\n{time.asctime(time.localtime())}: Listening...")
print("Server is waiting for connection...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")
file.write(f"\n{time.asctime(time.localtime())}: Connection made with {client_address} on {client_socket}")

# Receive the data
while True:
    try:
        ffff = input("Input message: ")
    except KeyboardInterrupt:
        print("\nServer used Keyboard Interrupt.")
    client_socket.send(ffff.encode())
    try:
        data = client_socket.recv(1024)  # 1024 bytes buffer size
    except KeyboardInterrupt:
        print("\nServer used Keyboard Interrupt.")
        break
    print(f"Received data: {data.decode()}")
    file.write(f"\n{time.asctime(time.localtime())}: Message received: {data}")
    if data == b"<<< Client used KeyboardInterrupt. Port is closing. >>>":
        break
 
# Close the client socket
client_socket.close()
file.write(f"\n{time.asctime(time.localtime())}: Socket closed.")

# Close the server socket
server_socket.close()
file.write(f"\n{time.asctime(time.localtime())}: Server closed.")