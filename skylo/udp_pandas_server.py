import socket
import pandas as pd
from datetime import datetime

# 1. Create a UDP socket
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind the socket to all interfaces
address = "0.0.0.0"
port = 51820
server_address = (address, port)
udp_server.bind(server_address)

print(f"UDP server is listening on {server_address}")

# 3. Initialize an empty DataFrame to store packets
columns = ["timestamp", "client_address", "data"]
df = pd.DataFrame(columns=columns)

# 4. Function to save a new packet to the DataFrame
def save_packet_to_dataframe(timestamp, client_address, data):
    global df  # Reference the global DataFrame
    new_entry = pd.DataFrame([[timestamp, client_address, data]], columns=columns)
    df = pd.concat([df, new_entry], ignore_index=True)
    print(f"Saved packet from {client_address} at {timestamp}")

# 5. Start receiving packets in a loop
try:
    while True:
        # Receive data from the client
        data, client_address = udp_server.recvfrom(1024)  # Buffer size 1024 bytes
        decoded_data = data.decode()

        # Capture the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Save the packet to the DataFrame
        save_packet_to_dataframe(timestamp, client_address, decoded_data)

        # Optional: Send a confirmation response to the client
        udp_server.sendto("Packet received".encode(), client_address)

except KeyboardInterrupt:
    print("\nServer stopped by user.")

finally:
    # Optional: Save DataFrame to a CSV file on exit
    df.to_csv("udp_packets.csv", index=False)
    print("Data saved to udp_packets.csv")
