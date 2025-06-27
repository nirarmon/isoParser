# ISO 8583 WebSocket Message Parser

This project provides a WebSocket server that receives ISO 8583 messages, parses them, and returns a JSON object with the following fields:
- message type (e.g., preauth, settlement, etc.)
- amount
- card reference id
- currency
- transaction description

## Usage

1. Start the server:
   ```bash
   python iso8583_ws_server.py
   ```
2. Connect to the WebSocket server and send a raw ISO 8583 message (as hex or ASCII string).
3. The server will respond with a JSON object containing the parsed fields.

## Requirements
- Python 3.8+
- websockets

## Notes
- The parser is based on the i2c ISO 8583 specification (v24.3.1).
- Only the required fields for the output JSON are parsed.
