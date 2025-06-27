# isoParser

## Overview

This project implements an ISO 8583 message parser and WebSocket server in Python. It receives ISO 8583 messages over a WebSocket connection, parses them into JSON, and extracts key fields such as message type, amount, card reference ID, currency, and transaction description. The parser is robust to missing or extra fields and follows the i2c ISO 8583 specification.

## Features
- ISO 8583 message parsing (MTI, bitmap, variable/fixed fields)
- WebSocket server for real-time message parsing
- JSON output with key transaction fields
- Sample WebSocket client
- 20+ unit tests and 10+ integration tests
- Robust to missing/extra/invalid fields

## Example Usage

### Example ISO 8583 Message
```
MTI: 0100
Primary Bitmap: 0xF220000000000000
Secondary Bitmap: 0x0000000000000002
Field 2 (Card Reference ID): 16 + 1234567890123456
Field 4 (Amount): 000000010000
Field 49 (Currency): 840
Field 111 (Transaction Description): PP
```

### Example JSON Output
```
{
  "message_type": "preauth",
  "transaction_code": "0100",
  "amount": "000000010000",
  "card_reference_id": "1234567890123456",
  "currency": "840",
  "currency_iso3": "USD",
  "transaction_description": "PP"
}
```

## How to Run the WebSocket Server

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   python iso8583_ws_server.py
   ```
   The server will run on `ws://localhost:8765`.

## How to Run the Sample Client

1. In a separate terminal, run:
   ```bash
   python sample_iso8583_client.py
   ```
   This will send a sample ISO 8583 message to the server and print the parsed JSON response.

## How to Run the Tests

1. Run all tests (unit and integration):
   ```bash
   pytest -v
   ```
2. To run only unit tests:
   ```bash
   pytest -v test_iso8583_parser.py
   ```
3. To run only integration tests:
   ```bash
   pytest -v test_iso8583_ws_integration.py
   ```

## Project Structure
- `iso8583_ws_server.py` - WebSocket server and ISO 8583 parser
- `sample_iso8583_client.py` - Sample client for testing
- `test_iso8583_parser.py` - Unit tests for the parser
- `test_iso8583_ws_integration.py` - Integration tests for the WebSocket server
- `requirements.txt` - Python dependencies
- `input.md` - i2c ISO 8583 field specification

## Supported Currency Codes

The following ISO 4217 numeric currency codes are mapped to their alpha-3 codes and names:

| Numeric Code | Alpha-3 Code | Currency Name       |
|:------------:|:------------:|:-------------------|
| 840          | USD          | US Dollar          |
| 978          | EUR          | Euro               |
| 392          | JPY          | Japanese Yen       |
| 826          | GBP          | British Pound      |
| 124          | CAD          | Canadian Dollar    |
| 036          | AUD          | Australian Dollar  |
| 756          | CHF          | Swiss Franc        |
| 156          | CNY          | Chinese Yuan       |
| 643          | RUB          | Russian Ruble      |
| 999          | XXX          | Unknown/Test       |

If a currency code is not listed, the numeric code will be returned as the alpha-3 code.

## Supported Transaction Codes (MTI)

The following Message Type Identifiers (MTI) are mapped to transaction types (from ISO 8583):

| MTI  | Transaction Type Description                |
|:----:|:-------------------------------------------|
| 0100 | Authorization request                      |
| 0110 | Authorization response                     |
| 0120 | Authorization advice                       |
| 0130 | Authorization advice response              |
| 0200 | Financial transaction request              |
| 0210 | Financial transaction response             |
| 0220 | Financial advice                           |
| 0230 | Financial advice response                  |
| 0300 | File actions request                       |
| 0310 | File actions response                      |
| 0320 | File actions advice                        |
| 0330 | File actions advice response               |
| 0400 | Reversal request                           |
| 0410 | Reversal response                          |
| 0420 | Reversal advice                            |
| 0430 | Reversal advice response                   |
| 0500 | Reconciliation request                     |
| 0510 | Reconciliation response                    |
| 0520 | Reconciliation advice                      |
| 0530 | Reconciliation advice response             |
| 0600 | Administrative request                     |
| 0610 | Administrative response                    |
| 0620 | Administrative advice                      |
| 0630 | Administrative advice response             |
| 0800 | Network management request                 |
| 0810 | Network management response                |

If an MTI is not listed, the transaction type will be returned as 'unknown'.

## Notes
- The parser is robust to short/invalid messages and extra fields.
- See `input.md` for field definitions and message structure.
- Integration tests require the WebSocket server to be running.