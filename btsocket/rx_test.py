from dotenv import load_dotenv
import os
import asyncio
from bleak import BleakClient

load_dotenv()

# Replace with the MAC address of the BLE peripheral/server
server_address = os.getenv("NIK_MAC")

# UUID of the characteristic to receive data from (notify characteristic)
CHARACTERISTIC_UUID = os.getenv("NIK_UUID")  # Replace with the actual UUID

# Define the callback function to handle received data
def notification_handler(sender, data):
    print(f"Received from {sender}: {data.decode()}")

async def receive_data():
    async with BleakClient(server_address) as client:
        # Enable notifications on the characteristic
        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        # Keep listening (for demonstration, we stop after 30 seconds)
        await asyncio.sleep(30)
        await client.stop_notify(CHARACTERISTIC_UUID)

# Start the RX (receive)
asyncio.run(receive_data())
