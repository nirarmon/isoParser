package main

import (
	"bufio"
	"crypto/sha1"
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"strconv"
	"strings"
)

type FieldSpec struct {
	LengthType string
	Length     int
}

var fieldSpecs = map[int]FieldSpec{
	2:   {"llvar", 19},
	3:   {"fixed", 6},
	4:   {"fixed", 12},
	6:   {"fixed", 12},
	7:   {"fixed", 10},
	10:  {"fixed", 8},
	11:  {"fixed", 6},
	12:  {"fixed", 6},
	13:  {"fixed", 4},
	15:  {"fixed", 4},
	18:  {"fixed", 4},
	25:  {"fixed", 2},
	28:  {"fixed", 9},
	32:  {"llvar", 11},
	37:  {"fixed", 12},
	38:  {"fixed", 6},
	39:  {"fixed", 2},
	41:  {"fixed", 8},
	42:  {"fixed", 15},
	43:  {"fixed", 40},
	49:  {"fixed", 3},
	51:  {"fixed", 3},
	54:  {"lllvar", 120},
	61:  {"lllvar", 50},
	63:  {"lllvar", 999},
	102: {"llvar", 28},
	111: {"lllvar", 999},
}

var mtiDescriptions = map[string]string{
	"0100": "Authorization Request",
	"0110": "Authorization Response",
	"0120": "Authorization Advice",
	"0130": "Authorization Advice Response",
	"0200": "Financial Transaction Request",
	"0210": "Financial Transaction Response",
	"0220": "Financial Transaction Advice",
	"0230": "Financial Transaction Advice Response",
	"0302": "File Update Request",
	"0312": "File Update Response",
	"0420": "Reversal Advice",
	"0430": "Reversal Advice Response",
	"0600": "Administrative Request",
	"0620": "Administrative Advice",
	"0630": "Administrative Advice Response",
	"0800": "Network Management Request",
	"0810": "Network Management Response",
}

// currencyISO3 maps numeric ISO 4217 currency codes to their alphabetic
// counterparts. Only a very small subset is required for the examples and tests
// contained in this repository.
var currencyISO3 = map[string]string{
	"840": "USD",
	"978": "EUR",
	"826": "GBP",
}

// ISOMessage represents a subset of the parsed ISO8583 fields. In addition to
// the original fields this structure now exposes the numeric transaction code
// (MTI), as well as the alphabetic ISO‑3 currency code.
type ISOMessage struct {
	TransactionCode string `json:"transaction_code"`
	MessageType     string `json:"message_type"`
	Amount          string `json:"amount"`
	CardReferenceID string `json:"card_reference_id"`
	Currency        string `json:"currency"`
	CurrencyISO3    string `json:"currency_iso3"`
	Description     string `json:"description"`
}

func bitsFromBytes(bytes []byte) []bool {
	bits := make([]bool, len(bytes)*8)
	for i, b := range bytes {
		for j := 0; j < 8; j++ {
			bits[i*8+j] = (b & (1 << uint(7-j))) != 0
		}
	}
	return bits
}

func parseField(data []byte, spec FieldSpec) (string, int, error) {
	switch spec.LengthType {
	case "fixed":
		if len(data) < spec.Length {
			return "", 0, io.ErrUnexpectedEOF
		}
		return string(data[:spec.Length]), spec.Length, nil
	case "llvar":
		if len(data) < 2 {
			return "", 0, io.ErrUnexpectedEOF
		}
		ln, err := strconv.Atoi(string(data[:2]))
		if err != nil || ln > spec.Length {
			return "", 0, fmt.Errorf("invalid llvar length")
		}
		if len(data) < 2+ln {
			return "", 0, io.ErrUnexpectedEOF
		}
		return string(data[2 : 2+ln]), 2 + ln, nil
	case "lllvar":
		if len(data) < 3 {
			return "", 0, io.ErrUnexpectedEOF
		}
		ln, err := strconv.Atoi(string(data[:3]))
		if err != nil || ln > spec.Length {
			return "", 0, fmt.Errorf("invalid lllvar length")
		}
		if len(data) < 3+ln {
			return "", 0, io.ErrUnexpectedEOF
		}
		return string(data[3 : 3+ln]), 3 + ln, nil
	default:
		return "", 0, fmt.Errorf("unknown length type")
	}
}

