import asyncio
import pytest
import websockets
import json

# Helper functions for tests (not part of main parser)
def make_bitmap(fields):
    bits = ['0'] * 64
    for f in fields:
        if 1 <= f <= 64:
            bits[f-1] = '1'
    return hex(int(''.join(bits), 2))[2:].upper().zfill(16)

def make_secondary_bitmap(fields):
    bits = ['0'] * 64
    for f in fields:
        if 65 <= f <= 128:
            bits[f-65] = '1'
    return hex(int(''.join(bits), 2))[2:].upper().zfill(16)

# Helper to build a message
def build_iso8583_msg(mti, card_ref, amount, currency, description):
    primary_bitmap = make_bitmap([1, 2, 4, 49])
    secondary_bitmap = make_secondary_bitmap([111])
    field2 = '16' + card_ref
    field4 = amount
    field49 = currency
    field111 = description
    return mti + primary_bitmap + secondary_bitmap + field2 + field4 + field49 + field111

@pytest.mark.asyncio
async def test_ws_preauth():
    msg = build_iso8583_msg('0100', '1234567890123456', '000000010000', '840', 'PP')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['message_type'] == 'preauth'
        assert data['amount'] == '000000010000'
        assert data['card_reference_id'] == '1234567890123456'
        assert data['currency'] == '840'
        assert data['transaction_description'] == 'PP'

@pytest.mark.asyncio
async def test_ws_settlement():
    msg = build_iso8583_msg('0420', '6543210987654321', '000000005000', '978', 'BB')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['message_type'] == 'settlement'
        assert data['amount'] == '000000005000'
        assert data['card_reference_id'] == '6543210987654321'
        assert data['currency'] == '978'
        assert data['transaction_description'] == 'BB'

@pytest.mark.asyncio
async def test_ws_unknown_mti():
    msg = build_iso8583_msg('9999', '1111222233334444', '000000000100', '392', 'AA')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['message_type'] == 'unknown'
        assert data['amount'] == '000000000100'
        assert data['card_reference_id'] == '1111222233334444'
        assert data['currency'] == '392'
        assert data['transaction_description'] == 'AA'

@pytest.mark.asyncio
async def test_ws_missing_fields():
    # Only field 2 (card_reference_id) present
    primary_bitmap = make_bitmap([2])
    msg = '0100' + primary_bitmap + '16' + '1234567890123456'
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['message_type'] == 'preauth'
        assert data['card_reference_id'] == '1234567890123456'
        assert data['amount'] is None
        assert data['currency'] is None
        assert data['transaction_description'] is None

@pytest.mark.asyncio
async def test_ws_invalid_message():
    # Send a message that's too short/invalid
    msg = '0100'  # Only MTI
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert 'error' in data

@pytest.mark.asyncio
async def test_ws_extra_fields_ignored():
    # Add an extra field (field 3, not parsed)
    primary_bitmap = make_bitmap([1, 2, 3, 4, 49])
    secondary_bitmap = make_secondary_bitmap([111])
    field2 = '16' + '9999888877776666'
    field3 = '123456'  # Processing code, not parsed
    field4 = '000000123456'
    field49 = '826'
    field111 = 'OG'
    msg = '0200' + primary_bitmap + secondary_bitmap + field2 + field3 + field4 + field49 + field111
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['message_type'] == 'financial'
        assert data['card_reference_id'] == '9999888877776666'
        assert data['amount'] == '000000123456'
        assert data['currency'] == '826'
        assert data['transaction_description'] == 'OG'

@pytest.mark.asyncio
async def test_ws_currency_jpy():
    msg = build_iso8583_msg('0200', '5555444433332222', '000000000500', '392', 'AA')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['currency'] == '392'  # JPY
        assert data['transaction_description'] == 'AA'

@pytest.mark.asyncio
async def test_ws_currency_eur():
    msg = build_iso8583_msg('0200', '1111000022223333', '000000002000', '978', 'BB')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['currency'] == '978'  # EUR
        assert data['transaction_description'] == 'BB'

@pytest.mark.asyncio
async def test_ws_transaction_desc_pp():
    msg = build_iso8583_msg('0200', '2222333344445555', '000000003000', '840', 'PP')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['transaction_description'] == 'PP'

@pytest.mark.asyncio
async def test_ws_transaction_desc_bb():
    msg = build_iso8583_msg('0200', '3333444455556666', '000000004000', '840', 'BB')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['transaction_description'] == 'BB'

@pytest.mark.asyncio
async def test_ws_transaction_desc_og():
    msg = build_iso8583_msg('0200', '4444555566667777', '000000005000', '840', 'OG')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['transaction_description'] == 'OG'

@pytest.mark.asyncio
async def test_ws_transaction_desc_aa():
    msg = build_iso8583_msg('0200', '5555666677778888', '000000006000', '840', 'AA')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['transaction_description'] == 'AA'

@pytest.mark.asyncio
async def test_ws_transaction_desc_bp():
    msg = build_iso8583_msg('0200', '6666777788889999', '000000007000', '840', 'BP')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['transaction_description'] == 'BP'

@pytest.mark.asyncio
async def test_ws_amount_large():
    msg = build_iso8583_msg('0200', '7777888899990000', '999999999999', '840', 'PP')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['amount'] == '999999999999'

@pytest.mark.asyncio
async def test_ws_amount_zero():
    msg = build_iso8583_msg('0200', '8888999900001111', '000000000000', '840', 'PP')
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['amount'] == '000000000000'

@pytest.mark.asyncio
async def test_ws_card_reference_short():
    # Card reference id with 8 digits
    primary_bitmap = make_bitmap([1, 2, 4, 49])
    secondary_bitmap = make_secondary_bitmap([111])
    field2 = '08' + '12345678'
    field4 = '000000000100'
    field49 = '840'
    field111 = 'PP'
    msg = '0200' + primary_bitmap + secondary_bitmap + field2 + field4 + field49 + field111
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['card_reference_id'] == '12345678'
        assert data['amount'] == '000000000100'

@pytest.mark.asyncio
async def test_ws_card_reference_long():
    # Card reference id with 19 digits (max typical for PAN)
    primary_bitmap = make_bitmap([1, 2, 4, 49])
    secondary_bitmap = make_secondary_bitmap([111])
    field2 = '19' + '1234567890123456789'
    field4 = '000000000200'
    field49 = '840'
    field111 = 'PP'
    msg = '0200' + primary_bitmap + secondary_bitmap + field2 + field4 + field49 + field111
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['card_reference_id'] == '1234567890123456789'
        assert data['amount'] == '000000000200'

@pytest.mark.asyncio
async def test_ws_all_fields_max_length():
    # Card reference id 19, amount 12, currency 3, desc 2
    primary_bitmap = make_bitmap([1, 2, 4, 49])
    secondary_bitmap = make_secondary_bitmap([111])
    field2 = '19' + '9876543210987654321'
    field4 = '123456789012'
    field49 = '999'
    field111 = 'ZZ'
    msg = '0100' + primary_bitmap + secondary_bitmap + field2 + field4 + field49 + field111
    async with websockets.connect('ws://localhost:8765') as ws:
        await ws.send(msg)
        resp = await ws.recv()
        data = json.loads(resp)
        assert data['card_reference_id'] == '9876543210987654321'
        assert data['amount'] == '123456789012'
        assert data['currency'] == '999'
        assert data['transaction_description'] == 'ZZ'
