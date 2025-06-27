import asyncio
import websockets
import json
from typing import Dict, Any

# ISO 8583 field mapping for required fields
FIELD_MAP = {
    2: 'card_reference_id',  # Primary Account Number (Card Reference)
    4: 'amount',             # Amount, Transaction
    49: 'currency',          # Currency Code, Transaction
    111: 'transaction_description', # Transaction Description (in subfield 15)
}

# MTI to message type mapping (simplified, extend as needed)
MTI_MAP = {
    '0100': 'preauth',
    '0200': 'financial',
    '0400': 'reversal',
    '0500': 'reconciliation',
    '0420': 'settlement',
    # Add more as needed
}

def parse_bitmap(bitmap_hex: str) -> list:
    bits = bin(int(bitmap_hex, 16))[2:].zfill(64)
    present_fields = [i+1 for i, b in enumerate(bits) if b == '1']
    return present_fields

def parse_iso8583_message(msg: str) -> Dict[str, Any]:
    mti = msg[:4]
    message_type = MTI_MAP.get(mti, 'unknown')
    bitmap_hex = msg[4:20]
    present_fields = parse_bitmap(bitmap_hex)
    idx = 20
    # Check for secondary bitmap (bit 1 set)
    if present_fields and present_fields[0] == 1:
        secondary_bitmap_hex = msg[idx:idx+16]
        idx += 16
        secondary_fields = parse_bitmap(secondary_bitmap_hex)
        present_fields = present_fields[1:] + [f+64 for f in secondary_fields]
    data = {}
    # Parse fields in order of appearance in the message
    for field in present_fields:
        if field == 2:
            length = int(msg[idx:idx+2])
            idx += 2
            data['card_reference_id'] = msg[idx:idx+length]
            idx += length
        elif field == 4:
            data['amount'] = msg[idx:idx+12]
            idx += 12
        elif field == 49:
            data['currency'] = msg[idx:idx+3]
            idx += 3
        elif field == 111:
            data['transaction_description'] = msg[idx:idx+2]
            idx += 2
        else:
            pass
    return {
        'message_type': message_type,
        'amount': data.get('amount'),
        'card_reference_id': data.get('card_reference_id'),
        'currency': data.get('currency'),
        'transaction_description': data.get('transaction_description'),
    }

async def handler(websocket):
    async for message in websocket:
        try:
            parsed = parse_iso8583_message(message)
            await websocket.send(json.dumps(parsed))
        except Exception as e:
            await websocket.send(json.dumps({'error': str(e)}))

async def main():
    async with websockets.serve(handler, 'localhost', 8765):
        print('ISO8583 WebSocket server running on ws://localhost:8765')
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
