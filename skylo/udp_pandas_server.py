import socket
import pandas as pd
from datetime import datetime

CHILD_IP = "1.1.1.1"
HUB_IP = "2.2.2.2"

# Create UDP server
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = "0.0.0.0"
port = 51820
server_address = (address, port)
udp_server.bind(server_address)
print(f"UDP server is listening on {server_address}")

# Create dataframe to store data
columns = ["timestamp", "source", "data"]
df = pd.DataFrame(columns=columns)

# 4. Function to save a new packet to the DataFrame
def save_packet_to_dataframe(timestamp, source, data):
    global df  # Reference the global DataFrame
    new_entry = pd.DataFrame([[timestamp, source, data]], columns=columns)
    df = pd.concat([df, new_entry], ignore_index=True)
    print(f"Saved packet from {source} at {timestamp}")

# 5. Start receiving packets in a loop
i = 0 # Random counter
try:
    while True:
        # Receive data from the client
        source = "unknown"
        data, client_address = udp_server.recvfrom(1024)  # Buffer size 1024 bytes
        decoded_data = data.decode()

        # Capture the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # if client_address[0] == CHILD_IP:
        #     source = "child"
        # elif client_address[0] == HUB_IP:
        #     source = "hub"
        
        # Remove once we have 2 IP addresses
        if i % 2 == 0:
            source = "child"
        else:
            source = "hub"

        # Save the packet to the DataFrame
        save_packet_to_dataframe(timestamp, source, decoded_data)

        # Optional: Send a confirmation response to the client
        udp_server.sendto("Packet received".encode(), client_address)
        
        i += 1

except KeyboardInterrupt:
    print("\nServer stopped by user.")

finally:
    # Optional: Save DataFrame to a CSV file on exit
    df.to_csv("udp_packets.csv", index=False)
    print("Data saved to udp_packets.csv")
