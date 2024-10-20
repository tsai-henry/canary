import socket

esp8266_ip = "192.168.4.1"  # default ip
esp8266_port = 8080 

# tcp socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(10)  # 10s timeout

diff = -200

try:
    print("Attempting to connect to ESP8266...")
    client_socket.connect((esp8266_ip, esp8266_port))
    print("Connected to ESP8266!")

    while True:
        try:
            data = client_socket.recv(1024).decode().strip()
            data = int(data) + diff
            print("Received:", data)
            with open("../sensor_data/child1.txt", 'w') as f:
                f.write(f"{data},1")
        except KeyboardInterrupt:
            break
        except:
            print("Waiting for data stream...")

finally:
    client_socket.close()
    print("\nConnection closed.")

