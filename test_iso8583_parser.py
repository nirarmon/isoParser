import pytest
from iso8583_ws_server import parse_iso8583_message

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

def build_msg(mti, card_ref, amount, currency, desc):
    primary_bitmap = make_bitmap([1, 2, 4, 49])
    secondary_bitmap = make_secondary_bitmap([111])
    field2 = f'{len(card_ref):02d}' + card_ref
    field4 = amount
    field49 = currency
    field111 = desc
    return mti + primary_bitmap + secondary_bitmap + field2 + field4 + field49 + field111

def build_msg_fields(mti, fields, sec_fields, field_values):
    primary_bitmap = make_bitmap(fields)
    msg = mti + primary_bitmap
    if sec_fields:
        secondary_bitmap = make_secondary_bitmap(sec_fields)
        msg += secondary_bitmap
    for f in fields:
        if f == 2:
            v = field_values.get(2, '')
            msg += f'{len(v):02d}' + v
        elif f == 4:
            msg += field_values.get(4, '')
        elif f == 49:
            msg += field_values.get(49, '')
        elif f == 3:
            msg += field_values.get(3, '')
    for f in sec_fields:
        if f == 111:
            msg += field_values.get(111, '')
    return msg

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

def test_missing_amount():
    msg = build_msg_fields('0100', [1, 2, 49], [111], {2: '1234567890123456', 49: '840', 111: 'PP'})
    result = parse_iso8583_message(msg)
    assert result['amount'] is None
    assert result['card_reference_id'] == '1234567890123456'
    assert result['currency'] == '840'
    assert result['transaction_description'] == 'PP'

def test_missing_currency():
    msg = build_msg_fields('0100', [1, 2, 4], [111], {2: '1234567890123456', 4: '000000010000', 111: 'PP'})
    result = parse_iso8583_message(msg)
    assert result['currency'] is None
    assert result['amount'] == '000000010000'
    assert result['transaction_description'] == 'PP'

def test_missing_card_reference():
    msg = build_msg_fields('0100', [1, 4, 49], [111], {4: '000000010000', 49: '840', 111: 'PP'})
    result = parse_iso8583_message(msg)
    assert result['card_reference_id'] is None
    assert result['amount'] == '000000010000'
    assert result['currency'] == '840'
    assert result['transaction_description'] == 'PP'

def test_missing_transaction_description():
    msg = build_msg_fields('0100', [2, 4, 49], [], {2: '1234567890123456', 4: '000000010000', 49: '840'})
    result = parse_iso8583_message(msg)
    assert result['transaction_description'] is None
    assert result['amount'] == '000000010000'
    assert result['currency'] == '840'
    assert result['card_reference_id'] == '1234567890123456'

def test_all_fields_missing():
    msg = '0100' + make_bitmap([])
    result = parse_iso8583_message(msg)
    assert result['amount'] is None
    assert result['currency'] is None
    assert result['card_reference_id'] is None
    assert result['transaction_description'] is None

def test_amount_zero():
    msg = build_msg('0200', '8888999900001111', '000000000000', '840', 'PP')
    result = parse_iso8583_message(msg)
    assert result['amount'] == '000000000000'

def test_amount_large():
    msg = build_msg('0200', '7777888899990000', '999999999999', '840', 'PP')
    result = parse_iso8583_message(msg)
    assert result['amount'] == '999999999999'

def test_currency_jpy():
    msg = build_msg('0200', '5555444433332222', '000000000500', '392', 'AA')
    result = parse_iso8583_message(msg)
    assert result['currency'] == '392'
    assert result['transaction_description'] == 'AA'

def test_currency_eur():
    msg = build_msg('0200', '1111000022223333', '000000002000', '978', 'BB')
    result = parse_iso8583_message(msg)
    assert result['currency'] == '978'
    assert result['transaction_description'] == 'BB'

def test_transaction_desc_pp():
    msg = build_msg('0200', '2222333344445555', '000000003000', '840', 'PP')
    result = parse_iso8583_message(msg)
    assert result['transaction_description'] == 'PP'

def test_transaction_desc_bb():
    msg = build_msg('0200', '3333444455556666', '000000004000', '840', 'BB')
    result = parse_iso8583_message(msg)
    assert result['transaction_description'] == 'BB'

def test_transaction_desc_og():
    msg = build_msg('0200', '4444555566667777', '000000005000', '840', 'OG')
    result = parse_iso8583_message(msg)
    assert result['transaction_description'] == 'OG'

def test_transaction_desc_aa():
    msg = build_msg('0200', '5555666677778888', '000000006000', '840', 'AA')
    result = parse_iso8583_message(msg)
    assert result['transaction_description'] == 'AA'

def test_transaction_desc_bp():
    msg = build_msg('0200', '6666777788889999', '000000007000', '840', 'BP')
    result = parse_iso8583_message(msg)
    assert result['transaction_description'] == 'BP'

def test_card_reference_short():
    msg = build_msg('0200', '12345678', '000000000100', '840', 'PP')
    result = parse_iso8583_message(msg)
    assert result['card_reference_id'] == '12345678'
    assert result['amount'] == '000000000100'

def test_card_reference_long():
    msg = build_msg('0200', '1234567890123456789', '000000000200', '840', 'PP')
    result = parse_iso8583_message(msg)
    assert result['card_reference_id'] == '1234567890123456789'
    assert result['amount'] == '000000000200'

def test_all_fields_max_length():
    msg = build_msg('0100', '9876543210987654321', '123456789012', '999', 'ZZ')
    result = parse_iso8583_message(msg)
    assert result['card_reference_id'] == '9876543210987654321'
    assert result['amount'] == '123456789012'
    assert result['currency'] == '999'
    assert result['transaction_description'] == 'ZZ'

def test_extra_field_ignored():
    msg = build_msg_fields('0200', [1, 2, 3, 4, 49], [111], {2: '9999888877776666', 3: '123456', 4: '000000123456', 49: '826', 111: 'OG'})
    result = parse_iso8583_message(msg)
    assert result['message_type'] == 'financial'
    assert result['card_reference_id'] == '9999888877776666'
    assert result['amount'] == '000000123456'
    assert result['currency'] == '826'
    assert result['transaction_description'] == 'OG'

def test_invalid_message():
    msg = '0100'  # Only MTI
    result = parse_iso8583_message(msg)
    assert result['amount'] is None
    assert result['currency'] is None
    assert result['card_reference_id'] is None
    assert result['transaction_description'] is None
