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

# MTI to message type mapping (full ISO 8583 transaction types)
MTI_MAP = {
    '0100': 'authorization_request',
    '0110': 'authorization_response',
    '0120': 'authorization_advice',
    '0130': 'authorization_advice_response',
    '0200': 'financial_transaction_request',
    '0210': 'financial_transaction_response',
    '0220': 'financial_advice',
    '0230': 'financial_advice_response',
    '0300': 'file_actions_request',
    '0310': 'file_actions_response',
    '0320': 'file_actions_advice',
    '0330': 'file_actions_advice_response',
    '0400': 'reversal_request',
    '0410': 'reversal_response',
    '0420': 'reversal_advice',
    '0430': 'reversal_advice_response',
    '0500': 'reconciliation_request',
    '0510': 'reconciliation_response',
    '0520': 'reconciliation_advice',
    '0530': 'reconciliation_advice_response',
    '0600': 'administrative_request',
    '0610': 'administrative_response',
    '0620': 'administrative_advice',
    '0630': 'administrative_advice_response',
    '0800': 'network_management_request',
    '0810': 'network_management_response',
    # Add more as needed
}

# ISO 4217 numeric to alpha code mapping (partial, extend as needed)
ISO4217_NUM_TO_ALPHA = {
    '840': 'USD',
    '978': 'EUR',
    '392': 'JPY',
    '826': 'GBP',
    '124': 'CAD',
    '036': 'AUD',
    '756': 'CHF',
    '156': 'CNY',
    '643': 'RUB',
    '999': 'XXX',  # Unknown/test
    # Add more as needed
}

def parse_bitmap(bitmap_hex: str) -> list:
    bits = bin(int(bitmap_hex, 16))[2:].zfill(64)
    present_fields = [i+1 for i, b in enumerate(bits) if b == '1']
    return present_fields

def parse_iso8583_message(msg: str) -> dict:
    try:
        mti = msg[:4]
        message_type = MTI_MAP.get(mti, 'unknown')
        transaction_code = mti  # Add raw MTI as transaction code
        bitmap_hex = msg[4:20]
        if not bitmap_hex or len(bitmap_hex) < 16:
            return {
                'message_type': message_type,
                'transaction_code': transaction_code,
                'amount': None,
                'card_reference_id': None,
                'currency': None,
                'currency_iso3': None,
                'transaction_description': None,
            }
        present_fields = parse_bitmap(bitmap_hex)
        idx = 20
        # Check for secondary bitmap (bit 1 set)
        if present_fields and present_fields[0] == 1:
            secondary_bitmap_hex = msg[idx:idx+16]
            idx += 16
            secondary_fields = parse_bitmap(secondary_bitmap_hex)
            present_fields = present_fields[1:] + [f+64 for f in secondary_fields]
        data = {}
        # Field length definitions (for skipping unknown fields)
        FIELD_LENGTHS = {
            2: 'var',   # variable, 2-digit length prefix
            3: 6,       # Processing code (example, 6 digits)
            4: 12,      # Amount
            49: 3,      # Currency
            111: 2,     # Transaction description
        }
        for field in present_fields:
            if field == 2:
                print(f"DEBUG: idx={idx}, msg[idx:]=<{msg[idx:]}> (len={len(msg)})")
                if idx + 2 <= len(msg):
                    length = int(msg[idx:idx+2])
                    idx += 2
                    if idx + length <= len(msg):
                        data['card_reference_id'] = msg[idx:idx+length]
                        idx += length
                    else:
                        data['card_reference_id'] = None
                else:
                    data['card_reference_id'] = None
            elif field == 4:
                if idx + 12 <= len(msg):
                    data['amount'] = msg[idx:idx+12]
                    idx += 12
                else:
                    data['amount'] = None
            elif field == 49:
                if idx + 3 <= len(msg):
                    currency = msg[idx:idx+3]
                    data['currency'] = currency
                    data['currency_iso3'] = ISO4217_NUM_TO_ALPHA.get(currency, currency)
                    idx += 3
                else:
                    data['currency'] = None
                    data['currency_iso3'] = None
            elif field == 111:
                if idx + 2 <= len(msg):
                    data['transaction_description'] = msg[idx:idx+2]
                    idx += 2
                else:
                    data['transaction_description'] = None
            else:
                flen = FIELD_LENGTHS.get(field, None)
                if flen == 'var':
                    if idx + 2 <= len(msg):
                        vlen = int(msg[idx:idx+2])
                        idx += 2 + vlen
                elif isinstance(flen, int):
                    if idx + flen <= len(msg):
                        idx += flen
                else:
                    pass
        return {
            'message_type': message_type,
            'transaction_code': transaction_code,
            'amount': data.get('amount'),
            'card_reference_id': data.get('card_reference_id'),
            'currency': data.get('currency'),
            'currency_iso3': data.get('currency_iso3'),
            'transaction_description': data.get('transaction_description'),
        }
    except Exception:
        return {
            'message_type': 'unknown',
            'transaction_code': None,
            'amount': None,
            'card_reference_id': None,
            'currency': None,
            'currency_iso3': None,
            'transaction_description': None,
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