func parseISO8583(hexMsg string) (ISOMessage, error) {
	var result ISOMessage
	b, err := hex.DecodeString(strings.TrimSpace(hexMsg))
	if err != nil {
		return result, err
	}
	if len(b) < 14 { // length + mti + bitmap
		return result, fmt.Errorf("message too short")
	}
	pos := 2 // skip length prefix
	mti := string(b[pos : pos+4])
	pos += 4
	primary := b[pos : pos+8]
	pos += 8
	bits := bitsFromBytes(primary)
	if bits[0] {
		if len(b) < pos+8 {
			return result, fmt.Errorf("invalid secondary bitmap")
		}
		secondary := b[pos : pos+8]
		pos += 8
		bits = append(bits, bitsFromBytes(secondary)...)
	}
	fields := make(map[int]string)
	for i := 1; i < len(bits); i++ {
		if !bits[i] {
			continue
		}
		num := i + 1
		spec, ok := fieldSpecs[num]
		if !ok {
			return result, fmt.Errorf("spec for field %d missing", num)
		}
		val, read, err := parseField(b[pos:], spec)
		if err != nil {
			return result, fmt.Errorf("field %d: %v", num, err)
		}
		fields[num] = val
		pos += read
	}
	result.TransactionCode = mti
	result.MessageType = mtiDescriptions[mti]
	if v, ok := fields[4]; ok {
		result.Amount = v
	}
	if v, ok := fields[102]; ok {
		result.CardReferenceID = v
	}
	if v, ok := fields[49]; ok {
		result.Currency = v
		if alpha, ok := currencyISO3[v]; ok {
			result.CurrencyISO3 = alpha
		}
	}
	if v, ok := fields[43]; ok {
		result.Description = strings.TrimSpace(v)
	}
	if result.MessageType == "" {
		result.MessageType = mti
	}
	return result, nil
}

func computeAcceptKey(key string) string {
	const wsGUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
	h := sha1.Sum([]byte(key + wsGUID))
	return base64.StdEncoding.EncodeToString(h[:])
}

func readFrame(r *bufio.Reader) ([]byte, error) {
	header1, err := r.ReadByte()
	if err != nil {
		return nil, err
	}
	fin := header1&0x80 != 0
	opcode := header1 & 0x0F
	if opcode == 8 { // close frame
		return nil, io.EOF
	}
	if !fin || opcode != 1 {
		return nil, fmt.Errorf("only single text frames supported")
	}
	header2, err := r.ReadByte()
	if err != nil {
		return nil, err
	}
	mask := header2&0x80 != 0
	length := int(header2 & 0x7F)
	if length == 126 {
		b1, _ := r.ReadByte()
		b2, _ := r.ReadByte()
		length = int(b1)<<8 | int(b2)
	} else if length == 127 {
		var l uint64
		for i := 0; i < 8; i++ {
			b, _ := r.ReadByte()
			l = (l << 8) | uint64(b)
		}
		length = int(l)
	}
	var maskingKey [4]byte
	if mask {
		if _, err := io.ReadFull(r, maskingKey[:]); err != nil {
			return nil, err
		}
	}
	payload := make([]byte, length)
	if _, err := io.ReadFull(r, payload); err != nil {
		return nil, err
	}
	if mask {
		for i := 0; i < length; i++ {
			payload[i] ^= maskingKey[i%4]
		}
	}
	return payload, nil
}

func writeFrame(w io.Writer, data []byte) error {
	length := len(data)
	header := []byte{0x81}
	if length <= 125 {
		header = append(header, byte(length))
	} else if length <= 65535 {
		header = append(header, 126, byte(length>>8), byte(length))
	} else {
		header = append(header, 127,
			byte(length>>56), byte(length>>48), byte(length>>40), byte(length>>32),
			byte(length>>24), byte(length>>16), byte(length>>8), byte(length))
	}
	if _, err := w.Write(header); err != nil {
		return err
	}
	_, err := w.Write(data)
	return err
}

func wsHandler(w http.ResponseWriter, r *http.Request) {
	if strings.ToLower(r.Header.Get("Upgrade")) != "websocket" {
		http.Error(w, "upgrade required", http.StatusBadRequest)
		return
	}
	key := r.Header.Get("Sec-WebSocket-Key")
	if key == "" {
		http.Error(w, "bad websocket key", http.StatusBadRequest)
		return
	}
	hijacker, ok := w.(http.Hijacker)
	if !ok {
		http.Error(w, "hijacking not supported", http.StatusInternalServerError)
		return
	}
	conn, _, err := hijacker.Hijack()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	accept := computeAcceptKey(key)
	response := "HTTP/1.1 101 Switching Protocols\r\n" +
		"Upgrade: websocket\r\n" +
		"Connection: Upgrade\r\n" +
		"Sec-WebSocket-Accept: " + accept + "\r\n\r\n"
	if _, err := conn.Write([]byte(response)); err != nil {
		conn.Close()
		return
	}
	reader := bufio.NewReader(conn)
	for {
		msg, err := readFrame(reader)
		if err != nil {
			if err != io.EOF {
				log.Println("read error:", err)
			}
			conn.Close()
			return
		}
		iso, err := parseISO8583(string(msg))
		if err != nil {
			log.Println("parse error:", err)
			continue
		}
		data, _ := json.Marshal(iso)
		if err := writeFrame(conn, data); err != nil {
			log.Println("write error:", err)
			conn.Close()
			return
		}
	}
}

func main() {
	http.HandleFunc("/ws", wsHandler)
	log.Println("listening on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
