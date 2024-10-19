import socket

# Create a Bluetooth socket using RFCOMM protocol
server_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Bind the socket to an address and port
# The empty string "" means it will bind to the local Bluetooth adapter
port = 1  # RFCOMM port (1 is commonly used for SPP)
server_sock.bind(("", port))
server_sock.listen(1)

print("Waiting for a connection on RFCOMM channel 1...")

# Accept a connection from the client
client_sock, client_info = server_sock.accept()
print(f"Accepted connection from {client_info}")

# Receive data from the client
try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")
except OSError:
    print("Connection closed")

# Close the sockets
client_sock.close()
server_sock.close()