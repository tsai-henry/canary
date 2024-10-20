import serial
import time

serial_port = '/dev/cu.usbmodem1101'
baud_rate = 9600
output_file = '../sensor_data/hub.txt'

diff = -100

def capture_serial_data():
    try:
        with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8').strip()  # get data
                    data = int(data) + diff
                    print(f"Received: {data}") 
                    
                    with open(output_file, 'w') as file:
                        file.write(f"{data},0") #overwrite first line
                time.sleep(1)

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")
        
if __name__ == "__main__":
    capture_serial_data()
