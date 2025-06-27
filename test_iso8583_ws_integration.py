import asyncio
import pytest
import websockets
import json
from iso8583_ws_server import make_bitmap, make_secondary_bitmap

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
