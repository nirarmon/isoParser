# ISO Parser

This project provides a simple ISO 8583 message parser implemented in Go. It exposes a small WebSocket server that accepts incoming hexadecimal ISO messages and returns a JSON structure describing selected data elements.

## Example

```
006330343330902000000020800000000000040000003030303030303031303030303132333435364143515549524552204E414D452043495459204E414D4520434155534120202020202020202020383430313631323334353637383930313233343536
```

Parsing the above message produces the following JSON:

```
{
  "transaction_code": "0430",
  "message_type": "Reversal Advice Response",
  "amount": "000000010000",
  "card_reference_id": "1234567890123456",
  "currency": "840",
  "currency_iso3": "USD",
  "description": "ACQUIRER NAME CITY NAME CAUSA"
}
```

## Transaction Codes

| Code | Type |
|------|------|
| 0100 | Authorization Request |
| 0110 | Authorization Response |
| 0120 | Authorization Advice |
| 0130 | Authorization Advice Response |
| 0200 | Financial Transaction Request |
| 0210 | Financial Transaction Response |
| 0220 | Financial Transaction Advice |
| 0230 | Financial Transaction Advice Response |
| 0302 | File Update Request |
| 0312 | File Update Response |
| 0420 | Reversal Advice |
| 0430 | Reversal Advice Response |
| 0600 | Administrative Request |
| 0620 | Administrative Advice |
| 0630 | Administrative Advice Response |
| 0800 | Network Management Request |
| 0810 | Network Management Response |

## Currency Codes

| Numeric | ISO-3 |
|---------|------|
| 840     | USD |
| 978     | EUR |
| 826     | GBP |

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

