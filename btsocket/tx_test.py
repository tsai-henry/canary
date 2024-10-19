import socket

# Create a Bluetooth socket using RFCOMM protocol
client_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Replace with the Bluetooth MAC address of the server MacBook
server_address = ""  # Example: "A0:B1:C2:D3:E4:F5"

# RFCOMM port (must match the server port)
port = 1

# Connect to the server
print(f"Connecting to {server_address} on port {port}...")
client_sock.connect((server_address, port))

# Send a message to the server
message = "Hello from the client!"
client_sock.send(message.encode())
print(f"Sent: {message}")

# Close the socket
client_sock.close()