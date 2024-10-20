import time
import serial

address = "/dev/ttyACM0"
recipient = "+1234567890"
message = "Hello, World!"
baudrate = 460800
timeout = 0

phone = serial.Serial(address, baudrate, timeout)
try:
    time.sleep(0.5)
    phone.write(b'ATZ\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGF=1\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
    time.sleep(0.5)
    phone.write(message.encode() + b"\r")
    time.sleep(0.5)
    phone.write(bytes([26]))
    time.sleep(0.5)
finally:
    phone.close()