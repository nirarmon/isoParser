import pytest
from iso8583_ws_server import parse_iso8583_message

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

# Test case 1: Preauth (0100), all fields present (2, 4, 49 in primary, 111 in secondary)
# Card Reference ID: '1234567890123456', Amount: '000000010000', Currency: '840', Transaction Description: 'PP'
def test_parse_iso8583_preauth():
    mti = '0100'
    # Bit 1 set (secondary bitmap present), bits 2, 4, 49 in primary, 47 in secondary (field 111)
    primary_bitmap = make_bitmap([1, 2, 4, 49])
    secondary_bitmap = make_secondary_bitmap([111])
    field2 = '16' + '1234567890123456'
    field4 = '000000010000'
    field49 = '840'
    field111 = 'PP'
    msg = mti + primary_bitmap + secondary_bitmap + field2 + field4 + field49 + field111
    result = parse_iso8583_message(msg)
    assert result['message_type'] == 'preauth'
    assert result['amount'] == '000000010000'
    assert result['card_reference_id'] == '1234567890123456'
    assert result['currency'] == '840'
    assert result['transaction_description'] == 'PP'

# Test case 2: Settlement (0420), different values
# Card Reference ID: '6543210987654321', Amount: '000000005000', Currency: '978', Transaction Description: 'BB'
def test_parse_iso8583_settlement():
    mti = '0420'
    primary_bitmap = make_bitmap([1, 2, 4, 49])
    secondary_bitmap = make_secondary_bitmap([111])
    field2 = '16' + '6543210987654321'
    field4 = '000000005000'
    field49 = '978'
    field111 = 'BB'
    msg = mti + primary_bitmap + secondary_bitmap + field2 + field4 + field49 + field111
    result = parse_iso8583_message(msg)
    assert result['message_type'] == 'settlement'
    assert result['amount'] == '000000005000'
    assert result['card_reference_id'] == '6543210987654321'
    assert result['currency'] == '978'
    assert result['transaction_description'] == 'BB'

# Test case 3: Unknown MTI
# Card Reference ID: '1111222233334444', Amount: '000000000100', Currency: '392', Transaction Description: 'AA'
def test_parse_iso8583_unknown_mti():
    mti = '9999'
    primary_bitmap = make_bitmap([1, 2, 4, 49])
    secondary_bitmap = make_secondary_bitmap([111])
    field2 = '16' + '1111222233334444'
    field4 = '000000000100'
    field49 = '392'
    field111 = 'AA'
    msg = mti + primary_bitmap + secondary_bitmap + field2 + field4 + field49 + field111
    result = parse_iso8583_message(msg)
    assert result['message_type'] == 'unknown'
    assert result['amount'] == '000000000100'
    assert result['card_reference_id'] == '1111222233334444'
    assert result['currency'] == '392'
    assert result['transaction_description'] == 'AA'
