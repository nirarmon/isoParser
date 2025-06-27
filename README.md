# ISO Parser

This project provides a simple ISO 8583 message parser implemented in Go. It exposes a small WebSocket server that accepts incoming hexadecimal ISO messages and returns a JSON structure describing selected data elements.

## Example

```
006330343330902000000020800000000000040000003030303030303031303030303132333435364143515549524552204E414D452043495459204E414D4520434155534120202020202020202020383430313631323334353637383930313233343536
```

Parsing the above message produces the following JSON:

```
{
  "message_type": "Reversal Advice Response",
  "amount": "000000010000",
  "card_reference_id": "1234567890123456",
  "currency": "840",
  "description": "ACQUIRER NAME CITY NAME CAUSA"
}
```

## Running the Server

Make sure you have Go installed (1.20 or newer). Start the WebSocket server with:

```bash
go run .
```

The server listens on `localhost:8080` and exposes a WebSocket endpoint at `/ws`. Send a hex string as the payload of a WebSocket text frame to receive the parsed JSON message.

## Running Tests

Execute all unit tests with:

```bash
go test ./...
```

The tests include several examples extracted from `input.md` to validate parsing of fixed and variable length fields.

