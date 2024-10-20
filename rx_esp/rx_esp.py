import socket

esp8266_ip = "192.168.4.1"  # default ip
esp8266_port = 8080 

# tcp socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(10)  # 10s timeout

try:
    print("Attempting to connect to ESP8266...")
    client_socket.connect((esp8266_ip, esp8266_port))
    print("Connected to ESP8266!")

    cnt = 1000
    while cnt > 0:
        try:
            data = client_socket.recv(1024).decode()
            print("Received:", data)
        except KeyboardInterrupt:
            break
        except:
            print("Waiting for data stream...")
        cnt -= 1

finally:
    client_socket.close()
    print("Connection closed.")

