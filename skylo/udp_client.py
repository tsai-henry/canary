import socket
from time import sleep
from datetime import datetime

# Create a UDP client socket
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address (replace with your VM's external IP)
address = "34.19.125.150"
port = 51820
server_address = (address, port)
message = "Hello! This default message is set before the for loop."
iterations = 10
delay = 2

# Send data to the server
for i in range(iterations):
    message = f"Packet {i} sent at {datetime.now()}"
    udp_client.sendto(message.encode(), server_address)
    
    # Receive response from the server
    response, _ = udp_client.recvfrom(1024)
    print(f"Received from server: {response.decode()}")
    
    sleep(delay)
