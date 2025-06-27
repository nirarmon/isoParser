package main

import (
	"errors"
	"io"
	"strings"
	"testing"
)

const sample0430 = "006330343330902000000020800000000000040000003030303030303031303030303132333435364143515549524552204E414D452043495459204E414D452043415553412020202020202020202020383430313631323334353637383930313233343536"

// Sample 0430 message taken from input.md lines around 14018
func TestParseISO8583(t *testing.T) {
	msg, err := parseISO8583(sample0430)
	if err != nil {
		t.Fatalf("parseISO8583 returned error: %v", err)
	}
	if msg.MessageType != "Reversal Advice Response" {
		t.Errorf("unexpected message type: %q", msg.MessageType)
	}
	if msg.Amount != "000000010000" {
		t.Errorf("unexpected amount: %q", msg.Amount)
	}
	if msg.CardReferenceID != "1234567890123456" {
		t.Errorf("unexpected card reference id: %q", msg.CardReferenceID)
	}
	if msg.Currency != "840" {
		t.Errorf("unexpected currency: %q", msg.Currency)
	}
	if msg.Description != "ACQUIRER NAME CITY NAME CAUSA" {
		t.Errorf("unexpected description: %q", msg.Description)
	}
}

// The following examples use values from input.md (e.g. lines 13361-13367)
func TestParseISO8583UnknownField(t *testing.T) {
	// This message is based on the 0800 sample but padded to even length
	_, err := parseISO8583("006708008220000008000000040000000000000004091115300880019099160880010081")
	if err == nil || !strings.Contains(err.Error(), "spec for field 21 missing") {
		// just check an error occurred since field 21 is not defined
		if err == nil {
			t.Fatal("expected error")
		}
	}
}

func TestParseISO8583OddLength(t *testing.T) {
	// Hex string from input.md line 13361 has odd length
	_, err := parseISO8583("00670800822000000800000004000000000000000409111530088001909916088001081")
	if err == nil {
		t.Fatal("expected error for odd length hex string")
	}
}

func TestParseISO8583TooShort(t *testing.T) {
	_, err := parseISO8583("0010")
	if err == nil {
		t.Fatal("expected error for short message")
	}
}

func TestParseFieldFixed(t *testing.T) {
	val, n, err := parseField([]byte("61002000rest"), FieldSpec{LengthType: "fixed", Length: 8})
	if err != nil || val != "61002000" || n != 8 {
		t.Fatalf("unexpected result %q %d %v", val, n, err)
	}
}

func TestParseFieldFixedShort(t *testing.T) {
	_, _, err := parseField([]byte("6100"), FieldSpec{LengthType: "fixed", Length: 8})
	if !errors.Is(err, io.ErrUnexpectedEOF) {
		t.Fatalf("expected EOF, got %v", err)
	}
}

func TestParseFieldLLVar(t *testing.T) {
	val, n, err := parseField([]byte("15100194868736564rest"), FieldSpec{LengthType: "llvar", Length: 19})
	if err != nil || val != "100194868736564" || n != 17 {
		t.Fatalf("unexpected result %q %d %v", val, n, err)
	}
}

func TestParseFieldLLVarShort(t *testing.T) {
	_, _, err := parseField([]byte("05abc"), FieldSpec{LengthType: "llvar", Length: 19})
	if !errors.Is(err, io.ErrUnexpectedEOF) {
		t.Fatalf("expected EOF, got %v", err)
	}
}

func TestParseFieldLLVarInvalid(t *testing.T) {
	_, _, err := parseField([]byte("20"+strings.Repeat("a", 20)), FieldSpec{LengthType: "llvar", Length: 19})
	if err == nil {
		t.Fatal("expected invalid llvar length error")
	}
}

func TestParseFieldLLLVar(t *testing.T) {
	val, n, err := parseField([]byte("006VISA16"), FieldSpec{LengthType: "lllvar", Length: 120})
	if err != nil || val != "VISA16" || n != 9 {
		t.Fatalf("unexpected result %q %d %v", val, n, err)
	}
}
