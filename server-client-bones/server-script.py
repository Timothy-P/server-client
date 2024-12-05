# You still here?
# Kinda. I'm working on this whenever I can. What class?
# Just whatever class I can. I have study hall for 7th, so I have all the time I need. Also, if you want to chat, go to chat.txt.
import socket, time, random
port = random.randint(1,12345)
# Create a socket object
file = open("server-logs.txt", "a")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file.write(f"\n{time.asctime(time.localtime())}: server-script launched.")
print(f"This machine's IP address is {socket.gethostbyname(socket.gethostname())}")
print(f"The server is being hosted on port {port}.")

# Bind the socket to a host and port
server_socket.bind(('', port))
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
    data = client_socket.recv(1024)  # 1024 bytes buffer size
    print(f"Received data: {data.decode()}")
    file.write(f"\n{time.asctime(time.localtime())}: Message received: {data}")
    if data == b"<<< Client used KeyboardInterrupt. Port is closing. >>>":
        quit()
 
# Close the client socket
client_socket.close()
file.write(f"\n{time.asctime(time.localtime())}: Socket closed.")

# Close the server socket
server_socket.close()
file.write(f"\n{time.asctime(time.localtime())}: Server closed.")