import socket, time


# Funcs
def serverConnect(host, port):
    try:
        client_socket.connect((host, port))
    except TimeoutError:
        print("Host didn't respond or connection failed. Check with host for more information.")
        file.write(f"\n{time.asctime(time.localtime())}: Host didn't respond or the connection failed.")
        quit()
    except Exception as e:
        print("Unexpected issue occured.")
        file.write(f"\n{time.asctime(time.localtime())}: Unexpected issue occured. {e}")
        quit()
    

# File stuff.
file = open("client-logs.txt", "a")
file.write(f"\n{time.asctime(time.localtime())}: client-script launched.")

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Is the server on a localhost?")
question = input("[Y] or [N]: ")
if "n" in question:
    host = input("Input the host's IP: ")
elif "y" in question:
    host = "localhost"
else:
    print("Invalid answer. Try again.")
    quit()
try:
    port = int(input("Input the server's port: "))
except ValueError:
    print("Invalid input. Try again.")
    quit()
# Connect to the server (server IP and port)
serverConnect(host, port)
file.write(f"\n{time.asctime(time.localtime())}: Connected to host.")
# Send data
while True:
    try:
        data = client_socket.recv(1024)
    except socket.error as e:
        print("Socket error:", e)
        break
    except KeyboardInterrupt:
        print("KeyboardInterrupt triggered.")
        break
    if not data:
        print("Server disconnected.")
        break
    print(f"Received data: {data.decode()}")

    try:
        message = input("Input message: ")
        client_socket.send(message.encode())
        file.write(f"\n{time.asctime(time.localtime())}: Message sent; \"{message}\"")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt triggered.")
        message = "<<< Client used KeyboardInterrupt. Port is closing. >>>"
        client_socket.send(message.encode())
        file.write(f"\n{time.asctime(time.localtime())}: Client closing using keyboardinterrupt.")
        file.write(f"\n{time.asctime(time.localtime())}: Disconnected from host.")
        break
    except ConnectionRefusedError:
        print("Host refused the connection.")
        file.write(f"\n{time.asctime(time.localtime())}: Host refused connection.")
client_socket.close()
file.write(f"\n{time.asctime(time.localtime())}: Socket closed.")
file.close()
quit()
