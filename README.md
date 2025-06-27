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
  "amount": "000000010000",
  "card_reference_id": "1234567890123456",
  "currency": "840",
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

## Notes
- The parser is robust to short/invalid messages and extra fields.
- See `input.md` for field definitions and message structure.
- Integration tests require the WebSocket server to be running.