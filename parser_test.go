package main

import "testing"

const sample0430 = "006330343330902000000020800000000000040000003030303030303031303030303132333435364143515549524552204E414D452043495459204E414D452043415553412020202020202020202020383430313631323334353637383930313233343536"

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
