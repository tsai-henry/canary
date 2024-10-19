from dotenv import load_dotenv
import os
import asyncio
from bleak import BleakClient

load_dotenv()

server_address = os.getenv("PSJ_MAC")

# UUID of the characteristic to receive data from (notify characteristic)
CHARACTERISTIC_UUID = os.getenv("PSJ_UUID")  # Replace with the actual UUID

async def send_data():
    async with BleakClient(server_address) as client:
        message = "Hello from Client!".encode()
        await client.write_gatt_char(CHARACTERISTIC_UUID, message)
        print(f"Sent: {message.decode()}")

# Start the TX (transmission)
asyncio.run(send_data())