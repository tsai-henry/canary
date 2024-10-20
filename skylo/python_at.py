import time
import serial

class RaspiSerial:
    def __init__(self, address: str, 
                 baudrate: int = 460800,
                 timeout: int = 0,
                 wait_time: int = 1,
                 latitude = "37.783860",
                 longitude = "-122.402311",
                 string_encoding = 'utf-8'):
        """
        Initialize the serial connection and configure basic settings.
        
        Parameters:
        address (str): Serial port address (e.g., "/dev/ttyACM0").
        baudrate (int): Communication speed in baud (default: 460800).
        timeout (int): Timeout value for the serial connection in seconds (default: 0).
        wait_time (int): Time to wait after sending a command (default: 1 second).
        latitude
        longitude
        string_encoding
        """
        self.address = address
        self.baudrate = baudrate
        self.timeout = timeout
        self.wait_time = wait_time
        self.latitude = latitude
        self.longitude = longitude
        self.string_encoding = string_encoding
        
        # Initialize the serial connection
        self.connection = serial.Serial(address, baudrate, timeout=timeout)
        
        # Initialize the Skylo board
        self.init_skylo()

        # Define AT commands
        self.commands = {
            "fun": f'AT+cfun=1\r',
            "pos": f'AT%NTNCFG="POS","STAT","{self.latitude}","{self.longitude}","160"\r',
            "allocate": f'AT%SOCKETCMD=“ALLOCATE”,0,”UDP”,“OPEN”,“34.19.125.150”,51820"\r',
            "setopt": f'AT%SOCKETCMD="SETOPT",{self.socket},36000\r',
            "activate": f'AT%SOCKETCMD="ACTIVATE",{self.socket}\r',
            "send": f'AT%SOCKETDATA="SEND",{self.socket},13,', # Trailing comma for message
            "info": f'AT%SOCKETCMD="INFO",{self.socket}',
            "close": f'AT%SOCKETCMD="DELETE",{self.socket}'
        }

    def send_command(self, command: str):
        """
        Send a command over the serial connection after encoding to binary.
        
        Parameters:
        command (str): The command to send.
        """
        self.connection.write(command.encode(self.string_encoding))
        time.sleep(self.wait_time)

    def init_skylo(self):
        """
        Run the initialization commands for setting up Skylo to send UDP packets.
        """
        self.send_command(self.commands["fun"])
        self.send_command(self.commands["pos"])
        self.send_command(self.commands["allocate"])
        self.send_command(self.commands["setopt"])
        self.send_command(self.commands["activate"])

    def send_udp(self, message: str):
        """
        Send a UDP packet with the specified message.
        
        Parameters:
        message (str): The message to send via UDP.
        """
        # Prepare the message with the command
        command_with_message = self.commands["send"] + message.encode(self.string_encoding) + b'\r'
        self.send_command(command_with_message)

    def close(self):
        """
        Close the serial connection.
        """
        self.send_command(self.commands["close"])

# Example usage:
if __name__ == "__main__":
    # Initialize the serial connection
    raspi = RaspiSerial(address="/dev/ttyACM0")

    try:
        # Initialize Skylo settings
        raspi.init_skylo()

        # Send a UDP message
        raspi.send_udp("Hello, World!")

    finally:
        # Close the connection when done
        raspi.close()


# AT commands from Stacey:
# AT+cfun=1
# AT%NTNCFG="POS","STAT","37.783860","-122.402311","160"

# AT%SOCKETCMD=“ALLOCATE”,0,”UDP”,“OPEN”,“34.19.125.150”,51820
# AT%SOCKETCMD="SETOPT",2,36000
# AT%SOCKETCMD="ACTIVATE",2
# AT%SOCKETDATA="SEND",2,13,"48656C6C6F2C20776F726C6421"