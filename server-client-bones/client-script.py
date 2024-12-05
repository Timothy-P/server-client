import socket, time


# Funcs
def serverConnect(host, port):
    try:
        client_socket.connect((host, port))
    except TimeoutError:
        print("Host didn't respond or connection failed. Check with host for more information.")
        quit()
    except:
        print("Unexpected issue occured.")
        quit()
    

# File stuff.
file = open("client-logs.txt", "a")
file.write(f"\n{time.asctime(time.localtime())}: client-script launched.")

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Input the host's IP: ")
port = int(input("Input the server's port: "))
# Connect to the server (server IP and port)
serverConnect(host, port)
file.write(f"\n{time.asctime(time.localtime())}: Connected to host!")
# Send data
while True:
    try:
        message = input("Input message: ")
        client_socket.send(message.encode())
        file.write(f"\n{time.asctime(time.localtime())}: Message sent; \"{message}\"")
    except KeyboardInterrupt:
        print("KeyboardInterrupt triggered.")
        message = "<<< Client used KeyboardInterrupt. Port is closing. >>>"
        client_socket.send(message.encode())
        file.write(f"\n{time.asctime(time.localtime())}: Client closing using keyboardinterrupt.")
        file.write(f"\n{time.asctime(time.localtime())}: Disconnected from host.")
    except ConnectionRefusedError:
        print("Host refused the connection.")
        file.write(f"\n{time.asctime(time.localtime())}: Host refused connection.")
client_socket.close()
file.write(f"\n{time.asctime(time.localtime())}: Socket closed.")
file.close()
quit()