import asyncio
import websockets
import binascii
import json

# Sample ISO 8583 message (hex string, simplified for demo)
# MTI: 0100 (preauth)
# Bitmap: 0xE000000000000000 (fields 2, 4, 49 set)
# Field 2: Card Reference ID (16 digits, LLVAR)
# Field 4: Amount (12 digits)
# Field 49: Currency (3 digits)
# Field 111: Transaction Description (2 chars, demo)
#
# For this demo, let's set:
#   Card Reference ID: '1234567890123456'
#   Amount: '000000010000' (100.00)
#   Currency: '840' (USD)
#   Transaction Description: 'PP' (Person to Person)

# Build the message step by step
mti = '0100'
bitmap = 'E000000000000000'  # fields 2, 4, 49, 111 (bits 2, 4, 49, 111)

# Field 2: LLVAR (16 digits)
field2 = '16' + '1234567890123456'
# Field 4: 12 digits
field4 = '000000010000'
# Field 49: 3 digits
field49 = '840'
# Field 111: 2 chars (demo)
field111 = 'PP'

# Concatenate all fields in order
sample_msg = mti + bitmap + field2 + field4 + field49 + field111

async def test_client():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        print(f'Sending sample ISO8583 message: {sample_msg}')
        await websocket.send(sample_msg)
        response = await websocket.recv()
        print('Received response:')
        print(json.dumps(json.loads(response), indent=2))

if __name__ == '__main__':
    asyncio.run(test_client())
