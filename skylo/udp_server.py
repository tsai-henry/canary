import socket

# 1. Create a UDP socket
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind the socket to all network interfaces
address = "0.0.0.0"
port = 51820
server_address = (address, port)
udp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp_server.bind(server_address)

print(f"UDP server is listening on {server_address}")

# 3. Receive and respond to data
while True:
    data, client_address = udp_server.recvfrom(1024)
    print(f"Received {data.decode()} from {client_address}")

    # Send a response
    message = "Message received".encode()
    udp_server.sendto(message, client_address)
