![](./image1.jpeg){width="7.342068022747156in"
height="10.48270341207349in"}

ISO:8583 Specifications

> i2c Reference Guide

1.  \| Standard

Confidential © i2c Inc. All rights reserved.

> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}
>
> *Published by i2c Inc. Copyright © 2024 i2c Inc. Version: 24.3.1 \|
> Standard*
>
> *Revision Date: May 16^th^, 2024*
>
> *All rights reserved. No part of the contents of this document can be
> reproduced or transmitted in any form or by any means without the
> written permission of i2c Inc. i2c has made every effort during the
> preparation of this document to ensure the accuracy of the information
> provided here. However, the information contained in this document
> comes without warranty, either expressed or implied. i2c will not be
> liable for any damage, cost, or alleged cost, arising either directly
> or indirectly on account of this document. Other product and company
> names mentioned herein may be the trademarks of their respective
> owners.*
>
> ![](./image2.jpeg){width="0.8465277777777778in"
> height="0.5229658792650919in"}Table of Contents

[Summary of Changes 7](#summary-of-changes)

[PART 1 -- Message Structure 12](#part-1-message-structure)

[ISO 8583 Protocol Format 12](#iso-8583-protocol-format)

[Message Length 12](#message-length)

[Message Type Identifier (MTI) 12](#message-type-identifier-mti)

[Message Bitmaps 12](#message-bitmaps)

[Message Data Elements 14](#message-data-elements)

[PART 2 -- Message Layouts 15](#part-2-message-layouts)

[PART 3 -- Co-operative Auth Model 19](#part-3-co-operative-auth-model)

[Block Diagram 19](#block-diagram)

[Connectivity Message Flows 20](#connectivity-message-flows)

[Sign-On Message 20](#sign-on-message)

[Sign-Off Message 20](#sign-off-message)

[Echo/Health Check Message 20](#echohealth-check-message)

[Transaction Flows 21](#transaction-flows)

[Authorized by Auth-Host Processor
21](#authorized-by-auth-host-processor)

[Declined by Auth-Host Processor 22](#declined-by-auth-host-processor)

[Exceptions Processing Flows 23](#exceptions-processing-flows)

[Fail at i2c Pre-Processing 23](#fail-at-i2c-pre-processing)

[Stand-in Processing 24](#stand-in-processing-auth-host-down)

[Post Processing Failure 26](#post-processing-failure)

[PART 4 -- Data Elements Definition
29](#part-4-data-elements-definition)

[Legends for Attributes Acronyms 29](#legends-for-attributes-acronyms)

[Data Elements Details 30](#data-elements-details)

[DE -- 002 -- PRIMARY ACCOUNT NUMBER 30](#de-002-primary-account-number)

[DE -- 003 -- PROCESSING CODE 30](#de-003-processing-code)

[DE -- 004 -- AMOUNT, TRANSACTION 30](#de-004-amount-transaction)

[DE -- 005 -- AMOUNT, SETTLEMENT 30](#de-005-amount-settlement)

[DE -- 006 -- AMOUNT, CARDHOLDER BILLING
30](#de-006-amount-cardholder-billing)

[DE -- 007 -- TRANSMISSION DATE AND TIME
31](#de-007-transmission-date-and-time)

[DE -- 009 -- CONVERSION RATE, SETTLEMENT
32](#de-009-conversion-rate-settlement)

[DE -- 010 -- CONVERSION RATE, CARDHOLDER BILLING
32](#de-010-conversion-rate-cardholder-billing)

[DE -- 011 -- SYSTEM TRACE AUDIT NUMBER
32](#de-011-system-trace-audit-number)

[DE -- 012 -- TIME, LOCAL TRANSACTION
32](#de-012-time-local-transaction)

[DE -- 013 -- DATE, LOCAL TRANSACTION
\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.... 32
![](./image2.jpeg){width="0.8465277777777778in"
height="0.5229658792650919in"} [DE -- 014 -- DATE, EXPIRATION
33](#de-014-date-expiration)](#de-013-date-local-transaction)

[DE -- 015 -- DATE, SETTLEMENT 33](#de-015-date-settlement)

[DE -- 018 -- MERCHANT TYPE 33](#de-018-merchant-type)

[DE -- 022 -- POINT-OF-SERVICE ENTRY MODE CODE
33](#de-022-point-of-service-entry-mode-code)

[DE -- 023 -- PAN SEQUENCE NUMBER 33](#de-023-pan-sequence-number)

[DE -- 025 -- POINT-OF-SERVICE CONDITION CODE
34](#de-025-point-of-service-condition-code)

[DE -- 026 -- POINT-OF-SERVICE PIN CAPTURE CODE
34](#de-026-point-of-service-pin-capture-code)

[DE -- 028 -- AMOUNT, TRANSACTION FEE
34](#de-028-amount-transaction-fee)

[DE -- 029 -- AMOUNT SETTLEMENT FEE 34](#de-029-amount-settlement-fee)

[DE -- 032 -- ACQUIRING INSTITUTION IDENTIFICATION CODE
34](#de-032-acquiring-institution-identification-code)

[DE -- 033 -- FORWARDING INSTITUTION IDENTIFICATION CODE
35](#de-033-forwarding-institution-identification-code)

[DE -- 037 -- RETRIEVAL REFERENCE NUMBER
35](#de-037-retrieval-reference-number)

[DE -- 038 -- AUTHORIZATION IDENTIFICATION RESPONSE
35](#de-038-authorization-identification-response)

[DE -- 039 -- RESPONSE CODE 35](#de-039-response-code)

[DE -- 041 -- CARD ACCEPTOR TERMINAL IDENTIFICATION
35](#de-041-card-acceptor-terminal-identification)

[DE -- 042 -- CARD ACCEPTOR IDENTIFICATION CODE
35](#de-042-card-acceptor-identification-code)

[DE -- 043 -- CARD ACCEPTOR NAME/LOCATION
36](#de-043-card-acceptor-namelocation)

[DE -- 048 -- ADDITIONAL PROCESSING DATA
36](#de-048-additional-processing-data)

[DE -- 049 -- CURRENCY CODE, TRANSACTION
36](#de-049-currency-code-transaction)

[DE -- 050 -- CURRENCY CODE, SETTLEMENT
36](#de-050-currency-code-settlement)

[DE -- 051 -- CURRENCY CODE, CARDHOLDER BILLING
36](#de-051-currency-code-cardholder-billing)

[DE -- 054 -- ADDITIONAL AMOUNTS 36](#de-054-additional-amounts)

[DE -- 057 -- AUTHORIZATION LIFE CYCLE
37](#de-057-authorization-life-cycle)

[DE -- 059 -- GEOGRAPHIC DATA 37](#de-059-geographic-data)

[DE -- 061 -- POINT-OF-SERVICE (POS) DATA
38](#de-061-point-of-service-pos-data)

[DE -- 063 -- NETWORK DATA 38](#de-063-network-data)

[DE -- 065 -- SECONDARY BITMAP DATA 38](#de-065-secondary-bitmap-data)

[DE -- 070 -- NETWORK MANAGEMENT INFORMATION CODE
38](#de-070-network-management-information-code)

[DE -- 080 -- DISPUTE ACTION INFORMATION
39](#de-080-dispute-action-information)

[DE -- 090 -- ORIGINAL DATA ELEMENTS 39](#de-090-original-data-elements)

[DE -- 102 -- ACCOUNT IDENTIFICATION 1
40](#de-102-account-identification-1)

[DE -- 108 -- RECEIVER/SENDER DATA 40](#de-108-receiversender-data)

[DE -- 110 -- MINI STATEMENT DATA 41](#de-110-mini-statement-data)

[DE -- 111 -- ADDITIONAL DATA 42](#de-111-additional-data)

[DE -- 123 -- VERIFICATION DATA 43](#de-123-verification-data)

[DE -- 125 -- SUPPORTING INFORMATION 43](#de-125-supporting-information)

[PART 5 -- Appendices 45](#part-5-appendices)

[Appendix A -- Message Matching Criteria
45](#appendix-a-message-matching-criteria)

[Matching Criteria for Clearing Message with Corresponding Authorization
(01xx with
022x](#matching-criteria-for-clearing-message-with-corresponding-authorization-01xx-with-022x-matching)
[Matching)
45](#matching-criteria-for-clearing-message-with-corresponding-authorization-01xx-with-022x-matching)

[Matching Criteria for Reversal Message with Corresponding Original
Message (01xx/02xx
with](#matching-criteria-for-reversal-message-with-corresponding-original-message-01xx02xx-with-042x-matching)
[042x Matching)
45](#matching-criteria-for-reversal-message-with-corresponding-original-message-01xx02xx-with-042x-matching)

[Appendix B -- Authorization Expiration Time
46](#appendix-b-authorization-expiration-time)

[Appendix C -- Data Elements Detailed Definitions
47](#appendix-c-data-elements-detailed-definitions)

[Data Element 003 -- Processing Codes Table
47](#data-element-003-processing-codes-table)

[Data Element 022 -- POS Entry Mode Codes Table
49](#data-element-022-pos-entry-mode-codes-table)

[Data Element 025 -- POS Condition Codes Table
51](#data-element-025-pos-condition-codes-table)

[Data Element 026 -- POS PIN Capture Codes Table
53](#data-element-026-pos-pin-capture-codes-table)

[Data Element 039 -- Response Codes Table
53](#data-element-039-response-codes-table)

[Data Element 043 -- Card Acceptor Name/Location
56](#data-element-043-card-acceptor-namelocation)

[Data Element 048 -- Additional Processing Data
58](#data-element-048-additional-processing-data)

[Data Element 054 -- Additional Amounts Codes Table
60](#data-element-054-additional-amounts-codes-table)

[Data Element 061 -- Point-of-Service Data Codes Table
62](#data-element-061-point-of-service-data-codes-table)

[Data Element 108 -- Receiver/Sender Data Table 71](#_bookmark88)

[Data Element 111 -- Additional Data Table
75](#data-element-111-additional-data-table)

[Data Element 125 - SUPPORTING INFORMATION
90](#data-element-125---supporting-information)

[Data Element 109 -- Advice Reason Code Table
117](#data-element-109-advice-reason-code-table)

[Appendix D -- Sample Messages 122](#appendix-d-sample-messages)

[Sample Network Request/Response Messages (0800, 0810)
122](#sample-network-requestresponse-messages-0800-0810)

[Sample Authorization Request/Response Messages (0100, 0110)
124](#sample-authorization-requestresponse-messages-0100-0110)

[Sample Authorization Advice Request/Response Messages (0120, 0130)
126](#sample-authorization-advice-requestresponse-messages-0120-0130)

[Sample Financial Request/Response Messages (0200, 0210)
128](#sample-financial-requestresponse-messages-0200-0210)

[Sample Financial Advice Request/Response Messages (0220, 0230)
130](#sample-financial-advice-requestresponse-messages-0220-0230)

[Sample Reversal Request/Response Messages (0420, 0430)
132](#sample-reversal-requestresponse-messages-0420-0430)

[Sample Token Notification Message (0620, 0320)
134](#sample-token-notification-message-0620-0320)

[Sample DE-111 -- Additional Data 135](#sample-de-111-additional-data)

[Appendix E -- Possible Values of New Sub-fields in DE-111
138](#appendix-e-possible-values-of-new-sub-fields-in-de-111)

[Stand In Trans Indicator 138](#stand-in-trans-indicator)

[Token Type 138](#token-type)

[Token Status 138](#token-status)

[Token Device Type 139](#token-device-type)

[Token Authorization Request Indicator
139](#token-authorization-request-indicator)

[Token Notification Type 140](#token-notification-type)

[Chargeback Flag (Data Element 111.45)
140](#chargeback-flag-data-element-111.45)

[On-behalf Service (Data Element 111.46)
140](#on-behalf-service-data-element-111.46)

[Fraud Scoring Data (Data Element 111.47)
141](#fraud-scoring-data-data-element-111.47)

[Appendix F -- Token Activation / OTP Notification Message
Identification
143](#appendix-f-token-activation-otp-notification-message-identification)

[Appendix G -- Token Provisioning -- Send OTP Request
143](#appendix-g-token-provisioning-send-otp-request)

[Appendix H -- Token Transactions Flow
144](#appendix-h-token-transactions-flow)

[Appendix I -- Token Creation Green/Red/Yellow Path Identification from
Issue Perspective
145](#appendix-i-token-creation-greenredyellow-path-identification-from-issue-perspective)

[Appendix J -- Message Type Identifiers
146](#appendix-j-message-type-identifiers)

[[Appendix K -- Anticipated Amount Transaction]{.mark}
146](#appendix-j-message-type-identifiers)

# Summary of Changes {#summary-of-changes .unnumbered}

+--------+---------+-------------------------+------------------------+
| >      | > **R   | > **Description of      | > **Where to Look**    |
| **Revi | eleased | > Change**              |                        |
| sion** | > On**  |                         |                        |
+========+=========+=========================+========================+
| >      | > May   | > Updated description   | > Refer to: [[Matching |
| 24.3.1 | > 16th, | > in Appendix A --      | > Criteria             |
|        | > 2023  | > Message Matching      | > for]{.underl         |
|        |         | > Criteria              | ine}](#matching-criter |
|        |         |                         | ia-for-reversal-messag |
|        |         |                         | e-with-corresponding-o |
|        |         |                         | riginal-message-01xx02 |
|        |         |                         | xx-with-042x-matching) |
|        |         |                         | > [[Reversal Message   |
|        |         |                         | > with]{.underl        |
|        |         |                         | ine}](#matching-criter |
|        |         |                         | ia-for-reversal-messag |
|        |         |                         | e-with-corresponding-o |
|        |         |                         | riginal-message-01xx02 |
|        |         |                         | xx-with-042x-matching) |
|        |         |                         | > [[Corresponding      |
|        |         |                         | > Original             |
|        |         |                         | > Message]{.underl     |
|        |         |                         | ine}](#matching-criter |
|        |         |                         | ia-for-reversal-messag |
|        |         |                         | e-with-corresponding-o |
|        |         |                         | riginal-message-01xx02 |
|        |         |                         | xx-with-042x-matching) |
|        |         |                         | > [[(01xx/02xx with    |
|        |         |                         | > 042x                 |
|        |         |                         | > Matching)]{.underl   |
|        |         |                         | ine}](#matching-criter |
|        |         |                         | ia-for-reversal-messag |
|        |         |                         | e-with-corresponding-o |
|        |         |                         | riginal-message-01xx02 |
|        |         |                         | xx-with-042x-matching) |
+--------+---------+-------------------------+------------------------+
| >      | >       | > Updated tag length    | > Refer to: [[DE --    |
| 23.2.2 |  August | > value of Decline      | > 080 --               |
|        | > 31st, | > Reasons from '03' to  | > DISPUTE]{.und        |
|        | > 2023  | > '02' in DE -- 080 --  | erline}](#de-080-dispu |
|        |         | > DISPUTE ACTION        | te-action-information) |
|        |         | > INFORMATION           | > [[ACTION             |
|        |         |                         | > INFORMATION]{.und    |
|        |         |                         | erline}](#de-080-dispu |
|        |         |                         | te-action-information) |
+--------+---------+-------------------------+------------------------+
| >      | >       | > Added new processing  | > Refer to: [[Data     |
| 23.2.2 |  August | > codes to DE 003 --    | > Element 003          |
|        | > 1st,  | > Processing Codes      | > --]{.underline       |
|        | > 2023  | > Table                 | }](#data-element-003-p |
|        |         |                         | rocessing-codes-table) |
|        |         |                         | > [[Processing Codes   |
|        |         |                         | > Table]{.underline    |
|        |         |                         | }](#data-element-003-p |
|        |         |                         | rocessing-codes-table) |
+--------+---------+-------------------------+------------------------+
| >      | > F     | > Added DE 80 --        | > Refer to: [[DE --    |
| 23.2.1 | ebruary | > Dispute Action        | > 080 --               |
|        | > 08th, | > Information           | > DISPUTE]{.und        |
|        | > 2023  | >                       | erline}](#de-080-dispu |
|        |         | > Added Dispute Decline | te-action-information) |
|        |         | > Reasons in Appendix D | > [[ACTION             |
|        |         | >                       | > INFORMATION]{.und    |
|        |         | > Added 80 -- Dispute   | erline}](#de-080-dispu |
|        |         | > Action Information in | te-action-information) |
|        |         | > "Message Layouts"     | >                      |
|        |         | > section               | > Refer to: [[Data     |
|        |         |                         | > Element 80           |
|        |         |                         | > Dispute]{.unde       |
|        |         |                         | rline}](#_bookmark104) |
|        |         |                         | > [[Action Information |
|        |         |                         | > Tag 05               |
|        |         |                         | > Decline]{.unde       |
|        |         |                         | rline}](#_bookmark104) |
|        |         |                         | > [R                   |
|        |         |                         | easons](#_bookmark104) |
|        |         |                         | >                      |
|        |         |                         | > Refer to: [PART 2 -- |
|        |         |                         | > Message              |
|        |         |                         | > Layouts](#p          |
|        |         |                         | art-2-message-layouts) |
+--------+---------+-------------------------+------------------------+
| > 2    | > Se    | > Added a Token Status  | > Refer to: [[Appendix |
| 2.09.1 | ptember | > D                     | > E --                 |
|        | > 21st, |                         | > Possible]{.unde      |
|        | > 2022  |                         | rline}](#token-status) |
|        |         |                         | > [[Values of New      |
|        |         |                         | > Sub-fields in        |
|        |         |                         | > DE-111]{.unde        |
|        |         |                         | rline}](#token-status) |
+--------+---------+-------------------------+------------------------+
| > 2    | > May   | > Incremental           | > Refer to: [[Data     |
| 2.06.1 | > 26th, | > Authorization         | > Element 111          |
|        | > 2022  | > Indicator Support     | > --]{.underlin        |
|        |         | > Added for Efund/FIS   | e}](#data-element-111- |
|        |         |                         | additional-data-table) |
|        |         |                         | > [[Additional Data    |
|        |         |                         | > Table]{.underlin     |
|        |         |                         | e}](#data-element-111- |
|        |         |                         | additional-data-table) |
+--------+---------+-------------------------+------------------------+
| > 2    | > April | > Segregation of 'GV'   | > Refer to: [[Data     |
| 2.05.1 | > 1st,  | > response code for     | > Element 039          |
|        | > 2022  | > status inquiry /      | > --]{.underli         |
|        |         | > Account verification  | ne}](#data-element-039 |
|        |         | > transactions in case  | -response-codes-table) |
|        |         | > of declined due to    | > [[Response Codes     |
|        |         | > invalid card status   | > Table]{.underli      |
|        |         | > ('SX') or expiry      | ne}](#data-element-039 |
|        |         | > ('EX'). Token         | -response-codes-table) |
|        |         | > Authorization         |                        |
|        |         | > Request - TAR red     |                        |
|        |         | > path response code    |                        |
|        |         | > updated as 'TR' from  |                        |
|        |         | > 'TX'                  |                        |
+--------+---------+-------------------------+------------------------+
| > 2    | > D     | > Support Added for     | > Refer to:            |
| 1.12.2 | ecember | > Sender Data for Visa. | >                      |
|        | > 08th, |                         | > [[DE -- 108 --       |
|        | > 2021  |                         | > Receiver/Sender      |
|        |         |                         | > Dat                  |
|        |         |                         | a]{.underline}](#de-10 |
|        |         |                         | 8-receiversender-data) |
+--------+---------+-------------------------+------------------------+
| > 2    | > N     | > Support added for     | > Refer to: [[Fiserv   |
| 1.12.1 | ovember | > Fiserv based auth-    | > DE                   |
|        | > 30th, | > hosts                 | > 43]{.und             |
|        | > 2021  |                         | erline}](#de-043-card- |
|        |         |                         | acceptor-namelocation) |
|        |         |                         | > [[Fiserv DE          |
|        |         |                         | > 90]{.und             |
|        |         |                         | erline}](#de-080-dispu |
|        |         |                         | te-action-information) |
|        |         |                         | > [[Fiserv DE          |
|        |         |                         | > 1                    |
|        |         |                         | 09]{.underline}](#de-1 |
|        |         |                         | 09-advice-reason-code) |
|        |         |                         | > [[Fiserv DE          |
|        |         |                         | > 11                   |
|        |         |                         | 1]{.underline}](#de-11 |
|        |         |                         | 0-mini-statement-data) |
+--------+---------+-------------------------+------------------------+
| > 2    | >       | > Addition of new Token | > Refer to:            |
| 1.10.1 | October | > Device Type Addition  | >                      |
|        | > 11th, | > of new Dataset in DE  | > Token Device Type    |
|        | > 2021  | > 125 for Visa          | > Data Element 125     |
+--------+---------+-------------------------+------------------------+
| > 2    | > Se    | > Addition of new Field | > Refer to:            |
| 1.09.1 | ptember | > for Mastercard        | >                      |
|        | > 7th,  |                         | > Data Element 108     |
|        | > 2021  |                         |                        |
+--------+---------+-------------------------+------------------------+

+--------+---------+-------------------------+------------------------+
| > 2    | >       | > Addition of new       | > Refer to:            |
| 1.08.2 |  August | > fields 33 and 90      | >                      |
|        | > 25th, |                         | > Data Element 33      |
|        | > 2021  |                         | >                      |
|        |         |                         | > Data Element 90      |
+========+=========+=========================+========================+
| >      | >       | > Addition of new Field | > Refer to:            |
|  21.08 |  August | > 59 for Mastercard and | >                      |
|        | > 15th, | > Visa                  | > Data Element 59      |
|        | > 2021  |                         |                        |
+--------+---------+-------------------------+------------------------+
| >      | > July  | > Field 125 and Field   | > Refer to:            |
|  21.07 | > 15th, | > 111 updated           | >                      |
|        | > 2021  |                         | > Data Element 125 --  |
|        |         |                         | > Discover Data        |
|        |         |                         | > Element 111          |
+--------+---------+-------------------------+------------------------+
| >      | > June  | > Field 125 updated     | > Refer to:            |
|  21.06 | > 1st,  |                         | >                      |
|        | > 2021  |                         | > [Data Element 125 -  |
|        |         |                         | >                      |
|        |         |                         |  Discover]{.underline} |
+--------+---------+-------------------------+------------------------+
| >      | > March | > Addition of           | > Refer to:            |
|  21.06 | > 30th, | > Transaction types     | >                      |
|        | > 2021  |                         | > [[Data Element       |
|        |         |                         | > 3]{.underline}](#d   |
|        |         |                         | e-003-processing-code) |
+--------+---------+-------------------------+------------------------+
| >      | > March | > Addition of a Field   | > Refer to:            |
|  21.06 | > 30th, | > 125 for Discover.     | >                      |
|        | > 2021  |                         | > [Data Element 125 -  |
|        |         |                         | >                      |
|        |         |                         |  Discover]{.underline} |
+--------+---------+-------------------------+------------------------+
| >      | > March | > Addition of a Field   | > Refer to:            |
|  21.06 | > 30th, | > 111 for Discover.     | >                      |
|        | > 2021  |                         | > Data Element 111 -   |
|        |         |                         | > Discover             |
+--------+---------+-------------------------+------------------------+
| >      | > March | > Addition of a Field   | > Refer to:            |
|  21.06 | > 30th, | > 109 for Discover.     | >                      |
|        | > 2021  |                         | > Data Element 109     |
+--------+---------+-------------------------+------------------------+
| >      | > May   | > Updated description   | > Refer to:            |
|  21.05 | > 4th,  | > for DE 111.47         | >                      |
|        | > 2021  | > (MasterCard Format)   | > Fraud Scoring Data   |
|        |         | > to show that it is in | > (Data Element        |
|        |         | > TLV format.           | > 111.47)              |
+--------+---------+-------------------------+------------------------+
| >      | > April | > Updated part 3. Added | > Refer to: Part-3     |
|  21.04 | > 13th, | > co-operative auth     |                        |
|        | > 2021  | > model. Improved       |                        |
|        |         | > explanations of       |                        |
|        |         | > message ﬂows          |                        |
+--------+---------+-------------------------+------------------------+
| >      | > March | > 3DS Related Data      | > Refer to:            |
|  21.04 | > 23rd, | > Added                 | >                      |
|        | > 2021  |                         | > Data Element 111     |
+--------+---------+-------------------------+------------------------+
| >      | > March | > Updated PART 2 --     | > Refer to: Message    |
|  21.03 | > 9th,  | > Message Layouts for   | > Layouts              |
|        | > 2021  | > DE02                  |                        |
+--------+---------+-------------------------+------------------------+
| >      | > N     | > Fee chunks for excess | > Refer to:            |
|  20.12 | ovember | > usage fee             | >                      |
|        | > 26th, |                         | > DE54 chunk 46-47     |
|        | > 2020  |                         |                        |
+--------+---------+-------------------------+------------------------+
| > 2    | > N     | > Description of DE57   | > Refer to:            |
| 0.11.2 | ovember | > updated               | >                      |
|        | > 10th, |                         | > Data Element 57      |
|        | > 2020  |                         |                        |
+--------+---------+-------------------------+------------------------+
| > 2    | > N     | > Value of POS Entry    | > Refer to:            |
| 0.11.1 | ovember | > Mode (29) updated     | >                      |
|        | > 2nd,  |                         | > POS Entry Mode Codes |
|        | > 2020  |                         | > Table                |
+--------+---------+-------------------------+------------------------+
| > 2    | >       | > Expire Pre Auth       | > Refer to:            |
| 0.10.2 | October | > Reversal Message      | >                      |
|        | > 9th,  | > Indicator             | > Data Element 048     |
|        | > 2020  |                         |                        |
+--------+---------+-------------------------+------------------------+

+--------+---------+-------------------------+------------------------+
| > 2    | > Se    | > Token Device Bound    | > Refer to:            |
| 0.10.1 | ptember | > Fields Added          | >                      |
|        | > 30th, |                         | > [[Data Element       |
|        | > 2020  |                         | > 111]{.underline}](#d |
|        |         |                         | e-111-additional-data) |
+========+=========+=========================+========================+
| >      | > Se    | > STAR Access Support   | > Refer to:            |
| 20.9.1 | ptember | > Added                 | >                      |
|        | > 01st, |                         | > [[Data Element       |
|        | > 2020  |                         | > 048]{.unde           |
|        |         |                         | rline}.](#de-048-addit |
|        |         |                         | ional-processing-data) |
|        |         |                         | >                      |
|        |         |                         | > [[Additional Amounts |
|        |         |                         | > Codes                |
|        |         |                         | > Tab                  |
|        |         |                         | le]{.underline}](#data |
|        |         |                         | -element-054-additiona |
|        |         |                         | l-amounts-codes-table) |
|        |         |                         | > [[Data Element       |
|        |         |                         | > 63]{.underline}]     |
|        |         |                         | (#de-063-network-data) |
|        |         |                         | >                      |
|        |         |                         | > [[Data Element       |
|        |         |                         | > 1                    |
|        |         |                         | 09]{.underline}](#de-1 |
|        |         |                         | 09-advice-reason-code) |
|        |         |                         | > [[Data Element       |
|        |         |                         | > 111]{.underline}](#d |
|        |         |                         | e-111-additional-data) |
+--------+---------+-------------------------+------------------------+
| >      | > July  | > Incremental           | > Refer to:            |
| 20.7.1 | > 25th, | > Authorizations and    | >                      |
|        | > 2020  | > Multi- Clearing       | > [[Data Element       |
|        |         | > Transactions related  | > 048]{.unde           |
|        |         | > indicators added for  | rline}.](#de-048-addit |
|        |         | > MC DMS based Clients  | ional-processing-data) |
|        |         |                         | > [[Data Element       |
|        |         |                         | > 1                    |
|        |         |                         | 09]{.underline}](#de-1 |
|        |         |                         | 09-advice-reason-code) |
|        |         |                         | > [[Data Element       |
|        |         |                         | > 111]{.underline}](#d |
|        |         |                         | e-111-additional-data) |
+--------+---------+-------------------------+------------------------+
| >      | > May   | > Application           | > Refer to:            |
| 20.5.1 | > 04th, | > Transaction Counter   | >                      |
|        | > 2020  | > (ATC) support added   | > [[Data Element       |
|        |         | > in 48.8 and new       | > 048]{.unde           |
|        |         | > response code 'AI'    | rline}.](#de-048-addit |
|        |         | > introduced            | ional-processing-data) |
|        |         |                         | > [[Response           |
|        |         |                         | > Codes]{.underli      |
|        |         |                         | ne}](#data-element-039 |
|        |         |                         | -response-codes-table) |
+--------+---------+-------------------------+------------------------+
| >      | > March | > Over Limit Fee and    | > Refer to             |
| 20.3.1 | > 18th, | > Over Payment Fee      | > [[Additional Amounts |
|        | > 2020  | > chunks 07 and 08      | > Cod                  |
|        |         | > added                 | es]{.underline}](#de-0 |
|        |         |                         | 54-additional-amounts) |
|        |         |                         | > [[Tab                |
|        |         |                         | le]{.underline}](#de-0 |
|        |         |                         | 54-additional-amounts) |
+--------+---------+-------------------------+------------------------+
| >      | >       | > UnionPay Support      | > Refer to: [[UnionPay |
| 20.2.1 | January | > Added, Update some    | > DE111]{.und          |
|        | > 31st, | > values for DE61       | erline}](#_bookmark91) |
|        | > 2020  |                         | > [[UnionPay           |
|        |         |                         | > DE125]{.und          |
|        |         |                         | erline}](#_bookmark93) |
|        |         |                         | > [Field               |
|        |         |                         | > 61](#de-061-poin     |
|        |         |                         | t-of-service-pos-data) |
+--------+---------+-------------------------+------------------------+
| >      | > D     | > Default timeout value | > Refer to Timeout     |
| 20.1.1 | ecember | > added                 | > Communication        |
|        | > 23rd, |                         | > [Exception           |
|        | > 2019  |                         | > Flows]{.underline}   |
+--------+---------+-------------------------+------------------------+
| > 19   | > Se    | > New Field 109 Added , | > Refer to [[Field     |
| .9.1.1 | ptember | > DE54 chunk 06 added   | > 1                    |
|        | > 17th, |                         | 09]{.underline}](#de-1 |
|        | > 2019  |                         | 09-advice-reason-code) |
+--------+---------+-------------------------+------------------------+
| > 19   | > Se    | > Addition of:          | > Refer to: [[Appendix |
| .8.1.2 | ptember | >                       | > G]{.underline}](#app |
|        | > 12th, | > New DE-007 added in   | endix-g-token-provisio |
|        | > 2019  | > Token Provisioning -- | ning-send-otp-request) |
|        |         | > Send OTP Request      |                        |
|        |         | > (0600)                |                        |
+--------+---------+-------------------------+------------------------+
| > 19   | >       | > Addition of:          | > Refer to: [[Appendix |
| .8.1.1 |  August | >                       | > G]{.underline}](#app |
|        | > 16th, | > Modified MTI 0100 --  | endix-g-token-provisio |
|        | > 2019  | > Token Provisioning -- | ning-send-otp-request) |
|        |         | > Send OTP Request to   |                        |
|        |         | > MTI 0600              |                        |
|        |         | > Administrative        |                        |
|        |         | > request               |                        |
|        |         | >                       |                        |
|        |         | > Appendix-G modified,  |                        |
|        |         | > New field 02 added in |                        |
|        |         | > request. Field 111    |                        |
|        |         | > modified DE-25 POS    |                        |
|        |         | > Condition code        |                        |
|        |         | > modified from 59 to   |                        |
|        |         | > 66                    |                        |
+--------+---------+-------------------------+------------------------+
| >      | > July  | > Addition of:          | > Refer to: [[Message  |
| 19.7.1 | > 16th, | >                       | > La                   |
|        | > 2019  | > New MTI 0100 -- Token | youts]{.underline}](#p |
|        |         | > Provisioning -- Send  | art-2-message-layouts) |
|        |         | > OTP Request           | >                      |
|        |         | >                       | > [[Sub Elements of DE |
|        |         | > New sub-fields 111.47 | > 111]{.underlin       |
|        |         | > & 111.48. Appendix-G. | e}](#data-element-111- |
|        |         |                         | additional-data-table) |
|        |         |                         | > [[Appendix           |
|        |         |                         | > G]{.underline}](#app |
|        |         |                         | endix-g-token-provisio |
|        |         |                         | ning-send-otp-request) |
+--------+---------+-------------------------+------------------------+
| >      | > June  | > Addition of new       | > Refer to [[Data      |
| 19.7.1 | > 25th, | > sub-fields 48.7 &     | > Element              |
|        | > 2019  | > 48.8.                 | > 048]{.unde           |
|        |         |                         | rline}.](#de-048-addit |
|        |         |                         | ional-processing-data) |
+--------+---------+-------------------------+------------------------+

+--------+---------+-------------------------+------------------------+
| >      | > April | > Description change    | > Refer to [[Data      |
| 19.4.1 | > 18th, | > for DE-07             | > Element              |
|        | > 2019  |                         | > 07]{.und             |
|        |         |                         | erline}](#de-007-trans |
|        |         |                         | mission-date-and-time) |
+========+=========+=========================+========================+
| >      | > April | > Addition of new       | > Refer to [[Response  |
| 19.4.1 | > 18th, | > response code value   | > Codes]{.underlin     |
|        | > 2019  | > 99                    | e}.](#data-element-039 |
|        |         |                         | -response-codes-table) |
+--------+---------+-------------------------+------------------------+
| >      | > April | > Addition of a new     | > Refer to [[Data      |
| 19.4.1 | > 18th, | > sub-field 48.4, 48.5, | > Element              |
|        | > 2019  | >                       | > 048]{.unde           |
|        |         | > 48.6 in DE-048.       | rline}.](#de-048-addit |
|        |         |                         | ional-processing-data) |
+--------+---------+-------------------------+------------------------+
| >      | > April | > Addition of a new     | > Refer to [[Data      |
| 19.4.1 | > 10th, | > sub-field 48.3 in DE- | > Element              |
|        | > 2019  | > 048.                  | > 048]{.unde           |
|        |         |                         | rline}.](#de-048-addit |
|        |         |                         | ional-processing-data) |
+--------+---------+-------------------------+------------------------+
| >      | > April | > Addition of a new     | > Refer to [[Response  |
| 19.4.1 | > 10th, | > Response Code value   | > Codes]{.underli      |
|        | > 2019  | > 1A -- Strong Customer | ne}](#data-element-039 |
|        |         | > Authentication        | -response-codes-table) |
|        |         | > Required in DE-39     | > section.             |
+--------+---------+-------------------------+------------------------+
| >      | > April | > Addition of new Field | > Refer to [[DE --     |
| 19.4.1 | > 10th, | > 110 -- Mini Statement | > 110                  |
|        | > 2019  | > Data.                 | ]{.underline}.](#de-11 |
|        |         |                         | 0-mini-statement-data) |
+--------+---------+-------------------------+------------------------+
| >      | > April | > Addition of new       | > Refer to             |
| 19.4.1 | > 10th, | > process code value 34 | > [[Processing         |
|        | > 2019  | > (ATM Mini Statement)  | > C                    |
|        |         | > in Field 3---         | odes]{.underline}.](#d |
|        |         | > Processing Code,      | e-003-processing-code) |
|        |         | > position 1--2.        |                        |
+--------+---------+-------------------------+------------------------+
| >      | > March | > Conditional new       | > Refer to [[Data      |
| 19.2.1 | > 1st,  | > Field-048 (Additional | > Element --           |
|        | > 2019  | > Processing Data)      | > 048]{.und            |
|        |         | > added in the ISO      | erline}](#de-048-addit |
|        |         | > specifications.       | ional-processing-data) |
+--------+---------+-------------------------+------------------------+
| >      | >       | > Description added of  | > DE 111 Mastercard    |
| 19.1.1 | January | > Sub field DE 111 and  | > Format:Sub Field     |
|        | > 10th, | > DE125                 | > 111.4, 111.18,       |
|        | > 2019  |                         | > 111.19, 125.6        |
+--------+---------+-------------------------+------------------------+
| >      | > July  | > Addition of new sub   | > DE 111 Mastercard    |
| 18.7.1 | > 5th,  | > field in DE 111 On-   | > Format: Sub Field    |
|        | > 2018  | > behalf Service, Fraud | > 111.46, 111.47       |
|        |         | > Scoring Data          |                        |
+--------+---------+-------------------------+------------------------+
| >      | > July  | > Addition of new sub   | > DE 111 Visa Format:  |
| 18.7.1 | > 5th,  | > field in DE 111       | > Sub Field 111.46 DE  |
|        | > 2018  | > Chargeback flag       | > 111 Mastercard       |
|        |         |                         | > Format: Sub Field    |
|        |         |                         | > 111.45               |
|        |         |                         | >                      |
|        |         |                         | > DE 111 Efund Format: |
|        |         |                         | > Sub Field 111.11     |
|        |         |                         | >                      |
|        |         |                         | > DE 111 Star Format:  |
|        |         |                         | > Sub Field 111.4      |
+--------+---------+-------------------------+------------------------+
| >      | > June  | > Addition of new code  | > DE 111 Token         |
| 18.6.1 | > 20th, | > in:                   | > Notification Type    |
|        | > 2018  | >                       |                        |
|        |         | > Appendix H, Token     |                        |
|        |         | > Event Notification    |                        |
|        |         | > Section.              |                        |
|        |         | >                       |                        |
|        |         | > Token Notification    |                        |
|        |         | > Type.                 |                        |
+--------+---------+-------------------------+------------------------+
| >      | > May   | > Addition of new sub   | > DE 111 Visa Format   |
| 18.5.1 | > 21st, | > field in DE 111 i.e.  | > Sub Field 111.45     |
|        | > 2018  | > 111.45                |                        |
+--------+---------+-------------------------+------------------------+
| >      | > April | > Addition of new sub   | > DE 111 MasterCard    |
| 18.5.1 | > 26th, | > field in DE 111 i.e.  | > Format Sub Field     |
|        | > 2018  | > 111.44                | > 111.44               |
+--------+---------+-------------------------+------------------------+
| >      | > April | > Text updated          | > Appendix F, Appendix |
| 18.5.1 | > 26th, |                         | > H                    |
|        | > 2018  |                         |                        |
+--------+---------+-------------------------+------------------------+
| >      | > July  | > Addition of new       | > See section [[Sub    |
| 18.7.1 | > 4th,  | > sub-field 111.47      | > Elements of          |
|        | > 2018  | > (Fraud Scoring Data)  | > DE-111]{.und         |
|        |         |                         | erline}](#_bookmark90) |
|        |         |                         | > [[when DE-63.7 =     |
|        |         |                         | > 'MASTERCARD']{.und   |
|        |         |                         | erline}](#_bookmark90) |
+--------+---------+-------------------------+------------------------+
| >      | > July  | > Addition of new       | > See section [[Sub    |
| 18.7.1 | > 4th,  | > sub-field 111.46 (On- | > Elements of          |
|        | > 2018  | > behalf Service)       | > DE-111]{.und         |
|        |         |                         | erline}](#_bookmark90) |
|        |         |                         | > [[when DE-63.7 =     |
|        |         |                         | > 'MASTERCARD']{.und   |
|        |         |                         | erline}](#_bookmark90) |
+--------+---------+-------------------------+------------------------+
| >      | > July  | > Addition of new       | > See section [[Sub    |
| 18.7.1 | > 4th,  | > sub-field 111.45      | > Elements of          |
|        | > 2018  | > (Chargeback flag)     | > DE-111]{.und         |
|        |         |                         | erline}](#_bookmark90) |
|        |         |                         | > [[when DE-63.7 =     |
|        |         |                         | > 'MASTERCARD']{.und   |
|        |         |                         | erline}](#_bookmark90) |
+--------+---------+-------------------------+------------------------+

# PART 1 -- Message Structure {#part-1-message-structure .unnumbered}

## ISO 8583 Protocol Format {#iso-8583-protocol-format .unnumbered}

+-------------+-------------------+-----------------+-----------------+
| > **Message | > **Message Type  | > **Bitmaps     | > **Data        |
| > Length**  | > Identifier      | > (Primary &    | > Elements**    |
|             | > (MTI)**         | > Secondary)**  |                 |
+=============+===================+=================+=================+
| > 2 or 4    | > 4 Bytes         | > 8 Bytes each  | > Variable      |
| > Bytes     |                   |                 |                 |
+-------------+-------------------+-----------------+-----------------+

##### Message Length {#message-length .unnumbered}

> The message length is the first 2 or 4 bytes of the message. The
> number of bytes which contains message length depends on the type of
> field configuration. Below are the two possible configurations:
>
> **ASCII format** -- The message length will be represented in 4-bytes
> ASCII format where the first 4 bytes of the message represents length.
> For example, for a 68 bytes message, the message length will be like
> 0068.
>
> **Bytes format** -- The first 2 bytes of the message will represent
> message length. The length will be in packed hexadecimal format.
>
> The message length will not include the length of bytes used to
> represent message length, which means Message Length = Length MTI +
> Length Bitmaps + Length Data Elements
>
> For the **bytes format**, below pseudo code can be used to extract
> message length:

##### Message Type Identifier (MTI) {#message-type-identifier-mti .unnumbered}

> The n-4 ASCII representation of the Message, called MTI. It is the
> first mandatory data element in ISO 8583 message and specifies general
> message category (e.g., financial or reversal).
>
> Refer to [[Appendix
> J]{.underline}](#appendix-j-message-type-identifiers) for the list of
> supported message type identifiers.

#### Message Bitmaps {#message-bitmaps .unnumbered}

> The data elements transmitted in the message are not fixed; bitmaps
> specify which data elements are present and which are not. The length
> of a bitmap can be of 8 or 16 bytes (64 binary values) depending upon
> the format of message i.e. ASCII format or Bytes format.

1.  **ASCII format** -- A bitmap will be comprised of 16 unpacked
    > hexadecimal digits where each digit will represent 4 bits.

2.  **Bytes format** -- A bitmap will be represented in 8-bytes packed
    > hexadecimal format. Each byte will contain 2 hexadecimal digits
    > i.e. 8 binary value.

> Each bitmap will contain 64 bits where each bit represents the
> presence of data element on that bit number. i2c's ISO 8583
> specification can contain two bitmaps i.e. Primary (mandatory) &
> Secondary (optional). The detail of each bitmap is described below.

##### Primary Bitmap {#primary-bitmap .unnumbered}

> Every message includes the Primary Bitmap. It is of 8 Bytes (64 bits)
> length, positioned after the message type identifier. Except for the
> first bit, each bit of the primary bitmap is associated with the
> corresponding data element, starting from 2 to 64. Each bit indicates
> the presence or absence of its associated data element.

-   If a bit is 0, the data element associated with the bit is not
    > present.

-   If a bit is 1, the data element associated with the bit is present
    > in the message.

> For example:
>
> The first bit of the Primary Bitmap indicates the presence of
> Secondary Bitmap. If the first bit is 1, a Secondary Bitmap follows
> this Bitmap.

##### Secondary Bitmap {#secondary-bitmap .unnumbered}

> Like the Primary Bitmap, Secondary Bitmap is also of 8 Bytes (64 bits)
> length, positioned after primary bitmap in the i2c message. Except for
> the first bit, each bit of the secondary bitmap is associated with the
> corresponding data element, starting from 66 to 128. Each bit
> indicates the presence or absence of its associated data element.

-   If a bit is 0, the data element associated with the bit is not
    > present.

-   If a bit is 1, the data element associated with the bit is present
    > in the message.

> For example:
>
> The first bit of the Secondary Bitmap indicates the presence of a
> Third Bitmap. If the first bit is 1, a Third Bitmap follows this
> Bitmap. This bit will always be 0.

##### Third Bitmap {#third-bitmap .unnumbered}

> The third bitmap is reserved for future use.

## Message Data Elements {#message-data-elements .unnumbered}

> The Message Data Elements section explains the available fields along
> with their formats that can be a part of the i2c message.

# PART 2 -- Message Layouts {#part-2-message-layouts .unnumbered}

> C = Conditional, CE = Conditional Echo, M = Mandatory, ME = Mandatory
> Echo, Blank Space = Not Available or Not Required
>
> \* For Non-PCI Compliant Auth-Host, secure data elements like PIN,
> CVV1, and CVV2 etc. will not be sent.
>
> **0100/0110\* --** Token Send OTP Request

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>010</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>011</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>011</strong></p>
<p><strong>0*</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>011</strong></p>
<p><strong>0*</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>012</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>013</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>020</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>021</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>022</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>023</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>042</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>043</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>080</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>081</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>030</strong></p>
<p><strong>2</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>031</strong></p>
<p><strong>2</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>062</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>06</strong></p>
<p><strong>30</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Primary Account Number</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Processing Code</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Amount</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Settlement Amount</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Cardholder Billing Amount</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Transmissio n Date/Time</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Settlement Conversion Rate</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Conversion Rate</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>Trace Number</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>Local Time</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>Local Date</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>Date, Expiration</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>Date, Settlement</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>Merchant Category Code (MCC)</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>010</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>011</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>011</strong></p>
<p><strong>0*</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>011</strong></p>
<p><strong>0*</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>012</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>013</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>020</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>021</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>022</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>023</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>042</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>043</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>080</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>081</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>030</strong></p>
<p><strong>2</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>031</strong></p>
<p><strong>2</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>062</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>06</strong></p>
<p><strong>30</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>Point of Service Entry Mode Code</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>POS</p>
<p>Condition Code</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>POS PIN</p>
<p>Capture Code</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>Amount, Transaction Fee</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td><blockquote>
<p>Amount, Settlement Fee</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>Acquirer Institution Identification Code</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td><blockquote>
<p>Retrieval Reference</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>Auth-ID Code</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td><blockquote>
<p>Response Code</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>41</p>
</blockquote></td>
<td><blockquote>
<p>Card Acceptor Terminal ID</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>42</p>
</blockquote></td>
<td><blockquote>
<p>Card Acceptor ID Code</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>43</p>
</blockquote></td>
<td><blockquote>
<p>Card Acceptor Name/Locati on</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>Additional Processing Data</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td><blockquote>
<p>Currency Code, Currency</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>010</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>011</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>011</strong></p>
<p><strong>0*</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>011</strong></p>
<p><strong>0*</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>012</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>013</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>020</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>021</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>022</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>023</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>042</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>043</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>080</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>081</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>030</strong></p>
<p><strong>2</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>031</strong></p>
<p><strong>2</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>062</strong></p>
<p><strong>0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>06</strong></p>
<p><strong>30</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>Currency Code, Settlement</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td><blockquote>
<p>Currency Code, Card- Holder Billing</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54</p>
</blockquote></td>
<td><blockquote>
<p>Additional Amounts</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>57</p>
</blockquote></td>
<td><blockquote>
<p>Authorizatio n Life Cycle</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>61</p>
</blockquote></td>
<td><blockquote>
<p>Point-of- Service (POS) Data</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63</p>
</blockquote></td>
<td><blockquote>
<p>Network Data</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>65</p>
</blockquote></td>
<td><blockquote>
<p>Tertiary Bitmap</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>70</p>
</blockquote></td>
<td><blockquote>
<p>Network Managemen t Information Code</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>Dispute Action Information</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>102</p>
</blockquote></td>
<td><blockquote>
<p>Account Identification 1</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>110</p>
</blockquote></td>
<td><blockquote>
<p>Mini Statement Data</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>111</p>
</blockquote></td>
<td><blockquote>
<p>Additional Data, Private Acquirer</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>123</p>
</blockquote></td>
<td><blockquote>
<p>Verification Data</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>125</p>
</blockquote></td>
<td><blockquote>
<p>Supporting Information</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
<td><blockquote>
<p>ME</p>
</blockquote></td>
</tr>
</tbody>
</table>

# PART 3 -- Co-operative Auth Model {#part-3-co-operative-auth-model .unnumbered}

## Block Diagram {#block-diagram .unnumbered}

![](./image3.png){width="4.77125in" height="4.90875in"}

## Connectivity Message Flows {#connectivity-message-flows .unnumbered}

> i2c will establish connection with Auth host. In case of
> disconnection, i2c will retry to establish connection.

##### Sign-On Message {#sign-on-message .unnumbered}

> Once connection is established, i2c will send sign on. Sign on must be
> successful before sending transaction to auth host.

![](./image4.jpeg){width="4.515520559930009in"
height="1.298124453193351in"}

##### Sign-Off Message {#sign-off-message .unnumbered}

> Auth host can initiate Sign-off message to not receive further
> transactions. Once Sign-off is performed by Auth host, Sign-on is
> expected by Auth host to resume transaction processing.

![](./image5.png){width="4.543437226596676in"
height="1.2911450131233595in"}

##### Echo/Health Check Message {#echohealth-check-message .unnumbered}

> Echo messages are sent on socket after defined intervals in-case there
> is no transaction in defined time- frame. Echo messages are sent by
> i2c to auth host.

![](./image6.png){width="4.489374453193351in"
height="1.2856244531933507in"}

## Transaction Flows {#transaction-flows .unnumbered}

##### Authorized by Auth-Host Processor {#authorized-by-auth-host-processor .unnumbered}

![](./image7.jpeg){width="6.42036854768154in" height="2.62in"}

+----+-----------------------------------------------------------------+
| ** | > **Description**                                               |
| St |                                                                 |
| ep |                                                                 |
| ** |                                                                 |
+====+=================================================================+
| 1  | > Network initiates a transaction request/(0xx0) message to i2c |
+----+-----------------------------------------------------------------+
| 2  | > Pre-processing process is executed at i2c prior to sending    |
|    | > transaction to auth host.                                     |
+----+-----------------------------------------------------------------+
| 3  | > i2c forwards the Financial Transaction Request message to the |
|    | > auth host                                                     |
+----+-----------------------------------------------------------------+
| 4  | > The auth host generates a success response(0X10/0X30) and     |
|    | > sends it to i2c.                                              |
+----+-----------------------------------------------------------------+
| 5  | > Post-processing process is executed at i2c prior to sending   |
|    | > response to network.                                          |
+----+-----------------------------------------------------------------+
| 6  | > i2c generates a success response (0x10/0x30) message and      |
|    | > sends it to network.                                          |
+----+-----------------------------------------------------------------+

##### Declined by Auth-Host Processor {#declined-by-auth-host-processor .unnumbered}

![](./image8.jpeg){width="6.323532370953631in"
height="2.5790616797900263in"}

+----+-----------------------------------------------------------------+
| ** | > **Description**                                               |
| St |                                                                 |
| ep |                                                                 |
| ** |                                                                 |
+====+=================================================================+
| 1  | > Network initiates a transaction request/(0xx0) message to i2c |
+----+-----------------------------------------------------------------+
| 2  | > Pre-processing process is executed at i2c prior to sending    |
|    | > transaction to auth host.                                     |
+----+-----------------------------------------------------------------+
| 3  | > i2c forwards the Financial Transaction Request message to the |
|    | > auth host                                                     |
+----+-----------------------------------------------------------------+
| 4  | > The auth host generates a decline response (0X10/0X30) and    |
|    | > sends it to i2c.                                              |
+----+-----------------------------------------------------------------+
| 5  | > Post-processing process is executed at i2c prior to sending   |
|    | > response to network.                                          |
+----+-----------------------------------------------------------------+
| 6  | > i2c generates a decline response (0x10/0x30) message and      |
|    | > sends it to network.                                          |
+----+-----------------------------------------------------------------+

## Exceptions Processing Flows {#exceptions-processing-flows .unnumbered}

##### Fail at i2c Pre-Processing {#fail-at-i2c-pre-processing .unnumbered}

> If a transaction fails pre-processing at i2c, then only a configurable
> notification will be sent to the auth host processor. The Decline
> response to the network will be sent (for non-force post
> transactions).

![](./image9.png){width="5.227910104986877in"
height="1.7652077865266842in"}

+-----+----------------------------------------------------------------+
| **  | > **Description**                                              |
| Ste |                                                                |
| p** |                                                                |
+=====+================================================================+
| 1   | > Network initiates a transaction request/(0xx0) message to    |
|     | > i2c                                                          |
+-----+----------------------------------------------------------------+
| 2   | > Transaction failed at i2c in pre-processing                  |
+-----+----------------------------------------------------------------+
| 3   | > i2c generates a decline response (0x10/0x30) message and     |
|     | > sends it to network.                                         |
+-----+----------------------------------------------------------------+
| 4   | > i2c will send a decline notification to auth host            |
+-----+----------------------------------------------------------------+
| 5   | > Auth host generates a transaction request                    |
|     | > response(0x10/0x30) message and sends it to i2c.             |
+-----+----------------------------------------------------------------+

##### Stand-in Processing Auth Host Down {#stand-in-processing-auth-host-down .unnumbered}

> If there occurs an exception in sending the request message to the
> auth host due to non- availability of auth host, then either a decline
> notification or a forced post notification will be sent to the auth
> host based on auth host configuration with i2c.

![](./image10.jpeg){width="6.237090988626422in"
height="2.09625in"}

+----+-----------------------------------------------------------------+
| *  | > **Description**                                               |
| *S |                                                                 |
| ta |                                                                 |
| ge |                                                                 |
| ** |                                                                 |
+====+=================================================================+
| >  | > Network initiates a transaction request/(0xx0) message to i2c |
|  1 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > i2c initiates a Financial Transaction Request message, but    |
|  2 | > unable to send this to auth host because of network           |
|    | > communication failure.                                        |
+----+-----------------------------------------------------------------+
| >  | > i2c will perform Stand In processing.                         |
|  3 | >                                                               |
|    | > Stand-in processing is configurable (Allowed/Not Allowed).    |
+----+-----------------------------------------------------------------+
| 4  | > If auth host has configuration with i2c to decline            |
| .1 | > transaction in its non-availability, then i2c sends a decline |
|    | > response (0x10/0x30) message to network.                      |
+----+-----------------------------------------------------------------+
| 4  | > If auth host has configuration with i2c to process            |
| .2 | > transaction in its non-availability, then i2c sends a success |
|    | > response (0x10/0x30) message to network.                      |
|    | >                                                               |
|    | > Stand-in limits are configurable for POS and ATM              |
|    | > transactions.                                                 |
|    | >                                                               |
|    | > Unit of accumulative limit is down time of auth host. For     |
|    | > example, \$100 is configured as stand-in limit then i2c will  |
|    | > not allow transactions once approved transactions             |
|    | > accumulative amount is reached \$100 within down time of auth |
|    | > host.                                                         |
|    | >                                                               |
|    | > Once auth is up again, accumulation counter is reset.         |
|    | >                                                               |
|    | > Note : Stand-in limit works only incase, system of record is  |
|    | > auth host.                                                    |
+----+-----------------------------------------------------------------+
| >  | > i2c stores decline / forced post notification to be sent to   |
|  5 | > auth host in SAF (Store & Forward).                           |
+----+-----------------------------------------------------------------+
| >  | > SAF mechanism will forward notifications to auth host when it |
|  6 | > is available for communication.                               |
+----+-----------------------------------------------------------------+
| >  | > Auth host generates a transaction request response            |
|  7 | > (0x10/0x30) message and sends it to i2c.                      |
+----+-----------------------------------------------------------------+

##### Auth Host Time-Out {#auth-host-time-out .unnumbered}

> If a transaction is successful at i2c in pre-processing but no
> response is received from the auth host at all or till the specific
> time, then either a decline notification or a forced post notification
> will be sent to the auth host based on auth host configuration with
> i2c.

![](./image11.jpeg){width="6.269746281714785in" height="2.09in"}

+----+-----------------------------------------------------------------+
| ** | > **Description**                                               |
| St |                                                                 |
| ep |                                                                 |
| ** |                                                                 |
+====+=================================================================+
| 1  | > Network initiates a transaction request/(0xx0) message to i2c |
+----+-----------------------------------------------------------------+
| 2  | > i2c initiates a Financial Transaction Request message & sent  |
|    | > this to auth host.                                            |
+----+-----------------------------------------------------------------+
| 3  | > No response from auth host in time.                           |
+----+-----------------------------------------------------------------+
| 4  | > i2c performs Stand In processing. Stand-in processing is      |
|    | > configurable (Allowed / Not Allowed).                         |
+----+-----------------------------------------------------------------+
| 5  | > If auth host has configuration with i2c to decline            |
| .1 | > transaction for timeout response, then i2c sends a decline    |
|    | > response (0x10/0x30) message to network.                      |
+----+-----------------------------------------------------------------+
| 5  | > If auth host has configuration with i2c to process            |
| .2 | > transaction for timeout response, then i2c sends a success    |
|    | > response (0x10/0x30) message to network.                      |
|    | >                                                               |
|    | > Stand-in limits are configurable for POS and ATM              |
|    | > transactions.                                                 |
|    | >                                                               |
|    | > Unit of accumulative limit is down time of auth host. For     |
|    | > example, \$100 is configured as stand-in limit then i2c will  |
|    | > not allow transactions once approved transactions             |
|    | > accumulative amount is reached \$100 within down time of auth |
|    | > host. Accumulation is reset once auth host is up.             |
|    | >                                                               |
|    | > Note : Stand-in limit works only incase, system of record is  |
|    | > auth host.                                                    |
+----+-----------------------------------------------------------------+
| 6  | > i2c store decline / forced post notification to be sent to    |
|    | > auth host in SAF (Store & Forward).                           |
+----+-----------------------------------------------------------------+
| 7  | > SAF mechanism will forward notifications to auth host.        |
+----+-----------------------------------------------------------------+
| 8  | > Auth host generates a transaction request response            |
|    | > (0x10/0x30) message and sends it to i2c.                      |
+----+-----------------------------------------------------------------+
| 9  | > Auth host generates a transaction request response            |
|    | > (0x10/0x30) message and sends it to i2c after specified time. |
|    | > (Late response)                                               |
+----+-----------------------------------------------------------------+
| 10 | > If auth host late response is successful, then i2c generates  |
|    | > a reversal to auth host only if 5.2 case is executed at step  |
|    | > 6.                                                            |
+----+-----------------------------------------------------------------+
| 11 | > The auth host generates reversal response (0X10/0X30) message |
|    | > and sends it to i2c.                                          |
+----+-----------------------------------------------------------------+

##### Post Processing Failure {#post-processing-failure .unnumbered}

> **Fail at i2c in Response to Network**
>
> If a transaction is successful in i2c in pre-processing, by auth host
> processor and in post- processing at i2c, but failed to send the
> response to the socket for network, then an auto reversal at i2c as
> well as initiate a reversal at the auth host processor side.
>
> If a transaction is successful in i2c in pre-processing, by auth host
> processor and in post- processing at i2c, but the response sent to the
> switch was rejected with a format error, then the switch will send the
> reversal to i2c and a reversal will be initiated at i2c as well as at
> auth host processor.
>
> If a transaction is successful in i2c in pre-processing, by auth host
> processor and in post- processing at i2c, but the response sent to the
> switch was rejected due to timeout at i2c, then the switch will send
> the reversal to i2c and a reversal will be initiated at i2c as well as
> at auth host processor.

![](./image12.jpeg){width="5.906076115485564in"
height="2.1508333333333334in"}

+----+-----------------------------------------------------------------+
| ** | > **Description**                                               |
| St |                                                                 |
| ep |                                                                 |
| ** |                                                                 |
+====+=================================================================+
| 1  | > Network initiates a transaction request/(0xx0) message to i2c |
+----+-----------------------------------------------------------------+
| 2  | > i2c forwards the Financial Transaction Request message to the |
|    | > auth host                                                     |
+----+-----------------------------------------------------------------+
| 3  | > Auth host generates a success transaction request             |
|    | > response(0X10/0X30) message and sends it to i2c.              |
+----+-----------------------------------------------------------------+
| 4  | > i2c generates a response (0x10/0x30) message and sends it to  |
|    | > network, but it cannot be delivered to network because of     |
|    | > network communication failure or i2c decline in post          |
|    | > processing.                                                   |
+----+-----------------------------------------------------------------+
| 5  | > i2c reverse transaction & store reversal to be sent to auth   |
|    | > host in SAF.                                                  |
+----+-----------------------------------------------------------------+
| 6  | > SAF mechanism will forward reversal to auth host.             |
+----+-----------------------------------------------------------------+
| 7  | > The auth host generates a transaction reversal response       |
|    | > (0X10/0X30) message and sends it to i2c.                      |
+----+-----------------------------------------------------------------+

##### Fail at i2c due to business rules / services {#fail-at-i2c-due-to-business-rules-services .unnumbered}

> Services that are executed after sending authorization request to auth
> host are called post processing services. For example, fraud and ADS
> services.

![](./image13.jpeg){width="6.321402012248469in"
height="2.59875in"}

+----+-----------------------------------------------------------------+
| >  | > **Description**                                               |
| ** |                                                                 |
| St |                                                                 |
| ep |                                                                 |
| ** |                                                                 |
+====+=================================================================+
| >  | > Network initiates a transaction request/(0xx0) message to     |
|  1 | > i2c.                                                          |
+----+-----------------------------------------------------------------+
| >  | > i2c forwards the Financial Transaction Request message to the |
|  2 | > auth host.                                                    |
| ,3 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Auth host generates a success transaction request             |
|  4 | > response(0X10/0X30) message and sends it to i2c.              |
+----+-----------------------------------------------------------------+
| >  | > Post processing is failed at i2c side due to services like    |
|  5 | > (Fraud, ADS, ...).                                            |
+----+-----------------------------------------------------------------+
| >  | > i2c generates a decline response (0x10/0x30) message and      |
|  6 | > sends it to network.                                          |
+----+-----------------------------------------------------------------+
| >  | > i2c sends reverse notification to auth host to reverse the    |
|  7 | > financial impact on its side.                                 |
+----+-----------------------------------------------------------------+

##### Fail at i2c in Parsing Response {#fail-at-i2c-in-parsing-response .unnumbered}

> If some exception occurs in parsing the response message from the auth
> host, then this (non- forced post) transaction will be considered &
> processed as a timed-out transaction at the auth host. For forced post
> transaction, it will be looped in and resent to the auth host until a
> successful response is received from the auth host.

# PART 4 -- Data Elements Definition {#part-4-data-elements-definition .unnumbered}

## Legends for Attributes Acronyms {#legends-for-attributes-acronyms .unnumbered}

+--------+-------------------------------------------------------------+
| >      | > **Description**                                           |
|  **Acr |                                                             |
| onym** |                                                             |
+========+=============================================================+
| > n    | > Numeric digits only. For example, n 6 in DE-11: System    |
|        | > Trace Audit Number indicates the                          |
|        | >                                                           |
|        | > data of fixed, definite length of 6 Numeric digits.       |
+--------+-------------------------------------------------------------+
| > an   | > Alphabetic and Numeric characters only.                   |
+--------+-------------------------------------------------------------+
| > ns   | > Numeric and Special characters only.                      |
+--------+-------------------------------------------------------------+
| > ans  | > Alphabetic, Numeric and Special Characters.               |
+--------+-------------------------------------------------------------+
| > x    | > Indicates a Debit or Credit. For example, x + n 8 in      |
|        | > DE-28: Amount, Transaction Fee means prefix C or D and 8  |
|        | > digits of amount, transaction.                            |
|        | >                                                           |
|        | > C indicates Credit (a positive amount).                   |
|        | >                                                           |
|        | > D indicates Debit (a negative amount).                    |
+--------+-------------------------------------------------------------+
| > b    | > Data in Bytes (Binary String) Format.                     |
+--------+-------------------------------------------------------------+
| >      | > Variable Length that follows from 01 -- 99, appended at   |
|  LLVAR | > the start of the Data Element\'s value to identify the    |
|        | > actual length of the value present. For example, n.. 19   |
|        | > in DE-2: Primary Account Number indicates variable length |
|        | > up to a maximum of 19 characters as its actual value may  |
|        | > vary from 16 to 19 characters.                            |
|        | >                                                           |
|        | > NOTE: In LLVAR format, the length identified is the       |
|        | > number of characters to read after the first 2 positions  |
|        | > to get the data element\'s value.                         |
+--------+-------------------------------------------------------------+
| >      | > Variable Length that follows from 001 -- 999, appended at |
| LLLVAR | > the start of the Data Element\'s value to identify the    |
|        | > actual length of the value present. For example, ans\...  |
|        | > 060 in DE-60: Advice Reason Code indicates variable       |
|        | > length up to a maximum of 60 alphanumeric and special     |
|        | > characters.                                               |
|        | >                                                           |
|        | > NOTE: In LLLVAR format, the actual length is added in     |
|        | > first 3 positions that gives number of characters to read |
|        | > after these positions to get the data element\'s value.   |
+--------+-------------------------------------------------------------+

## Data Elements Details {#data-elements-details .unnumbered}

### DE -- 002 -- PRIMARY ACCOUNT NUMBER {#de-002-primary-account-number .unnumbered}

> **Format**: LLVAR
>
> **Attributes**: n..19
>
> **Description**: A series of digits used to identify a customer
> account or relationship. This can be 16 to 19 digits card number or
> card reference number.
>
> ***Note:** For Non-PCI Compliant auth-host, the card reference number
> will be sent instead of card number.*

### DE -- 003 -- PROCESSING CODE {#de-003-processing-code .unnumbered}

> **Attributes:** an 6
>
> **Description:** A series of digits used to describe the effect of a
> transaction on the customer account and identify the accounts
> affected.
>
> Positions 1--2, Transaction Type: A 2-digit code identifying the
> customer transaction type, or the center function being processed.
>
> Positions 3--4, Account Type (From): A 2-digit code identifying the
> cardholder account type affected for cardholder account debits and
> inquiries, and the \"from\" account type for cardholder account
> transfer transactions.
>
> Positions 5--6, Account Type (To): A 2-digit code identifying the
> cardholder account type affected for cardholder account credits and
> the \"to\" account type for cardholder account transfer transactions.
>
> Refer to the [[Processing Codes
> Table]{.underline}](#data-element-003-processing-codes-table) for a
> list of valid processing codes.

### DE -- 004 -- AMOUNT, TRANSACTION {#de-004-amount-transaction .unnumbered}

> **Attributes:** n 12
>
> **Description:** Funds requested by the cardholder in the local
> currency of the acquirer or source location of the transaction,
> exclusive of transaction fee amount.

### DE -- 005 -- AMOUNT, SETTLEMENT {#de-005-amount-settlement .unnumbered}

> **Attributes:** n 12
>
> **Description:** Funds to be transferred between the acquirer and
> issuer. This amount equals the transaction amount in the currency of
> settlement.

### DE -- 006 -- AMOUNT, CARDHOLDER BILLING {#de-006-amount-cardholder-billing .unnumbered}

> **Attributes:** n 12
>
> **Description:** The amount billed to the cardholder in the currency
> of the cardholder account, exclusive of cardholder billing fees. It
> will always contain the fee amount in addition to transaction amount
> in cardholder billing currency i.e. DE 51.

### DE -- 007 -- TRANSMISSION DATE AND TIME {#de-007-transmission-date-and-time .unnumbered}

> **Attributes:** n 10
>
> **Format:** MMddhhmmss
>
> **Description:** The date and time the message entered into the data
> interchange system. Greenwich Mean Time (GMT) can be used as timezone,
> forwarded data is unaltered

### DE -- 009 -- CONVERSION RATE, SETTLEMENT {#de-009-conversion-rate-settlement .unnumbered}

##### Attributes: n 8 {#attributes-n-8 .unnumbered}

> **Description:** The factor used in the conversion from the
> transaction to settlement amount. The transaction amount is multiplied
> by the settlement conversion rate to determine the settlement amount.
>
> This data element is in the format ABBBBBBB, where:
>
> A = the decimal position from the right
>
> B = the actual conversion factor

### DE -- 010 -- CONVERSION RATE, CARDHOLDER BILLING {#de-010-conversion-rate-cardholder-billing .unnumbered}

##### Attributes: n 8 {#attributes-n-8-1 .unnumbered}

> **Description:** The factor used in the conversion from the
> transaction to cardholder billing amount. The transaction amount is
> multiplied by the cardholder billing conversion rate to determine the
> cardholder billing amount.
>
> This data element is in the format ABBBBBBB, where:
>
> A = the decimal position from the right
>
> B = the actual conversion factor

### DE -- 011 -- SYSTEM TRACE AUDIT NUMBER {#de-011-system-trace-audit-number .unnumbered}

##### Attributes: n 6 {#attributes-n-6 .unnumbered}

> **Description:** A number assigned by the message initiator to
> uniquely identify a transaction. The trace number remains unchanged
> for all messages throughout the life of the transaction.
>
> For Token Authorization Request, (MTI = 01xx and TAR Indicator = 1),
> this field is Conditional. See
>
> [DE -- 111, Additional Data Details]{.underline} for TAR indicator.

### DE -- 012 -- TIME, LOCAL TRANSACTION {#de-012-time-local-transaction .unnumbered}

> **Attributes**: n 6
>
> **Format:** hhmmss
>
> **Description:** The local time at which the transaction takes place
> at the point of the card acceptor location. This time must remain
> unchanged throughout the life of the transaction.

### DE -- 013 -- DATE, LOCAL TRANSACTION {#de-013-date-local-transaction .unnumbered}

##### Attributes: n 4 {#attributes-n-4 .unnumbered}

> **Format:** MMdd
>
> **Description:** The local month and day on which the transaction
> takes place at the card acceptor location. This date must remain the
> same throughout
>
> the life of the transaction.

### DE -- 014 -- DATE, EXPIRATION {#de-014-date-expiration .unnumbered}

##### Attributes: n 4 {#attributes-n-4-1 .unnumbered}

> **Format:** yymm
>
> **Description:** The year and month after which the card expires.

### DE -- 015 -- DATE, SETTLEMENT {#de-015-date-settlement .unnumbered}

##### Attributes: n 4 {#attributes-n-4-2 .unnumbered}

> **Format:** MMdd
>
> Description: The month and day funds are transferred between the
> acquirer and issuer or any intermediate network facility.

### DE -- 018 -- MERCHANT TYPE {#de-018-merchant-type .unnumbered}

##### Attributes: n 4 {#attributes-n-4-3 .unnumbered}

> **Description:** The classification of the merchant's type of business
> product or service.
>
> For Token OTP Notification Request, its value will be 7299
> (Miscellaneous personal services---Not elsewhere classified). See
> Appendix F for OTP Notification Request Identification.

### DE -- 022 -- POINT-OF-SERVICE ENTRY MODE CODE {#de-022-point-of-service-entry-mode-code .unnumbered}

##### Attributes: n 3 {#attributes-n-3 .unnumbered}

> **Description:** Two numeric to indicate the method by which the
> primary account number was entered into the system and one numeric to
> indicate PIN entry capabilities.
>
> Positions 1--2, PAN and Date Entry Mode: A 2-digit code that
> identifies the actual method used to enter the cardholder account
> number and card expiration date.
>
> For Token OTP Notification Request, its value will be 01 (Manual key
> entry). See Appendix F for OTP Notification Request Identification.
>
> Position 3, PIN Entry Capability: A 1-digit code that identifies the
> capability of terminal to capture PINs. This code does not necessarily
> mean that a PIN was entered or is included in this message. Refer to
> POS Entry Mode Codes Table for the complete list of valid codes.

### DE -- 023 -- PAN SEQUENCE NUMBER {#de-023-pan-sequence-number .unnumbered}

##### Attributes: n 3 {#attributes-n-3-1 .unnumbered}

> **Description:** DE 23 (Card Sequence Number) distinguishes among
> separate cards having the same PAN or DE 34 (Primary Account Number
> \[PAN\] Extended). Issuers mayencode chip cards with Card Sequence
> Numbers. Acquirers with chip-reading capability may pass this
> information encoded on the chip in DE 23 of Financial Transaction/0200
> messages.

##### Values: {#values .unnumbered}

> Valid values for Card Sequence Number are in the range 000--099.

### DE -- 025 -- POINT-OF-SERVICE CONDITION CODE {#de-025-point-of-service-condition-code .unnumbered}

##### Attributes: n 2 {#attributes-n-2 .unnumbered}

> **Description:** An identification of the condition under which the
> transaction takes place at the point- of-service.
>
> For Token OTP Notification Request, its value will be 66 (E-commerce
> request through public network). See [[Appendix
> F]{.underline}](#appendix-f-token-activation-otp-notification-message-identification)
> for OTP Notification Request Identification.
>
> Refer to [[POS Condition Codes
> Table]{.underline}](#data-element-025-pos-condition-codes-table) for
> the complete list of valid codes.

### DE -- 026 -- POINT-OF-SERVICE PIN CAPTURE CODE {#de-026-point-of-service-pin-capture-code .unnumbered}

##### Attributes: n 2 {#attributes-n-2-1 .unnumbered}

> Description: A code indicating the technique and/or maximum number of
> PIN characters accepted by the point-of-service device used to
> construct the PIN data.
>
> Refer to POS PIN Capture Codes Table for the complete list of valid
> codes.

### DE -- 028 -- AMOUNT, TRANSACTION FEE {#de-028-amount-transaction-fee .unnumbered}

> **Attributes:** x + n 8
>
> **Description:** The fee charged (for example, by the acquirer) for
> transaction activity in the currency of the transaction amount. This
> fee can be a surcharge, rebate, or transaction fee.
>
> Transaction fee must be represented in numeric 8 digits while the x
> represents the Credit or Debit sign where,
>
> C = Credit amount
>
> D or 0 = Debit amount

### DE -- 029 -- AMOUNT SETTLEMENT FEE {#de-029-amount-settlement-fee .unnumbered}

> **Attributes:** x + n 8
>
> **Description:** The fee transferred between the acquirer and the
> issuer equal to the transaction fee amount in the currency of the
> settlement amount. This amount must be the same value in the response
> as in the request. The value is a debit for a fee and a credit for a
> rebate.
>
> Settlement fee must be represented in numeric 8 digits while the x
> represents the Credit or Debit sign where,
>
> C = Credit amount
>
> D or 0 = Debit amount

### DE -- 032 -- ACQUIRING INSTITUTION IDENTIFICATION CODE {#de-032-acquiring-institution-identification-code .unnumbered}

> **Format**: LLVAR
>
> **Attributes**: n 11
>
> **Description**: A code identifying the acquiring institution (for
> example, merchant bank) or its agent. This can be any uniquely
> identifying number agreed upon by the network.
>
> For Token OTP Notification Request, its value will be 746922. See
> [[Appendix
> F]{.underline}](#appendix-f-token-activation-otp-notification-message-identification)
> for OTP Notification Request Identification.

### DE -- 033 -- FORWARDING INSTITUTION IDENTIFICATION CODE {#de-033-forwarding-institution-identification-code .unnumbered}

> **Format**: LLVAR
>
> **Attributes**: n... 11
>
> **Description**: DE 33 (Forwarding Institution Identification Code)
> identifies the institution forwarding a Request or Advice message in
> an interchange system if not the same institution as specified in the
> DE 32 (Acquiring Institution Identification Code).

### DE -- 037 -- RETRIEVAL REFERENCE NUMBER {#de-037-retrieval-reference-number .unnumbered}

> **Attributes:** an 12
>
> **Description:** This field contains a number that is used with other
> data elements as a key to identify and track all messages related to a
> given cardholder transaction; that is, to a given transaction set. For
> x8xx messages, retrieval reference number can be generated using
> following format:

+--------+-------------------------------------------------------------+
| >      | > **Data**                                                  |
| **Posi |                                                             |
| tion** |                                                             |
+========+=============================================================+
| > 1-4  | > The yddd equivalent of the field 7 date                   |
+--------+-------------------------------------------------------------+
| > 5-6  | > The hours from the time in field 7                        |
+--------+-------------------------------------------------------------+
| > 7-12 | > The value from field 11                                   |
+--------+-------------------------------------------------------------+

### DE -- 038 -- AUTHORIZATION IDENTIFICATION RESPONSE {#de-038-authorization-identification-response .unnumbered}

> **Attributes:** an 6
>
> **Description:** Field 38 contains the authorization code provided by
> the issuer when a transaction is approved or a "no reason to decline"
> code provided for successful verification.

### DE -- 039 -- RESPONSE CODE {#de-039-response-code .unnumbered}

> **Attributes**: an 2
>
> **Description:** A code that defines the disposition of a message.
> When the response code is 30, then Additional Response Data (bit 044)
> contains the bit number in error.
>
> Refer to Response Codes Table for the complete list of valid codes.

### DE -- 041 -- CARD ACCEPTOR TERMINAL IDENTIFICATION {#de-041-card-acceptor-terminal-identification .unnumbered}

> **Attributes:** an 8
>
> **Description:** A unique code identifying a terminal at the card
> acceptor location.
>
> For Token OTP Notification Request, its value will be 11111111. See
> Appendix F for OTP Notification Request Identification.

### DE -- 042 -- CARD ACCEPTOR IDENTIFICATION CODE {#de-042-card-acceptor-identification-code .unnumbered}

> **Attributes:** an 15
>
> **Description:** A code identifying the card acceptor that defines the
> point of the transaction in both local and interchange environments.
>
> For Token OTP Notification Request, its value will be 111111111111111.
> See [[Appendix
> F]{.underline}](#appendix-f-token-activation-otp-notification-message-identification)
> for OTP Notification Request Identification.

### DE -- 043 -- CARD ACCEPTOR NAME/LOCATION {#de-043-card-acceptor-namelocation .unnumbered}

> **Usage**: Usage 1: For existing clients; Usage 2: For new clients
>
> **Attributes:** an 43 (Usage 1); an 70 (Usage 2)
>
> **Description:** This field contains the name and location of the card
> acceptor (merchant), including the city name, state and country code.
>
> For details, please refer to [[DE -- 43 -- Card Acceptor
> Name/Location]{.underline}](#data-element-043-card-acceptor-namelocation).

### DE -- 048 -- ADDITIONAL PROCESSING DATA {#de-048-additional-processing-data .unnumbered}

> **Format**: LLLVAR
>
> **Attributes**: ans\... 255
>
> **Description**: This data element is reserved for communicating the
> results of i2c processing for example Issuer Script Command sent in
> case of EMV transactions or any other processing data. This field is
> applicable for x1xx, x2xx & x4xx transactions.
>
> For details of sub-fields, please refer to [[DE -- 48, Additional
> Processing
> Details]{.underline}](#data-element-043-card-acceptor-namelocation).

### DE -- 049 -- CURRENCY CODE, TRANSACTION {#de-049-currency-code-transaction .unnumbered}

##### Attributes: n 3 {#attributes-n-3-2 .unnumbered}

> **Description:** The local currency of the acquirer or source location
> of the transaction. Currency used in transaction amount and
> transaction fee amount.
>
> For Token Authorization Request, (MTI = 01xx and TAR Indicator = 1),
> this field is Conditional. See DE -- 111, Additional Data Details for
> TAR indicator.

### DE -- 050 -- CURRENCY CODE, SETTLEMENT {#de-050-currency-code-settlement .unnumbered}

##### Attributes: n 3 {#attributes-n-3-3 .unnumbered}

> **Description:** A code defining the currency of the settlement amount
> and the settlement fee amount.

### DE -- 051 -- CURRENCY CODE, CARDHOLDER BILLING {#de-051-currency-code-cardholder-billing .unnumbered}

##### Attributes: n 3 {#attributes-n-3-4 .unnumbered}

> **Description:** A code defining the currency of the cardholder
> billing amount and the cardholder billing fee amount.

### DE -- 054 -- ADDITIONAL AMOUNTS {#de-054-additional-amounts .unnumbered}

> **Format**: LLLVAR
>
> **Attributes**: ans\... 120
>
> **Description**: This field contains additional amounts like
> additional fees, card balances, etc. which applies to the transaction.
>
> The field will be formatted in chunks of 20 bytes each, where chunk
> represents one amount to be communicated. This means maximum of 6
> amounts can be communicated in this field. Each chunk (20-bytes) will
> be formatted as follows:
>
> **Positions 1--2, Account Type:** This 2-digit code (field 54.1)
> identifies the account type. **Positions 3--4, Amount Type:** This
> 2-digit code (field 54.2) describes the use of the amount. **Positions
> 5--7, Currency Code:** This 3-digit code (field 54.3) defines the
> currency used in positions 9--20.
>
> **Position 8, Amount, Sign:** This 1-digit code (field 54.4) defines
> the value of the amount as either positive or negative, where C =
> Positive balance & D = Negative balance.
>
> **Positions 9--20, Amount:** This 12-character amount (field 54.5) is
> right-justified and contains leading zeros. The amount also includes
> an implied decimal relative to the currency code specified in
> positions 5--7.
>
> Refer to Additional Amounts Codes Table for the complete list of valid
> account / amount types. Refer to Additional Amounts Business Use Cases
> table.

### DE -- 057 -- AUTHORIZATION LIFE CYCLE {#de-057-authorization-life-cycle .unnumbered}

> **Format**: LLLVAR
>
> **Attributes**: an 003
>
> **Description:** The ANSI X9.2-1988 standard defines this data element
> as the Authorization Life Cycle, a value in calendar days, hours, or
> minutes that identifies the time for which an acquirer is requesting
> guarantee of funds.
>
> This data element is subdivided into the following two sub-elements:
>
> **Position 1, Life Cycle Indicator (n 1):** It indicates the type of
> time interval in effect for a pre- authorization. Possible values are:
>
> 1 = Calendar days
>
> 2 = Hours
>
> 3 = Minutes
>
> **Position 2-3, Life cycle (n 2):** It is the time interval in effect
> for a pre-authorization.

##### DE -- 059 -- GEOGRAPHIC DATA {#de-059-geographic-data .unnumbered}

> **Format**: LLLVAR
>
> **Attribute**: ans... 018
>
> **Description**: This field contains geographic information about POS
> location

+----------------------+--------------------+-------------------------+
| > **Position**       | > **Attribute**    | > **Description**       |
+======================+====================+=========================+
| > 1-10               | > ans 10           | > Merchant Postal code  |
+----------------------+--------------------+-------------------------+

+----------------------+----------------------+-----------------------+
| > 11-18              | > ans 18             | > Reserved for future |
+======================+======================+=======================+
+----------------------+----------------------+-----------------------+

### DE -- 061 -- POINT-OF-SERVICE (POS) DATA {#de-061-point-of-service-pos-data .unnumbered}

> **Format**: LLLVAR
>
> **Attributes**: ans\... 019
>
> **Description:** The ANSI X9.2-1988 standard defines this data element
> as the National Point-Of- Service Condition Code, a series of codes
> intended to identify terminal class, presentation data, and security
> condition.
>
> Refer to Point-of-Service (POS) Data Table for the complete list of
> valid i2c POS Codes.

### DE -- 063 -- NETWORK DATA {#de-063-network-data .unnumbered}

> **Format**: LLLVAR
>
> **Attributes**: ans\... 070
>
> **Description:** DE 63 (Network Data) is generated by the
> Authorization Platform for each originating message routed through the
> network. The receiver must retain the data element and use it in any
> response or acknowledgment message associated with the originating
> message. The Sub-Fields of DE-63 are as follows:

+--------+-----------+------------------------------------------------+
| >      | > **At    | > **Description**                              |
| **Posi | tribute** |                                                |
| tion** |           |                                                |
+========+===========+================================================+
| > 1-4  | > an 4    | > Acquirer Network ID                          |
+--------+-----------+------------------------------------------------+
| > 5-8  | > an 4    | > Issuer Network ID                            |
+--------+-----------+------------------------------------------------+
| > 9-24 | > an 16   | > Transaction Identifier/Access Transaction    |
|        |           | > Sequence Number                              |
+--------+-----------+------------------------------------------------+
| >      | > an 9    | > Bank Net Reference Number                    |
|  25-33 |           |                                                |
+--------+-----------+------------------------------------------------+
| > 34   | > an 1    | > Interchange Rate Indicator                   |
+--------+-----------+------------------------------------------------+
| >      | > n 24    | > Acquirer Reference Number                    |
|  35-58 |           |                                                |
+--------+-----------+------------------------------------------------+
| >      | > an 12   | > Network Type                                 |
|  59-70 |           |                                                |
+--------+-----------+------------------------------------------------+

> **Note:** All sub-fields are right justified space filled. If data in
> any of the sub-field is not present, it must be space filled.
>
> For Token Authorization Request, (MTI = 01xx and TAR Indicator = 1),
> this field is Conditional. See
>
> [[DE -- 111, Additional Data
> Details]{.underline}](#data-element-111-additional-data-table) for TAR
> indicator.

### DE -- 065 -- SECONDARY BITMAP DATA {#de-065-secondary-bitmap-data .unnumbered}

> **Attributes:** b 64
>
> **Description:** A series of 64 bits used to identify the presence
> (denoted by 1) or absence (denoted by a 0) of data elements 66 through
> 128.

### DE -- 070 -- NETWORK MANAGEMENT INFORMATION CODE {#de-070-network-management-information-code .unnumbered}

##### Attributes: n 3 {#attributes-n-3-5 .unnumbered}

> **Description:** Used to identify network status.

+--------+-------------------------------------------------------------+
| > **   | > **Description**                                           |
| Code** |                                                             |
+========+=============================================================+
| > 081  | > Sign On Code                                              |
+--------+-------------------------------------------------------------+
| > 082  | > Sign Off Code                                             |
+--------+-------------------------------------------------------------+
| > 301  | > Echo/Health Check Code                                    |
+--------+-------------------------------------------------------------+

### DE -- 080 -- DISPUTE ACTION INFORMATION {#de-080-dispute-action-information .unnumbered}

> **Format**: LLLVAR
>
> **Attributes**: ans\... 999
>
> This is a field is setup in Tag, Length, Value (TLV) format which
> contain information about the Dispute Actions transactions. It
> contains multiple tags. The description for each of the tag is given
> below:

+-----+-------+-----------+-----+------------------------------------+
| > * | >     | >         | > * | > **Content**                      |
| *Ta | **Len | **Value** | *Fo |                                    |
| g** | gth** |           | rma |                                    |
|     |       |           | t** |                                    |
+=====+=======+===========+=====+====================================+
| >   | >     | > Dispute | > N | > It is a unique identifier in our |
|  \' | \'02' | > Trans   |     | > system against a dispute.        |
| 01' |       | > ID      |     |                                    |
+-----+-------+-----------+-----+------------------------------------+
| >   | >     | > Dispute | > N | > The claimed dispute Amount by    |
|  \' | \'02' | > Amount  |     | > Card holder.                     |
| 02' |       |           |     |                                    |
+-----+-------+-----------+-----+------------------------------------+
| >   | >     | > Credit  | >   | > This is applicable only for the  |
|  \' | \'02' | > Type    |  AN | > Credit transactions. This tag    |
| 03' |       |           |     | > will not be available for debit  |
|     |       |           |     | > transactions.                    |
|     |       |           |     | >                                  |
|     |       |           |     | > Credit Type Possible value are:  |
|     |       |           |     |                                    |
|     |       |           |     | -   Admin Credit: Administratively |
|     |       |           |     |     > Credit is given to           |
|     |       |           |     |     > Cardholder.                  |
|     |       |           |     |                                    |
|     |       |           |     | -   Network: Network has accepted  |
|     |       |           |     |     > the claim and send the       |
|     |       |           |     |     > charge-back.                 |
|     |       |           |     |                                    |
|     |       |           |     | > None: where settlement of funds  |
|     |       |           |     | > is already completed between     |
|     |       |           |     | > merchant and card holder.        |
+-----+-------+-----------+-----+------------------------------------+
| >   | >     | > Agent   | >   | > The ID of the chargeback         |
|  \' | \'02' | > ID      |  AN | > analyst.                         |
| 04' |       |           |     |                                    |
+-----+-------+-----------+-----+------------------------------------+
| >   | >     | > Decline | >   | > The reasons on the basis of      |
|  \' | \'02' | > Reasons |  AN | > which the claim does not         |
| 05' |       |           |     | > fulfills. The tag will contain   |
|     |       |           |     | > the comma separated list of      |
|     |       |           |     | > reason ids.                      |
|     |       |           |     | >                                  |
|     |       |           |     | > Details against each ID can be   |
|     |       |           |     | > seen in [[Data Element           |
|     |       |           |     | > 80]{.underline}](#_bookmark104)  |
|     |       |           |     | > [[Dispute Action Information Tag |
|     |       |           |     | > 05 Decline                       |
|     |       |           |     | > Rea                              |
|     |       |           |     | sons]{.underline}.](#_bookmark104) |
+-----+-------+-----------+-----+------------------------------------+
| >   | >     | > CH Loss | > D | > The date on which cardholder     |
|  \' | \'02' | > Date    | ate | > faces the loss. \[YYYYMMDD\]     |
| 06' |       |           |     |                                    |
+-----+-------+-----------+-----+------------------------------------+

### DE -- 090 -- ORIGINAL DATA ELEMENTS {#de-090-original-data-elements .unnumbered}

> **Usages**: Usage 1: For existing clients; Usage 2: For new clients
>
> **Attributes**: n 42 (Usage 1); n 44 (Usage 2)
>
> **Description**: DE 90 (Original Data Elements) are data elements
> contained in an original message that may identify a transaction for
> correction or reversal. Below is detail for field sub elements:
>
> **\*\*Usage-1 Details (For existing clients):**

+------+------+-------------------------------------------------------+
| >    | >    | > **Element**                                         |
| **Po | **Ty |                                                       |
| siti | pe** |                                                       |
| on** |      |                                                       |
+======+======+=======================================================+
| > 1  | >    | > Message Type Identifier                             |
| > -- |  n - |                                                       |
| > 4  | > 4  |                                                       |
+------+------+-------------------------------------------------------+
| >    | >    | > System trace audit no                               |
|  5 - |  n - |                                                       |
| > 10 | > 6  |                                                       |
+------+------+-------------------------------------------------------+
| > 11 | >    | > Transmission date time                              |
| > -- |  n - |                                                       |
| > 20 | > 10 |                                                       |
+------+------+-------------------------------------------------------+
| >    | > n  | > Acquirer Institution Id                             |
| 21 - | > -- |                                                       |
| > 31 | > 11 |                                                       |
+------+------+-------------------------------------------------------+
| >    | >    | > Forwarding Institution ID Code                      |
| 32 - |  n - |                                                       |
| > 42 | > 11 |                                                       |
+------+------+-------------------------------------------------------+

> **\*\*Usage-2 Details (For existing clients):**

+------+------+-------------------------------------------------------+
| >    | >    | > **Element**                                         |
| **Po | **Ty |                                                       |
| siti | pe** |                                                       |
| on** |      |                                                       |
+======+======+=======================================================+
| > 1  | >    | > Message Type Identifier                             |
| > -- |  n - |                                                       |
| > 4  | > 4  |                                                       |
+------+------+-------------------------------------------------------+
| >    | >    | > System trace audit no                               |
|  5 - |  n - |                                                       |
| > 10 | > 6  |                                                       |
+------+------+-------------------------------------------------------+
| > 11 | >    | > Transmission date time                              |
| > -- |  n - |                                                       |
| > 22 | > 12 |                                                       |
+------+------+-------------------------------------------------------+
| >    | > n  | > Acquirer Institution Id                             |
| 23 - | > -- |                                                       |
| > 33 | > 11 |                                                       |
+------+------+-------------------------------------------------------+
| >    | >    | > Forwarding Institution ID Code                      |
| 34 - |  n - |                                                       |
| > 44 | > 11 |                                                       |
+------+------+-------------------------------------------------------+

### DE -- 102 -- ACCOUNT IDENTIFICATION 1 {#de-102-account-identification-1 .unnumbered}

> **Format**: LLVAR
>
> **Attributes**: ans.. 28
>
> **Description**: A series of digits used to identify a customer
> account or relationship Id.
>
> Account identification 1 identifies the account involved for a single
> account transaction. In the case of transfers, Account Identification
> 1 identifies the From account in a transaction.

### DE -- 108 -- RECEIVER/SENDER DATA {#de-108-receiversender-data .unnumbered}

> **Format:** LLLVAR
>
> **Attributes:** ans\... 999
>
> **When DE-63.7 = 'VISA':** DE 108 (Additional Transaction Reference
> Data) provides the capability for the acquirers to send sender data
> required in 0200 and 0100 original credit transactions.
>
> Refer to [[details]{.underline}](#_bookmark88) for the complete list
> of sender data fields with sub elements.
>
> **When DE-63.7 = 'MASTERCARD':** DE 108 (Additional Transaction
> Reference Data) provides the capability for the acquirers to send
> sender, receiver, and transaction level data to the issuer in funding
> transfer transactions and MoneySend payment transactions. DE 108
> provides the
>
> capability to acquirers to send to the issuer data for Mastercard™
> Merchant Presented QR payment transactions and Mastercard Merchant
> Presented QR funding transactions.

+--------+---------+-----------------+---------------------------------+
| >      | > *     | > **R           | > **Element**                   |
|  **Sub | *Length | epresentation** |                                 |
| > Ele  | >       |                 |                                 |
| ment** | Field** |                 |                                 |
+========+=========+=================+=================================+
| > 01   | > 3     | > ans\...322;   | > Receiver Data                 |
|        |         | > LLLVAR        |                                 |
+--------+---------+-----------------+---------------------------------+
| > 02   | > 3     | > ans\...322;   | > Sender Data                   |
|        |         | > LLLVAR        |                                 |
+--------+---------+-----------------+---------------------------------+
| > 03   | > 3     | > ans\...138;   | > Transaction reference Data    |
|        |         | > LLLVAR        |                                 |
+--------+---------+-----------------+---------------------------------+
| > 04   | > 3     | > ans\...61;    | > Language Description          |
|        |         | > LLLVAR        |                                 |
+--------+---------+-----------------+---------------------------------+
| > 05   | > 3     | > ans\...99;    | > Digital Account Info          |
|        |         | > LLLVAR        |                                 |
+--------+---------+-----------------+---------------------------------+
| > 06   | > 3     | > ans\...237;   | > QR Dynamic Code Data          |
|        |         | > LLLVAR        |                                 |
+--------+---------+-----------------+---------------------------------+

### DE -- 109 -- ADVICE REASON CODE {#de-109-advice-reason-code .unnumbered}

> **Format**: LLLVAR, Fixed Format
>
> **Attributes**: ans 999
>
> This data element is reserved by ISO for private definition and use.
> i2c defines this data element as Additional Data, which contains
> additional information for Visa®, MasterCard®, FIS®, Discover®, and
> Fiserv format.
>
> This contains data in fixed length sub-fields. The number and contents
> of sub-fields varies according to different networks, based on the
> value of DE-63.7 (Network Type).
>
> Refer to Advice Reason Code for the complete list of network specific
> additional data fields for Fixed Format.

### DE -- 110 -- MINI STATEMENT DATA {#de-110-mini-statement-data .unnumbered}

> **Format**: LLLVAR
>
> **Attributes**: an 360
>
> **Description**: This field is required in responses (0110/0210) of
> 0100/0200 ATM Mini Statement requests.
>
> Issuers that choose to support the new mini statement requests, must
> be able to receive the new transaction type value 34 (ATM Mini
> Statement) carried in existing Field 3, positions 1--2 and must be
> able to send Field 110 in the 0110/0210 responses.
>
> The field will be formatted just like Field-54 where data of each
> transaction will be formatted in a chunk of 36-bytes. This means
> maximum of 10 transactions (i.e. 10 chunks of 36 bytes each) can be
> communicated in this field.
>
> Each chunk (36-bytes) will be formatted as follows:
>
> **Positions 1--8** will contain an 8-digit transaction date in
> yyyymmdd format.
>
> **Positions 9--23** will contain a 15-character alphanumeric
> transaction description that is left-justified with trailing spaces.
>
> **Position 24** will contain a 1-digit code prefix that defines
> whether the transaction amount is credit or debit, where, C (Credit) &
> D (Debit).
>
> **Positions 25--36** will contain a 12-character amount that is
> right-justified and contains leading zeros. The amount also includes
> an implied decimal relative to the cardholder billing currency code.

### DE -- 111 -- ADDITIONAL DATA {#de-111-additional-data .unnumbered}

> **Format**: LLLVAR, Fixed Format
>
> **Attributes**: ans\... 999
>
> **Description**: This data element is reserved by ISO for private
> definition and use. i2c defines this data element as *Additional
> Data*, which contains additional information for Visa^®^,
> MasterCard^®^, FIS^®^ , Discover^®^ , Star^®^, UnionPay^®^, and Fiserv
> format.
>
> This contains data in fixed length sub-fields. The number and contents
> of sub-fields varies according to different networks, based on the
> value of DE-63.7 (Network Type).

-   Sub Field/s for Token Authorization Request (TAR 0100)

-   Token Authorization Request (TAR) Indicator

-   Sub Field/s for Token Financial Transactions (01XX, 02XX,04XX)

-   Token Device Id

-   Token Device No

-   Token Device Name

-   Token Device Type

-   Token ID

-   Token Type

-   Token Status

-   Sub Field/s for Token OTP Request (0100)

    -   Token OTP Code

    -   Token OTP Expiry Date Time

-   Sub Field/s for Token PAN Management (0302)

    -   Replacement PAN

    -   Replacement PAN Expiration Date

-   Sub Field/s for Token Life Cycle (0620)

    -   Token Notification Type

> Refer to Additional Data Table for the complete list of network
> specific additional data fields for Fixed Format.

### DE -- 123 -- VERIFICATION DATA {#de-123-verification-data .unnumbered}

> **Format**: LLLVAR
>
> **Attributes**: ans\... 255
>
> **Description:** It is an i2c-defined private-use field that contains
> information used for certain types of verification data, including
> selected portions of the cardholder's postal code and street address.
> All merchants whose acquirers subscribe to the i2c Address
> Verification Service may request postal code and street address
> verification for a cardholder.
>
> The field has two sub-fields which are described below:

+-------+---------------+---------------------------------------------+
| > *   | > **Data**    | > **Description**                           |
| *Posi |               |                                             |
| tio** |               |                                             |
| >     |               |                                             |
| >     |               |                                             |
| **n** |               |                                             |
+=======+===============+=============================================+
| > 1-9 | > Postal code | > This value is the 5-digit postal code     |
|       |               | > (left-justified with 4                    |
|       |               | >                                           |
|       |               | > positions of right-space-fill), or        |
|       |               | > 9-digit postal code.                      |
+-------+---------------+---------------------------------------------+
| >     | > Cardholder  | > This sub-field contains up to 20          |
| 10-29 | > street      | > characters of street address. The         |
|       | > address     | > acquirer converts spelled-out numbers to  |
|       |               | >                                           |
|       |               | > digits, left-justified with right         |
|       |               | > space-fill.                               |
+-------+---------------+---------------------------------------------+

### DE -- 125 -- SUPPORTING INFORMATION {#de-125-supporting-information .unnumbered}

> **Format**: LLLVAR, BER-TLV Format for Visa (DE-63.7 = VISA) LLLVAR,
> Fixed Format for MasterCard (DE-63.7 = MASTERCARD) **Attributes**: ans
> 999
>
> **Description:** It is an i2c-defined private-use field that contains
> supporting information used for certain types of transactions,
> including Token Authorization Transactions (TAR) and Administrative
> Advice Messages. All merchants whose acquirers subscribe to the i2c
> Tokenization Service may request supporting information of a
> transaction.
>
> Refer to Supporting Information Table for the complete list of data
> fields for BER-TLV and Fixed Format.

##### BER-TLV Format for Visa {#ber-tlv-format-for-visa .unnumbered}

> For VISA, this field allows for multiple data-sets in TLV format. Each
> data-set can have multiple TLV sub-fields. The format is shown below:
>
> ![](./image14.jpeg){width="6.569542869641295in"
> height="2.341353893263342in"}
>
> In the Basic Encoding Rules (BER), the Tag-Length-Value (TLV) format
> is an ISO convention that treats field content as data-sets.
>
> **Length Sub-field:** This one-byte binary sub-field contains the
> number of bytes following the length sub-field. The maximum value is
> 255.
>
> **Position 1, Dataset ID:** This one-byte binary sub-field contains a
> hexadecimal value that identifies the TLV data that follows. Following
> are the valid values:
>
> Dataset Value Hex 68, Token Data Dataset Value Hex 01, Token Device
> Dataset Value Hex 02, Wallet Provider
>
> Dataset Value Hex 40, Terms and Conditions
>
> **Positions 2--3, Dataset Length:** This 2-byte binary sub-field
> specifies the total length of the TLV fields present in the dataset.
> The length is variable, depending on the data that follows.
>
> **Positions 4--999, TLV Elements:** Each sub-field of a dataset has a
> defined tag, length, and value. The tag is used in conjunction with
> the dataset ID value. The dataset sub-fields can be present in any
> order with other TLV sub-fields.

# PART 5 -- Appendices {#part-5-appendices .unnumbered}

## Appendix A -- Message Matching Criteria {#appendix-a-message-matching-criteria .unnumbered}

#### Matching Criteria for Clearing Message with Corresponding Authorization (01xx with 022x Matching) {#matching-criteria-for-clearing-message-with-corresponding-authorization-01xx-with-022x-matching .unnumbered}

+---------+------------+-----------------------------------------------+
| > **C   | >          | > **Criteria Fields**                         |
| riteria |  **Message |                                               |
| > \#**  | > Type**   |                                               |
+=========+============+===============================================+
| > 1     | >          | > DE-002, Transaction Identifier              |
|         |  0100/0220 |                                               |
+---------+------------+-----------------------------------------------+
| > 2     | >          | > DE-002, DE-038                              |
|         |  0100/0220 |                                               |
+---------+------------+-----------------------------------------------+
| > 3     | >          | > DE-002, DE-037                              |
|         |  0100/0220 |                                               |
+---------+------------+-----------------------------------------------+
| > 4     | >          | > DE-002, DE-111.31                           |
|         |  0100/0220 |                                               |
+---------+------------+-----------------------------------------------+

#### Matching Criteria for Reversal Message with Corresponding Original Message (01xx/02xx with 042x Matching) {#matching-criteria-for-reversal-message-with-corresponding-original-message-01xx02xx-with-042x-matching .unnumbered}

+---------+------------+-----------------------------------------------+
| > **C   | >          | > **Criteria Fields**                         |
| riteria |  **Message |                                               |
| > \#**  | > Type**   |                                               |
+=========+============+===============================================+
| > 1     | > 0420     | > DE-002, Transaction Identifier              |
+---------+------------+-----------------------------------------------+
| > 2     | > 0420     | > DE-002, DE-011, DE-012, DE-032 and DE-037   |
+---------+------------+-----------------------------------------------+
| > 3     | > 0420     | > DE-002, DE-011, DE-032 and DE-037           |
+---------+------------+-----------------------------------------------+
| > 4     | > 0420     | > DE-002, Banknet Reference No.               |
+---------+------------+-----------------------------------------------+
| > 5     | > 0420     | > DE-002, DE-038                              |
+---------+------------+-----------------------------------------------+

> **Transaction Identifier:** A number which remains unique throughout a
> transaction life cycle. The value is received in DE63.3 (Transaction
> Identifier) DE111.7 (for MASTERCARD)

## Appendix B -- Authorization Expiration Time {#appendix-b-authorization-expiration-time .unnumbered}

> In authorization (01xx), funds are held for a configurable time
> period. Possible configuration can be:

-   Auth Expiry Days for Electronic PAN entry Mode

-   Auth Expiry Days for Manual PAN entry Mode

-   Auth Expiry Days according to Merchant Cat Code

> If a particular authorization (01xx) is not settled by merchant within
> time, then funds are released, and a reversal will be sent to the auth
> host by i2c for this authorization.

## Appendix C -- Data Elements Detailed Definitions {#appendix-c-data-elements-detailed-definitions .unnumbered}

#### Data Element 003 -- Processing Codes Table {#data-element-003-processing-codes-table .unnumbered}

+-----+----------------------------------------------------------------+
| >   |                                                                |
|  ** |                                                                |
| Pos |                                                                |
| iti |                                                                |
| ons |                                                                |
| >   |                                                                |
|  1- |                                                                |
| -2: |                                                                |
| >   |                                                                |
|  Tr |                                                                |
| ans |                                                                |
| act |                                                                |
| ion |                                                                |
| >   |                                                                |
| Typ |                                                                |
| e** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Purchase                                                     |
|  00 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Withdrawal                                                   |
|  01 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Debit Adjustment                                             |
|  02 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Guarantee with Conversion (POS Check Service) (Future Use)   |
|  03 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Verification with Conversion (POS Check Service) (Future     |
|  04 | > Use)                                                         |
+-----+----------------------------------------------------------------+
| >   | > Traveler Check                                               |
|  06 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Purchase with Cash Back                                      |
|  09 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Account Funding                                              |
|  10 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Quasi-Cash Transaction--Debit or Internet Gambling           |
|  11 | > Transaction                                                  |
+-----+----------------------------------------------------------------+
| >   | > Funds Withdrawal for Electronic Purse / Address Verification |
|  13 | > with a goods or services Authorization for Recurring Billing |
|     | > (Recurring Payments)                                         |
+-----+----------------------------------------------------------------+
| >   | > Recurring Billing (Recurring Payments) -- goods or services  |
|  14 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Installment Payment -- goods or Services                     |
|  15 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Cash Disbursement                                            |
|  17 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Deferred Goods and Services / Scrip Issue / Conversion Only  |
|  18 | > (POS Check Service) / Card Account Verification              |
+-----+----------------------------------------------------------------+
| >   | > Debit Fee Collection / Deferred Goods and Services With Cash |
|  19 | > Disbursement                                                 |
+-----+----------------------------------------------------------------+
| >   | > Credit Return (of goods) / Credit Transaction / Credit       |
|  20 | > Voucher or Merchandise / Return Authorization (U.S. Only) /  |
|     | > Purchase Return/Refund                                       |
+-----+----------------------------------------------------------------+
| >   | > Deposit                                                      |
|  21 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Credit Adjustment                                            |
|  22 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Check Deposit Guarantee                                      |
|  23 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Check Deposit                                                |
|  24 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Envelope-less Cash Deposit                                   |
|  25 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Original Credit                                              |
|  26 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Prepaid Activation and Load Prepaid Load / Payment           |
|  28 | > Transaction                                                  |
+-----+----------------------------------------------------------------+
| >   | > Credit Funds Disbursement / Primary Credit                   |
|  29 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Available Funds Inquiry / Commercial Deposit                 |
|  30 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Balance Inquiry                                              |
|  31 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Account Updater Code / Account Verification (Future Use)     |
|  33 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > ATM Mini Statement                                           |
|  34 |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   | > Eligibility Inquiry / Generic Balance Inquiry (Future Use)   |
|  39 |                                                                |
+=====+================================================================+
| >   | > Cardholder Account Transfer                                  |
|  40 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Bill Payment / Payment to Another Party                      |
|  50 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Payment (U.S. only)                                          |
|  53 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Payment Debit (P2P)                                          |
|  54 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Payment from Third Party                                     |
|  55 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Payment Credit (P2P)                                         |
|  56 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Payment from Account to Credit/Loan                          |
|  58 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Payment Enclosed                                             |
|  59 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Prepaid Activation                                           |
|  72 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > PIN Unblock                                                  |
|  91 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > PIN Change                                                   |
|  92 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > PV Credit Transaction                                        |
|  PV |                                                                |
+-----+----------------------------------------------------------------+
| >   | > PV Debit Transaction                                         |
|  PD |                                                                |
+-----+----------------------------------------------------------------+
| >   | > CHARGEBACK CREDIT                                            |
|  CB |                                                                |
+-----+----------------------------------------------------------------+
| >   | > SPECIAL CREDIT 2                                             |
|  Q2 |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
|  ** |                                                                |
| Pos |                                                                |
| iti |                                                                |
| ons |                                                                |
| >   |                                                                |
|  3- |                                                                |
| -4: |                                                                |
| > A |                                                                |
| cco |                                                                |
| unt |                                                                |
| > T |                                                                |
| ype |                                                                |
| >   |                                                                |
|  (F |                                                                |
| rom |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Default Account (Not specified or Not applicable)            |
|  00 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Savings Account                                              |
|  10 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Checking Account                                             |
|  20 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Credit Card Account                                          |
|  30 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Credit Line Account                                          |
|  38 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Corporate Account                                            |
|  39 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Universal Account                                            |
|  40 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Money Market Investment Account                              |
|  50 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Stored Value /[Prepaid]{.mark} account                       |
|  60 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Revolving Loan Account                                       |
|  90 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > [Deferred debit account]{.mark}                              |
|  [3 |                                                                |
| 5]{ |                                                                |
| .ma |                                                                |
| rk} |                                                                |
+-----+----------------------------------------------------------------+
| >   | > [Charge account]{.mark}                                      |
|  [3 |                                                                |
| 6]{ |                                                                |
| .ma |                                                                |
| rk} |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
|  ** |                                                                |
| Pos |                                                                |
| iti |                                                                |
| ons |                                                                |
| >   |                                                                |
|  5- |                                                                |
| -6: |                                                                |
| > A |                                                                |
| cco |                                                                |
| unt |                                                                |
| > T |                                                                |
| ype |                                                                |
| >   |                                                                |
| (To |                                                                |
| )** |                                                                |
+=====+================================================================+
| **  | > **Definition**                                               |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| 00  | > Default Account (Not specified or Not applicable)            |
+-----+----------------------------------------------------------------+
| 10  | > Savings Account                                              |
+-----+----------------------------------------------------------------+
| 20  | > Checking Account                                             |
+-----+----------------------------------------------------------------+
| 30  | > Credit Card Account                                          |
+-----+----------------------------------------------------------------+
| 38  | > Credit Line Account                                          |
+-----+----------------------------------------------------------------+
| 40  | > Universal Account                                            |
+-----+----------------------------------------------------------------+
| 50  | > Money Market Investment Account                              |
+-----+----------------------------------------------------------------+
| 58  | > IRA Investment Account                                       |
+-----+----------------------------------------------------------------+
| 90  | > Revolving Loan Account                                       |
+-----+----------------------------------------------------------------+
| 91  | > Installment Loan Account                                     |
+-----+----------------------------------------------------------------+
| 92  | > Real Estate Loan Account                                     |
+-----+----------------------------------------------------------------+

#### Data Element 022 -- POS Entry Mode Codes Table {#data-element-022-pos-entry-mode-codes-table .unnumbered}

+-----+----------------------------------------------------------------+
| > * |                                                                |
| *Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| >   |                                                                |
|  1- |                                                                |
| -2: |                                                                |
| >   |                                                                |
| PAN |                                                                |
| >   |                                                                |
| and |                                                                |
| > D |                                                                |
| ate |                                                                |
| >   |                                                                |
|  En |                                                                |
| try |                                                                |
| >   |                                                                |
| Mod |                                                                |
| e** |                                                                |
+=====+================================================================+
| **  | > **Definition**                                               |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| 00  | > Unspecified                                                  |
+-----+----------------------------------------------------------------+
| 01  | > Manual                                                       |
+-----+----------------------------------------------------------------+
| 02  | > Magnetic stripe                                              |
+-----+----------------------------------------------------------------+
| 03  | > Bar code / Consumer-presented QRC, chip information excluded |
+-----+----------------------------------------------------------------+
| 04  | > OCR / Consumer-presented QR Code (QRC), chip information     |
|     | > included                                                     |
+-----+----------------------------------------------------------------+
| 05  | > Integrated circuit card                                      |
+-----+----------------------------------------------------------------+
| 06  | > Manual (key-entered)                                         |
+-----+----------------------------------------------------------------+
| 07  | > Contact-less via Chip rules                                  |
+-----+----------------------------------------------------------------+
| 08  | > Reserved for ISO use                                         |
+-----+----------------------------------------------------------------+
| 09  | > PAN entry via electronic commerce, including remote chip     |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   | > From file                                                    |
|  10 |                                                                |
+=====+================================================================+
| >   | > Full magnetic stripe read (optionally supported)             |
|  11 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Contactless via magnetic stripe rules                        |
|  12 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Integrated circuit card, CVV data may be unreliable          |
|  13 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > PAN auto-entry via chip PayPass mapping                      |
|  14 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Contactless M/Chip PayPass Mapping                           |
|  15 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > PAN manual entry via e-commerce                              |
|  16 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Contactless input PayPass Mapping Service                    |
|  17 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Store-and-forward                                            |
|  18 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > MICR Reader (POS Check Service); U.S. Only                   |
|  19 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Store-and-forward resubmission                               |
|  20 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Electronic Commerce                                          |
|  21 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Radio Frequency Identification Indicator                     |
|  22 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Mobile Commerce (mCommerce)                                  |
|  23 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Voice Authorizations                                         |
|  24 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Voice Response Unit (VRU)                                    |
|  25 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Batch Authorizations                                         |
|  26 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Batch Authorization Cash Access                              |
|  27 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Biometrics                                                   |
|  28 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Credentials on File                                          |
|  29 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Reserved for ISO use                                         |
|  30 |                                                                |
| -60 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Reserved for national use                                    |
|  61 |                                                                |
| -78 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Chip card or chip-capable terminal was unable to process the |
|  79 | > transaction using the data on the chip or magnetic stripe,   |
|     | > the PAN was entered manually, or the Acquirer is not         |
|     | > certified to process the value 80.                           |
+-----+----------------------------------------------------------------+
| >   | > Chip card or chip-capable terminal was unable to process the |
|  80 | > transaction using the data on the chip, the PAN was entered  |
|     | > via magnetic stripe. The full track data was read from the   |
|     | > data encoded on the card and transmitted within the          |
|     | > authorization request on Track-2 Data (DE 35) or Track-1     |
|     | > Data (DE 45) without alteration or truncation.               |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   | > Reserved for private use                                     |
|  81 |                                                                |
| -89 |                                                                |
+=====+================================================================+
| >   | > PAN auto-entry via magnetic stripe---the full track data has |
|  90 | > been read from the data encoded on the card and transmitted  |
|     | > within the authorization request in DE 35 (Track 2 Data) or  |
|     | > DE 45 (Track 1 Data) without alteration or truncation.       |
+-----+----------------------------------------------------------------+
| >   | > PAN auto-entry via contact-less magnetic stripe---the full   |
|  91 | > track data has been read from the data on the card and       |
|     | > transmitted within the authorization request in DE 35 (Track |
|     | > 2 Data) or DE 45 (Track 1 Data) without alteration or        |
|     | > truncation.                                                  |
+-----+----------------------------------------------------------------+
| >   | > PAN Auto Entry via Server (issuer, acquirer, or third-party  |
|  92 | > vendor system)                                               |
+-----+----------------------------------------------------------------+
| >   | > Merchant-presented QR code, chip information included        |
|  93 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Merchant-presented QR code, chip information excluded        |
|  94 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Visa only. Chip card with unreliable Card Verification Value |
|  95 | > (CVV) data.                                                  |
+-----+----------------------------------------------------------------+
| >   | > Reserved for private use                                     |
|  96 |                                                                |
| -99 |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| > * |                                                                |
| *Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| >   |                                                                |
|  3: |                                                                |
| >   |                                                                |
| PIN |                                                                |
| >   |                                                                |
|  En |                                                                |
| try |                                                                |
| >   |                                                                |
| Cap |                                                                |
| abi |                                                                |
| lit |                                                                |
| y** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > Unspecified                                                  |
+-----+----------------------------------------------------------------+
| > 1 | > PIN entry capability                                         |
+-----+----------------------------------------------------------------+
| > 2 | > No PIN entry capability                                      |
+-----+----------------------------------------------------------------+
| > 3 | > Terminal has PIN entry capability, but PIN pad is out of     |
|     | > service                                                      |
+-----+----------------------------------------------------------------+
| >   | > Reserved for ISO use                                         |
| 4-5 |                                                                |
+-----+----------------------------------------------------------------+
| > 6 | > PIN pad inoperative                                          |
+-----+----------------------------------------------------------------+
| > 7 | > Reserved for national use                                    |
+-----+----------------------------------------------------------------+
| > 8 | > Reserved for private use                                     |
+-----+----------------------------------------------------------------+
| > 9 | > PIN verified by terminal device                              |
+-----+----------------------------------------------------------------+

#### Data Element 025 -- POS Condition Codes Table {#data-element-025-pos-condition-codes-table .unnumbered}

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 025 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| > P |                                                                |
| oin |                                                                |
| t-o |                                                                |
| f-S |                                                                |
| erv |                                                                |
| ice |                                                                |
| >   |                                                                |
| Con |                                                                |
| dit |                                                                |
| ion |                                                                |
| > C |                                                                |
| ode |                                                                |
| s** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Normal presentment                                           |
|  00 |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   | > Customer not present                                         |
|  01 |                                                                |
+=====+================================================================+
| >   | > ATM Transactions                                             |
|  02 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Merchant suspicious                                          |
|  03 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Electronic card register interface                           |
|  04 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Customer present, card not present                           |
|  05 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Pre-Authorized request                                       |
|  06 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Telephone device/mobile phone request                        |
|  07 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Mail and/or telephone order                                  |
|  08 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Security alert                                               |
|  09 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Customer identity verified                                   |
|  10 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Suspected fraud                                              |
|  11 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Security reasons                                             |
|  12 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Customer terminal (home terminal)                            |
|  15 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Administration terminal                                      |
|  16 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Chargeback (validation request or advice)                    |
|  17 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Unattended terminal unable to retain card                    |
|  27 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Reserved for ISO use                                         |
|  28 |                                                                |
| -39 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Customer not present, standing order/recurring payment       |
|  40 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Reserved for national use                                    |
|  41 |                                                                |
| -50 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Point of Sale (POS)                                          |
|  51 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > CVV verified and valid                                       |
|  52 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > CVV verified and invalid                                     |
|  53 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Non-Secure/Security unknown electronic commerce transaction  |
|  54 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Secure electronic transaction with cardholder certificate    |
|  55 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Secure electronic transaction without cardholder certificate |
|  56 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Channel-encrypted electronic commerce transaction            |
|  57 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Secure electronic transaction containing a digital signature |
|  58 |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   | > Deferred billing                                             |
|  59 |                                                                |
+=====+================================================================+
| >   | > Internet PIN debit transaction                               |
|  60 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Reserved for private use                                     |
|  61 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Account Verification w/o Auth; product eligibility inquiry   |
|  62 | > without authorization                                        |
+-----+----------------------------------------------------------------+
| >   | > POS Check original full financial transaction or adjustment; |
|  63 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Chargeback reversal                                          |
|  64 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Request for telecode verification without authorization      |
|  65 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Electronic commerce request by public network                |
|  66 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Reserved for private use                                     |
|  67 |                                                                |
| -70 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Card present, magnetic stripe cannot be read (key-entered)   |
|  71 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Unattended terminal able to retain card                      |
|  72 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Reserved for private use                                     |
|  73 |                                                                |
| -99 |                                                                |
+-----+----------------------------------------------------------------+

#### Data Element 026 -- POS PIN Capture Codes Table {#data-element-026-pos-pin-capture-codes-table .unnumbered}

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 026 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| > P |                                                                |
| oin |                                                                |
| t-o |                                                                |
| f-S |                                                                |
| erv |                                                                |
| ice |                                                                |
| >   |                                                                |
| PIN |                                                                |
| > C |                                                                |
| apt |                                                                |
| ure |                                                                |
| > C |                                                                |
| ode |                                                                |
| s** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid                                                      |
|  00 |                                                                |
| -04 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Indicates the maximum number of PIN characters that the      |
|  05 | > terminal can accept                                          |
| -12 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Reserved                                                     |
|  13 |                                                                |
| -99 |                                                                |
+-----+----------------------------------------------------------------+

#### Data Element 039 -- Response Codes Table {#data-element-039-response-codes-table .unnumbered}

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 039 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Re |                                                                |
| spo |                                                                |
| nse |                                                                |
| > C |                                                                |
| ode |                                                                |
| s** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Approved                                                     |
|  00 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Refer to Card Issuer                                         |
|  01 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Refer to Card Issuer, Special Condition                      |
|  02 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid Merchant                                             |
|  03 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Lost/Stolen Card                                             |
|  04 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Do not Honor                                                 |
|  05 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Error                                                        |
|  06 |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   | > Pick-up Card, Special Condition                              |
|  07 |                                                                |
+=====+================================================================+
| >   | > Honor with Identification                                    |
|  08 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Approved -- Partial Amount                                   |
|  10 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid Transaction                                          |
|  12 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid Amount                                               |
|  13 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid Card Number                                          |
|  14 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid Issuer                                               |
|  15 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Customer Cancellation, Reversal                              |
|  17 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Issuer File Update Field Edit Error                          |
|  27 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Format Error                                                 |
|  30 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Bank Not Supported by Switch (Future Use)                    |
|  31 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Partial Reversal                                             |
|  32 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Expired Card, Pick-up                                        |
|  33 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Suspect Fraud                                                |
|  34 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > No Credit Account (Future Use)                               |
|  39 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Requested Function Not Supported                             |
|  40 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Lost Card Not Captured                                       |
|  41 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > No universal account                                         |
|  42 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Stolen Card, Pick-up                                         |
|  43 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Insufficient Funds                                           |
|  51 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > No Checking Account (Future Use)                             |
|  52 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > No Savings Account (Future Use)                              |
|  53 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Expired Card                                                 |
|  54 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid PIN                                                  |
|  55 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > No Card Account                                              |
|  56 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Transaction not Permitted to Cardholder                      |
|  57 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Transaction not Permitted to Acquirer/Terminal               |
|  58 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Suspected Fraud                                              |
|  59 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Exceeds Withdrawal Amount Limit                              |
|  61 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Restricted Card                                              |
|  62 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Decline Error in Decryption of PIN Block / Security          |
|  63 | > Violation                                                    |
+-----+----------------------------------------------------------------+
| >   | > Original Amount Incorrect, Reversal                          |
|  64 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Exceeds Withdrawal Frequency Limit                           |
|  65 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Response Received Late                                       |
|  68 |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   | > Invalid Transaction; Contact Card Issuer                     |
|  70 |                                                                |
+=====+================================================================+
| >   | > PIN Change Decline                                           |
|  71 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Allowed Number of PIN Tries Exceeded                         |
|  75 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid/Nonexistent "To" Account Specified (Future Use)      |
|  76 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid/Nonexistent "From" Account Specified (Future Use)    |
|  77 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid/Nonexistent Account Specified (General) (Future Use) |
|  78 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Key Exchange Validation Failed                               |
|  79 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > System not Available (Future Use)                            |
|  80 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid Transaction (PIN Block Format Error)                 |
|  81 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Time Out Issuer                                              |
|  82 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid Authorization Life Cycle                             |
|  84 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Approved -- Account Verification                             |
|  85 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > PIN Validation Not Possible or Invalid PVK/ZPK/Offset/PVV    |
|  86 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Approved -- Purchase Only                                    |
|  87 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid Transaction (CVC1/CVV2/CID/iCVV Format Error)        |
|  88 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Bad CVC1/iCVV/Expiry Date                                    |
|  89 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Issuer or Switch Inoperative                                 |
|  91 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Unable to Route Transaction                                  |
|  92 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Transaction Cannot be Completed                              |
|  93 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Duplicate Transmission                                       |
|  94 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Refer to Card Issuer / System Error                          |
|  96 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Already Activated Card                                       |
|  97 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Approve Transaction in Super Green Path                      |
|  99 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Auth-Host Timed Out                                          |
|  AT |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Cryptogram Decline                                           |
|  CD |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Invalid Currency                                             |
|  CN |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Duplicate Record Found Against Name and DOB / Auth-Host Down |
|  DN |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Status inquiry / Account Verification declined due to        |
|  EX | > invalid Card Expiry                                          |
+-----+----------------------------------------------------------------+
| >   | > Bad CVV2/CID/Expiry Date                                     |
|  E7 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > General AVS Decline                                          |
|  GA |                                                                |
+-----+----------------------------------------------------------------+
| >   | > General Card Decline                                         |
|  GC |                                                                |
+-----+----------------------------------------------------------------+
| >   | > General CVV2 Decline                                         |
|  GV |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Card is Pre-Active                                           |
|  PA |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Purse Found with Invalid Status                              |
|  PF |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   | > PIN Change Fail Invalid Data                                 |
|  PI |                                                                |
+=====+================================================================+
| >   | > Bad PIN (Invalid PIN Block Length)                           |
|  PL |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Inactive Card                                                |
|  SA |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Account Closed                                               |
|  SD |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Status inquiry / Account Verification declined due to        |
|  SX | > invalid Card Status                                          |
+-----+----------------------------------------------------------------+
| >   | > Card Technology Mismatch                                     |
|  TM |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Token Provisioning / Authorization Request declined with Red |
|  TR | > Path                                                         |
+-----+----------------------------------------------------------------+
| >   | > Bad AVS                                                      |
|  X1 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Strong Customer Authentication Required                      |
|  1A |                                                                |
+-----+----------------------------------------------------------------+
| >   | > ATC Validation Failed (Authorization Host must set response  |
|  AI | > code AI in case of ATC validation failure at authorization   |
|     | > host side)                                                   |
+-----+----------------------------------------------------------------+
| >   | > [Valid account but amount not supported]{.mark}              |
|  [X |                                                                |
| 6]{ |                                                                |
| .ma |                                                                |
| rk} |                                                                |
+-----+----------------------------------------------------------------+

> \*\*For any forced post message 0x2x, auth host must respond with
> approved response code i.e. "00"

##### Data Element 043 -- Card Acceptor Name/Location {#data-element-043-card-acceptor-namelocation .unnumbered}

> \*\*Usage-1 Details (For existing clients):

+----+----------------+----------------------------+------+-----------+
| >  |                |                            |      |           |
|  * |                |                            |      |           |
| *S |                |                            |      |           |
| ub |                |                            |      |           |
| >  |                |                            |      |           |
| El |                |                            |      |           |
| em |                |                            |      |           |
| en |                |                            |      |           |
| ts |                |                            |      |           |
| >  |                |                            |      |           |
| of |                |                            |      |           |
| >  |                |                            |      |           |
|  D |                |                            |      |           |
| E- |                |                            |      |           |
| 43 |                |                            |      |           |
| >  |                |                            |      |           |
| -- |                |                            |      |           |
| >  |                |                            |      |           |
| Ca |                |                            |      |           |
| rd |                |                            |      |           |
| >  |                |                            |      |           |
| Ac |                |                            |      |           |
| ce |                |                            |      |           |
| pt |                |                            |      |           |
| or |                |                            |      |           |
| >  |                |                            |      |           |
|  N |                |                            |      |           |
| am |                |                            |      |           |
| e/ |                |                            |      |           |
| Lo |                |                            |      |           |
| ca |                |                            |      |           |
| ti |                |                            |      |           |
| on |                |                            |      |           |
| >  |                |                            |      |           |
|  ( |                |                            |      |           |
| Us |                |                            |      |           |
| ag |                |                            |      |           |
| e- |                |                            |      |           |
| 1) |                |                            |      |           |
| ** |                |                            |      |           |
+====+================+============================+======+===========+
| >  | > **Field      | > **Description**          | > *  | >         |
|  * | > Name**       |                            | *Pos |  **Format |
| *S |                |                            | itio | >         |
| ub |                |                            | >    | (ASCII)** |
| >  |                |                            |  n** |           |
|  F |                |                            |      |           |
| ie |                |                            |      |           |
| ld |                |                            |      |           |
| >  |                |                            |      |           |
|  N |                |                            |      |           |
| o. |                |                            |      |           |
| ** |                |                            |      |           |
+----+----------------+----------------------------+------+-----------+
| >  | > Address      | > Merchant's Street        | >    | > 25 AN   |
| 43 |                | > Address                  | 1-25 |           |
| .1 |                |                            |      |           |
+----+----------------+----------------------------+------+-----------+
| >  | > City         | > Merchant's City Name     | > 2  | > 13 AN   |
| 43 |                |                            | 6-38 |           |
| .2 |                |                            |      |           |
+----+----------------+----------------------------+------+-----------+
| >  | > State        | > Merchant's State         | > 3  | > 2 AN    |
| 43 |                |                            | 9-40 |           |
| .3 |                |                            |      |           |
+----+----------------+----------------------------+------+-----------+
| >  | > Country      | > Merchant's Country Code  | > 4  | > 3 AN    |
| 43 |                |                            | 1-43 |           |
| .4 |                |                            |      |           |
+----+----------------+----------------------------+------+-----------+

> \*\*Usage-2 Details (For new clients):

+----+----------------+----------------------------+------+-----------+
| >  |                |                            |      |           |
|  * |                |                            |      |           |
| *S |                |                            |      |           |
| ub |                |                            |      |           |
| >  |                |                            |      |           |
| El |                |                            |      |           |
| em |                |                            |      |           |
| en |                |                            |      |           |
| ts |                |                            |      |           |
| >  |                |                            |      |           |
| of |                |                            |      |           |
| >  |                |                            |      |           |
|  D |                |                            |      |           |
| E- |                |                            |      |           |
| 43 |                |                            |      |           |
| >  |                |                            |      |           |
| -- |                |                            |      |           |
| >  |                |                            |      |           |
| Ca |                |                            |      |           |
| rd |                |                            |      |           |
| >  |                |                            |      |           |
| Ac |                |                            |      |           |
| ce |                |                            |      |           |
| pt |                |                            |      |           |
| or |                |                            |      |           |
| >  |                |                            |      |           |
|  N |                |                            |      |           |
| am |                |                            |      |           |
| e/ |                |                            |      |           |
| Lo |                |                            |      |           |
| ca |                |                            |      |           |
| ti |                |                            |      |           |
| on |                |                            |      |           |
| >  |                |                            |      |           |
|  ( |                |                            |      |           |
| Us |                |                            |      |           |
| ag |                |                            |      |           |
| e- |                |                            |      |           |
| 2) |                |                            |      |           |
| ** |                |                            |      |           |
+====+================+============================+======+===========+
| >  | > **Field      | > **Description**          | > *  | >         |
|  * | > Name**       |                            | *Pos |  **Format |
| *S |                |                            | itio | >         |
| ub |                |                            | >    | (ASCII)** |
| >  |                |                            |  n** |           |
|  F |                |                            |      |           |
| ie |                |                            |      |           |
| ld |                |                            |      |           |
| >  |                |                            |      |           |
|  N |                |                            |      |           |
| o. |                |                            |      |           |
| ** |                |                            |      |           |
+----+----------------+----------------------------+------+-----------+
| >  | > Address      | > Merchant's Street        | >    | > 25 AN   |
| 43 |                | > Address                  | 1-25 |           |
| .1 |                |                            |      |           |
+----+----------------+----------------------------+------+-----------+

+----+----------------+----------------------------+------+-----------+
| >  | > City         | > Merchant's City Name     | > 2  | > 15 AN   |
| 43 |                |                            | 6-40 |           |
| .2 |                |                            |      |           |
+====+================+============================+======+===========+
| >  | > State        | > Merchant's State         | > 4  | > 2 AN    |
| 43 |                |                            | 1-42 |           |
| .3 |                |                            |      |           |
+----+----------------+----------------------------+------+-----------+
| >  | > Country      | > Merchant's Country Code  | > 4  | > 3 AN    |
| 43 |                |                            | 3-45 |           |
| .4 |                |                            |      |           |
+----+----------------+----------------------------+------+-----------+
| >  | > Card         | > Merchant's Name          | > 4  | > 25 AN   |
| 43 | > Acceptor     |                            | 6-70 |           |
| .5 | > Name         |                            |      |           |
+----+----------------+----------------------------+------+-----------+

> \*\* Note: In case of Usage-2, Card Acceptor Name will be sent to
> Auth-Host if only received from network as mostly it is sent by
> network in Address field (43.1). In this case, field-43.5 will consist
> of ALL spaces.
>
> Currently, it is only supported by FISERV.

#### Data Element 048 -- Additional Processing Data {#data-element-048-additional-processing-data .unnumbered}

+----+------------+--------------------------------+------+-----------+
| >  |            |                                |      |           |
|  * |            |                                |      |           |
| *S |            |                                |      |           |
| ub |            |                                |      |           |
| >  |            |                                |      |           |
| El |            |                                |      |           |
| em |            |                                |      |           |
| en |            |                                |      |           |
| ts |            |                                |      |           |
| >  |            |                                |      |           |
| of |            |                                |      |           |
| >  |            |                                |      |           |
|  D |            |                                |      |           |
| E- |            |                                |      |           |
| 48 |            |                                |      |           |
| >  |            |                                |      |           |
| -- |            |                                |      |           |
| >  |            |                                |      |           |
| Ad |            |                                |      |           |
| di |            |                                |      |           |
| ti |            |                                |      |           |
| on |            |                                |      |           |
| al |            |                                |      |           |
| >  |            |                                |      |           |
| Pr |            |                                |      |           |
| oc |            |                                |      |           |
| es |            |                                |      |           |
| si |            |                                |      |           |
| ng |            |                                |      |           |
| >  |            |                                |      |           |
| Da |            |                                |      |           |
| ta |            |                                |      |           |
| ** |            |                                |      |           |
+====+============+================================+======+===========+
| >  | > **Field  | > **Description**              | >    | >         |
|  * | > Name**   |                                | **Po |  **Format |
| *S |            |                                | siti | >         |
| ub |            |                                | on** | (ASCII)** |
| >  |            |                                |      |           |
|  F |            |                                |      |           |
| ie |            |                                |      |           |
| ld |            |                                |      |           |
| >  |            |                                |      |           |
|  N |            |                                |      |           |
| o. |            |                                |      |           |
| ** |            |                                |      |           |
+----+------------+--------------------------------+------+-----------+
| >  | > EMV --   | > The identifiers of the       | >    | > 12 AN   |
| 48 | > Issuer   | > Issuer Script Commands sent  | 1-12 |           |
| .1 | > Script   | > in the response as a result  |      |           |
|    | > Command  | > of EMV processing.           |      |           |
|    | > I        | >                              |      |           |
|    | dentifiers | > Below are the supported      |      |           |
|    |            | > Script Command Identifiers:  |      |           |
|    |            |                                |      |           |
|    |            | -   **01** -- PIN Change       |      |           |
|    |            |                                |      |           |
|    |            | -   **02** -- PIN Unblock      |      |           |
|    |            |                                |      |           |
|    |            | > The field will be            |      |           |
|    |            | > left-justified space-filled. |      |           |
|    |            | > If multiple script commands  |      |           |
|    |            | > are sent in a transaction,   |      |           |
|    |            | > this field will contain all  |      |           |
|    |            | > script commands identifiers. |      |           |
|    |            | > For example, if both PIN     |      |           |
|    |            | > Change (01) & PIN Unblock    |      |           |
|    |            | > (02) scripts are sent, this  |      |           |
|    |            | > sub-field will be formatted  |      |           |
|    |            | > as: \'0102 \'.               |      |           |
+----+------------+--------------------------------+------+-----------+
| >  | > EMV --   | > The status of the EMV Issuer | > 13 | > 1 AN    |
| 48 | > Result   | > Script Commands sent in the  |      |           |
| .2 | > of       | > previous transaction. It     |      |           |
|    | > Issuer   | > will tell that whether the   |      |           |
|    | > Script   | > issuer script sent in        |      |           |
|    | > Commands | > response was successfully    |      |           |
|    | > sent in  | > executed on the card or not. |      |           |
|    | > Previous | > Possible values are:         |      |           |
|    | > T        |                                |      |           |
|    | ransaction | -   **(space)** -- Pending     |      |           |
|    |            |                                |      |           |
|    |            | -   **P** -- Passed            |      |           |
|    |            |                                |      |           |
|    |            | -   **F** -- Failed            |      |           |
+----+------------+--------------------------------+------+-----------+
| >  | > T        | > The indicator which          | > 1  | > 2 AN    |
| 48 | ransaction | > described the purpose or     | 4-15 |           |
| .3 | >          | > type of processing performed |      |           |
|    | Processing | > on a transaction.            |      |           |
|    | >          | >                              |      |           |
|    |  Indicator | > The field is a 2 byte        |      |           |
|    |            | > alphanumeric which can hold  |      |           |
|    |            | > below list of possible       |      |           |
|    |            | > values:                      |      |           |
|    |            |                                |      |           |
|    |            | -   **PC** -- The indicator    |      |           |
|    |            |     > identifies a Pending     |      |           |
|    |            |     > Credit Financial Advice  |      |           |
|    |            |     > (0220). The credit will  |      |           |
|    |            |     > be posted to the card    |      |           |
|    |            |     > account against the      |      |           |
|    |            |     > credit authorization.    |      |           |
|    |            |                                |      |           |
|    |            | -   **HC** -- The indicator    |      |           |
|    |            |     > represents a debit       |      |           |
|    |            |     > authorization            |      |           |
|    |            |     > advice (0120) which is   |      |           |
|    |            |     > to hold the credit given |      |           |
|    |            |     > in 0220 credit financial |      |           |
|    |            |     > advice.                  |      |           |
+----+------------+--------------------------------+------+-----------+
| >  | > Card     | > This field will identify the | > 16 | > 1 AN    |
| 48 | > Status   | > result of the Card Status    |      |           |
| .4 | >          | > Validation Service. Refer to |      |           |
|    | Validation | > the table below for the      |      |           |
|    | > Result   | > possible result code values. |      |           |
|    | > Code     |                                |      |           |
+----+------------+--------------------------------+------+-----------+

+----+------------+--------------------------------+------+-----------+
| >  | > Card     | > This field will describe the | > 17 | > 1 N     |
| 48 | > Expiry   | > result of the Card Expiry    |      |           |
| .5 | >          | > Validation Service. Possible |      |           |
|    | Validation | > result code values are:      |      |           |
|    | > Result   |                                |      |           |
|    | > Code     | -   1 -- Expired Card          |      |           |
+====+============+================================+======+===========+
| >  | > Card     | > This field will indicate the | > 18 | > 1 N     |
| 48 | > Balance  | > state of the card balance    |      |           |
| .6 | >          | > (in case of insufficient     |      |           |
|    |  Indicator | > funds). Possible result code |      |           |
|    |            | > values are:                  |      |           |
|    |            |                                |      |           |
|    |            | -   0 -- Card has zero balance |      |           |
|    |            |                                |      |           |
|    |            | -   1 -- Card has positive     |      |           |
|    |            |     > balance                  |      |           |
|    |            |                                |      |           |
|    |            | -   2 -- Card has negative     |      |           |
|    |            |     > balance                  |      |           |
+----+------------+--------------------------------+------+-----------+
| >  | > Message  | > This field is used in        | > 1  | > 2 AN    |
| 48 | > Reason   | > reversals (04xx) to indicate | 9-20 |           |
| .7 | > Code     | > the response code of         |      |           |
|    |            | > original transaction.        |      |           |
|    |            | >                              |      |           |
|    |            | > This code will be used in    |      |           |
|    |            | > reversals initiated by i2c   |      |           |
|    |            | > as a result of processing    |      |           |
|    |            | > failure of authorizations    |      |           |
|    |            | > which are already approved   |      |           |
|    |            | > by the Authorization Host.   |      |           |
|    |            | >                              |      |           |
|    |            | > The key possible values      |      |           |
|    |            | > includes:                    |      |           |
|    |            | >                              |      |           |
|    |            | > **03** -- Invalid merchant   |      |           |
|    |            | >                              |      |           |
|    |            | > **05** -- System malfunction |      |           |
|    |            | >                              |      |           |
|    |            | > **57** -- Transaction not    |      |           |
|    |            | > permitted to cardholder      |      |           |
|    |            | >                              |      |           |
|    |            | > **59** -- Suspected Fraud /  |      |           |
|    |            | > Limits Violation             |      |           |
|    |            | >                              |      |           |
|    |            | > Other possible values may    |      |           |
|    |            | > include all values of Field  |      |           |
|    |            | > 39.                          |      |           |
+----+------------+--------------------------------+------+-----------+
| >  | > A        | > It will contain 5 digit ATC  | > 2  | > 5 N     |
| 48 | pplication | > value. Default Value 00000.  | 1-25 |           |
| .8 | > T        |                                |      |           |
|    | ransaction |                                |      |           |
|    | > Counter  |                                |      |           |
|    | > (ATC)    |                                |      |           |
+----+------------+--------------------------------+------+-----------+
| >  | > Process  | > It will contain process      | > 2  | > 3 AN    |
| 48 | > Mode     | > mode. Possible Values:       | 6-28 |           |
| .9 |            |                                |      |           |
|    |            | -   SMS                        |      |           |
|    |            |                                |      |           |
|    |            | -   DMS                        |      |           |
|    |            |                                |      |           |
|    |            | -   AXS (Represents STAR       |      |           |
|    |            |     > Access network)          |      |           |
+----+------------+--------------------------------+------+-----------+
| >  | > Expire   | > This will only applicable    | > 2  | > 1 N     |
|  4 | > Pre Auth | > for Reversal messages x4xx.  | 9-33 |           |
| 8. | > Reversal | > Possible values:             |      |           |
| 10 | > Message  |                                |      |           |
|    | >          | -   Y                          |      |           |
|    | Indicator. |                                |      |           |
|    |            | -   N                          |      |           |
|    |            |                                |      |           |
|    |            | > Value Y represent that the   |      |           |
|    |            | > respective x4xx is the       |      |           |
|    |            | > reversal messages of Pre     |      |           |
|    |            | >                              |      |           |
|    |            | > Authorization transaction    |      |           |
|    |            | > automatically generated by   |      |           |
|    |            | > i2c System to expire the     |      |           |
|    |            | > authorization for which no   |      |           |
|    |            | > clearing / completion        |      |           |
|    |            | > message receive from network |      |           |
|    |            | > after N number of configured |      |           |
|    |            | > days.                        |      |           |
+----+------------+--------------------------------+------+-----------+

+------------------------------------------------+---------------------+
| > **Card Status Result Codes**                 |                     |
+================================================+=====================+
| > **Card Status**                              | > **Result Code**   |
+------------------------------------------------+---------------------+
| > Already Active Card                          | > 1                 |
+------------------------------------------------+---------------------+
| > Pick Up -- No Fraud                          | > 2                 |
+------------------------------------------------+---------------------+
| > Pick Up -- Fraud Account                     | > 3                 |
+------------------------------------------------+---------------------+
| > Restricted Card                              | > 4                 |
+------------------------------------------------+---------------------+
| > Lost Card                                    | > 5                 |
+------------------------------------------------+---------------------+
| > Stolen Card                                  | > 6                 |
+------------------------------------------------+---------------------+
| > Inactive Card                                | > 7                 |
+------------------------------------------------+---------------------+
| > Suspected Card                               | > 8                 |
+------------------------------------------------+---------------------+
| > Pre-active Card                              | > 9                 |
+------------------------------------------------+---------------------+
| > Closed Card                                  | > A                 |
+------------------------------------------------+---------------------+

#### Data Element 054 -- Additional Amounts Codes Table {#data-element-054-additional-amounts-codes-table .unnumbered}

+----+-----------------------------------------------------------------+
| >  |                                                                 |
| ** |                                                                 |
| Da |                                                                 |
| ta |                                                                 |
| >  |                                                                 |
|  E |                                                                 |
| le |                                                                 |
| me |                                                                 |
| nt |                                                                 |
| >  |                                                                 |
|  0 |                                                                 |
| 54 |                                                                 |
| >  |                                                                 |
| -- |                                                                 |
| >  |                                                                 |
|  P |                                                                 |
| os |                                                                 |
| it |                                                                 |
| io |                                                                 |
| ns |                                                                 |
| >  |                                                                 |
|  1 |                                                                 |
| -- |                                                                 |
| 2: |                                                                 |
| >  |                                                                 |
|  A |                                                                 |
| cc |                                                                 |
| ou |                                                                 |
| nt |                                                                 |
| >  |                                                                 |
| Ty |                                                                 |
| pe |                                                                 |
| ** |                                                                 |
+====+=================================================================+
| >  | > **Definition**                                                |
| ** |                                                                 |
| Co |                                                                 |
| de |                                                                 |
| ** |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Not Specified or Default Account                              |
| 00 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Savings Account                                               |
| 10 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Checking Account                                              |
| 20 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Credit Card Account                                           |
| 30 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Universal Account                                             |
| 40 |                                                                 |
+----+-----------------------------------------------------------------+

+----+-----------------------------------------------------------------+
| >  |                                                                 |
| ** |                                                                 |
| Da |                                                                 |
| ta |                                                                 |
| >  |                                                                 |
|  E |                                                                 |
| le |                                                                 |
| me |                                                                 |
| nt |                                                                 |
| >  |                                                                 |
|  0 |                                                                 |
| 54 |                                                                 |
| >  |                                                                 |
| -- |                                                                 |
| >  |                                                                 |
|  P |                                                                 |
| os |                                                                 |
| it |                                                                 |
| io |                                                                 |
| ns |                                                                 |
| >  |                                                                 |
|  3 |                                                                 |
| -- |                                                                 |
| 4: |                                                                 |
| >  |                                                                 |
| Am |                                                                 |
| ou |                                                                 |
| nt |                                                                 |
| >  |                                                                 |
| Ty |                                                                 |
| pe |                                                                 |
| ** |                                                                 |
+====+=================================================================+
| >  | > **Definition**                                                |
| ** |                                                                 |
| Co |                                                                 |
| de |                                                                 |
| ** |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Unknown                                                       |
| 00 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Ledger Balance                                                |
| 01 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Available Balance                                             |
| 02 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Amount Owing                                                  |
| 03 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Amount Due                                                    |
| 04 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Account Available Credit                                      |
| 05 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Amount Currency Conversion Assessment                         |
| 06 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Over Limit Fee                                                |
| 07 |                                                                 |
+----+-----------------------------------------------------------------+

+----+-----------------------------------------------------------------+
| >  | > Over Payment Fee                                              |
| 08 |                                                                 |
+====+=================================================================+
| >  | > Healthcare Eligibility Amount                                 |
| 10 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Prescription Eligibility Amount                               |
| 11 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Credit Line                                                   |
| 16 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Prepaid Online Bill Pay Fee Amount or POS balance/ATM         |
| 17 | > overdraft protection balance                                  |
+----+-----------------------------------------------------------------+
| >  | > Beginning Balance                                             |
| 18 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Amount Remaining this Cycle                                   |
| 20 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Amount Cash Back                                              |
| 40 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Amount Goods and Services                                     |
| 41 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Amount Surcharge [Amount, anticipated]{.mark}                 |
| 42 |                                                                 |
| >  |                                                                 |
| >  |                                                                 |
|  [ |                                                                 |
| 44 |                                                                 |
| ]{ |                                                                 |
| .m |                                                                 |
| ar |                                                                 |
| k} |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Hold Amount                                                   |
| 56 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Original Amount or Pre-Authorized Amount                      |
| 57 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Authorized Amount (StarAccess)                                |
| 58 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Floor Limit                                                   |
| 59 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Fee Amount: Added in Card-Holder Billing Amount i.e. DE 06.   |
| 72 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Co-pay Amount                                                 |
| 80 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Available Credit or Check Amount                              |
| 90 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Credit Limit or Original amount/Tip or Gratuity for Service   |
| 91 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Cash Deposit Amount                                           |
| 93 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Check Deposit Amount                                          |
| 94 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Foreign Exchange Fee                                          |
| 95 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Merchant Local Currency/Cash Benefit Amount                   |
| 96 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Courtesy Amount                                               |
| 98 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Original Cash Back Amount                                     |
| 99 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Interchange Fee                                               |
| 73 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Total Authorization Amount (in case of Incremental            |
| 43 | > Authorization total accumulative amount)                      |
+----+-----------------------------------------------------------------+
| >  | > ATM Excess Usage Fee                                          |
| 46 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Currency Conversion Excess Usage Fee                          |
| 47 |                                                                 |
+----+-----------------------------------------------------------------+

#### Data Element 061 -- Point-of-Service Data Codes Table {#data-element-061-point-of-service-data-codes-table .unnumbered}

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| > 1 |                                                                |
| >   |                                                                |
|  (A |                                                                |
| tte |                                                                |
| nda |                                                                |
| nce |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > Attended                                                     |
+-----+----------------------------------------------------------------+
| > 1 | > Unattended                                                   |
+-----+----------------------------------------------------------------+
| > 2 | > No terminal used (voice/audio response unit \[ARU\]          |
|     | > authorization)                                               |
+-----+----------------------------------------------------------------+
| > 9 | > Unknown/data not available                                   |
+-----+----------------------------------------------------------------+
| > R | > Reserved for National or Private Use                         |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| > 2 |                                                                |
| >   |                                                                |
| (Op |                                                                |
| era |                                                                |
| tor |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > Customer-operated                                            |
+-----+----------------------------------------------------------------+
| > 1 | > Card acceptor-operated                                       |
+-----+----------------------------------------------------------------+
| > 2 | > Administrative                                               |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| > 3 |                                                                |
| >   |                                                                |
| (Te |                                                                |
| rmi |                                                                |
| nal |                                                                |
| >   |                                                                |
|  Lo |                                                                |
| cat |                                                                |
| ion |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > On premise                                                   |
+-----+----------------------------------------------------------------+
| > 1 | > Off premise                                                  |
+-----+----------------------------------------------------------------+
| > 2 | > On premises of cardholder (Home PC)                          |
+-----+----------------------------------------------------------------+
| > 3 | > No terminal used                                             |
+-----+----------------------------------------------------------------+
| > 4 | > On premises of card acceptor facility \[Card-Holder terminal |
|     | > including Home PC, mobile phone, PDA\]                       |
+-----+----------------------------------------------------------------+
| > 6 | > Off cardholder premised, unattended                          |
+-----+----------------------------------------------------------------+
| > 9 | > Unknown data not available                                   |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| > 4 |                                                                |
| >   |                                                                |
|  (C |                                                                |
| ard |                                                                |
| hol |                                                                |
| der |                                                                |
| >   |                                                                |
|  Pr |                                                                |
| ese |                                                                |
| nce |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > Customer present                                             |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| > 1 | > Customer not present                                         |
+=====+================================================================+
| > 2 | > Mail/Facsimile order (customer not present)                  |
+-----+----------------------------------------------------------------+
| > 3 | > Telephone order                                              |
+-----+----------------------------------------------------------------+
| > 4 | > Customer not present, standing order/recurring payment       |
+-----+----------------------------------------------------------------+
| > 5 | > Cardholder not present (Electronic order \[home PC,          |
|     | > Internet, mobile phone, PDS\])                               |
+-----+----------------------------------------------------------------+
| > 8 | > Pre-Authorized purchase                                      |
+-----+----------------------------------------------------------------+
| > 9 | > Unknown data not available                                   |
+-----+----------------------------------------------------------------+
| > S | > Installment Payment                                          |
+-----+----------------------------------------------------------------+
| > R | > Reserved                                                     |
+-----+----------------------------------------------------------------+
| > A | > CardHolder not present Stand-In Authorization                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| > 5 |                                                                |
| >   |                                                                |
|  (C |                                                                |
| ard |                                                                |
| >   |                                                                |
|  Pr |                                                                |
| ese |                                                                |
| nce |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > Card present                                                 |
+-----+----------------------------------------------------------------+
| > 1 | > Card not present                                             |
+-----+----------------------------------------------------------------+
| > 8 | > Pre-Authorized purchase                                      |
+-----+----------------------------------------------------------------+
| > 9 | > Unknown / data not available                                 |
+-----+----------------------------------------------------------------+
| > R | > Reserved                                                     |
+-----+----------------------------------------------------------------+
| > 2 | > Amex contactless Transaction                                 |
+-----+----------------------------------------------------------------+
| > 3 | > Digital Wallet -- Conatctless Initiated                      |
+-----+----------------------------------------------------------------+
| > 4 | > Digital Wallet -- Application Initiated                      |
+-----+----------------------------------------------------------------+
| > 5 | > Issuer Originated Payments                                   |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| > 6 |                                                                |
| >   |                                                                |
|  (C |                                                                |
| ard |                                                                |
| >   |                                                                |
| Ret |                                                                |
| ent |                                                                |
| ion |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > Device does not have card retention capability               |
+-----+----------------------------------------------------------------+
| > 1 | > Device has card retention capability                         |
+-----+----------------------------------------------------------------+
| > 9 | > Unknown data not available                                   |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| > 7 |                                                                |
| >   |                                                                |
| (Tr |                                                                |
| ans |                                                                |
| act |                                                                |
| ion |                                                                |
| >   |                                                                |
| Sta |                                                                |
| tus |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| > 0 | > Original presentment                                         |
+=====+================================================================+
| > 1 | > First representment                                          |
+-----+----------------------------------------------------------------+
| > 2 | > Second representment                                         |
+-----+----------------------------------------------------------------+
| > 3 | > Third representment                                          |
+-----+----------------------------------------------------------------+
| > 4 | > Previously authorized request                                |
+-----+----------------------------------------------------------------+
| > 5 | > Resubmission                                                 |
+-----+----------------------------------------------------------------+
| > 6 | > Merchant-approved Purchase                                   |
+-----+----------------------------------------------------------------+
| > 7 | > Time Based Payment Authorization Request or CDC inquiry      |
|     | > request                                                      |
+-----+----------------------------------------------------------------+
| > 8 | > Pre-authorization request/Card Validation/Account Status     |
|     | > Check                                                        |
+-----+----------------------------------------------------------------+
| > 9 | > Debit MasterCard Stand-In                                    |
+-----+----------------------------------------------------------------+
| > A | > Purchase with Cash back                                      |
+-----+----------------------------------------------------------------+
| > B | > Single transaction of a mail/phone order                     |
+-----+----------------------------------------------------------------+
| > C | > Recurring transaction                                        |
+-----+----------------------------------------------------------------+
| > D | > Installment payment                                          |
+-----+----------------------------------------------------------------+
| > E | > Unknown classification                                       |
+-----+----------------------------------------------------------------+
| > F | > Secure electronic commerce transaction                       |
+-----+----------------------------------------------------------------+
| > G | > Non-authenticated security transaction at a 3-D              |
|     | > Secure-capable merchant, and merchant attempted to           |
|     | > authenticate the cardholder using 3-D Secure                 |
+-----+----------------------------------------------------------------+
| > H | > Non-authenticated Security Transaction                       |
+-----+----------------------------------------------------------------+
| > I | > Non-secure transaction                                       |
+-----+----------------------------------------------------------------+
| > J | > Not Applicable                                               |
+-----+----------------------------------------------------------------+
| > K | > Account Status Inquiry Service                               |
+-----+----------------------------------------------------------------+
| > L | > Non-SET trans from SET-enabled merchant                      |
+-----+----------------------------------------------------------------+
| > M | > Secure Code Phone Order                                      |
+-----+----------------------------------------------------------------+
| > N | > ATC Update                                                   |
+-----+----------------------------------------------------------------+
| > R | > Reserved                                                     |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| > 8 |                                                                |
| >   |                                                                |
| (Tr |                                                                |
| ans |                                                                |
| act |                                                                |
| ion |                                                                |
| >   |                                                                |
|  Se |                                                                |
| cur |                                                                |
| ity |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > No security concern                                          |
+-----+----------------------------------------------------------------+
| > 1 | > Suspected fraud                                              |
+-----+----------------------------------------------------------------+
| > 2 | > Identification verified                                      |
+-----+----------------------------------------------------------------+
| > 3 | > Electronic commerce transaction with digital signature       |
+-----+----------------------------------------------------------------+
| > 4 | > Non-secure/Security unknown electronic commerce transaction  |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| > 5 | > Secure electronic transaction with cardholder certificate    |
+=====+================================================================+
| > 7 | > Channel-encrypted electronic commerce transaction            |
+-----+----------------------------------------------------------------+
| > 8 | > CVV validated and valid                                      |
+-----+----------------------------------------------------------------+
| > 9 | > CVV validated and invalid                                    |
+-----+----------------------------------------------------------------+
| > A | > Cardholder verified by Biometrics                            |
+-----+----------------------------------------------------------------+
| > B | > Unknown                                                      |
+-----+----------------------------------------------------------------+
| > C | > Chip Transaction Indicator present                           |
+-----+----------------------------------------------------------------+
| > D | > Acquirer indicates that Card Authentication may not be       |
|     | > reliable.                                                    |
+-----+----------------------------------------------------------------+
| > E | > V.I.P. indicates acquirer inactive for Card Authentication.  |
+-----+----------------------------------------------------------------+
| > F | > V.I.P. indicates issuer inactive for Card Authentication.    |
+-----+----------------------------------------------------------------+
| > R | > Reserved                                                     |
+-----+----------------------------------------------------------------+

+----+---------------------------------------------------------------+---+
| >  |                                                               |   |
| ** |                                                               |   |
| Da |                                                               |   |
| ta |                                                               |   |
| >  |                                                               |   |
|  E |                                                               |   |
| le |                                                               |   |
| me |                                                               |   |
| nt |                                                               |   |
| >  |                                                               |   |
|  0 |                                                               |   |
| 61 |                                                               |   |
| >  |                                                               |   |
| -- |                                                               |   |
| >  |                                                               |   |
| Po |                                                               |   |
| si |                                                               |   |
| ti |                                                               |   |
| on |                                                               |   |
| >  |                                                               |   |
| 9- |                                                               |   |
| 10 |                                                               |   |
| >  |                                                               |   |
|  ( |                                                               |   |
| Te |                                                               |   |
| rm |                                                               |   |
| in |                                                               |   |
| al |                                                               |   |
| >  |                                                               |   |
| Ty |                                                               |   |
| pe |                                                               |   |
| >  |                                                               |   |
| In |                                                               |   |
| di |                                                               |   |
| ca |                                                               |   |
| to |                                                               |   |
| r) |                                                               |   |
| ** |                                                               |   |
+====+===============================================================+===+
| >  | > **Definition**                                              |   |
| ** |                                                               |   |
| Co |                                                               |   |
| de |                                                               |   |
| ** |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Administrative terminal                                     |   |
| 00 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > POS terminal                                                |   |
| 01 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > ATM                                                         |   |
| 02 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Home terminal                                               |   |
| 03 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > ECR                                                         |   |
| 04 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Dial terminal/Call Center Operator                          |   |
| 05 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Fuel machine/ Travelers Check Machine                       |   |
| 06 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Fuel Machine                                                |   |
| 07 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > POS script machine                                          |   |
| 08 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Coupon machine                                              |   |
| 09 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Ticket machine                                              |   |
| 10 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Franchise teller/Point of Banking terminal                  |   |
| 11 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Personal banking                                            |   |
| 12 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Public utility                                              |   |
| 13 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Vending                                                     |   |
| 14 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Self-service                                                |   |
| 15 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Authorization                                               |   |
| 16 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Payment                                                     |   |
| 17 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > VRU                                                         |   |
| 18 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Smart phone                                                 |   |
| 19 |                                                               |   |
+----+---------------------------------------------------------------+---+

+----+---------------------------------------------------------------+---+
| >  | > Interactive television                                      |   |
| 20 |                                                               |   |
+====+===============================================================+===+
| >  | > Personal Digital Assistant (PDA)/Mobile Device              |   |
| 21 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Screen phone                                                |   |
| 22 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Electronic commerce                                         |   |
| 23 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Transponder (IBM-only) / MICR terminals at POS              |   |
| 24 | > (Tandem-only)                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Off Premise                                                 |   |
| 26 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Not a CAT transaction                                       |   |
| 27 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Authorized Level 1 CAT: automated dispensing machine with   |   |
| 28 | > PIN or ATM                                                  |   |
+----+---------------------------------------------------------------+---+
| >  | > Authorized Level 3 CAT: limited amount terminal             |   |
| 29 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Authorized Level 4 CAT: In-flight Commerce                  |   |
| 30 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Unspecified                                                 |   |
| 31 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Reserved                                                    |   |
| 32 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Unattended customer terminal                                |   |
| 33 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Travelers Check Machine                                     |   |
| 34 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > MICR terminal at teller                                     |   |
| 35 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Internet Terminal                                           |   |
| 36 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > POS terminal allows partial pre-authorizations              |   |
| 37 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Multimedia Terminal                                         |   |
| 38 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Manual Transactions at Bank Counter                         |   |
| 39 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Personal Computer                                           |   |
| 40 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Mobile Phone                                                |   |
| 41 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > I type fixed phone (Telephone without PIN pad)              |   |
| 42 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > II type fixed phone                                         |   |
| 43 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Wireless POS                                                |   |
| 44 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > CDRS                                                        |   |
| 45 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Merchant's Terminal                                         |   |
| 46 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Setup Box                                                   |   |
| 47 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Batch File Processing System                                |   |
| 48 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Authorized Level 2 CAT                                      |   |
| 49 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Unknown                                                     |   |
| 99 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  |                                                               |   |
| ** |                                                               |   |
| Da |                                                               |   |
| ta |                                                               |   |
| >  |                                                               |   |
|  E |                                                               |   |
| le |                                                               |   |
| me |                                                               |   |
| nt |                                                               |   |
| >  |                                                               |   |
|  0 |                                                               |   |
| 61 |                                                               |   |
| >  |                                                               |   |
| -- |                                                               |   |
| >  |                                                               |   |
| Po |                                                               |   |
| si |                                                               |   |
| ti |                                                               |   |
| on |                                                               |   |
| >  |                                                               |   |
| 11 |                                                               |   |
| >  |                                                               |   |
|  ( |                                                               |   |
| Te |                                                               |   |
| rm |                                                               |   |
| in |                                                               |   |
| al |                                                               |   |
| >  |                                                               |   |
|  I |                                                               |   |
| np |                                                               |   |
| ut |                                                               |   |
| >  |                                                               |   |
| Ca |                                                               |   |
| pa |                                                               |   |
| bi |                                                               |   |
| li |                                                               |   |
| ty |                                                               |   |
| >  |                                                               |   |
| In |                                                               |   |
| di |                                                               |   |
| ca |                                                               |   |
| to |                                                               |   |
| r) |                                                               |   |
| ** |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > **Definition**                                              |   |
| ** |                                                               |   |
| Co |                                                               |   |
| de |                                                               |   |
| ** |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Unknown                                                     |   |
| 00 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Manual, no terminal                                         |   |
| 01 |                                                               |   |
+----+---------------------------------------------------------------+---+
| >  | > Magnetic stripe                                             |   |
| 02 |                                                               |   |
+----+---------------------------------------------------------------+---+

+----+-----------------------------------------------------------------+
| >  | > Bar code                                                      |
| 03 |                                                                 |
+====+=================================================================+
| >  | > OCR                                                           |
| 04 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > ICC                                                           |
| 05 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > File                                                          |
| 06 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Contact-less read capability via Mag stripe rules             |
| 07 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Contact-less read capability via Chip rules                   |
| 08 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Mag stripe reader and key entry/Terminal does not read card   |
| 09 | > data                                                          |
+----+-----------------------------------------------------------------+
| >  | > Mag stripe reader and key entry and EMV-Compatible ICC reader |
| 10 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Contact-less M/Chip (Proximity Chip) Terminal supports        |
| 11 | > PayPass M/Chip and PayPass mag-stripe transactions. The       |
|    | > terminal also may support contact transactions; however, this |
|    | >                                                               |
|    | > value must only be used for Contact-Less Transactions.        |
+----+-----------------------------------------------------------------+
| >  | > EMV specification (compatible chip reader) and magnetic       |
| 12 | > stripe reader. This terminal can                              |
|    | >                                                               |
|    | > also support contact-less transactions; however, these values |
|    | > must only be used for contact transactions.                   |
+----+-----------------------------------------------------------------+
| >  | > Key entry only                                                |
| 13 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > EMV specification (compatible chip reader) only. This         |
| 14 | > terminal can also support contact- less transactions;         |
|    | > however, this value must only be used for contact             |
|    | > transactions.                                                 |
+----+-----------------------------------------------------------------+
| >  | > MICR read (POS Check Service), U.S. Only                      |
| 15 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > MICR read and image-capable (POS Check Service), U.S. Only    |
| 16 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Terminal does not read card data                              |
| 17 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Radio Frequency Identification (RFID)                         |
| 18 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Secure Electronic Transaction (SET) with certificate          |
| 19 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > SET without certificate                                       |
| 20 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Channel-encrypted Electronic Commerce Transaction (SSL)       |
| 21 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Non-secure Electronic Commerce Transaction                    |
| 22 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Mobile Device                                                 |
| 23 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > F (No Value)                                                  |
| 24 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Secure Cardless Entry                                         |
| 25 |                                                                 |
+----+-----------------------------------------------------------------+

+----+-----------------------------------------------------------------+
| >  |                                                                 |
| ** |                                                                 |
| Da |                                                                 |
| ta |                                                                 |
| >  |                                                                 |
|  E |                                                                 |
| le |                                                                 |
| me |                                                                 |
| nt |                                                                 |
| >  |                                                                 |
|  0 |                                                                 |
| 61 |                                                                 |
| >  |                                                                 |
| -- |                                                                 |
| >  |                                                                 |
| Po |                                                                 |
| si |                                                                 |
| ti |                                                                 |
| on |                                                                 |
| >  |                                                                 |
| 13 |                                                                 |
| >  |                                                                 |
|  ( |                                                                 |
| Ch |                                                                 |
| ip |                                                                 |
| >  |                                                                 |
|  C |                                                                 |
| on |                                                                 |
| di |                                                                 |
| ti |                                                                 |
| on |                                                                 |
| >  |                                                                 |
| Co |                                                                 |
| de |                                                                 |
| s) |                                                                 |
| ** |                                                                 |
+====+=================================================================+
| >  | > **Definition**                                                |
| ** |                                                                 |
| Co |                                                                 |
| de |                                                                 |
| ** |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > Not applicable to fallback transactions.                      |
|  0 |                                                                 |
+----+-----------------------------------------------------------------+
| >  | > This value applies to fallback transactions. Transaction was  |
|  1 | > initiated from a magnetic stripe with a service code          |
|    | > beginning with 2 or 6 and the last read at VSDC terminal was  |
|    | > a successful chip read or was not a chip transaction.         |
+----+-----------------------------------------------------------------+
| >  | > This value applies to fallback transactions. Transaction was  |
|  2 | > initiated at a chip-capable                                   |
+----+-----------------------------------------------------------------+

> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

+----+-----------------------------------------------------------------+
|    | > terminal from a magnetic stripe that contains service code 2  |
|    | > or 6, and the previous                                        |
|    | >                                                               |
|    | > transaction initiated by that terminal was an unsuccessful    |
|    | > chip read.                                                    |
+====+=================================================================+
+----+-----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| >   |                                                                |
|  14 |                                                                |
| >   |                                                                |
|  (S |                                                                |
| pec |                                                                |
| ial |                                                                |
| >   |                                                                |
| Con |                                                                |
| dit |                                                                |
| ion |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > Default Value                                                |
+-----+----------------------------------------------------------------+
| > 9 | > Payment on existing debt                                     |
+-----+----------------------------------------------------------------+
| > 1 | > Electronic Commerce with security                            |
+-----+----------------------------------------------------------------+
| > 2 | > Electronic Commerce without security                         |
+-----+----------------------------------------------------------------+
| > 4 | > In-Flight Transaction                                        |
+-----+----------------------------------------------------------------+
| > 7 | > Purchase of Cryptocurrency                                   |
+-----+----------------------------------------------------------------+
| > 8 | > Quasi Cash                                                   |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
| **D |                                                                |
| ata |                                                                |
| > E |                                                                |
| lem |                                                                |
| ent |                                                                |
| >   |                                                                |
| 061 |                                                                |
| >   |                                                                |
|  -- |                                                                |
| >   |                                                                |
|  Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| >   |                                                                |
|  15 |                                                                |
| >   |                                                                |
|  (C |                                                                |
| hip |                                                                |
| >   |                                                                |
|  Tr |                                                                |
| ans |                                                                |
| act |                                                                |
| ion |                                                                |
| >   |                                                                |
| Ind |                                                                |
| ica |                                                                |
| tor |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > Not applicable; subsequent sub-fields are present When an    |
|     | > Early Data option acquirer, or a Full Data option acquirer,  |
|     | > submits Early Data, field 60.6 must contain zero (0) or be   |
|     | > excluded from the message.                                   |
+-----+----------------------------------------------------------------+
| > 1 | > This value is sent by acquirers using either the standard    |
|     | > third bitmap or field 55 to submit chip data.                |
+-----+----------------------------------------------------------------+
| > 2 | > This value is sent by acquirers using the expanded third     |
|     | > bitmap for their chip data. The value 2 applies only to      |
|     | > acquirers; V.I.P. changes it to 1 before the request is      |
|     | > forwarded to the issuer.                                     |
+-----+----------------------------------------------------------------+
| > 3 | > V.I.P. (not the acquirer) inserts this code and downgrades   |
|     | > the transaction by dropping chip data section.               |
+-----+----------------------------------------------------------------+
| > 4 | > V.I.P inserts this code based on the presence of a Visa      |
|     | > issued token.                                                |
+-----+----------------------------------------------------------------+

+------+---------------------------------------------------------------+
| > ** |                                                               |
| Data |                                                               |
| >    |                                                               |
|  Ele |                                                               |
| ment |                                                               |
| >    |                                                               |
|  061 |                                                               |
| > -- |                                                               |
| >    |                                                               |
| Posi |                                                               |
| tion |                                                               |
| > 16 |                                                               |
| >    |                                                               |
|  (Ca |                                                               |
| rdho |                                                               |
| lder |                                                               |
| > ID |                                                               |
| > Me |                                                               |
| thod |                                                               |
| >    |                                                               |
| Indi |                                                               |
| cato |                                                               |
| r)** |                                                               |
+======+===============================================================+
| >    | > **Definition**                                              |
| **Co |                                                               |
| de** |                                                               |
+------+---------------------------------------------------------------+
| > 0  | > Not specified                                               |
+------+---------------------------------------------------------------+
| > 1  | > Signature                                                   |
+------+---------------------------------------------------------------+
| > 2  | > PIN                                                         |
+------+---------------------------------------------------------------+
| > 3  | > Unattended terminal, no PIN pad                             |
+------+---------------------------------------------------------------+
| > 4  | > Mail/Telephone/Electronic Commerce                          |
+------+---------------------------------------------------------------+

+------+---------------------------------------------------------------+
| > 5  | > TransQPS Action (Quick payment Service), I will pay without |
|      | > signature                                                   |
+======+===============================================================+
| > 10 | > Biometric                                                   |
+------+---------------------------------------------------------------+
| > 11 | > Offline PIN                                                 |
+------+---------------------------------------------------------------+
| > 12 | > Pattern Recognition                                         |
+------+---------------------------------------------------------------+
| > 13 | > Device Code / Other                                         |
+------+---------------------------------------------------------------+

+------+---------------------------------------------------------------+
| > ** |                                                               |
| Data |                                                               |
| >    |                                                               |
|  Ele |                                                               |
| ment |                                                               |
| >    |                                                               |
|  061 |                                                               |
| > -- |                                                               |
| >    |                                                               |
| Posi |                                                               |
| tion |                                                               |
| > 17 |                                                               |
| > (  |                                                               |
| Chip |                                                               |
| >    |                                                               |
| Card |                                                               |
| > Au |                                                               |
| then |                                                               |
| tica |                                                               |
| tion |                                                               |
| >    |                                                               |
|  Rel |                                                               |
| iabi |                                                               |
| lity |                                                               |
| >    |                                                               |
| Indi |                                                               |
| cato |                                                               |
| r)** |                                                               |
+======+===============================================================+
| >    | > **Definition**                                              |
| **Co |                                                               |
| de** |                                                               |
+------+---------------------------------------------------------------+
| > 0  | > Not specified                                               |
+------+---------------------------------------------------------------+
| > 1  | > Acquirer indicates that Card Authentication may not be      |
|      | > reliable                                                    |
+------+---------------------------------------------------------------+
| > 2  | > Switch indicates acquirer inactive for Card Authentication. |
+------+---------------------------------------------------------------+
| > 3  | > Switch indicates issuer inactive for Card Authentication.   |
+------+---------------------------------------------------------------+
| > 4  | > Switch Center indicates that the transaction has used Token |
|      | > Service provided by the network itself.                     |
+------+---------------------------------------------------------------+

+------+---------------------------------------------------------------+
| > ** |                                                               |
| Data |                                                               |
| >    |                                                               |
|  Ele |                                                               |
| ment |                                                               |
| >    |                                                               |
|  061 |                                                               |
| > -- |                                                               |
| >    |                                                               |
| Posi |                                                               |
| tion |                                                               |
| > 18 |                                                               |
| > (M |                                                               |
| ail/ |                                                               |
| Phon |                                                               |
| e/El |                                                               |
| ectr |                                                               |
| onic |                                                               |
| >    |                                                               |
| Comm |                                                               |
| erce |                                                               |
| >    |                                                               |
|  and |                                                               |
| >    |                                                               |
|  Pay |                                                               |
| ment |                                                               |
| >    |                                                               |
| Indi |                                                               |
| cato |                                                               |
| r)** |                                                               |
+======+===============================================================+
| >    | > **Definition**                                              |
| **Co |                                                               |
| de** |                                                               |
+------+---------------------------------------------------------------+
| > 0  | > Not Applicable                                              |
+------+---------------------------------------------------------------+
| > 1  | > Unknown/Unspecified                                         |
+------+---------------------------------------------------------------+
| > 2  | > Not an e-commerce transaction                               |
+------+---------------------------------------------------------------+
| > 3  | > Single transaction of a mail/phone order                    |
+------+---------------------------------------------------------------+
| > 4  | > Recurring transaction                                       |
+------+---------------------------------------------------------------+
| > 5  | > Installment payment                                         |
+------+---------------------------------------------------------------+
| > 6  | > Secure electronic commerce transaction                      |
+------+---------------------------------------------------------------+
| > 7  | > Non-authenticated security transaction at a 3-D             |
|      | > Secure-capable merchant, and merchant attempted to          |
|      | > authenticate the cardholder using 3-D Secure                |
+------+---------------------------------------------------------------+
| > 8  | > Non-authenticated Security Transaction                      |
+------+---------------------------------------------------------------+
| > 9  | > Non-secure transaction                                      |
+------+---------------------------------------------------------------+
| > A  | > In-App Authentication                                       |
+------+---------------------------------------------------------------+
| > B  | > Electronic commerce transaction with digital signature      |
+------+---------------------------------------------------------------+
| > C  | > Secure electronic transaction with cardholder certificate   |
+------+---------------------------------------------------------------+
| > D  | > Secure electronic transaction without cardholder            |
|      | > certificate                                                 |
+------+---------------------------------------------------------------+

+------+---------------------------------------------------------------+
| > ** |                                                               |
| Data |                                                               |
| >    |                                                               |
|  Ele |                                                               |
| ment |                                                               |
| >    |                                                               |
|  061 |                                                               |
| > -- |                                                               |
| >    |                                                               |
| Posi |                                                               |
| tion |                                                               |
| > 19 |                                                               |
| >    |                                                               |
| (Int |                                                               |
| erac |                                                               |
| tive |                                                               |
| >    |                                                               |
| Mode |                                                               |
| > I  |                                                               |
| dent |                                                               |
| ifie |                                                               |
| r)** |                                                               |
+======+===============================================================+
| >    | > **Definition**                                              |
| **Co |                                                               |
| de** |                                                               |
+------+---------------------------------------------------------------+
| > 0  | > Default                                                     |
+------+---------------------------------------------------------------+
| > 1  | > Internet                                                    |
+------+---------------------------------------------------------------+
| > 2  | > Text Message (SMS)                                          |
+------+---------------------------------------------------------------+
| > 3  | > Voice (IVR)                                                 |
+------+---------------------------------------------------------------+
| >    | > Reserved                                                    |
|  4-9 |                                                               |
+------+---------------------------------------------------------------+
| > K  | > Failed CUPSecure safe authentication, and does not adopt    |
|      | > the security technology of encryption.                      |
+------+---------------------------------------------------------------+
| > E  | > Channel-encrypted electronic commerce transaction           |
+------+---------------------------------------------------------------+
| > F  | > UnionPay safe entry mode authentication conducted, and      |
|      | > cardholder security information is input successfully       |
+------+---------------------------------------------------------------+
| > G  | > Certification of Issuer SAA direct authentication           |
|      | > authorization conducted, and the SAA authentication         |
|      | > authorization is successful                                 |
+------+---------------------------------------------------------------+
| > H  | > Authentication of Issuer SA direct status verification      |
|      | > conducted, and the cardholder status verification is        |
|      | > successful                                                  |
+------+---------------------------------------------------------------+
| > I  | > Tried to conduct the issuer direct status verification      |
+------+---------------------------------------------------------------+
| > J  | > Failed CUPSecure safe authentication, but adopt the         |
|      | > security technology of channel                              |
+------+---------------------------------------------------------------+
| > L  | > Issuer Authentication Mode in card-no-present self-service  |
|      | > transactions                                                |
+------+---------------------------------------------------------------+
| > M  | > Issuer Non-Authentication Mode in card-no-present           |
|      | > self-service transaction                                    |
+------+---------------------------------------------------------------+
| > N  | > Static UCAF Value (Switch assigned static AAV)              |
+------+---------------------------------------------------------------+
| > O  | > Issuer Risk based Decision                                  |
+------+---------------------------------------------------------------+
| > P  | > Aquirer Risk based Decision                                 |
+------+---------------------------------------------------------------+
| >    | > Reserved                                                    |
|  Q-Z |                                                               |
+------+---------------------------------------------------------------+

> []{#_bookmark88 .anchor}**Data Element 108 -- Receiver/Sender Data
> Table DE 108 -- TLV Fields Details when DE-63.7 = 'VISA':**

+-----+-----+-------------+-----+------------------------------------+
| >   |     |             |     |                                    |
|  ** |     |             |     |                                    |
| Sub |     |             |     |                                    |
| >   |     |             |     |                                    |
|  El |     |             |     |                                    |
| eme |     |             |     |                                    |
| nts |     |             |     |                                    |
| >   |     |             |     |                                    |
|  of |     |             |     |                                    |
| >   |     |             |     |                                    |
| DE- |     |             |     |                                    |
| 108 |     |             |     |                                    |
| > w |     |             |     |                                    |
| hen |     |             |     |                                    |
| > D |     |             |     |                                    |
| E-6 |     |             |     |                                    |
| 3.7 |     |             |     |                                    |
| > = |     |             |     |                                    |
| >   |     |             |     |                                    |
|  'V |     |             |     |                                    |
| ISA |     |             |     |                                    |
| '** |     |             |     |                                    |
+=====+=====+=============+=====+====================================+
| > * | > * | > **Value** | > * | > **Content of Sub-Element**       |
| *Ta | *Le |             | *Fo |                                    |
| g** | ngt |             | rma |                                    |
|     | h** |             | t** |                                    |
+-----+-----+-------------+-----+------------------------------------+
| >   | >   | > Sender    | >   | > Contains a transaction reference |
|  01 |  16 | > Reference |  AN | > number that is provided by the   |
|     |     | > Number    |     | > originator or acquirer and can   |
|     |     |             |     | > be used to uniquely identify the |
|     |     |             |     | > entity funding the transaction.  |
+-----+-----+-------------+-----+------------------------------------+
| >   | >   | > Sender    | >   | > Contains the account number of   |
|  02 |  34 | > Account   |  AN | > the entity funding the           |
|     |     | > Number    |     | > transaction.                     |
+-----+-----+-------------+-----+------------------------------------+
| >   | >   | > Sender    | >   | > Contains the name of the entity  |
|  03 |  30 | > Name      |  AN | > funding the transaction.         |
+-----+-----+-------------+-----+------------------------------------+
| >   | >   | > Sender    | >   | > Contains the address of the      |
|  04 |  35 | > Address   |  AN | > entity funding the transaction.  |
+-----+-----+-------------+-----+------------------------------------+
| >   | >   | > Sender    | >   | > Contains the city of the entity  |
|  05 |  25 | > City      |  AN | > funding the transaction.         |
+-----+-----+-------------+-----+------------------------------------+
| >   | > 2 | > Sender    | >   | > Contains the geographical state  |
|  06 |     | > State     |  AN | > or province of the entity        |
|     |     |             |     | > funding the transaction.         |
|     |     |             |     | >                                  |
|     |     |             |     | > Sender State is required when    |
|     |     |             |     | > Sender Country in Tag 07         |
|     |     |             |     | > contains **124** (Canada) or     |
|     |     |             |     | > **840** (U.S.). This field is    |
|     |     |             |     | > optional otherwise.              |
+-----+-----+-------------+-----+------------------------------------+
| >   | > 3 | > Sender    | >   | > Contains the country of the      |
|  07 |     | > Country   |  AN | > entity funding the transaction.  |
|     |     |             |     | >                                  |
|     |     |             |     | > **Format**: 3-digit ISO country  |
|     |     |             |     | > code.                            |
+-----+-----+-------------+-----+------------------------------------+
| >   | > 2 | > Source of | >   | > Indicates the method used by the |
|  08 |     | > Funds     |  AN | > sender to fund an OCT.           |
|     |     |             |     | >                                  |
|     |     |             |     | > The tag is required in all       |
|     |     |             |     | > domestic and cross- bordermoney  |
|     |     |             |     | > transfer OCTs destined to U.S.   |
|     |     |             |     | > recipient issuers.               |
|     |     |             |     | >                                  |
|     |     |             |     | > Values are:                      |
|     |     |             |     | >                                  |
|     |     |             |     | > **01** = Visa credit **02** =    |
|     |     |             |     | > Visa debit **03** = Visa prepaid |
|     |     |             |     | > **04** = Cash                    |
|     |     |             |     | >                                  |
|     |     |             |     | > **05** = Debit/deposit access    |
|     |     |             |     | > accounts other than those linked |
|     |     |             |     | > to a Visa card (includes         |
|     |     |             |     | > checking / savings accounts and  |
|     |     |             |     | > proprietary debit/ Automated     |
|     |     |             |     | > Teller Machine (ATM) cards)      |
|     |     |             |     | >                                  |
|     |     |             |     | > **06** = Credit accounts other   |
|     |     |             |     | > than those linked to a Visa card |
|     |     |             |     | > (includes credit cards and       |
|     |     |             |     | > proprietary credit lines)        |
+-----+-----+-------------+-----+------------------------------------+
| >   | >   | > Claim     | >   | > **Visa Mobile Prepaid (VMP)      |
|  09 |  20 | > Code      |  AN | > Transaction**: Tag contains the  |
|     |     |             |     | > third-party request reference    |
|     |     |             |     | > number. VMP transactions are     |
|     |     |             |     | > supported for certain countries  |
|     |     |             |     | > in the AP, CEMEA, and LAC        |
|     |     |             |     | > regions only. For a              |
+-----+-----+-------------+-----+------------------------------------+

+-----+-----+-------------+-----+------------------------------------+
|     |     |             |     | > given transaction, the issuer,   |
|     |     |             |     | > acquirer, and merchant must be   |
|     |     |             |     | > within the same country.         |
+=====+=====+=============+=====+====================================+
| >   | >   | > Recipient | >   | > Contains the name of the entity  |
|  0A |  30 | > Name      |  AN | > receiving the funds.             |
+-----+-----+-------------+-----+------------------------------------+
| >   | >   | > C         | >   |                                    |
|  0B |  20 | onfirmation |  AN |                                    |
|     |     | > Number    |     |                                    |
+-----+-----+-------------+-----+------------------------------------+
| >   | >   | > Recipient | >   | > Contains the city of the entity  |
|  0C |  25 | > City      |  AN | > receiving the funds.             |
+-----+-----+-------------+-----+------------------------------------+
| >   | > 3 | > Recipient | > N |                                    |
|  0D |     | > Country   |     |                                    |
+-----+-----+-------------+-----+------------------------------------+
| >   | > 3 | >           | >   | > Contains the country of the      |
|  0E |     | Proprietary |  AN | > entity receiving the funds.      |
|     |     | > Account   |     | >                                  |
|     |     | > Type      |     | > **Format**: 3-digit ISO country  |
|     |     |             |     | > code.                            |
+-----+-----+-------------+-----+------------------------------------+
| >   | >   | >           | > N |                                    |
|  0F |  12 | Proprietary |     |                                    |
|     |     | > Amount    |     |                                    |
+-----+-----+-------------+-----+------------------------------------+
| >   | > 5 | > Sender    | >   | > Contains the postal code of the  |
|  10 | -10 | > postal    |  AN | > entity funding the transaction.  |
|     |     | > Code      |     |                                    |
+-----+-----+-------------+-----+------------------------------------+

> **DE 108 - Sub Field 01 Details when DE-63.7 = 'MASTERCARD'**:

+---------+--------------------------------+-----------+--------------+
| > **Sub |                                |           |              |
| >       |                                |           |              |
| Element |                                |           |              |
| > 01 of |                                |           |              |
| >       |                                |           |              |
|  DE-108 |                                |           |              |
| >       |                                |           |              |
|  \[Rece |                                |           |              |
| iver/Re |                                |           |              |
| cipient |                                |           |              |
| >       |                                |           |              |
|  Data\] |                                |           |              |
| > when  |                                |           |              |
| >       |                                |           |              |
| DE-63.7 |                                |           |              |
| > =     |                                |           |              |
| >       |                                |           |              |
| 'MASTER |                                |           |              |
| CARD'** |                                |           |              |
+=========+================================+===========+==============+
| > **Sub | > **Sub Field Name**           | > **Sub   | > **Data     |
| > Field |                                | > Field   | > Repr       |
| > No.** |                                | >         | esentation** |
|         |                                |  Length** |              |
+---------+--------------------------------+-----------+--------------+
| > 01    | > First Name                   | > 2       | > ans...35;  |
|         |                                |           | > LLVAR      |
+---------+--------------------------------+-----------+--------------+
| > 02    | > Middle Name                  | > 2       | > ans-1      |
+---------+--------------------------------+-----------+--------------+
| > 03    | > Last Name                    | > 2       | > ans...35;  |
|         |                                |           | > LLVAR      |
+---------+--------------------------------+-----------+--------------+
| > 04    | > Street Address               | > 2       | > ans...50;  |
|         |                                |           | > LLVAR      |
+---------+--------------------------------+-----------+--------------+
| > 05    | > City                         | > 2       | > ans...25;  |
|         |                                |           | > LLVAR      |
+---------+--------------------------------+-----------+--------------+
| > 06    | > State/Province Code          | > 2       | > ans...3;   |
|         |                                |           | > LLVAR      |
+---------+--------------------------------+-----------+--------------+
| > 07    | > Country                      | > 2       | > ans-3      |
+---------+--------------------------------+-----------+--------------+
| > 08    | > Postal Code                  | > 2       | > ans...10;  |
|         |                                |           | > LLVAR      |
+---------+--------------------------------+-----------+--------------+
| > 09    | > Phone Number                 | > 2       | > ans...20;  |
|         |                                |           | > LLVAR      |
+---------+--------------------------------+-----------+--------------+
| > 10    | > Date of Birth                | > 2       | > n-8        |
+---------+--------------------------------+-----------+--------------+
| > 11    | > Account Number               | > 2       | > n...20;    |
|         |                                |           | > LLVAR      |
+---------+--------------------------------+-----------+--------------+
| > 12    | > Identification Type          | > 2       | > n-2        |
+---------+--------------------------------+-----------+--------------+
| > 13    | > Identification Number        | > 2       | > ans...25;  |
|         |                                |           | > LLVAR      |
+---------+--------------------------------+-----------+--------------+
| > 14    | > Identification Country Code  | > 2       | > ans-3      |
+---------+--------------------------------+-----------+--------------+
| > 15    | > Identification Expiration    | > 2       | > n-8        |
|         | > Date                         |           |              |
+---------+--------------------------------+-----------+--------------+
| > 16    | > Nationality                  | > 2       | > ans-3      |
+---------+--------------------------------+-----------+--------------+
| > 17    | > Country of Birth             | > 2       | > ans-3      |
+---------+--------------------------------+-----------+--------------+
| > 18    | > Account Type                 | > 2       | > n-2        |
+---------+--------------------------------+-----------+--------------+

> **DE 108 - Sub Field 02 Details when DE-63.7 = 'MASTERCARD':**

+----------+----------------------------+---------------+--------------+
| > **Sub  |                            |               |              |
| >        |                            |               |              |
|  Element |                            |               |              |
| > 02 of  |                            |               |              |
| > DE-108 |                            |               |              |
| >        |                            |               |              |
| \[Sender |                            |               |              |
| > Data\] |                            |               |              |
| > when   |                            |               |              |
| >        |                            |               |              |
|  DE-63.7 |                            |               |              |
| > =      |                            |               |              |
| > 'MASTE |                            |               |              |
| RCARD'** |                            |               |              |
+==========+============================+===============+==============+
| > **Sub  | > **Sub Field Name**       | > **Sub Field | > **Data     |
| > Field  |                            | > Length**    | > Repr       |
| > No.**  |                            |               | esentation** |
+----------+----------------------------+---------------+--------------+
| > 01     | > First Name               | > 2           | > ans...35;  |
|          |                            |               | > LLVAR      |
+----------+----------------------------+---------------+--------------+
| > 02     | > Middle Name              | > 2           | > ans-1      |
+----------+----------------------------+---------------+--------------+
| > 03     | > Last Name                | > 2           | > ans...35;  |
|          |                            |               | > LLVAR      |
+----------+----------------------------+---------------+--------------+
| > 04     | > Street Address           | > 2           | > ans...50;  |
|          |                            |               | > LLVAR      |
+----------+----------------------------+---------------+--------------+
| > 05     | > City                     | > 2           | > ans...25;  |
|          |                            |               | > LLVAR      |
+----------+----------------------------+---------------+--------------+
| > 06     | > State/Province Code      | > 2           | > ans...3;   |
|          |                            |               | > LLVAR      |
+----------+----------------------------+---------------+--------------+
| > 07     | > Country                  | > 2           | > ans-3      |
+----------+----------------------------+---------------+--------------+
| > 08     | > Postal Code              | > 2           | > ans...10;  |
|          |                            |               | > LLVAR      |
+----------+----------------------------+---------------+--------------+
| > 09     | > Phone Number             | > 2           | > ans...20;  |
|          |                            |               | > LLVAR      |
+----------+----------------------------+---------------+--------------+
| > 10     | > Date of Birth            | > 2           | > n-8        |
+----------+----------------------------+---------------+--------------+
| > 11     | > Account Number           | > 2           | > n...20;    |
|          |                            |               | > LLVAR      |
+----------+----------------------------+---------------+--------------+
| > 12     | > Identification Type      | > 2           | > n-2        |
+----------+----------------------------+---------------+--------------+
| > 13     | > Identification Number    | > 2           | > ans...25;  |
|          |                            |               | > LLVAR      |
+----------+----------------------------+---------------+--------------+
| > 14     | > Identification Country   | > 2           | > ans-3      |
|          | > Code                     |               |              |
+----------+----------------------------+---------------+--------------+
| > 15     | > Identification           | > 2           | > n-8        |
|          | > Expiration Date          |               |              |
+----------+----------------------------+---------------+--------------+
| > 16     | > Nationality              | > 2           | > ans-3      |
+----------+----------------------------+---------------+--------------+
| > 17     | > Country of Birth         | > 2           | > ans-3      |
+----------+----------------------------+---------------+--------------+
| > 18     | > Account Type             | > 2           | > n-2        |
+----------+----------------------------+---------------+--------------+

> **DE 108 - Sub Field 03 Details when DE-63.7 = 'MASTERCARD':**

+-----------+-------------------------+---------+---------------------+
| > **Sub   |                         |         |                     |
| > Element |                         |         |                     |
| > 03 of   |                         |         |                     |
| > DE-108  |                         |         |                     |
| > \[Tr    |                         |         |                     |
| ansaction |                         |         |                     |
| >         |                         |         |                     |
| Reference |                         |         |                     |
| > Data\]  |                         |         |                     |
| > when    |                         |         |                     |
| > DE-63.7 |                         |         |                     |
| > =       |                         |         |                     |
| > 'MAST   |                         |         |                     |
| ERCARD'** |                         |         |                     |
+===========+=========================+=========+=====================+
| > **Sub   | > **Sub Field Name**    | > **Sub | > **Data            |
| > Field   |                         | > Field | > Representation**  |
| > No.**   |                         | > L     |                     |
|           |                         | ength** |                     |
+-----------+-------------------------+---------+---------------------+
| > 01      | > Unique Transaction    | > 2     | ans...19; LLVAR     |
|           | > reference             |         |                     |
+-----------+-------------------------+---------+---------------------+
| > 02      | > Additional Message    | > 2     | ans...65; LLVAR     |
+-----------+-------------------------+---------+---------------------+
| > 03      | > Funding Source        | > 2     | > n...2             |
+-----------+-------------------------+---------+---------------------+
| > 04      | > Participation ID      | > 2     | ans...30; LLVAR     |
+-----------+-------------------------+---------+---------------------+
| > 05      | > Transaction Purpose   | > 2     | > n...2             |
|           | > (Possible Values are  |         |                     |
|           | > listed in below table |         |                     |
|           | > )                     |         |                     |
+-----------+-------------------------+---------+---------------------+

> **DE108.03.05: Possible Values for Transaction Purpose when DE-63.7 =
> 'MASTERCARD'**

+------+---------------------------------------------------------------+
| > ** |                                                               |
| Poss |                                                               |
| ible |                                                               |
| >    |                                                               |
|  val |                                                               |
| ue** |                                                               |
+======+===============================================================+
| > *  | > **Definition**                                              |
| *Val |                                                               |
| ue** |                                                               |
+------+---------------------------------------------------------------+
| > 00 | > Family Support                                              |
+------+---------------------------------------------------------------+
| > 01 | > Regular Labor Transfers (expatriates)                       |
+------+---------------------------------------------------------------+
| > 02 | > Travel & Tourism                                            |
+------+---------------------------------------------------------------+
| > 03 | > Education                                                   |
+------+---------------------------------------------------------------+
| > 04 | > Hospitalization & Medical Treatment                         |
+------+---------------------------------------------------------------+
| > 05 | > Emergency Need                                              |
+------+---------------------------------------------------------------+
| > 06 | > Savings                                                     |
+------+---------------------------------------------------------------+
| > 07 | > Gifts                                                       |
+------+---------------------------------------------------------------+
| > 08 | > Others                                                      |
+------+---------------------------------------------------------------+
| > 09 | > Salary                                                      |
+------+---------------------------------------------------------------+
| >    | > Reserved                                                    |
| 10 - |                                                               |
| > 15 |                                                               |
+------+---------------------------------------------------------------+

> **DE 108 - Sub Field 04 Details when DE-63.7 = 'MASTERCARD':**

+-----------+-------------------------+---------+---------------------+
| > **Sub   |                         |         |                     |
| > Element |                         |         |                     |
| > 04 of   |                         |         |                     |
| > DE-108  |                         |         |                     |
| > \       |                         |         |                     |
| [Language |                         |         |                     |
| > Desc    |                         |         |                     |
| ription\] |                         |         |                     |
| > when    |                         |         |                     |
| > DE-63.7 |                         |         |                     |
| > =       |                         |         |                     |
| > 'MAST   |                         |         |                     |
| ERCARD'** |                         |         |                     |
+===========+=========================+=========+=====================+
| > **Sub   | > **Sub Field Name**    | > **Sub | > **Data            |
| > Field   |                         | > Field | > Representation**  |
| > No.**   |                         | > L     |                     |
|           |                         | ength** |                     |
+-----------+-------------------------+---------+---------------------+
| > 01      | > Language              | > 2     | > ans...2           |
|           | > Identification        |         |                     |
+-----------+-------------------------+---------+---------------------+
| > 02      | > Language Data         | > 2     | > b...50; LLVAR     |
+-----------+-------------------------+---------+---------------------+

> **DE 108 - Sub Field 05 Details when DE-63.7 = 'MASTERCARD':**

+-----------+-------------------------+---------+---------------------+
| > **Sub   |                         |         |                     |
| > Element |                         |         |                     |
| > 05 of   |                         |         |                     |
| > DE-108  |                         |         |                     |
| >         |                         |         |                     |
| \[Digital |                         |         |                     |
| > Account |                         |         |                     |
| > Info    |                         |         |                     |
| rmation\] |                         |         |                     |
| > when    |                         |         |                     |
| > DE-63.7 |                         |         |                     |
| > =       |                         |         |                     |
| > 'MAST   |                         |         |                     |
| ERCARD'** |                         |         |                     |
+===========+=========================+=========+=====================+
| > **Sub   | > **Sub Field Name**    | > **Sub | > **Data            |
| > Field   |                         | > Field | > Representation**  |
| > No.**   |                         | > L     |                     |
|           |                         | ength** |                     |
+-----------+-------------------------+---------+---------------------+
| > 01      | > Digital Account       | > 2     | > n...19; LLVAR     |
|           | > reference Number      |         |                     |
+-----------+-------------------------+---------+---------------------+
| > 02      | > Mastercard Merchant   | > 2     | > ans...34; LLVAR   |
|           | > Presented QR          |         |                     |
|           | > Receiving Account     |         |                     |
|           | > Number                |         |                     |
+-----------+-------------------------+---------+---------------------+

##### Data Element 111 -- Additional Data Table {#data-element-111-additional-data-table .unnumbered}

+------+-----------------------------------+-----+------+------------+
| > ** |                                   |     |      |            |
| Elem |                                   |     |      |            |
| ents |                                   |     |      |            |
| > of |                                   |     |      |            |
| > DE |                                   |     |      |            |
| -111 |                                   |     |      |            |
| >    |                                   |     |      |            |
| when |                                   |     |      |            |
| >    |                                   |     |      |            |
|  DE- |                                   |     |      |            |
| 63.7 |                                   |     |      |            |
| > =  |                                   |     |      |            |
| >    |                                   |     |      |            |
| 'VIS |                                   |     |      |            |
| A'** |                                   |     |      |            |
+======+===================================+=====+======+============+
| > *  | > **Sub Field Name**              | >   | >    | > **Format |
| *Sub |                                   | **V | **Po | >          |
| > F  |                                   | isa | siti |  (ASCII)** |
| ield |                                   | >   | on** |            |
| > N  |                                   | Bit |      |            |
| o.** |                                   | >   |      |            |
|      |                                   |  No |      |            |
|      |                                   | .** |      |            |
+------+-----------------------------------+-----+------+------------+
| > 1  | > Authorization characteristics   | > 6 | > 1  | > 1 AN     |
| 11.1 | > indicator                       | 2.1 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 1  | > Transaction identifier          | > 6 | >    | > 15 N     |
| 11.2 |                                   | 2.2 | 2-16 |            |
+------+-----------------------------------+-----+------+------------+
| > 1  | > Validation code                 | > 6 | > 1  | > 4 AN     |
| 11.3 |                                   | 2.3 | 7-20 |            |
+------+-----------------------------------+-----+------+------------+
| > 1  | > Market-specific data indicator  | > 6 | > 21 | > 1 AN     |
| 11.4 | > 2                               | 2.4 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 1  | > Duration                        | > 6 | > 2  | > 2 N      |
| 11.5 |                                   | 2.5 | 2-23 |            |
+------+-----------------------------------+-----+------+------------+
| > 1  | > Purchase identifier             | > 6 | > 2  | > 26 AN    |
| 11.6 |                                   | 2.7 | 4-49 |            |
+------+-----------------------------------+-----+------+------------+
| > 1  | > Date; auto rental check-out,    | > 6 | > 5  | > 6 N      |
| 11.7 | > lodging check-in                | 2.8 | 0-55 |            |
+------+-----------------------------------+-----+------+------------+
| > 1  | > No show indicator               | > 6 | > 56 | > 1 AN     |
| 11.8 |                                   | 2.9 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 1  | > Extra charges                   | >   | > 5  | > 6 N      |
| 11.9 |                                   |  62 | 7-62 |            |
|      |                                   | .10 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Multiple clearing sequence      | >   | > 6  | > 2 N      |
| 1.10 | > number                          |  62 | 3-64 |            |
|      |                                   | .11 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Multiple clearing sequence      | >   | > 6  | > 2 N      |
| 1.11 | > count                           |  62 | 5-66 |            |
|      |                                   | .12 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Restricted ticket indicator     | >   | > 67 | > 1 AN     |
| 1.12 |                                   |  62 |      |            |
|      |                                   | .13 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Total amount authorized         | >   | > 6  | > 12 N     |
| 1.13 |                                   |  62 | 8-79 |            |
|      |                                   | .14 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Requested payment service       | >   | > 80 | > 1 AN     |
| 1.14 |                                   |  62 |      |            |
|      |                                   | .15 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Chargeback rights indicator     | >   | > 8  | > 2 AN     |
| 1.15 |                                   |  62 | 1-82 |            |
|      |                                   | .16 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Electronic commerce goods       | >   | > 8  | > 2 AN     |
| 1.16 | > indicator                       |  62 | 3-84 |            |
|      |                                   | .19 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Merchant verification value     | >   | > 8  | > 10 N     |
| 1.17 |                                   |  62 | 5-94 |            |
|      |                                   | .20 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Online risk assessment risk     | >   | > 9  | > 4 AN     |
| 1.18 | > score and reason codes          |  62 | 5-98 |            |
|      |                                   | .21 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Online risk assessment          | >   | > 99 | > 6 AN     |
| 1.19 | > condition codes                 |  62 | -104 |            |
|      |                                   | .22 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Card-level results              | >   | >    | > 2 AN     |
| 1.20 |                                   |  62 |  105 |            |
|      |                                   | .23 | -106 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Network ID                      | > 6 | >    | > 4 N      |
| 1.21 |                                   | 3.1 |  107 |            |
|      |                                   |     | -110 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Message reason code             | > 6 | >    | > 4 N      |
| 1.22 |                                   | 3.3 |  111 |            |
|      |                                   |     | -114 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > STIP/Switch reason code         | > 6 | >    | > 4 N      |
| 1.23 |                                   | 3.4 |  115 |            |
|      |                                   |     | -118 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Visa acquirer's business id     | > 6 | >    | > 8 N      |
| 1.24 |                                   | 3.8 |  119 |            |
|      |                                   |     | -126 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Fraud data                      | > 6 | >    | > 14 ANS   |
| 1.25 |                                   | 3.9 |  127 |            |
|      |                                   |     | -140 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Reimbursement attribute         | >   | >    | > 1 ANS    |
| 1.26 |                                   |  63 |  141 |            |
|      |                                   | .11 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Merchant volume indicator       | >   | >    | > 2 N      |
| 1.27 |                                   |  63 |  142 |            |
|      |                                   | .18 | -143 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Fee program indicator           | >   | >    | > 3 AN     |
| 1.28 |                                   |  63 |  144 |            |
|      |                                   | .19 | -146 |            |
+------+-----------------------------------+-----+------+------------+

+------+-----------------------------------+-----+------+------------+
| > 11 | > Charge indicator                | >   | >    | > 1 ANS    |
| 1.29 |                                   |  63 |  147 |            |
|      |                                   | .21 |      |            |
+======+===================================+=====+======+============+
| > 11 | > Stand In Trans Indicator        |     | >    | > 1 N      |
| 1.30 | > ([[Possible                     |     |  148 |            |
|      | > Values]{.underl                 |     |      |            |
|      | ine}](#stand-in-trans-indicator)) |     |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Transaction Unique Identifier   |     | >    | > 6 AN     |
| 1.31 |                                   |     |  149 |            |
|      |                                   |     | -154 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token Device Id                 | >   | >    | > 64 AN    |
| 1.32 |                                   | 125 |  155 |            |
|      |                                   | .03 | -218 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token Device No                 | >   | >    | > 15 N     |
| 1.33 |                                   | 125 |  219 |            |
|      |                                   | .04 | -233 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token Device Name               | >   | >    | > 20 AN    |
| 1.34 |                                   | 125 |  234 |            |
|      |                                   | .05 | -253 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token Device Type ([[Possible   | >   | >    | > 2 AN     |
| 1.35 | > Values]{                        | 125 |  254 |            |
|      | .underline}](#token-device-type)) | -01 | -255 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token ID                        | >   | >    | > 19 AN    |
| 1.36 |                                   | 123 |  256 |            |
|      |                                   | .01 | -274 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token Type ([[Possible          | >   | >    | > 2 AN     |
| 1.37 | > V                               | 123 |  275 |            |
|      | alues]{.underline}](#token-type)) | .07 | -276 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token Status ([[Possible        | >   | >    | > 1 AN     |
| 1.38 | > Val                             | 123 |  277 |            |
|      | ues]{.underline}](#token-status)) | .08 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token Authorization Request     |     | >    | > 1 N      |
| 1.39 | > (TAR) Indicator ([[Possible     |     |  278 |            |
|      | > Values]{.underline}](#token-    |     |      |            |
|      | authorization-request-indicator)) |     |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token Notification Type         |     | >    | > 4 N      |
| 1.40 | > ([[Possible                     |     |  279 |            |
|      | > Values]{.under                  |     | -282 |            |
|      | line}](#token-notification-type)) |     |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token OTP Code (spaced padded   | > 4 | >    | > 8 AN     |
| 1.41 | > on left)                        | 3.1 |  283 |            |
|      |                                   |     | -590 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Token OTP Expiry Date Time      | >   | >    | > 10 N     |
| 1.42 | > (Format: YYMMDDhhmm)            |  NA |  291 |            |
|      |                                   |     | -300 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Replacement PAN                 | >   | >    | > 19 AN    |
| 1.43 |                                   | 127 |  301 |            |
|      |                                   | .41 | -319 |            |
|      |                                   | >   |      |            |
|      |                                   | >   |      |            |
|      |                                   | tag |      |            |
|      |                                   | >   |      |            |
|      |                                   |  01 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Replacement PAN Expiration Date | >   | >    | > 4 N      |
| 1.44 | > (Format: YYMM)                  | 127 |  320 |            |
|      |                                   | .41 | -323 |            |
|      |                                   | >   |      |            |
|      |                                   | >   |      |            |
|      |                                   | tag |      |            |
|      |                                   | >   |      |            |
|      |                                   |  02 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Partial Authorization Indicator | >   | >    | > 1N       |
| 1.45 |                                   |  60 |  324 |            |
|      |                                   | .10 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Chargeback Flag                 |     | >    | > 1AN      |
| 1.46 |                                   |     |  325 |            |
+------+-----------------------------------+-----+------+------------+
| >    | > Cardholder Verification Method  |     | >    | > 1 N      |
| 111. | > Identifier                      |     |  326 |            |
| 47\* |                                   |     |      |            |
+------+-----------------------------------+-----+------+------------+
| >    | > Cardholder Verification Method  |     | >    | > 64 AN    |
| 111. | > Value                           |     |  327 |            |
| 48\* |                                   |     | -390 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Bound Device Index              | >   | >    | > 2 AN     |
| 1.49 |                                   | 123 |  391 |            |
|      |                                   | .80 | -392 |            |
+------+-----------------------------------+-----+------+------------+
| >    | > Token User Identifier           | >   | >    | > 11AN     |
| 111. |                                   | 123 |  393 |            |
| 50\* |                                   | .81 | -403 |            |
+------+-----------------------------------+-----+------+------------+
| >    | > Token User Application Type     | >   | >    | > 2 AN     |
| 111. |                                   | 123 |  404 |            |
| 51\* |                                   | .82 | -405 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > 3D Secure Indicator             | >   | >    | > 1 ANS    |
| 1.52 |                                   | 126 |  406 |            |
|      |                                   | .20 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > CAVV Result Code                | >   | >    | > 1 ANS    |
| 1.53 |                                   |  44 |  407 |            |
|      |                                   | .13 |      |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > E-Commerce and payment          | > 6 | >    | > 2 N      |
| 1.54 | > indicator                       | 0.8 |  408 |            |
|      |                                   |     | -409 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > E-Commerce Security Indicator   | > 6 | >    | > 1 ANS    |
| 1.55 |                                   | 3.6 |  410 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > CAVV Data                       | >   | >    | > 40 AN    |
| 1.56 |                                   |  12 |  411 |            |
|      |                                   | 6.9 | -451 |            |
+------+-----------------------------------+-----+------+------------+
| > 11 | > Wallet Type                     |     | >    | > 5 AN     |
| 1.57 |                                   |     |  451 |            |
|      |                                   |     | -455 |            |
+------+-----------------------------------+-----+------+------------+

> **111.47 -- Cardholder Verification Method Identifier**
>
> The cardholder verification method identifier represents the
> verification method selected by the cardholder during the token
> provision process when a Yellow path is opted and OTP (One-Time
> Password) is selected as a step-up authentication method.
>
> The possible values can be:

-   Cell Phone

-   Email

##### 111.48 -- Cardholder Verification Method Value {#cardholder-verification-method-value .unnumbered}

> This field will contain the content of the selected cardholder
> verification method. For example, if value 1 i.e., Cell Phone is
> selected in Field 111.47, then this field will contain the
> cardholder's phone number on which on which OTP has to be sent.
> Similarly, if value 2 i.e., Email is selected in Field 111.47, then
> will contain cardholder's email address on which email has to be sent.

##### 111.49- Bound Device Index {#bound-device-index .unnumbered}

> This field will contain the index number from the Visa database where
> the device ID is stored. The value will be a one-byte hexadecimal
> value in the range of **01**--**63** (Decimal 1--99).

##### 111.51- Token User Application Type {#token-user-application-type .unnumbered}

> This field will contain the application type of the token user. This
> entity can be the merchant, a marketplace, or a check out host. The
> application type is one of the following valid values:

-   **00** (Unknown)

-   **01** (Web)

-   **02** (Mobile web)

-   **03** (Mobile application)

-   **04** (Marketplace application)

-   **05** (Voice application)

-   **06** (Biometric application)

-   **07**--**FF** (Reserved)

+---------+----------------------------+---------+------+------------+
| > [     |                            |         |      |            |
| ]{#_boo |                            |         |      |            |
| kmark90 |                            |         |      |            |
| >       |                            |         |      |            |
|  .ancho |                            |         |      |            |
| r}**Sub |                            |         |      |            |
| > E     |                            |         |      |            |
| lements |                            |         |      |            |
| > of    |                            |         |      |            |
| >       |                            |         |      |            |
|  DE-111 |                            |         |      |            |
| > when  |                            |         |      |            |
| >       |                            |         |      |            |
| DE-63.7 |                            |         |      |            |
| > =     |                            |         |      |            |
| >       |                            |         |      |            |
| 'MASTER |                            |         |      |            |
| CARD'** |                            |         |      |            |
+=========+============================+=========+======+============+
| > **Sub | > **Field Name**           | > **MC  | >    | >          |
| >       |                            | > Bit   | **Po | **Format** |
| Field** |                            | > No.** | siti | >          |
| >       |                            |         | on** | > *        |
| >       |                            |         |      | *(ASCII)** |
| **No.** |                            |         |      |            |
+---------+----------------------------+---------+------+------------+
| > 111.1 | > Account category         | > 48.38 | > 1  | > 1 AN     |
+---------+----------------------------+---------+------+------------+
| > 111.2 | > Electronic commerce      | > 48.40 | >    | > 40 AN    |
|         | >                          |         | 2-41 |            |
|         | > merchant/cardholder      |         |      |            |
|         | > certificate serial       |         |      |            |
|         | > number                   |         |      |            |
+---------+----------------------------+---------+------+------------+

+---------+----------------------------+---------+------+------------+
| > 111.3 | > Electronic commerce      | > 48.41 | > 42 | > 95 ANS   |
|         | > certificate qualifying   |         | -136 |            |
|         | >                          |         |      |            |
|         | > information              |         |      |            |
+=========+============================+=========+======+============+
| >       | > Electronic commerce      | > 48.42 | >    | > 7 N      |
| 111.4\* | > indicators               |         |  137 |            |
|         |                            |         | -143 |            |
+---------+----------------------------+---------+------+------------+
| > 111.5 | > Universal cardholder     | > 48.43 | >    | > 32 ANS   |
|         | > authentication field     |         |  144 |            |
|         | >                          |         | -175 |            |
|         | > (UCAF)                   |         |      |            |
+---------+----------------------------+---------+------+------------+
| > 111.6 | > Mobile Program           | > 48.48 | >    | > 73ANS    |
|         | > Indicators               |         |  176 |            |
|         |                            |         | -248 |            |
+---------+----------------------------+---------+------+------------+
| > 111.7 | > Original Switch Serial   | > 48.59 | >    | > 9 N      |
|         | > Number                   |         |  249 |            |
|         |                            |         | -257 |            |
+---------+----------------------------+---------+------+------------+
| > 111.8 | > POS Data, extended       | > 48.61 | >    | > 5 N      |
|         | > condition codes\*        |         |  258 |            |
|         |                            |         | -262 |            |
+---------+----------------------------+---------+------+------------+
| > 111.9 | > Trace ID                 | > 48.63 | >    | > 15 ANS   |
|         |                            |         |  263 |            |
|         |                            |         | -277 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Transit program          | > 48.64 | >    | > 4 N      |
|  111.10 |                            |         |  278 |            |
|         |                            |         | -281 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Implied decimal          | > 48.70 | >    | > 5 N      |
|  111.11 |                            |         |  282 |            |
|         |                            |         | -286 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Issuer chip              | > 48.72 | >    | > 16 AN    |
|  111.12 | > authentication           |         |  287 |            |
|         |                            |         | -302 |            |
+---------+----------------------------+---------+------+------------+
| >       | > MasterCard electronic    | > 48.76 | >    | > 1 A      |
|  111.13 | > transaction              |         |  303 |            |
|         | >                          |         |      |            |
|         | > indicator                |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Payment transaction type | > 48.77 | >    | > 3 AN     |
|  111.14 | > indicator                |         |  304 |            |
|         |                            |         | -306 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Chip CVR/TVR bit error   | > 48.79 | >    | > 50 AN    |
|  111.15 | > results listing          |         |  307 |            |
|         |                            |         | -356 |            |
+---------+----------------------------+---------+------+------------+
| >       | > PIN Service code         | > 48.80 | >    | > 2 A      |
|  111.16 |                            |         |  357 |            |
|         |                            |         | -358 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Maestro PIN-less program | > 48.81 | >    | > 1 AN     |
|  111.17 | > indicator                |         |  359 |            |
+---------+----------------------------+---------+------+------------+
| > 1     | > Address verification     | > 48.82 | >    | > 2 N      |
| 11.18\* | > service request          |         |  360 |            |
|         |                            |         | -361 |            |
+---------+----------------------------+---------+------+------------+
| > 1     | > Address verification     | > 48.83 | >    | > 1 N      |
| 11.19\* | > service response         |         |  362 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Merchant advice code     | > 48.84 | >    | > 2 AN     |
|  111.20 |                            |         |  363 |            |
|         |                            |         | -364 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Card validation code     | > 48.87 | >    | > 1 AN     |
|  111.21 | > result                   |         |  365 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Magnetic stripe          | > 48.88 | >    | > 1 AN     |
|  111.22 | > compliance status        |         |  366 |            |
|         | >                          |         |      |            |
|         | > indicator                |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Magnetic stripe          | > 48.89 | >    | > 1 AN     |
|  111.23 | > compliance error         |         |  367 |            |
|         | > indicator                |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > CVC 2 Value              | > 48.92 | >    | > 3 N      |
|  111.24 |                            |         |  368 |            |
|         |                            |         | -370 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Program participation    | > 48.94 | >    | > 28 ANS   |
|  111.25 | > indicator                |         |  371 |            |
|         |                            |         | -398 |            |
+---------+----------------------------+---------+------+------------+
| >       | > MasterCard promotion     | > 48.95 | >    | > 6 AN     |
|  111.26 | > code                     |         |  399 |            |
|         |                            |         | -404 |            |
+---------+----------------------------+---------+------+------------+
| >       | > MasterCard corporate     | > 48.98 | >    | > 6 N      |
|  111.27 | > fleet card id/driver     |         |  405 |            |
|         | >                          |         | -410 |            |
|         | > number                   |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > MasterCard corporate     | > 48.99 | >    | > 15 AN    |
|  111.28 | > fleet card vehicle       |         |  411 |            |
|         | >                          |         | -425 |            |
|         | > number                   |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Stand In Trans Indicator |         | >    | > 1 N      |
|  111.29 | > ([[Possible              |         |  426 |            |
|         | > Values]{.underline}](#   |         |      |            |
|         | stand-in-trans-indicator)) |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Transaction Unique       |         | >    | > 6 AN     |
|  111.30 | > Identifier               |         |  427 |            |
|         |                            |         | -432 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token Device Id          | > NA    | >    | > 64 AN    |
|  111.31 |                            |         |  433 |            |
|         |                            |         | -496 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token Device No          | >       | >    | > 15 N     |
|  111.32 |                            | 124.191 |  497 |            |
|         |                            |         | -511 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token Device Name        | >       | >    | > 20 AN    |
|  111.33 |                            |  120.92 |  512 |            |
|         |                            |         | -531 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token Device Type        | > NA    | >    | > 2 AN     |
|  111.34 | > ([[Possible              |         |  532 |            |
|         | > Values]{.underl          |         | -533 |            |
|         | ine}](#token-device-type)) |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token ID                 | > 120.1 | >    | > 19 AN    |
|  111.35 |                            | > Or    |  534 |            |
|         |                            | >       | -552 |            |
|         |                            | >       |      |            |
|         |                            |  120.24 |      |            |
|         |                            | > Or    |      |            |
|         |                            | >       |      |            |
|         |                            | > 48.33 |      |            |
|         |                            | > tag   |      |            |
|         |                            | > 02    |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token Type ([[Possible   | >       | >    | > 2 AN     |
|  111.36 | > Values]{                 | 120.253 |  553 |            |
|         | .underline}](#token-type)) | > Or    | -554 |            |
|         |                            | >       |      |            |
|         |                            | >       |      |            |
|         |                            | 124.195 |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token Status ([[Possible |         | >    | > 1 AN     |
|  111.37 | > Values]{.u               |         |  555 |            |
|         | nderline}](#token-status)) |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token Authorization      |         | >    | > 1 N      |
|  111.38 | > Request (TAR)            |         |  556 |            |
+---------+----------------------------+---------+------+------------+

+---------+----------------------------+---------+------+------------+
|         | > Indicator ([[Possible    |         |      |            |
|         | > Values]{.                |         |      |            |
|         | underline}](#token-authori |         |      |            |
|         | zation-request-indicator)) |         |      |            |
+=========+============================+=========+======+============+
| >       | > Token Notification Type  |         | >    | > 4 N      |
|  111.39 | > ([[Possible              |         |  557 |            |
|         | > Values]{.underline}](    |         | -560 |            |
|         | #token-notification-type)) |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token OTP Code (spaced   | >       | >    | > 8 AN     |
|  111.40 | > padded on left)          |  120.38 |  561 |            |
|         |                            |         | -568 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Token OTP Expiry Date    | >       | >    | > 10 N     |
|  111.41 | > Time (Format:            |  120.46 |  569 |            |
|         | >                          |         | -578 |            |
|         | > YYMMDDhhmm)              |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Replacement PAN          | > NA    | >    | > 19 AN    |
|  111.42 |                            |         |  579 |            |
|         |                            |         | -597 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Replacement PAN          | > NA    | >    | > 4 N      |
|  111.43 | > Expiration Date          |         |  598 |            |
|         | >                          |         | -601 |            |
|         | > (Format: YYMM)           |         |      |            |
+---------+----------------------------+---------+------+------------+
| > 1     | > Customer's Activation    | > 120.6 | >    | > 165 ANS  |
| 11.44\* | > Code                     |         |  602 |            |
|         | >                          |         | -766 |            |
|         | > DistributionMethod       |         |      |            |
|         | > Preference               |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Chargeback flag (For     |         | >    | > 1AN      |
|  111.45 | > details, see             |         |  767 |            |
|         | >                          |         |      |            |
|         | > [[Appe                   |         |      |            |
|         | ndix-E]{.underline}](#appe |         |      |            |
|         | ndix-e-possible-values-of- |         |      |            |
|         | new-sub-fields-in-de-111)) |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > On-behalf Service (OBS)  | > 48.71 | >    | > 40 ANS   |
|  111.46 | > (For details, see        |         |  768 |            |
|         | >                          |         | -807 |            |
|         | > [[Appe                   |         |      |            |
|         | ndix-E]{.underline}](#appe |         |      |            |
|         | ndix-e-possible-values-of- |         |      |            |
|         | new-sub-fields-in-de-111)) |         |      |            |
+---------+----------------------------+---------+------+------------+
| >       | > Fraud Scoring Data (For  | > 48.75 | >    | > 32 AN    |
|  111.47 | > details, see             |         |  808 |            |
|         | >                          |         | -839 |            |
|         | > [[Appe                   |         |      |            |
|         | ndix-E]{.underline}](#appe |         |      |            |
|         | ndix-e-possible-values-of- |         |      |            |
|         | new-sub-fields-in-de-111)) |         |      |            |
+---------+----------------------------+---------+------+------------+
| > 1     | > Incremental              |         | >    | > 1AN      |
| 11.48\* | > Authorization Indicator  |         |  840 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Final Auth Indicator     | > 48.61 | >    | > 1 N      |
|  111.49 |                            |         |  841 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Issuer Transaction       |         | >    | > 1 N      |
|  111.50 | > Transformation Flag      |         |  842 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Network Billing Amount   | > 6     | >    | > 12 N     |
|  111.51 |                            |         |  843 |            |
|         |                            |         | -854 |            |
+---------+----------------------------+---------+------+------------+
| >       | > Network Billing Exchange | > 10    | >    | > 8 N      |
|  111.52 | > Rate                     |         |  855 |            |
|         |                            |         | -862 |            |
+---------+----------------------------+---------+------+------------+
| >       | > On Demand Acquirer ID    |         | >    | > 4 N      |
|  111.53 |                            |         |  863 |            |
|         |                            |         | -866 |            |
+---------+----------------------------+---------+------+------------+
| > [     | > [File Update             | > [91]  | >    | > [1       |
| 111.54] | > Code]{.mark}             | {.mark} | [867 | >          |
| {.mark} |                            |         | ]{.m | AN]{.mark} |
|         |                            |         | ark} |            |
+---------+----------------------------+---------+------+------------+
| > [     | > [File Name]{.mark}       | > [101] | >    | > [17      |
| 111.55] |                            | {.mark} | [868 | > A        |
| {.mark} |                            |         | -884 | NS]{.mark} |
|         |                            |         | ]{.m |            |
|         |                            |         | ark} |            |
+---------+----------------------------+---------+------+------------+
| > [     | > [Primary Account Card    | > [120] | >    | > [3       |
| 111.56] | > Sequence Number]{.mark}  | {.mark} | [885 | > A        |
| {.mark} |                            |         | -887 | NS]{.mark} |
|         |                            |         | ]{.m |            |
|         |                            |         | ark} |            |
+---------+----------------------------+---------+------+------------+

##### POS Data, extended condition codes: {#pos-data-extended-condition-codes .unnumbered}

> Sub field -- 1: Partial Approval Terminal Support Indicator
>
> Sub field -- 2: Purchase Amount Only Terminal Support Indicator Sub
> field -- 3: Real time Substantiation Indicator
>
> Sub field -- 4: Reserved for Future Use Sub field -- 5: Final
> Authorization Indicators

##### \* Electronic Commerce Indicators

> Contains the electronic commerce indicators representing the security
> level and cardholder authentication associated with the transaction.
> This subfield must be present in all Authorization Request/0100
> messages
>
> for electronic commerce transactions. This subfield consists of
> further three sub-fields SF1, SF2 and SF3. SF1 and SF2 have length 3-N
> with 3 different positions & SF3 has length 1-N. Each position has
> possible values.

##### Possible Values of Position 1 of SF1: {#possible-values-of-position-1-of-sf1 .unnumbered}

> 0 = Reserved for existing Mastercard Europe/Visa definitions
>
> 1 = Reserved for future use
>
> 2 = Chanel
>
> 3-8 = Reserved for future use 9 = None (no security protocol)

##### Possible Values of Position 2 of SF1: {#possible-values-of-position-2-of-sf1 .unnumbered}

> 0 = Reserved for future use
>
> 1 = Cardholder certificate not used
>
> 2 = Processed through Masterpass
>
> 4 = Digital Secure Remote Payment Transaction 5--9 = Reserved for
> future use

##### Possible Values of Position 3 of SF1: {#possible-values-of-position-3-of-sf1 .unnumbered}

> 0 = UCAF data collection is not supported by the merchant
>
> 1 = UCAF data collection is supported by the merchant, and UCAF data
> should be available
>
> 2 = Issuer Authenticated
>
> 3 = UCAF data collection is supported by the merchant.
>
> 4 = Reserved for future use
>
> 5 = Issuer risk based decisioning
>
> 6 = Merchant Risk Based Decisioning
>
> 7 = Partial shipment or recurring payment. Liability will depend on
> the original UCAF values provided and matching with the initial
> transaction.
>
> Subelement 111.4, subfields 2 and 3 are only present in the Financial
> Transaction Request, Response/0210 message provided by Mastercard to
> the acquirer if an Security Level Indicator (SLI) downgrade occurred.
>
> Issuers will not see subfields 2 or 3 in the Financial Transaction
> Request/0200 messages.

##### 111.18\* (Address Verification Service Request) {#address-verification-service-request .unnumbered}

> Indicates that verification of the cardholder billing address is
> requested in the authorization message and this field must be present
> in authorization request message whenever cardholder address
> verification is required.

##### Possible Values: {#possible-values .unnumbered}

> 52 = AVS and Authorization Request/0100

##### 111.19\* (Address Verification Service Response) {#address-verification-service-response .unnumbered}

> Contains the AVS verification response code in the Authorization
> Request Response message.

##### Possible Values: {#possible-values-1 .unnumbered}

> **A =** Address matches, postal code does not.
>
> **B =** Visa only. Street address match. Postal code not verified
> because of incompatible formats. (Acquirer sent both street address
> and postal code.)
>
> **C =** Visa only. Street address and postal code not verified because
> of incompatible formats. (Acquirer sent both street address and postal
> code.)
>
> **D =** Visa only. Street address and postal code match.
>
> **F =** Visa only. Street address and postal code match. Applies to
> U.K. only.
>
> **G =** Visa only. Non-AVS participant outside the U.S.; address not
> verified for international transaction.
>
> **I =** Visa only. Address information not verified for international
> transaction.
>
> **M =** Visa only. Street addresses and postal code match.
>
> **N =** Neither address nor postal code matches.
>
> **P =** Visa only. Postal codes match. Street address not verified
> because of incompatible formats. (Acquirer sent both street address
> and postal code.)
>
> **R =** Retry, system unable to process.
>
> **S =** AVS currently not supported.
>
> **U =** No data from issuer/Authorization Platform
>
> **W =** For U.S. addresses, nine-digit postal code matches, address
> does not; for address outside the U.S., postal code matches, address
> does not.
>
> **X =** For U.S. addresses, nine-digit postal code and address
> matches; for addresses outside the U.S., postal code and address
> match.
>
> **Y =** For U.S. addresses, five-digit postal code and address
> matches.
>
> **Z =** For U.S. addresses, five-digit postal code matches, address
> does not.

##### 111.44\* {#section .unnumbered}

> There will be only one method contained within this field. This field
> will only be present if the cardholder provides a choice.
>
> [Activation Code Distribution Method Type (n-1)]{.underline}
>
> Possible Values are:
>
> **1** = Masked mobile phone number
>
> **2** = Masked email address
>
> **3** = Automated call center phone number
>
> **4** = Call center phone number
>
> **5** = Website
>
> **6** = Mobile application
>
> **7** = Masked voice call phone number
>
> Activation Code Distribution Method Value (ans...164) See below
> examples:

###### "1(###) \### 4567" {#section-1 .unnumbered}

> 1 = Masked mobile phone number
>
> The "1" will be followed by the masked mobile phone number.
> "**2a\*\*\*<d@anymail.com>"**
>
> 2 = Masked email address
>
> The "2" will be followed by the consumer's masked email address (the
> issuer will mask according to their own format).

###### "3(555) 123 4567" {#section-2 .unnumbered}

> 3 = Automated call center phone number
>
> The "3" will be followed by the phone number. This phone number is not
> masked. "4(555) 123 8901"
>
> 4 = Call center phone number
>
> The "4" will be followed by the phone number. This phone number is not
> masked. "[5http://www.anybank.com](http://www.anybank.com/)"
>
> 5 = Website
>
> The "5" will be followed by the issuer's website URL.
> "6com.anybank.mobileapp"
>
> 6 = Mobile app
>
> The "6" will be followed by the issuer's mobile app information, the
> content of which depends upon the mobile device operating system.
>
> "7(###) \### 2345"
>
> 7 = Masked voice call phone number
>
> The "7" will be followed by the masked voice call phone number.

##### 111.48\*: Incremental authorization Indicator {#incremental-authorization-indicator .unnumbered}

> Possible Values: Y/N
>
> \[will be received in Authorization messages (x1xx) only, If
> Incremental Auth then → 'Y', else → 'N'\]

+----------+-------------------------------+------+------+------------+
| > **Sub  |                               |      |      |            |
| >        |                               |      |      |            |
| Elements |                               |      |      |            |
| > of     |                               |      |      |            |
| > DE-111 |                               |      |      |            |
| > when   |                               |      |      |            |
| >        |                               |      |      |            |
|  DE-63.7 |                               |      |      |            |
| > =      |                               |      |      |            |
| > 'E     |                               |      |      |            |
| FUNDS'** |                               |      |      |            |
+==========+===============================+======+======+============+
| > **Sub  | > **Field Name**              | > *  | >    | >          |
| > Field  |                               | *FIS | **Po | **Format** |
| > No.**  |                               | > B  | siti | >          |
|          |                               | it** | on** | > *        |
|          |                               | >    |      | *(ASCII)** |
|          |                               | >    |      |            |
|          |                               |  **N |      |            |
|          |                               | o.** |      |            |
+----------+-------------------------------+------+------+------------+
| > 111.1  | > Partial Authorization       | > 6  | > 1  | > 1 AN     |
|          | > Indicator                   | 3.40 |      |            |
+----------+-------------------------------+------+------+------------+
| > 111.2  | > Stand In Trans Indicator    |      | > 2  | > 1 N      |
|          | > ([[Possible                 |      |      |            |
|          | > Values]{.underline}         |      |      |            |
|          | ](#stand-in-trans-indicator)) |      |      |            |
+----------+-------------------------------+------+------+------------+
| > 111.3  | > Transaction Unique          |      | >    | > 6 AN     |
|          | > Identifier                  |      |  3-8 |            |
+----------+-------------------------------+------+------+------------+
| > 111.4  | > Token Device Id             | > NA | >    | > 64 AN    |
|          |                               |      | 9-72 |            |
+----------+-------------------------------+------+------+------------+
| > 111.5  | > Token Device No             | > NA | > 7  | > 15 N     |
|          |                               |      | 3-87 |            |
+----------+-------------------------------+------+------+------------+
| > 111.6  | > Token Device Name           | > NA | > 88 | > 20 AN    |
|          |                               |      | -107 |            |
+----------+-------------------------------+------+------+------------+
| > 111.7  | > Token Device Type           |      | >    | > 2 AN     |
|          | > ([[Possible                 |      |  108 |            |
|          | > Values]{.und                |      | -109 |            |
|          | erline}](#token-device-type)) |      |      |            |
+----------+-------------------------------+------+------+------------+
| > 111.8  | > Token ID                    | > NA | >    | > 19 AN    |
|          |                               |      |  110 |            |
|          |                               |      | -128 |            |
+----------+-------------------------------+------+------+------------+
| > 111.9  | > Token Type ([[Possible      |      | >    | > 2 AN     |
|          | > Value                       |      |  129 |            |
|          | s]{.underline}](#token-type)) |      | -130 |            |
+----------+-------------------------------+------+------+------------+

+----------+-------------------------------+------+------+------------+
| > 111.10 | > Token Status ([[Possible    |      | >    | > 1 AN     |
|          | > Values]                     |      |  131 |            |
|          | {.underline}](#token-status)) |      |      |            |
+==========+===============================+======+======+============+
| > TBD    | > Token Authorization Request |      | >    | > 1 N      |
|          | > (TAR) Indicator             |      |  TBD |            |
|          | >                             |      |      |            |
|          | > ([[Possible                 |      |      |            |
|          | > Val                         |      |      |            |
|          | ues]{.underline}](#token-auth |      |      |            |
|          | orization-request-indicator)) |      |      |            |
+----------+-------------------------------+------+------+------------+
| > TBD    | > Token Notification Type     |      | >    | > 4 N      |
|          | > ([[Possible                 |      |  TBD |            |
|          | > Values]{.underline          |      |      |            |
|          | }](#token-notification-type)) |      |      |            |
+----------+-------------------------------+------+------+------------+
| > TBD    | > Token OTP Code (spaced      | > NA | >    | > 8 AN     |
|          | > padded on left)             |      |  TBD |            |
+----------+-------------------------------+------+------+------------+
| > TBD    | > Token OTP Expiry Date Time  | > NA | >    | > 10 N     |
|          | > (Format:                    |      |  TBD |            |
|          | >                             |      |      |            |
|          | > YYMMDDhhmm)                 |      |      |            |
+----------+-------------------------------+------+------+------------+
| > TBD    | > Replacement PAN             | > NA | >    | > 19 AN    |
|          |                               |      |  TBD |            |
+----------+-------------------------------+------+------+------------+
| > TBD    | > Replacement PAN Expiration  | > NA | >    | > 4 N      |
|          | > Date (Format:               |      |  TBD |            |
|          | >                             |      |      |            |
|          | > YYMM)                       |      |      |            |
+----------+-------------------------------+------+------+------------+
| > 111.11 | > Chargeback flag             |      | >    | > 1AN      |
|          |                               |      |  132 |            |
+----------+-------------------------------+------+------+------------+
| > 111.12 | > Incremental Authorization   | > 60 | >    | > 1AN      |
|          | > Flag                        |      |  133 |            |
+----------+-------------------------------+------+------+------------+
| > 111.13 | > Multi-Clearing Sequence     | >    | >    | > 2N       |
|          |                               |  124 |  134 |            |
+----------+-------------------------------+------+------+------------+
| > 111.14 | > Multi-Clearing Count        | >    | >    | > 2N       |
|          |                               |  124 |  136 |            |
+----------+-------------------------------+------+------+------------+

+--------+------------------------------+-----+------+----------------+
| >      |                              |     |      |                |
|  **Sub |                              |     |      |                |
| > El   |                              |     |      |                |
| ements |                              |     |      |                |
| > of   |                              |     |      |                |
| >      |                              |     |      |                |
| DE-111 |                              |     |      |                |
| > when |                              |     |      |                |
| > D    |                              |     |      |                |
| E-63.7 |                              |     |      |                |
| > =    |                              |     |      |                |
| > 'S   |                              |     |      |                |
| TAR'** |                              |     |      |                |
+========+==============================+=====+======+================+
| >      | > **Field Name**             | >   | >    | > **Format     |
|  **Sub |                              |  ** | **Po | > (ASCII)**    |
| >      |                              | STA | siti |                |
|  Field |                              | R** | on** |                |
| >      |                              | >   |      |                |
|  No.** |                              | >   |      |                |
|        |                              |  ** |      |                |
|        |                              | Bit |      |                |
|        |                              | >   |      |                |
|        |                              |  No |      |                |
|        |                              | .** |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Partial                    | > 6 | > 1  | > 1 AN         |
|  111.1 | > Authorization/Approval     | 3.7 |      |                |
|        | > Indicator                  |     |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Stand In Trans Indicator   |     | > 2  | > 1 N          |
|  111.2 |                              |     |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Transaction Unique         |     | >    | > 6 AN         |
|  111.3 | > Identifier                 |     |  3-8 |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Chargeback flag            |     | > 9  | > 1 AN         |
|  111.4 |                              |     |      |                |
+--------+------------------------------+-----+------+----------------+
| > 1    | > Incremental Authorization  | >   | > 10 | > 1 AN         |
| 11.5\* |                              |  11 |      |                |
|        |                              | 0.2 |      |                |
+--------+------------------------------+-----+------+----------------+
| > 1    | > Multiple Transaction       | >   | > 1  | > 3 N          |
| 11.6\* | > Sequence                   |  11 | 1-13 |                |
|        |                              | 0.6 |      |                |
+--------+------------------------------+-----+------+----------------+
| > 1    | > Multiple Transaction Count | >   | > 1  | > 3 N          |
| 11.7\* |                              |  11 | 4-16 |                |
|        |                              | 0.7 |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Pseduo-Terminal Id         | > 6 | > 1  | > 6 AN         |
|  111.8 |                              | 3.1 | 7-22 |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Interchange Program        | >   | > 2  | > 3 N          |
|  111.9 | > Identifier                 |  10 | 3-25 |                |
|        |                              | 4.2 |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > STAR® Verification Value   | >   | > 2  | > 10 AN        |
| 111.10 |                              |  10 | 6-35 |                |
|        |                              | 4.3 |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Market Indicator           | >   | > 36 | > 1 AN         |
| 111.11 |                              |  10 |      |                |
|        |                              | 4.4 |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Merchant Aggregation       | >   | > 37 | > 1 AN         |
| 111.12 | > Indicator                  |  10 |      |                |
|        |                              | 4.5 |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Transaction Aggregation    | >   | > 38 | > 1 AN         |
| 111.13 | > Indicator                  |  10 |      |                |
|        |                              | 4.6 |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Money/Funds                | >   | > 39 | > 1 AN         |
| 111.14 | > Transfer/Prepaid Load      |  10 |      |                |
|        | > Definition                 | 4.7 |      |                |
+--------+------------------------------+-----+------+----------------+
| > 11   | > Transaction Description    | >   | > 4  | > 2 AN         |
| 1.15\* |                              |  10 | 0-41 |                |
|        |                              | 4.8 |      |                |
+--------+------------------------------+-----+------+----------------+
| >      | > Purchase Identifier        | >   | > 4  | > 26 AN        |
| 111.16 |                              |  11 | 2-67 |                |
|        |                              | 0.3 |      |                |
+--------+------------------------------+-----+------+----------------+
| > 11   | > STAR® Predictive Fraud     | >   | > 6  | > 3 N          |
| 1.17\* | > Score                      | 110 | 8-70 |                |
|        |                              | >   |      |                |
|        |                              | >   |      |                |
|        |                              | Tag |      |                |
|        |                              | >   |      |                |
|        |                              |  SF |      |                |
+--------+------------------------------+-----+------+----------------+
| > 11   | > STAR® Predictive Fraud     | >   | > 7  | > 2 AN         |
| 1.18\* | > Reason Code                | 110 | 1-72 |                |
|        |                              | >   |      |                |
|        |                              | >   |      |                |
|        |                              | Tag |      |                |
|        |                              | >   |      |                |
|        |                              |  SF |      |                |
+--------+------------------------------+-----+------+----------------+

##### \*: Incremental authorization Indicator

> Possible Values: Y/N
>
> \[will be received in Authorization messages (x1xx) only, If
> Incremental Auth then → 'Y', else → 'N'\]

##### \*: Multiple Transaction Sequence

> If there are multiple completions, the number of completion that this
> record represents.

##### \*: Multiple Transaction Count

> Indicates the total number of completions expected in a multi-clearing
> scenario.

##### 111.15\*: Transaction Description {#transaction-description .unnumbered}

> Possible values and their corresponding detail for this field:

+-------+--------------------------------------------------------------+
| > *   | > Account to Account                                         |
| *AA** |                                                              |
+=======+==============================================================+
| > *   | > Business to Business                                       |
| *BB** |                                                              |
+-------+--------------------------------------------------------------+
| > *   | > Business to Person                                         |
| *BP** |                                                              |
+-------+--------------------------------------------------------------+
| > *   | > Online gambling (winnings) -- for future                   |
| *OG** | >                                                            |
|       | > use                                                        |
+-------+--------------------------------------------------------------+
| > *   | > Person to Person                                           |
| *PP** |                                                              |
+-------+--------------------------------------------------------------+

##### \*: Predictive Fraud Score

> Represents a score ranging from **000 to 999**. The higher the value,
> more likely it is to be a fraudulent transaction.

##### \*: Predictive Fraud Reason Code

> Reflects the reason code that supports the STAR predictive fraud score
> value.

+---------+-------------------------------+-------+-----+------------+
| > [     |                               |       |     |            |
| ]{#_boo |                               |       |     |            |
| kmark91 |                               |       |     |            |
| >       |                               |       |     |            |
|  .ancho |                               |       |     |            |
| r}**Sub |                               |       |     |            |
| > E     |                               |       |     |            |
| lements |                               |       |     |            |
| > of    |                               |       |     |            |
| >       |                               |       |     |            |
|  DE-111 |                               |       |     |            |
| > when  |                               |       |     |            |
| >       |                               |       |     |            |
| DE-63.7 |                               |       |     |            |
| > =     |                               |       |     |            |
| > 'UNIO |                               |       |     |            |
| NPAY'** |                               |       |     |            |
+=========+===============================+=======+=====+============+
| > **Sub | > **Field Name**              | >     | >   | > **Format |
| > Field |                               | **Uni | **P | >          |
| > No.** |                               | onPay | osi |  (ASCII)** |
|         |                               | > Bit | tio |            |
|         |                               | >     | n** |            |
|         |                               | No.** |     |            |
+---------+-------------------------------+-------+-----+------------+
| > 111.1 | > Minor Unit of Transaction   | > 6   | >   | > 3 AN     |
|         | > Currency                    | 0.3.3 | 1-3 |            |
+---------+-------------------------------+-------+-----+------------+
| > 111.2 | > Partial Authorization       | > 6   | > 4 | > 1 AN     |
|         | > Indicator                   | 0.3.4 |     |            |
+---------+-------------------------------+-------+-----+------------+
| > 111.3 | > Transaction Medium          | > 6   | > 5 | > 1 AN     |
|         |                               | 0.3.6 |     |            |
+---------+-------------------------------+-------+-----+------------+
| > 111.4 | > IC card application type    | > 6   | > 6 | > 1 AN     |
|         |                               | 0.3.7 |     |            |
+---------+-------------------------------+-------+-----+------------+
| > 111.5 | > Account Attribute           | > 6   | >   | > 2 AN     |
|         |                               | 0.3.8 | 7-8 |            |
+---------+-------------------------------+-------+-----+------------+
| > 111.6 | > Card Level                  | > 6   | > 9 | > 1 AN     |
|         |                               | 0.3.9 |     |            |
+---------+-------------------------------+-------+-----+------------+
| > 111.7 | > Card Product                | > 60  | >   | > 2 AN     |
|         |                               | .3.10 |  10 |            |
|         |                               |       | -11 |            |
+---------+-------------------------------+-------+-----+------------+
| > 111.8 | > Transaction Cancellation    |       | >   | > 1 AN     |
|         | > Indicator                   |       |  12 |            |
+---------+-------------------------------+-------+-----+------------+
| > 111.9 | > Original MTI of             |       | >   | > 4 AN     |
|         | > Cancellation Transaction    |       |  13 |            |
|         |                               |       | -16 |            |
+---------+-------------------------------+-------+-----+------------+
| >       | > OTP Code (spaced padded on  |       | >   | > 10 AN    |
|  111.10 | > left)                       |       |  17 |            |
|         |                               |       | -26 |            |
+---------+-------------------------------+-------+-----+------------+
| >       | > Token OTP Expiry Date Time  |       | >   | > 10 AN    |
|  111.11 | > (Format:                    |       |  27 |            |
|         |                               |       | -36 |            |
+---------+-------------------------------+-------+-----+------------+

+---------+-------------------------------+-------+-----+------------+
|         | > YYMMDDhhmm)                 |       |     |            |
+=========+===============================+=======+=====+============+
| >       | > OTP Business Type           |       | >   | > 1 AN     |
|  111.12 |                               |       |  37 |            |
+---------+-------------------------------+-------+-----+------------+
| >       | > ID Number                   | >     | >   | > 22 AN    |
|  111.13 |                               |  61.1 |  38 |            |
|         |                               |       | -59 |            |
+---------+-------------------------------+-------+-----+------------+
| >       | > CVN Rsult Code              | >     | >   | > 1 AN     |
|  111.14 |                               |  61.2 |  60 |            |
+---------+-------------------------------+-------+-----+------------+
| >       | > PVV Result Code             | >     | >   | > 1 AN     |
|  111.15 |                               |  61.3 |  61 |            |
+---------+-------------------------------+-------+-----+------------+
| >       | > CVN2 Result Code            | > 6   | >   | > 1 AN     |
|  111.16 |                               | 1.4.3 |  62 |            |
+---------+-------------------------------+-------+-----+------------+
| >       | > ARQC Authentication Result  | >     | >   | > 1 AN     |
|  111.17 |                               |  61.5 |  63 |            |
+---------+-------------------------------+-------+-----+------------+
| >       | > Card-Holder Mobile Number   | > 6   | >   | > 20 AN    |
|  111.18 |                               | 1.6.A |  64 |            |
|         |                               | M.9.2 | -83 |            |
+---------+-------------------------------+-------+-----+------------+
| >       | > OTP Generate and Send       |       | >   | > 1 AN     |
|  111.19 | > Indicator                   |       |  84 |            |
+---------+-------------------------------+-------+-----+------------+

##### \* (Transaction Cancellation Indicator)

> This field will contain 1 char transaction cancellation indicators
> with possible values:

-   0 → Transaction is a not cancellation transaction.

-   1 → Transaction is a cancellation advice of an earlier approved
    transaction.

-   2 → Transaction is a reversal of cancellation advice.

> This indicator is only applicable for reversal 0220 and 0420
> transactions. It will indicate if a transaction is cancellation or
> cancellation reversal transaction.
>
> Union Pay has a unique functionality where they can cancel any
> previously sent ISO pre-authorization or financial message e.g. 01XX
> and 02XX.
>
> For authorization host i2c will send cancellation/cancellation
> reversal transactions with MTI 0220/0420 and 20 transaction type along
> with flag in DE- 111.8 transaction cancellation indicator and DE 111.9
> Original MTI of Cancellation Transaction.
>
> If a cancellation of 01xx transaction is received to authorization
> host than they should cancel pre- authorization and release funds, and
> for cancellations of 02xx transactions they should credit their
> respective systems.
>
> If a reversal of cancellation of 01xx transaction is received to
> authorization host than they should reacquire funds for said amount,
> and for reversal of cancellation of 02xx transactions they should
> reverse earlier credited 0220 transactions.

##### 111.3\* (Transaction Medium) {#transaction-medium .unnumbered}

> This field will contain 1 char transaction medium indicators with
> possible values:

-   0 → Unknown

-   1 → Magnetic stripe card transaction

-   2 → Chip card transaction via chip

-   3 → Magstripe transaction of chip and magstripe hybrid card

-   4 → Virtual card transaction

-   5 → QRC-based transaction

-   6 → Biological traits transaction

-   7 → Card-not-present transaction

> **NOTE**: This field is used for identification on QR Code based
> transactions. For QR code transaction transaction medium must be 5 and
> Pan Entry mode must be in 03,04,93,94.

##### OTP Generation Indicator

> This field indicates whether to generate and send generated OTP to
> card holder. Possible values:

-   0 → Do not generate or match OTP

-   1 → Generate OTP

-   2 → Match OTP

##### 111.12 OTP Business Type {#otp-business-type .unnumbered}

> This field determine business type of OTP is used in this transaction.
> Below are given values:

-   0 → No OTP present

-   1 → E-Commerce OTP

-   2 → QR Transaction OTP

-   3 → Digital Wallet Tokenization OTP (Reversed for Future)

+---------+-------------------------------+------+------+------------+
| > **Sub |                               |      |      |            |
| > E     |                               |      |      |            |
| lements |                               |      |      |            |
| > of    |                               |      |      |            |
| >       |                               |      |      |            |
|  DE-111 |                               |      |      |            |
| > when  |                               |      |      |            |
| >       |                               |      |      |            |
| DE-63.7 |                               |      |      |            |
| > =     |                               |      |      |            |
| > 'DISC |                               |      |      |            |
| OVER'** |                               |      |      |            |
+=========+===============================+======+======+============+
| > **Sub | > **Field Name**              | > ** | >    | > **Format |
| > Field |                               | Disc | **Po | >          |
| > No.** |                               | over | siti |  (ASCII)** |
|         |                               | >    | on** |            |
|         |                               |  Bit |      |            |
|         |                               | > N  |      |            |
|         |                               | o.** |      |            |
+---------+-------------------------------+------+------+------------+
| > 111.1 | > Transaction Status          | >    | > 1  | > 1 ANS    |
|         | > Indicator                   | 61.7 |      |            |
+---------+-------------------------------+------+------+------------+
| > 111.2 | > Transaction Identifier      | > 4  | >    | > 15 ANS   |
|         |                               | 8.11 | 2-16 |            |
+---------+-------------------------------+------+------+------------+
| > 111.3 | > Chargeback flag             |      | > 17 | > 1 AN     |
+---------+-------------------------------+------+------+------------+
| > 111.4 | > Stand In Trans Indicator    |      | > 18 | > 1 N      |
+---------+-------------------------------+------+------+------------+
| > 111.5 | > Transaction Unique          |      | > 1  | > 6 N      |
|         | > Identifier                  |      | 9-24 |            |
+---------+-------------------------------+------+------+------------+
| > 111.6 | > Partial                     | >    | > 25 | > 1 N      |
|         | > Authorization/Approval      | 61.2 |      |            |
|         | > Indicator                   |      |      |            |
+---------+-------------------------------+------+------+------------+
| > 111.7 | > Incremental Authorization   | >    | > 26 | > 1 N      |
|         |                               | 61.7 |      |            |
+---------+-------------------------------+------+------+------------+

##### Partial Authorization/Approval Indicator {#partial-authorizationapproval-indicator .unnumbered}

+-----+----------------------------------------------------------------+
| > * |                                                                |
| *Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| >   |                                                                |
|  2: |                                                                |
| > P |                                                                |
| art |                                                                |
| ial |                                                                |
| >   |                                                                |
|  Ap |                                                                |
| pro |                                                                |
| val |                                                                |
| >   |                                                                |
|  In |                                                                |
| dic |                                                                |
| ato |                                                                |
| r** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 0 | > Partial Approval Not Supported                               |
+-----+----------------------------------------------------------------+
| > 1 | > Partial Approval Supported: Merchandise can be partially     |
|     | > approved                                                     |
|     | >                                                              |
|     | > Cash Over can be partially approved                          |
+-----+----------------------------------------------------------------+
| > 2 | > Partial Approval Supported: Merchandise can be partially     |
|     | > approved                                                     |
|     | >                                                              |
|     | > Cash Over must be fully approved or declined                 |
+-----+----------------------------------------------------------------+
| > 3 | > Partial Approval Supported:                                  |
|     | >                                                              |
|     | > Merchandise must be fully approved or declined Cash Over can |
|     | > be partially approved                                        |
+-----+----------------------------------------------------------------+
| > 4 | > Partial Approval Supported:                                  |
|     | >                                                              |
|     | > Merchandise must be fully approved or declined Cash Over     |
|     | > must be fully approved or declined                           |
+-----+----------------------------------------------------------------+

> **Incremental Authorization:**
>
> This field indicates whether the auth is incremental one or not. If
> value in "I" then value 1 will be send to Authhost otherwise 0.

+-----+----------------------------------------------------------------+
| > * |                                                                |
| *Po |                                                                |
| sit |                                                                |
| ion |                                                                |
| >   |                                                                |
|  7: |                                                                |
| >   |                                                                |
| POS |                                                                |
| >   |                                                                |
|  Tr |                                                                |
| ans |                                                                |
| act |                                                                |
| ion |                                                                |
| >   |                                                                |
| Sta |                                                                |
| tus |                                                                |
| >   |                                                                |
|  In |                                                                |
| dic |                                                                |
| ato |                                                                |
| r** |                                                                |
+=====+================================================================+
| **  | > **Definition**                                               |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| 0   | > Normal Request (original presentment)                        |
+-----+----------------------------------------------------------------+
| 4   | > Pre-authorized Request                                       |
+-----+----------------------------------------------------------------+
| A   | > Re-authorize for Full Amount                                 |
+-----+----------------------------------------------------------------+
| D   | > Delayed Card Sale                                            |
+-----+----------------------------------------------------------------+
| E   | > Resubmission of Card Sale                                    |
+-----+----------------------------------------------------------------+
| G   | > Transit Aggregated Transaction                               |
+-----+----------------------------------------------------------------+
| I   | > Incremental Authorization                                    |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| > N | > No-Show Charge                                               |
+=====+================================================================+
| > P | > Partial Shipment                                             |
+-----+----------------------------------------------------------------+
| > R | > Recurring Payment                                            |
+-----+----------------------------------------------------------------+
| > S | > Installment Payment                                          |
+-----+----------------------------------------------------------------+
| > U | > Unscheduled Payment                                          |
+-----+----------------------------------------------------------------+

+---------+--------------------------------+------+------+------------+
| > **Sub |                                |      |      |            |
| > E     |                                |      |      |            |
| lements |                                |      |      |            |
| > of    |                                |      |      |            |
| >       |                                |      |      |            |
|  DE-111 |                                |      |      |            |
| > when  |                                |      |      |            |
| >       |                                |      |      |            |
| DE-63.7 |                                |      |      |            |
| > =     |                                |      |      |            |
| > 'FI   |                                |      |      |            |
| SERV'** |                                |      |      |            |
+=========+================================+======+======+============+
| > **Sub | > **Field Name**               | >    | >    | > **Format |
| > Field |                                | **Fi | **Po | >          |
| > No.** |                                | serv | siti |  (ASCII)** |
|         |                                | >    | on** |            |
|         |                                |  Bit |      |            |
|         |                                | > N  |      |            |
|         |                                | o.** |      |            |
+---------+--------------------------------+------+------+------------+
| > 111.1 | > Stand-In Transaction         | >    | > 1  | > 1 ANS    |
|         | > Indicator                    |  N/A |      |            |
+---------+--------------------------------+------+------+------------+
| > 111.2 | > Transaction Unique           | >    | >    | > 6 ANS    |
|         | > Identifier                   |  N/A |  2-7 |            |
+---------+--------------------------------+------+------+------------+

#### Data Element 125 - [[SUPPORTING INFORMATION]{.underline}](#de-125-supporting-information) {#data-element-125---supporting-information .unnumbered}

+------+-----+-------------+------+----------------------------------+
| > *  |     |             |      |                                  |
| *Sub |     |             |      |                                  |
| >    |     |             |      |                                  |
| Elem |     |             |      |                                  |
| ents |     |             |      |                                  |
| > of |     |             |      |                                  |
| > DE |     |             |      |                                  |
| -125 |     |             |      |                                  |
| >    |     |             |      |                                  |
| when |     |             |      |                                  |
| >    |     |             |      |                                  |
|  DE- |     |             |      |                                  |
| 63.7 |     |             |      |                                  |
| > =  |     |             |      |                                  |
| >    |     |             |      |                                  |
| 'VIS |     |             |      |                                  |
| A'** |     |             |      |                                  |
+======+=====+=============+======+==================================+
| >    | > * | > **Value** | > ** | > **Content of Sub-Element**     |
|  **T | *Le |             | Form |                                  |
| ag** | ngt |             | at** |                                  |
|      | h** |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > ** |     |             |      |                                  |
| *Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  68, |     |             |      |                                  |
| > T  |     |             |      |                                  |
| oken |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Dat |     |             |      |                                  |
| a*** |     |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > 4 | > Elapsed   | > N  | > This tag contains the elapsed  |
| 1F31 |     | > Time To   |      | > time in hours since the        |
|      |     | > Live      |      | > current limited-use key (LUK)  |
|      |     |             |      | > is provisioned on the device.  |
+------+-----+-------------+------+----------------------------------+
| >    | > 3 | > Count of  | > N  | > This tag contains the          |
| 1F32 |     | > Number of |      | > cumulative count of            |
|      |     | > T         |      | > transactions for the current   |
|      |     | ransactions |      | > limited-use key (LUK).         |
+------+-----+-------------+------+----------------------------------+
| >    | > 7 | >           | > N  | > This tag contains the          |
| 1F33 |     |  Cumulative |      | > cumulative total of            |
|      |     | >           |      | > transaction amounts in USD for |
|      |     | Transaction |      | > the current limited-use key    |
|      |     | > Amount    |      | > (LUK).                         |
+------+-----+-------------+------+----------------------------------+
| > 01 | >   | > Token     | > AN | > Ignore this tag. It is already |
|      | 13- |             |      | > included in DE 111.            |
|      | -19 |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 02 | > 2 | > Token     | > AN | > Reserved for future use. This  |
|      |     | > Assurance |      | > field contains spaces.         |
|      |     | > Level     |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 03 | >   | > Token     | > N  | > This tag contains the token    |
|      |  11 | > Requestor |      | > requestor ID.                  |
|      |     | > ID        |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 04 | >   | > Primary   | >    | > Ignore this tag. It is already |
|      |  Up | > Account   |  ANS | > included in DE 02.             |
|      | >   | > Number,   |      |                                  |
|      |  to | > Account   |      |                                  |
|      | >   | > Range     |      |                                  |
|      |  19 |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 05 | >   | > Token     | > AN | > This tag contains the token    |
|      |  Up | > Reference |      | > reference ID.                  |
|      | >   | > ID        |      |                                  |
|      |  to |             |      |                                  |
|      | >   |             |      |                                  |
|      |  32 |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 06 | > 4 | > Token     | > N  | > This tag will contain the      |
|      |     | >           |      | > token expiration date. The     |
|      |     |  Expiration |      |                                  |
+------+-----+-------------+------+----------------------------------+

+------+-----+-------------+------+----------------------------------+
|      |     | > Date      |      | > date is in yymm format, where  |
|      |     |             |      | > yy = year (00--99) and mm =    |
|      |     |             |      | > month (01--12).                |
+======+=====+=============+======+==================================+
| > 07 | > 2 | > Token     | > AN | > Ignore this tag. It is already |
|      |     | > Type      |      | > included in DE 111.            |
+------+-----+-------------+------+----------------------------------+
| > 08 | > 1 | > Token     | > AN | > Ignore this tag. It is already |
|      |     | > Status    |      | > included in DE 111.            |
+------+-----+-------------+------+----------------------------------+
| > 0A | > 1 | > Last      | > AN | > This tag is present in the     |
|      |     | > Updated   |      | > response when the token is     |
|      |     | > By        |      | > located.                       |
+------+-----+-------------+------+----------------------------------+
| > 0B | >   | > PAN       | >    | > This tag contains a unique     |
|      |  32 | > Reference |  ANS | > reference ID generated by Visa |
|      |     | > ID        |      | > for the card account number.   |
|      |     |             |      | >                                |
|      |     |             |      | > This tag is required in 0302   |
|      |     |             |      | > Token File Inquiry Messages if |
|      |     |             |      | > Field 2---Primary Account      |
|      |     |             |      | > Number is not present.         |
+------+-----+-------------+------+----------------------------------+
| > 1A | > 6 | >           | > AN | > Ignore this tag. It is already |
|      | --8 |  Activation |      | > included in DE 111.            |
|      |     | > Code      |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 1B | >   | >           | > N, | > Ignore this tag. It is already |
|      |  12 |  Activation | >    | > included in DE 111.            |
|      |     | > Code      |  BCD |                                  |
|      |     | > Expiry    |      |                                  |
|      |     | > Date/Time |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 1C | > 2 | >           | > N, | > This tag contains the number   |
|      |     |  Activation | >    | > of attempts to verify the      |
|      |     | > Code      |  BCD | > current activation code.       |
|      |     | > V         |      |                                  |
|      |     | erification |      |                                  |
|      |     | > Attempts  |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 1D | > 2 | > Number of | > N, | > This tag contains the total    |
|      |     | >           | >    | > number of token activation     |
|      |     |  Activation |  BCD | > codes issued.                  |
|      |     | > Codes     |      |                                  |
|      |     | > Issued    |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 10 | > 2 | > Visa      | > N  | > This tag contains the degree   |
|      |     | > Token     |      | > of risk associated with the    |
|      |     | > Score     |      | > token. The valid values are    |
|      |     |             |      | > from 01--99.                   |
+------+-----+-------------+------+----------------------------------+
| > 11 | > 2 | > Visa      | > AN | > This tag contains the results  |
|      |     | > Token     |      | > of the token provisioning      |
|      |     | >           |      | > decision. The valid values     |
|      |     | Decisioning |      | > are: 00 = Provision and        |
|      |     |             |      | > activate.                      |
|      |     |             |      | >                                |
|      |     |             |      | > 05 = Do not provision.         |
|      |     |             |      | >                                |
|      |     |             |      | > 85 = Provision inactive state  |
|      |     |             |      | >                                |
|      |     |             |      | > -- requires further consumer   |
|      |     |             |      | > authentication before          |
|      |     |             |      | > activation.                    |
+------+-----+-------------+------+----------------------------------+
| > 12 | > 2 | > Number of | > N  | > This tag contains the number   |
|      |     | > Active    |      | > of device tokens currently     |
|      |     | > Tokens    |      | > active for this PAN.           |
+------+-----+-------------+------+----------------------------------+
| > 13 | > 2 | > Number of | > N  | > This tag contains the number   |
|      |     | > Inactive  |      | > of device tokens currently     |
|      |     | > Tokens    |      | > inactive (device tokens that   |
|      |     |             |      | > have not been activated) for   |
|      |     |             |      | > this PAN.                      |
+------+-----+-------------+------+----------------------------------+
| > 14 | > 2 | > Number of | > N  | > This tag contains the number   |
|      |     | > Suspended |      | > of device tokens that were     |
|      |     | > Tokens    |      | > activated but are suspended    |
|      |     |             |      | > for payments for this PAN.     |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Token    | >    | > [Token activation date and     |
|  [1E | 6]{ | > Activat   | [TLV | > time in yymmddhhmmss]{.mark}   |
| ]{.m | .ma | ion]{.mark} | ]{.m | > [format expressed in           |
| ark} | rk} | > [Date/T   | ark} | > GMT.]{.mark}                   |
|      |     | ime]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+

+------+-----+--------------+----+-----------------------------------+
| >    | > [ | > [Bound     | >  | > [Index number from the Visa     |
|  [80 | 1]{ | > Device     | [T | > database where the]{.mark}      |
| ]{.m | .ma | > I          | LV | > [device ID is stored. Value can |
| ark} | rk} | ndex]{.mark} | ]{ | > be 01-63 (in]{.mark}            |
|      |     |              | .m | > [hexadecimal format). (Decimal  |
|      |     |              | ar | > 1-99).]{.mark}                  |
|      |     |              | k} |                                   |
+======+=====+==============+====+===================================+
| >    | > [ | > [Token     | >  | > [Contains unique value that     |
|  [81 | 1-1 | >            | [T | > identifies the token            |
| ]{.m | 1]{ | User]{.mark} | LV | > user.]{.mark} [Token user is an |
| ark} | .ma | > [Identi    | ]{ | > entity that initiates a         |
|      | rk} | fier]{.mark} | .m | > payment]{.mark}                 |
|      |     |              | ar | > [request.]{.mark}               |
|      |     |              | k} | >                                 |
|      |     |              |    | > [Applicable for e-commerce      |
|      |     |              |    | > transactions (device            |
|      |     |              |    | > and]{.mark} [Card-on-File token |
|      |     |              |    | > types).]{.mark}                 |
+------+-----+--------------+----+-----------------------------------+
| >    | > [ | > [Token     | >  | > [Application type of token      |
|  [82 | 1]{ | >            | [T | > user. Entities can be a]{.mark} |
| ]{.m | .ma | User]{.mark} | LV | > [merchant, a marketplace, or a  |
| ark} | rk} | >            | ]{ | > check out host.]{.mark}         |
|      |     | [Application | .m | > [Application types:]{.mark}     |
|      |     | >            | ar | >                                 |
|      |     | Type]{.mark} | k} | > [00 = Unknown]{.mark}           |
|      |     |              |    | >                                 |
|      |     |              |    | > [01 = Web]{.mark}               |
|      |     |              |    | >                                 |
|      |     |              |    | > [02 = Mobile web]{.mark}        |
|      |     |              |    | >                                 |
|      |     |              |    | > [03 = Mobile                    |
|      |     |              |    | > application]{.mark}             |
|      |     |              |    | >                                 |
|      |     |              |    | > [04 = Marketplace               |
|      |     |              |    | > application]{.mark}             |
|      |     |              |    | >                                 |
|      |     |              |    | > [05 = Voice application]{.mark} |
|      |     |              |    | >                                 |
|      |     |              |    | > [06 = Biometric                 |
|      |     |              |    | > application]{.mark} [07-FF =    |
|      |     |              |    | > Reserved]{.mark}                |
+------+-----+--------------+----+-----------------------------------+
| >    | > [ | > [T         | >  | > [Authentication factor used by  |
|  [83 | 1]{ | oken]{.mark} | [T | > token requestors and]{.mark}    |
| ]{.m | .ma | >            | LV | > [merchants to authenticate      |
| ark} | rk} |  [Authentica | ]{ | > cardholder at time of]{.mark}   |
|      |     | tion]{.mark} | .m | > [transaction.]{.mark}           |
|      |     | > [Factor    | ar | >                                 |
|      |     | > A]{.mark}  | k} | > [Applicable for e-commerce      |
|      |     |              |    | > transactions (device            |
|      |     |              |    | > and]{.mark} [Card-on-File token |
|      |     |              |    | > types).]{.mark}                 |
|      |     |              |    | >                                 |
|      |     |              |    | > [Authentication Values:]{.mark} |
|      |     |              |    | >                                 |
|      |     |              |    | > [00 = No authentication method  |
|      |     |              |    | > acquired]{.mark}                |
|      |     |              |    | >                                 |
|      |     |              |    | > [01 = Username/password]{.mark} |
|      |     |              |    | >                                 |
|      |     |              |    | > [02 = Passcode or               |
|      |     |              |    | > password]{.mark}                |
|      |     |              |    | >                                 |
|      |     |              |    | > [Consumer Device Cardholder     |
|      |     |              |    | > Verifi cation Method]{.mark}    |
|      |     |              |    | > [(CDCVM):]{.mark}               |
|      |     |              |    | >                                 |
|      |     |              |    | > [10 = Passcode]{.mark}          |
|      |     |              |    | >                                 |
|      |     |              |    | > [11 = Password]{.mark}          |
|      |     |              |    | >                                 |
|      |     |              |    | > [12 = Pattern]{.mark}           |
|      |     |              |    | >                                 |
|      |     |              |    | > [13 = Biometric                 |
|      |     |              |    | > fingerprint]{.mark}             |
|      |     |              |    | >                                 |
|      |     |              |    | > [14 = Biometric facial          |
|      |     |              |    | > recognition]{.mark}             |
|      |     |              |    | >                                 |
|      |     |              |    | > [15 = Biometric iris            |
|      |     |              |    | > recognition]{.mark}             |
|      |     |              |    | >                                 |
|      |     |              |    | > [16 = Biometric voice           |
|      |     |              |    | > recognition]{.mark}             |
|      |     |              |    | >                                 |
|      |     |              |    | > [17 = Behavioral                |
|      |     |              |    | > biometric]{.mark} [One Time     |
|      |     |              |    | > Passcode (OTP):]{.mark}         |
|      |     |              |    | >                                 |
|      |     |              |    | > [18 = Device unlocked (CDCVM    |
|      |     |              |    | > unknown)]{.mark}                |
|      |     |              |    | >                                 |
|      |     |              |    | > [30 = Short message system      |
|      |     |              |    | > (SMS)]{.mark}                   |
|      |     |              |    | >                                 |
|      |     |              |    | > [31 = Email]{.mark}             |
|      |     |              |    | >                                 |
|      |     |              |    | > [32 = Hardware token without    |
|      |     |              |    | > user verification]{.mark}       |
+------+-----+--------------+----+-----------------------------------+

+------+----+-------------+------+-----------------------------------+
|      |    |             |      | > [33 = Hardware token with user  |
|      |    |             |      | > verifi cation]{.mark}           |
|      |    |             |      | >                                 |
|      |    |             |      | > [34 = Soft token]{.mark}        |
|      |    |             |      | >                                 |
|      |    |             |      | > [35 = Any other method]{.mark}  |
|      |    |             |      | >                                 |
|      |    |             |      | > [40 = Knowledge based           |
|      |    |             |      | > authentication]{.mark}          |
|      |    |             |      | >                                 |
|      |    |             |      | > [41 = Out of band (OOB)         |
|      |    |             |      | > authentication]{.mark}          |
|      |    |             |      | >                                 |
|      |    |             |      | > [42 = Local                     |
|      |    |             |      | > authentication]{.mark} [Fast    |
|      |    |             |      | > Identity Online (FIDO):]{.mark} |
|      |    |             |      | >                                 |
|      |    |             |      | > [50 = Possession only. No user  |
|      |    |             |      | > verifi cation.]{.mark}          |
|      |    |             |      | >                                 |
|      |    |             |      | > [51 = With user verification    |
|      |    |             |      | > (biometric)]{.mark}             |
|      |    |             |      | >                                 |
|      |    |             |      | > [52 = With user verification    |
|      |    |             |      | > (passcode/password)]{.mark} [60 |
|      |    |             |      | > = SE based token: cryptogram    |
|      |    |             |      | > generated from a]{.mark} [SE    |
|      |    |             |      | > device for a davice-bound token |
|      |    |             |      | > was provided,]{.mark}           |
|      |    |             |      | > [establishes possession         |
|      |    |             |      | > factor.]{.mark}                 |
|      |    |             |      | >                                 |
|      |    |             |      | > [61 = Device bound token:       |
|      |    |             |      | > device bound token              |
|      |    |             |      | > (token]{.mark} [reference) was  |
|      |    |             |      | > provided by token requestor     |
|      |    |             |      | > along]{.mark} [with proof of    |
|      |    |             |      | > device used for binding         |
|      |    |             |      | > token,]{.mark} [establishes     |
|      |    |             |      | > possession factor.]{.mark}      |
|      |    |             |      | >                                 |
|      |    |             |      | > [In Europe, token user          |
|      |    |             |      | > identifier may be used          |
|      |    |             |      | > to]{.mark} [support dynamic     |
|      |    |             |      | > linking requirements of         |
|      |    |             |      | > PSD2/RTS.]{.mark}               |
+======+====+=============+======+===================================+
| >    | >  | > [To       | >    | > [Authentication factor used by  |
|  [84 | [1 | ken]{.mark} | [TLV | > token requestors and]{.mark}    |
| ]{.m | ]{ | > [         | ]{.m | > [merchants to authenticate      |
| ark} | .m | Authenticat | ark} | > cardholder at time of]{.mark}   |
|      | ar | ion]{.mark} |      | > [transaction.]{.mark}           |
|      | k} | > [Factor   |      | >                                 |
|      |    | > B]{.mark} |      | > [Applicable for e-commerce      |
|      |    |             |      | > transactions (device            |
|      |    |             |      | > and]{.mark} [Card-on-File token |
|      |    |             |      | > types).]{.mark}                 |
|      |    |             |      | >                                 |
|      |    |             |      | > [Authentication Values:]{.mark} |
|      |    |             |      | >                                 |
|      |    |             |      | > [00 = No authentication method  |
|      |    |             |      | > acquired]{.mark}                |
|      |    |             |      | >                                 |
|      |    |             |      | > [01 = Username/password]{.mark} |
|      |    |             |      | >                                 |
|      |    |             |      | > [02 = Passcode or               |
|      |    |             |      | > password]{.mark}                |
|      |    |             |      | >                                 |
|      |    |             |      | > [Consumer Device Cardholder     |
|      |    |             |      | > Verifi cation Method]{.mark}    |
|      |    |             |      | > [(CDCVM):]{.mark}               |
|      |    |             |      | >                                 |
|      |    |             |      | > [10 = Passcode]{.mark}          |
|      |    |             |      | >                                 |
|      |    |             |      | > [11 = Password]{.mark}          |
|      |    |             |      | >                                 |
|      |    |             |      | > [12 = Pattern]{.mark}           |
|      |    |             |      | >                                 |
|      |    |             |      | > [13 = Biometric                 |
|      |    |             |      | > fingerprint]{.mark}             |
|      |    |             |      | >                                 |
|      |    |             |      | > [14 = Biometric facial          |
|      |    |             |      | > recognition]{.mark}             |
|      |    |             |      | >                                 |
|      |    |             |      | > [15 = Biometric iris            |
|      |    |             |      | > recognition]{.mark}             |
|      |    |             |      | >                                 |
|      |    |             |      | > [16 = Biometric voice           |
|      |    |             |      | > recognition]{.mark}             |
|      |    |             |      | >                                 |
|      |    |             |      | > [17 = Behavioral                |
|      |    |             |      | > biometric]{.mark} [One Time     |
|      |    |             |      | > Passcode (OTP):]{.mark}         |
|      |    |             |      | >                                 |
|      |    |             |      | > [18 = Device unlocked (CDCVM    |
|      |    |             |      | > unknown)]{.mark}                |
|      |    |             |      | >                                 |
|      |    |             |      | > [30 = Short message system      |
|      |    |             |      | > (SMS)]{.mark}                   |
|      |    |             |      | >                                 |
|      |    |             |      | > [31 = Email]{.mark}             |
|      |    |             |      | >                                 |
|      |    |             |      | > [32 = Hardware token without    |
|      |    |             |      | > user verification]{.mark}       |
|      |    |             |      | >                                 |
|      |    |             |      | > [33 = Hardware token with user  |
|      |    |             |      | > verifi cation]{.mark}           |
|      |    |             |      | >                                 |
|      |    |             |      | > [34 = Soft token]{.mark}        |
+------+----+-------------+------+-----------------------------------+

+-----+------+-------------+-----+-----------------------------------+
|     |      |             |     | > [35 = Any other method]{.mark}  |
|     |      |             |     | >                                 |
|     |      |             |     | > [40 = Knowledge based           |
|     |      |             |     | > authentication]{.mark}          |
|     |      |             |     | >                                 |
|     |      |             |     | > [41 = Out of band (OOB)         |
|     |      |             |     | > authentication]{.mark}          |
|     |      |             |     | >                                 |
|     |      |             |     | > [42 = Local                     |
|     |      |             |     | > authentication]{.mark} [Fast    |
|     |      |             |     | > Identity Online (FIDO):]{.mark} |
|     |      |             |     | >                                 |
|     |      |             |     | > [50 = Possession only. No user  |
|     |      |             |     | > verifi cation.]{.mark}          |
|     |      |             |     | >                                 |
|     |      |             |     | > [51 = With user verification    |
|     |      |             |     | > (biometric)]{.mark}             |
|     |      |             |     | >                                 |
|     |      |             |     | > [52 = With user verification    |
|     |      |             |     | > (passcode/password)]{.mark} [60 |
|     |      |             |     | > = SE based token: cryptogram    |
|     |      |             |     | > generated from a]{.mark} [SE    |
|     |      |             |     | > device for a davice-bound token |
|     |      |             |     | > was provided,]{.mark}           |
|     |      |             |     | > [establishes possession         |
|     |      |             |     | > factor.]{.mark}                 |
|     |      |             |     | >                                 |
|     |      |             |     | > [61 = Device bound token:       |
|     |      |             |     | > device bound token              |
|     |      |             |     | > (token]{.mark} [reference) was  |
|     |      |             |     | > provided by token requestor     |
|     |      |             |     | > along]{.mark} [with proof of    |
|     |      |             |     | > device used for binding         |
|     |      |             |     | > token,]{.mark} [establishes     |
|     |      |             |     | > possession factor.]{.mark}      |
|     |      |             |     | >                                 |
|     |      |             |     | > [In Europe, token user          |
|     |      |             |     | > identifier may be used          |
|     |      |             |     | > to]{.mark} [support dynamic     |
|     |      |             |     | > linking requirements of         |
|     |      |             |     | > PSD2/RTS.]{.mark}               |
+=====+======+=============+=====+===================================+
| [8  | > [3 | > [To       | [TL | > [Payment amount made visible by |
| 5]{ | ]{.m | ken]{.mark} | V]{ | > the token]{.mark} [requestor to |
| .ma | ark} | > [         | .ma | > consumer at time of             |
| rk} |      | Authenticat | rk} | > purchase.]{.mark} [Applicable   |
|     |      | ion]{.mark} |     | > for e-commerce transactions     |
|     |      | > [Amo      |     | > (device and]{.mark}             |
|     |      | unt]{.mark} |     | > [Card-on-File token             |
|     |      |             |     | > types).]{.mark}                 |
|     |      |             |     | >                                 |
|     |      |             |     | > [In Europe, token user          |
|     |      |             |     | > identifier may be used          |
|     |      |             |     | > to]{.mark} [support dynamic     |
|     |      |             |     | > linking requirements of         |
|     |      |             |     | > PSD2/RTS.]{.mark}               |
+-----+------+-------------+-----+-----------------------------------+
| [8  | > [6 | > [Token    | [TL | > [Unique value that identifies   |
| 6]{ | ]{.m | > requestor | V]{ | > the service provider for        |
| .ma | ark} | >           | .ma | > a]{.mark} [token requestor. A   |
| rk} |      |  --]{.mark} | rk} | > token service provider is       |
|     |      | > [token    |     | > the]{.mark} [integration        |
|     |      | > serv      |     | > partner for token requestors    |
|     |      | ice]{.mark} |     | > for]{.mark} [provisioning and   |
|     |      | > [provider |     | > cryptogram requests.]{.mark}    |
|     |      | >           |     | >                                 |
|     |      |  ID]{.mark} |     | > [Applicable for e-commerce and  |
|     |      |             |     | > Card-on-File]{.mark}            |
|     |      |             |     | > [transactions.]{.mark}          |
+-----+------+-------------+-----+-----------------------------------+
| > * |      |             |     |                                   |
| **D |      |             |     |                                   |
| ata |      |             |     |                                   |
| set |      |             |     |                                   |
| >   |      |             |     |                                   |
| ID: |      |             |     |                                   |
| >   |      |             |     |                                   |
| 01, |      |             |     |                                   |
| >   |      |             |     |                                   |
|  To |      |             |     |                                   |
| ken |      |             |     |                                   |
| >   |      |             |     |                                   |
| Dev |      |             |     |                                   |
| ice |      |             |     |                                   |
| *** |      |             |     |                                   |
+-----+------+-------------+-----+-----------------------------------+
| [0  | > [2 | > [Device   | [TL | > [Ignore this tag. It is already |
| 1]{ | ]{.m | > T         | V]{ | > included in DE 111.]{.mark}     |
| .ma | ark} | ype]{.mark} | .ma |                                   |
| rk} |      |             | rk} |                                   |
+-----+------+-------------+-----+-----------------------------------+
| [0  | > [3 | > [Device   | [TL | > [This tag contains a            |
| 2]{ | ]{.m | > Langu     | V]{ | > three-character language        |
| .ma | ark} | age]{.mark} | .ma | > code]{.mark} [that conforms     |
| rk} |      | > [C        | rk} | > with ISO 639 standards.]{.mark} |
|     |      | ode]{.mark} |     | >                                 |
|     |      |             |     | > [An example would be eng        |
|     |      |             |     | > (English).]{.mark}              |
+-----+------+-------------+-----+-----------------------------------+
| [0  | >    | > [Device   | [TL | > [Ignore this tag. It is already |
| 3]{ |  [Up | >           | V]{ | > included in DE 111.]{.mark}     |
| .ma | > to |  ID]{.mark} | .ma |                                   |
| rk} | > 48 |             | rk} |                                   |
|     | ]{.m |             |     |                                   |
|     | ark} |             |     |                                   |
+-----+------+-------------+-----+-----------------------------------+
| [0  | >    | > [Device   | [TL | > [Ignore this tag. It is already |
| 4]{ |  [Up | > Num       | V]{ | > included in DE 111.]{.mark}     |
| .ma | > to | ber]{.mark} | .ma |                                   |
| rk} | > 15 |             | rk} |                                   |
|     | ]{.m |             |     |                                   |
|     | ark} |             |     |                                   |
+-----+------+-------------+-----+-----------------------------------+
| [0  | >    | > [Device   | [TL | > [Ignore this tag. It is already |
| 5]{ |  [16 | > N         | V]{ | > included in DE 111.]{.mark}     |
| .ma | ]{.m | ame]{.mark} | .ma |                                   |
| rk} | ark} |             | rk} |                                   |
+-----+------+-------------+-----+-----------------------------------+
| [0  | >    | > [Device   | [TL | > [This tag contains the          |
| 6]{ |  [Up | > Locat     | V]{ | > obfuscated geographic           |
| .ma | > to | ion]{.mark} | .ma | > location]{.mark} [of the device |
| rk} | > 25 |             | rk} | > or the coarse location of the   |
|     | ]{.m |             |     | > device.]{.mark}                 |
|     | ark} |             |     | >                                 |
|     |      |             |     | > [Location is latitude/longitude |
|     |      |             |     | > with up to 4 digits of]{.mark}  |
|     |      |             |     | > [precision; for                 |
|     |      |             |     | > instance]{.mark}                |
|     |      |             |     | >                                 |
|     |      |             |     | > [+37.7799/-122.4290. Precision  |
|     |      |             |     | > is rounded off to a]{.mark}     |
+-----+------+-------------+-----+-----------------------------------+

+------+-----+-------------+------+----------------------------------+---+
| >    |     |             |      | > [less granular level e.g.      |   |
|  [07 |     |             |      | > +37/-122 or                    |   |
| ]{.m |     |             |      | > +37.78/-122.43.]{.mark}        |   |
| ark} |     |             |      |                                  |   |
+======+=====+=============+======+==================================+===+
|      | >   | > [IP       | >    | > [This tag contains the IP      |   |
|      |  [1 | > Addr      | [TLV | > address of the device at       |   |
|      | 5]{ | ess]{.mark} | ]{.m | > the]{.mark} [time of the       |   |
|      | .ma |             | ark} | > provisioning request.]{.mark}  |   |
|      | rk} |             |      | >                                |   |
|      |     |             |      | > [The value will be in the      |   |
|      |     |             |      | > format:                        |   |
|      |     |             |      | > 255.255.255.255.]{.mark} [Each |   |
|      |     |             |      | > octet (255)]{.mark}            |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > [may be 1--3 digits in         |   |
|      |     |             |      | > length.]{.mark}                |   |
+------+-----+-------------+------+----------------------------------+---+
| > ** |     |             |      |                                  |   |
| *Dat |     |             |      |                                  |   |
| aset |     |             |      |                                  |   |
| >    |     |             |      |                                  |   |
|  ID: |     |             |      |                                  |   |
| >    |     |             |      |                                  |   |
|  02, |     |             |      |                                  |   |
| > Wa |     |             |      |                                  |   |
| llet |     |             |      |                                  |   |
| >    |     |             |      |                                  |   |
|  Pro |     |             |      |                                  |   |
| vide |     |             |      |                                  |   |
| r*** |     |             |      |                                  |   |
+------+-----+-------------+------+----------------------------------+---+
| > 03 | > 1 | > Wallet    | >    | > This tag contains one of the   |   |
|      |     | > Provider  |  TLV | > following valid values:        |   |
|      |     | > Risk      |      | >                                |   |
|      |     | >           |      | > 0 = Unconditionally approved.  |   |
|      |     |  Assessment |      | >                                |   |
|      |     |             |      | > 1 = Conditionally approved     |   |
|      |     |             |      | > with further verification.     |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > 2 = Not approved.              |   |
+------+-----+-------------+------+----------------------------------+---+
| > 04 | >   | > Wallet    | >    | > This tag contains the Wallet   |   |
|      |  10 | > Provider  |  TLV | > Provider Risk Assessment       |   |
|      |     | > Risk      |      | > Version.                       |   |
|      |     | >           |      |                                  |   |
|      |     |  Assessment |      |                                  |   |
|      |     | > Version   |      |                                  |   |
+------+-----+-------------+------+----------------------------------+---+
| > 05 | > 2 | > Wallet    | >    | > This tag contains the value of |   |
|      |     | > Provider  |  TLV | > 1--5, with 5 being the most    |   |
|      |     | > Device    |      | > trusted.                       |   |
|      |     | > Score     |      |                                  |   |
+------+-----+-------------+------+----------------------------------+---+
| > 06 | > 2 | > Wallet    | >    | > This tag contains the value of |   |
|      |     | > Provider  |  TLV | > 1--5, with 5 being the most    |   |
|      |     | > Account   |      | > trusted.                       |   |
|      |     | > Score     |      |                                  |   |
+------+-----+-------------+------+----------------------------------+---+
| > 07 | >   | > Wallet    | >    | > This tag contains up to 15     |   |
|      |  30 | > Provider  |  TLV | > reason codes of 2 bytes each.  |   |
|      |     | > Reason    |      | > The valid values are:          |   |
|      |     | > Codes     |      | >                                |   |
|      |     |             |      | > **01** = Cardholders' wallet   |   |
|      |     |             |      | > account is too new relative to |   |
|      |     |             |      | > launch.                        |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > **02** = Cardholders' wallet   |   |
|      |     |             |      | > account is too new relative to |   |
|      |     |             |      | > provisioning request.          |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > **03** = Cardholders' wallet   |   |
|      |     |             |      | > account/card pair is newer     |   |
|      |     |             |      | > than date threshold.           |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > **04** = Changes made to       |   |
|      |     |             |      | > account data within the date   |   |
|      |     |             |      | > threshold.                     |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > **05** = Suspicious            |   |
|      |     |             |      | > transactions linked to this    |   |
|      |     |             |      | > account. **06** = Account has  |   |
|      |     |             |      | > not had activity in the last   |   |
|      |     |             |      | > year. **07** = Suspended cards |   |
|      |     |             |      | > in the secure element.         |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > **08** = Device was put in     |   |
|      |     |             |      | > lost mode in the last 7 days   |   |
|      |     |             |      | > for longer than the duration   |   |
|      |     |             |      | > threshold.                     |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > **09** = The number of         |   |
|      |     |             |      | > provisioning attempts on this  |   |
|      |     |             |      | > device in 24 hours exceeds     |   |
|      |     |             |      | > threshold.                     |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > **0A** = There have been more  |   |
|      |     |             |      | > than the threshold number of   |   |
|      |     |             |      | > different cards attempted at   |   |
|      |     |             |      | > provisioning to this phone in  |   |
|      |     |             |      | > 24 hours.                      |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > **0B** = The card provisioning |   |
|      |     |             |      | > request contains a distinct    |   |
|      |     |             |      | > name in excess of the          |   |
|      |     |             |      | > permitted threshold. **0C** =  |   |
|      |     |             |      | > The device score is less than  |   |
|      |     |             |      | > 3.                             |   |
|      |     |             |      | >                                |   |
|      |     |             |      | > **0D** = The account score is  |   |
|      |     |             |      | > less than 4.                   |   |
+------+-----+-------------+------+----------------------------------+---+

+------+-----+-------------+------+----------------------------------+
|      |     |             |      | > **0E** = Device provisioning   |
|      |     |             |      | > location outside of the        |
|      |     |             |      | > cardholder's wallet account    |
|      |     |             |      | > home country.                  |
|      |     |             |      | >                                |
|      |     |             |      | > **0G** = Suspect fraud.        |
+======+=====+=============+======+==================================+
| > 08 | > 2 | > PAN       | >    | > This tag contains one of the   |
|      |     | > Source    |  TLV | > following valid values:        |
|      |     |             |      | >                                |
|      |     |             |      | > **01** = Key-entered.          |
|      |     |             |      | >                                |
|      |     |             |      | > **02** = On file.              |
|      |     |             |      | >                                |
|      |     |             |      | > **03** = Mobile banking app.   |
+------+-----+-------------+------+----------------------------------+
| > 09 | >   | > Wallet    | >    | > This tag contains the Wallet   |
|      |  32 | > Account   |  TLV | > Account ID.                    |
|      |     | > ID        |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 0A | >   | > Wallet    | >    | > This tag contains the Wallet   |
|      |  Up | > Account   |  TLV | > Account E-mail Address.        |
|      | >   | > E- mail   |      |                                  |
|      |  to | > Address   |      |                                  |
|      | >   |             |      |                                  |
|      |  32 |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > ** |     |             |      |                                  |
| *Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  40, |     |             |      |                                  |
| > T  |     |             |      |                                  |
| erms |     |             |      |                                  |
| >    |     |             |      |                                  |
|  and |     |             |      |                                  |
| > C  |     |             |      |                                  |
| ondi |     |             |      |                                  |
| tion |     |             |      |                                  |
| s*** |     |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 01 | >   | > Terms and | > AN | > This field contains the terms  |
|      |  64 | >           |      | > and conditions data when field |
|      |     |  Conditions |      | > 63.3 contains message reason   |
|      |     | > V         |      | > code 3700.                     |
|      |     | erification |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 02 | >   | > Issuer    | > AN | > This field contains the date   |
|      |  32 | > Terms and |      | > and time.                      |
|      |     | >           |      |                                  |
|      |     |  Conditions |      |                                  |
|      |     | > Date/Time |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > ** |     |             |      |                                  |
| *Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  58, |     |             |      |                                  |
| >    |     |             |      |                                  |
| Orig |     |             |      |                                  |
| inal |     |             |      |                                  |
| > T  |     |             |      |                                  |
| oken |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Dat |     |             |      |                                  |
| a*** |     |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 80 | >   | > Original  | > AN | > This field contains the        |
|      |  13 | > Token     |      | > original token number used for |
|      | -19 |             |      | > provisioning of a new token.   |
+------+-----+-------------+------+----------------------------------+
| > 81 | > 2 | > Original  | > AN | > This field contains the        |
|      |     | > Token     |      | > Assurance Level of original    |
|      |     | > Assurance |      | > token.                         |
|      |     | > Level     |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 82 | >   | > Original  | > N  | > This field contains the        |
|      |  11 | > Token     |      | > original token Requestor ID.   |
|      |     | > Requestor |      |                                  |
|      |     | > ID        |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 83 | > U | > Original  | > AN | > This field contains the        |
|      | pto | > Token Ref |      | > original token ref ID.         |
|      | >   | > ID        |      |                                  |
|      |  32 |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > 84 | > 2 | > Original  | > AN | > This field will contain the    |
|      |     | > Token     |      | > token type of the source token |
|      |     | > Type      |      | > used for provisioning a new    |
|      |     |             |      | > token.                         |
|      |     |             |      | >                                |
|      |     |             |      | > Valid values are:              |
|      |     |             |      |                                  |
|      |     |             |      | -   01 (ECOM/COF                 |
|      |     |             |      |     > (e-commerce/card on file)) |
|      |     |             |      |                                  |
|      |     |             |      | -   02 (SE (secure element))     |
|      |     |             |      |                                  |
|      |     |             |      | -   03 (CBP (cloud-based         |
|      |     |             |      |     > payment))                  |
|      |     |             |      |                                  |
|      |     |             |      | -   05 (E-commerce enabler)      |
+------+-----+-------------+------+----------------------------------+
| > 85 | > 2 | > Original  | > AN | > This field will contain the    |
|      |     | > Device    |      | > device type of the source      |
|      |     | > Type      |      | > token used for provisioning a  |
|      |     |             |      | > new token.                     |
|      |     |             |      | >                                |
|      |     |             |      | > Valid values are:              |
|      |     |             |      |                                  |
|      |     |             |      | -   00 (Unknown)                 |
|      |     |             |      |                                  |
|      |     |             |      | -   01 (Mobile phone)            |
|      |     |             |      |                                  |
|      |     |             |      | -   02 (Tablet)                  |
|      |     |             |      |                                  |
|      |     |             |      | -   03 (Watch)                   |
+------+-----+-------------+------+----------------------------------+

+------+-----+-------------+------+----------------------------------+
|      |     |             |      | -   04 (Mobile phone or tablet)  |
|      |     |             |      |                                  |
|      |     |             |      | -   05 (Personal computer)       |
|      |     |             |      |                                  |
|      |     |             |      | -   06 (Household device)        |
|      |     |             |      |                                  |
|      |     |             |      | -   07 (Wearable device)         |
|      |     |             |      |                                  |
|      |     |             |      | -   08 (Automobile device)       |
+======+=====+=============+======+==================================+
| > 86 | > U | > Original  | >    | > This field will contain the    |
|      | pto | > Device ID |  ANS | > device ID of the source token  |
|      | >   |             |      | > used for provisioning a new    |
|      |  48 |             |      | > token.                         |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [PAN      | >    | > [This tag contains the PAN     |
|  [01 | 3]{ | > Issued    | [TLV | > Issued Date.]{.mark}           |
| ]{.m | .ma | > D         | ]{.m |                                  |
| ark} | rk} | ate]{.mark} | ark} |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [PAN      | >    | > [This tag contains the date of |
|  [02 | 3]{ | > Activat   | [TLV | > activation of the              |
| ]{.m | .ma | ion]{.mark} | ]{.m | > card.]{.mark}                  |
| ark} | rk} | > [D        | ark} |                                  |
|      |     | ate]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    |     |             |      |                                  |
|  *** |     |             |      |                                  |
| [Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  67, |     |             |      |                                  |
| > T  |     |             |      |                                  |
| oken |     |             |      |                                  |
| >    |     |             |      |                                  |
| Veri |     |             |      |                                  |
| fica |     |             |      |                                  |
| tion |     |             |      |                                  |
| > Re |     |             |      |                                  |
| sult |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Cod |     |             |      |                                  |
| e]{. |     |             |      |                                  |
| mark |     |             |      |                                  |
| }*** |     |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Token    | >    | -   [1 = TAVV cryptogram failed  |
|  [08 | 1]{ | > Verificat | [TLV |     > validation]{.mark}         |
| ]{.m | .ma | ion]{.mark} | ]{.m |                                  |
| ark} | rk} | > [Result   | ark} | -   [2 = TAVV cryptogram passed  |
|      |     | > C         |      |     > validation]{.mark}         |
|      |     | ode]{.mark} |      |                                  |
|      |     |             |      | -   [3 = DTVV or Visa-defined    |
|      |     |             |      |     > format cryptogram]{.mark}  |
|      |     |             |      |     > [passed validation]{.mark} |
|      |     |             |      |                                  |
|      |     |             |      | -   [4 = DTVV or Visa-defined    |
|      |     |             |      |     > format cryptogram]{.mark}  |
|      |     |             |      |     > [passed validation]{.mark} |
|      |     |             |      |                                  |
|      |     |             |      | > [The TAVV-only cryptogram      |
|      |     |             |      | > option is]{.mark} [applicable  |
|      |     |             |      | > for token transactions         |
|      |     |             |      | > without]{.mark} [3DS           |
|      |     |             |      | > data]{.mark}                   |
+------+-----+-------------+------+----------------------------------+
| > ** |     |             |      |                                  |
| [Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  41, |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Rep |     |             |      |                                  |
| lace |     |             |      |                                  |
| ment |     |             |      |                                  |
| >    |     |             |      |                                  |
|  PAN |     |             |      |                                  |
| > Da |     |             |      |                                  |
| ta]{ |     |             |      |                                  |
| .mar |     |             |      |                                  |
| k}** |     |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [         | >    | > [This field is required when   |
|  [01 |  [1 | Replacement | [TLV | > the PAN contained in]{.mark}   |
| ]{.m | 3-1 | >           | ]{.m | > [Field 2---Primary Account     |
| ark} | 9]{ | PAN]{.mark} | ark} | > Number is being                |
|      | .ma |             |      | > replaced]{.mark} [with a new   |
|      | rk} |             |      | > PAN.]{.mark}                   |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [         | >    | > [This field contains the       |
|  [02 | 4]{ | Replacement | [TLV | > expiration date of the         |
| ]{.m | .ma | >           | ]{.m | > new]{.mark} [PAN in tag 01 or  |
| ark} | rk} | PAN]{.mark} | ark} | > updatedexpiration date of      |
|      |     | >           |      | > the]{.mark}                    |
|      |     | [Expiration |      | >                                |
|      |     | > D         |      | > [existing PAN. Format =        |
|      |     | ate]{.mark} |      | > yymm.]{.mark}                  |
+------+-----+-------------+------+----------------------------------+
| > *  |     |             |      |                                  |
| *Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  56, |     |             |      |                                  |
| > De |     |             |      |                                  |
| vice |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Par |     |             |      |                                  |
| amet |     |             |      |                                  |
| er** |     |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [Device   | >    | > [This tag will contain the     |
|  [01 |  [2 | > I         | [TLV | > hardware ID of the             |
| ]{.m | 4]{ | MEI]{.mark} | ]{.m | > device.]{.mark} [NOTE]{.mark}  |
| ark} | .ma |             | ark} | >                                |
|      | rk} |             |      | > [This field will be included   |
|      |     |             |      | > in the 0600 Token]{.mark}      |
|      |     |             |      | > [notification online request   |
|      |     |             |      | > message when]{.mark}           |
|      |     |             |      | >                                |
|      |     |             |      | > [Field 63.3---Message Reason   |
|      |     |             |      | > Code contains the]{.mark}      |
|      |     |             |      | >                                |
|      |     |             |      | > [value of 3700 (Token          |
|      |     |             |      | > create).]{.mark}               |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [OS       | >    | > [This tag contains the ID of   |
|  [02 | 1]{ | >           | [TLV | > Operating System               |
| ]{.m | .ma |  ID]{.mark} | ]{.m | > during]{.mark}                 |
| ark} | rk} |             | ark} | > [Provisioning.]{.mark}         |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | >           | >    | > [This tag will contain the     |
|  [03 | 1]{ |  [Provision | [TLV | > number of provisioning]{.mark} |
| ]{.m | .ma | ing]{.mark} | ]{.m | > [attempts on the device within |
| ark} | rk} | > [attempts | ark} | > the last 24 hours.]{.mark}     |
|      |     | > on        |      |                                  |
|      |     | >           |      |                                  |
|      |     | the]{.mark} |      |                                  |
|      |     | > [dev      |      |                                  |
|      |     | ice]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Acc      | >    | > [This tag will contain the     |
|  [04 | 1]{ | ount-To-Dev | [TLV | > number of days the             |
| ]{.m | .ma | ice]{.mark} | ]{.m | > device]{.mark}                 |
| ark} | rk} |             | ark} |                                  |
+------+-----+-------------+------+----------------------------------+

+------+-----+-------------+------+----------------------------------+
| > *  |     |             |      |                                  |
| *Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  57, |     |             |      |                                  |
| > Wa |     |             |      |                                  |
| llet |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Par |     |             |      |                                  |
| amet |     |             |      |                                  |
| er** |     |             |      |                                  |
+======+=====+=============+======+==================================+
| >    | > [ | > [Wallet   | >    | > [This tag will contain the     |
|  [01 | 2]{ | > Provi     | [TLV | > number of days that            |
| ]{.m | .ma | der]{.mark} | ]{.m | > the]{.mark} [user's PAN has    |
| ark} | rk} | > [PAN      | ark} | > been on file for the           |
|      |     | >           |      | > user.]{.mark}                  |
|      |     | Age]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | [User       | >    | > [This tag will contain the     |
|  [02 | 2]{ | Account     | [TLV | > number of days since           |
| ]{.m | .ma | Age]{.mark} | ]{.m | > the]{.mark} [user account for  |
| ark} | rk} |             | ark} | > this user exists.]{.mark}      |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | [Wallet     | >    | > [This tag will contain the     |
|  [03 | 2]{ | Account     | [TLV | > number of days since           |
| ]{.m | .ma | Age]{.mark} | ]{.m | > the]{.mark}                    |
| ark} | rk} |             | ark} | >                                |
|      |     |             |      | > [user created the wallet       |
|      |     |             |      | > account or started             |
|      |     |             |      | > using]{.mark} [the             |
|      |     |             |      | > account.]{.mark}               |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Days     | >    | > [This tag will contain the     |
|  [04 | 2]{ | > Since     | [TLV | > number of days since           |
| ]{.m | .ma | > L         | ]{.m | > the]{.mark} [last activity on  |
| ark} | rk} | ast]{.mark} | ark} | > the account.]{.mark}           |
|      |     | > [Activ    |      |                                  |
|      |     | ity]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Number   | >    | > [This tag will contain the     |
|  [05 | 2]{ | >           | [TLV | > number of transactions         |
| ]{.m | .ma |  Of]{.mark} | ]{.m | > on]{.mark} [this account       |
| ark} | rk} | > [Tr       | ark} | > within the last 12             |
|      |     | ansactions, |      | > months.]{.mark}                |
|      |     | > L         |      |                                  |
|      |     | ast]{.mark} |      |                                  |
|      |     | > [12       |      |                                  |
|      |     | > mon       |      |                                  |
|      |     | ths]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Days     | >    | > [This tag will contain the     |
|  [06 | 2]{ | > Since     | [TLV | > number of days since]{.mark}   |
| ]{.m | .ma | > L         | ]{.m | > [account settings were         |
| ark} | rk} | ast]{.mark} | ark} | > changed.]{.mark}               |
|      |     | > [Account  |      |                                  |
|      |     | > Cha       |      |                                  |
|      |     | nge]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | >           | >    | > [This tag will contain the     |
|  [07 | 1]{ |  [Suspended | [TLV | > number of cards                |
| ]{.m | .ma | > Ca        | ]{.m | > suspended]{.mark} [on the      |
| ark} | rk} | rds]{.mark} | ark} | > account]{.mark}                |
|      |     | > [in       |      |                                  |
|      |     | > Acco      |      |                                  |
|      |     | unt]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Wallet   | >    | > [This tag will contain the     |
|  [08 | 2]{ | > Acco      | [TLV | > two-character alpha            |
| ]{.m | .ma | unt]{.mark} | ]{.m | > ISO]{.mark} [country code of   |
| ark} | rk} | > [Coun     | ark} | > the account holder]{.mark}     |
|      |     | try]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Number   | >    | > [This tag will contain the     |
|  [09 | 1]{ | > Of        | [TLV | > number of active               |
| ]{.m | .ma | > Act       | ]{.m | > tokens]{.mark}                 |
| ark} | rk} | ive]{.mark} | ark} | >                                |
|      |     | > [Tok      |      | > [on this account]{.mark}       |
|      |     | ens]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Number   | >    | > [This tag will contain the     |
|  [0A | 1]{ | > Of        | [TLV | > number of devices for          |
| ]{.m | .ma | > Devi      | ]{.m | > this]{.mark} [user with the    |
| ark} | rk} | ces]{.mark} | ark} | > same token.]{.mark}            |
|      |     | > [With     |      |                                  |
|      |     | > Active    |      |                                  |
|      |     | > To        |      |                                  |
|      |     | ken]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Number   | >    | > [This tag will contain the     |
|  [0B | 1]{ | > Of        | [TLV | > number of active               |
| ]{.m | .ma | > Act       | ]{.m | > tokens]{.mark} [for this user  |
| ark} | rk} | ive]{.mark} | ark} | > across all devices]{.mark}     |
|      |     | > [Tokens   |      |                                  |
|      |     | > on        |      |                                  |
|      |     | >           |      |                                  |
|      |     | All]{.mark} |      |                                  |
|      |     | > [Devi     |      |                                  |
|      |     | ces]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Consumer | >    | > [This tag will indicate how    |
|  [0C | 1]{ | > En        | [TLV | > the card information           |
| ]{.m | .ma | try]{.mark} | ]{.m | > was]{.mark} [entered on the    |
| ark} | rk} | > [M        | ark} | > device. Valid values           |
|      |     | ode]{.mark} |      | > are:]{.mark}                   |
|      |     |             |      |                                  |
|      |     |             |      | -   [1 (Key-entered)]{.mark}     |
|      |     |             |      |                                  |
|      |     |             |      | -   [2 (Camera captured)]{.mark} |
|      |     |             |      |                                  |
|      |     |             |      | -   [3 (Unknown)]{.mark}         |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Wallet   | >    | > [Number of days email address  |
|  [80 | 2]{ | > Acco      | [TLV | > exists (0000 - 9999).]{.mark}  |
| ]{.m | .ma | unt]{.mark} | ]{.m |                                  |
| ark} | rk} | > [Email    | ark} |                                  |
|      |     | > Address   |      |                                  |
|      |     | >           |      |                                  |
|      |     | Age]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Wallet   | >    | > [Value between 1 - 5, where 1  |
|  [81 | 1]{ | > Provi     | [TLV | > is least trusted and 5]{.mark} |
| ]{.m | .ma | der]{.mark} | ]{.m | > [is most trusted.]{.mark}      |
| ark} | rk} | > [Phone    | ark} |                                  |
|      |     | > Sc        |      |                                  |
|      |     | ore]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+

+------+-----------------------------------+------+------+------------+
| > *  |                                   |      |      |            |
| *Sub |                                   |      |      |            |
| >    |                                   |      |      |            |
| Elem |                                   |      |      |            |
| ents |                                   |      |      |            |
| > of |                                   |      |      |            |
| > DE |                                   |      |      |            |
| -125 |                                   |      |      |            |
| >    |                                   |      |      |            |
| when |                                   |      |      |            |
| >    |                                   |      |      |            |
|  DE- |                                   |      |      |            |
| 63.7 |                                   |      |      |            |
| > =  |                                   |      |      |            |
| > 'M |                                   |      |      |            |
| ASTE |                                   |      |      |            |
| RCAR |                                   |      |      |            |
| D'** |                                   |      |      |            |
+======+===================================+======+======+============+
| > *  | > **Field Name**                  | >    | >    | > **Format |
| *Sub |                                   | **MC | **Po | >          |
| > F  |                                   | >    | siti |  (ASCII)** |
| ield |                                   |  Bit | on** |            |
| > N  |                                   | > N  |      |            |
| o.** |                                   | o.** |      |            |
+------+-----------------------------------+------+------+------------+
| > 1  | > Token Expiration Date           |      | >    | > 4 N      |
| 25.1 |                                   |      |  1-4 |            |
+------+-----------------------------------+------+------+------------+
| > 1  | > Token Service Provider          |      | >    | > 1 A      |
| 25.2 | > Identification                  |      |  5-5 |            |
+------+-----------------------------------+------+------+------------+
| > 1  | > Token Assurance Level           |      | >    | > 2 N      |
| 25.3 |                                   |      |  6-7 |            |
+------+-----------------------------------+------+------+------------+
| > 1  | > Token Requestor ID              |      | >    | > 11 N     |
| 25.4 |                                   |      | 8-18 |            |
+------+-----------------------------------+------+------+------------+
| > 1  | > Contactless Usage               |      | > 1  | > 1 N      |
| 25.5 |                                   |      | 9-19 |            |
+------+-----------------------------------+------+------+------------+
| >    | > Card on File Electronic         |      | > 2  | > 1 N      |
|  125 | > Commerce Usage                  |      | 0-20 |            |
| .6\* |                                   |      |      |            |
+------+-----------------------------------+------+------+------------+
| > 1  | > Mobile/Digital Wallet           |      | > 2  | > 1 N      |
| 25.7 | > Electronic Commerce Usage       |      | 1-21 |            |
+------+-----------------------------------+------+------+------------+
| > 1  | > Correlation ID                  |      | > 2  | > 14 AN    |
| 25.8 |                                   |      | 2-35 |            |
+------+-----------------------------------+------+------+------------+
| > 1  | > Number of Active Tokens for the |      | > 3  | > 2 ANS    |
| 25.9 | > Primary Account Number          |      | 6-37 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Issuer Product Configuration ID |      | > 3  | > 10 ANS   |
| 5.10 |                                   |      | 8-47 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Consumer Language               |      | > 4  | > 2 A      |
| 5.11 |                                   |      | 8-49 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Final Tokenization Decision     |      | > 5  | > 1 ANS    |
| 5.12 |                                   |      | 0-50 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Final Tokenization Decision     |      | > 5  | > 1 ANS    |
| 5.13 | > Indicator                       |      | 1-51 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > T&C Identifier                  |      | > 5  | > 32 ANS   |
| 5.14 |                                   |      | 2-83 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > T&C Date and Time               |      | > 8  | > 10 ANS   |
| 5.15 |                                   |      | 4-93 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Number of Activation Attempts   |      | > 9  | > 1 ANS    |
| 5.16 |                                   |      | 4-94 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Token Unique Reference          |      | > 95 | > 48 ANS   |
| 5.17 |                                   |      | -142 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Primary Account Number Unique   |      | >    | > 48 ANS   |
| 5.18 | > Reference                       |      |  143 |            |
|      |                                   |      | -190 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Tokenization Event Indicator    |      | >    | > 1 N      |
| 5.19 |                                   |      |  191 |            |
|      |                                   |      | -191 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Tokenization Event Reason Code  |      | >    | > 2 AN     |
| 5.20 |                                   |      |  192 |            |
|      |                                   |      | -193 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Event Requestor                 |      | >    | > 1 ANS    |
| 5.21 |                                   |      |  194 |            |
|      |                                   |      | -194 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Primary Account Number Source   |      | >    | > 1 AN     |
| 5.22 |                                   |      |  195 |            |
|      |                                   |      | -195 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Payment Application Instance    |      | >    | > 48 ANS   |
| 5.23 |                                   |      |  196 |            |
|      |                                   |      | -243 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Device Source IP Address        |      | >    | > 12 ANS   |
| 5.24 |                                   |      |  244 |            |
|      |                                   |      | -255 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Wallet Service Provider Account |      | >    | > 64 ANS   |
| 5.25 | > ID Hash                         |      |  256 |            |
|      |                                   |      | -319 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Cardholder Name                 |      | >    | > 27 ANS   |
| 5.26 |                                   |      |  320 |            |
|      |                                   |      | -346 |            |
+------+-----------------------------------+------+------+------------+

+------+-----------------------------------+------+------+------------+
| > 12 | > Wallet Service Provider         |      | >    | > 1 AN     |
| 5.27 | > Tokenization Recommendation     |      |  347 |            |
|      |                                   |      | -347 |            |
+======+===================================+======+======+============+
| > 12 | > Wallet Service Provider         |      | >    | > 2 AN     |
| 5.28 | > Tokenization Recommendation     |      |  348 |            |
|      | > Standard Version                |      | -349 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Wallet Service Provider Device  |      | >    | > 1 N      |
| 5.29 | > Score                           |      |  350 |            |
|      |                                   |      | -350 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Wallet Service Provider Account |      | >    | > 1 N      |
| 5.30 | > Score                           |      |  351 |            |
|      |                                   |      | -351 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Wallet Service Provider         |      | >    | > 6 ANS    |
| 5.31 | > Tokenization Recommendation     |      |  352 |            |
|      | > Reason Codes                    |      | -357 |            |
+------+-----------------------------------+------+------+------------+
| > 12 | > Device Location                 |      | >    | > 9 ANS    |
| 5.32 |                                   |      |  358 |            |
|      |                                   |      | -366 |            |
+------+-----------------------------------+------+------+------------+

> **\*Tlv Fields of DE-125 when DE-63.7 = 'MASTERCARD'**

+------+----+--------------+------+-----------------------------------+
| *    |    |              | > ** | > **Content of Sub-Element**      |
| *Tag |    |              | Form |                                   |
| Le   |    |              | at** |                                   |
| ngth |    |              |      |                                   |
| Val  |    |              |      |                                   |
| ue** |    |              |      |                                   |
|      |    |              |      |                                   |
| **   |    |              |      |                                   |
| [Dat |    |              |      |                                   |
| aset |    |              |      |                                   |
| ID:  |    |              |      |                                   |
| 01,  |    |              |      |                                   |
| Wa   |    |              |      |                                   |
| llet |    |              |      |                                   |
| Pro  |    |              |      |                                   |
| gram |    |              |      |                                   |
| Da   |    |              |      |                                   |
| ta]{ |    |              |      |                                   |
| .mar |    |              |      |                                   |
| k}** |    |              |      |                                   |
|      |    |              |      |                                   |
| >    |    |              |      |                                   |
|  [Wa |    |              |      |                                   |
| llet |    |              |      |                                   |
| > Id |    |              |      |                                   |
| enti |    |              |      |                                   |
| fier |    |              |      |                                   |
| ]{.m |    |              |      |                                   |
| ark} |    |              |      |                                   |
| >    |    |              |      |                                   |
| >    |    |              |      |                                   |
|  [01 |    |              |      |                                   |
| ]{.m |    |              |      |                                   |
| ark} |    |              |      |                                   |
| > [3 |    |              |      |                                   |
| ]{.m |    |              |      |                                   |
| ark} |    |              |      |                                   |
| >    |    |              |      |                                   |
| >    |    |              |      |                                   |
|  [02 |    |              |      |                                   |
| ]{.m |    |              |      |                                   |
| ark} |    |              |      |                                   |
| > [2 |    |              |      |                                   |
| ]{.m |    |              |      |                                   |
| ark} |    |              |      |                                   |
| > [T |    |              |      |                                   |
| oken |    |              |      |                                   |
| >    |    |              |      |                                   |
|  Tra |    |              |      |                                   |
| nsac |    |              |      |                                   |
| tion |    |              |      |                                   |
| ]{.m |    |              |      |                                   |
| ark} |    |              |      |                                   |
| >    |    |              |      |                                   |
| [Ide |    |              |      |                                   |
| ntif |    |              |      |                                   |
| iers |    |              |      |                                   |
| ]{.m |    |              |      |                                   |
| ark} |    |              |      |                                   |
+======+====+==============+======+===================================+
|      |    |              | >    | > [The Wallet Identifier is added |
|      |    |              | [TLV | > for MDES transactions]{.mark}   |
|      |    |              | ]{.m | > [when it is available,          |
|      |    |              | ark} | > which]{.mark}                   |
|      |    |              | >    | >                                 |
|      |    |              | >    | > [identifies the wallet through  |
|      |    |              | [TLV | > which the MDES token]{.mark}    |
|      |    |              | ]{.m | > [was initiated.]{.mark}         |
|      |    |              | ark} | >                                 |
|      |    |              |      | > [103 - Apple Pay]{.mark}        |
|      |    |              |      | >                                 |
|      |    |              |      | > [216 - Google Pay]{.mark}       |
|      |    |              |      | >                                 |
|      |    |              |      | > [217 - Samsung Pay]{.mark}      |
|      |    |              |      | >                                 |
|      |    |              |      | > [327 - Merchant tokenization    |
|      |    |              |      | > program]{.mark}                 |
|      |    |              |      | >                                 |
|      |    |              |      | > [This subelement will contain,  |
|      |    |              |      | > when available, the]{.mark}     |
|      |    |              |      | > [calculated Token               |
|      |    |              |      | > Transaction]{.mark}             |
|      |    |              |      | >                                 |
|      |    |              |      | > [Identifier to identify the     |
|      |    |              |      | > transaction. Token]{.mark}      |
|      |    |              |      | > [Transaction Identifier is to   |
|      |    |              |      | > be retained]{.mark}             |
|      |    |              |      | >                                 |
|      |    |              |      | > [and used to provide the        |
|      |    |              |      | > transaction details]{.mark}     |
|      |    |              |      | > [associated with an original    |
|      |    |              |      | > purchase]{.mark}                |
|      |    |              |      | >                                 |
|      |    |              |      | > [and subsequent reversal        |
|      |    |              |      | > messages. The Token]{.mark}     |
|      |    |              |      | > [Transaction Identifier is only |
|      |    |              |      | > sent to]{.mark}                 |
|      |    |              |      | >                                 |
|      |    |              |      | > [issuers participating in the   |
|      |    |              |      | > Mastercard Digital]{.mark}      |
|      |    |              |      | > [Enablement Service.]{.mark}    |
+------+----+--------------+------+-----------------------------------+
| > ** |    |              |      |                                   |
| [Dat |    |              |      |                                   |
| aset |    |              |      |                                   |
| >    |    |              |      |                                   |
|  ID: |    |              |      |                                   |
| >    |    |              |      |                                   |
|  02, |    |              |      |                                   |
| >    |    |              |      |                                   |
|  PAN |    |              |      |                                   |
| >    |    |              |      |                                   |
|  Map |    |              |      |                                   |
| ping |    |              |      |                                   |
| >    |    |              |      |                                   |
| File |    |              |      |                                   |
| > I  |    |              |      |                                   |
| nfor |    |              |      |                                   |
| mati |    |              |      |                                   |
| on]{ |    |              |      |                                   |
| .mar |    |              |      |                                   |
| k}** |    |              |      |                                   |
+------+----+--------------+------+-----------------------------------+
| >    | >  | > [Account   | >    | > [(Account Number Indicator)     |
|  [01 | [1 | > Nu         | [TLV | > indicates the type of]{.mark}   |
| ]{.m | ]{ | mber]{.mark} | ]{.m | > [PAN mapping account.]{.mark}   |
| ark} | .m | > [Indic     | ark} | >                                 |
|      | ar | ator]{.mark} |      | > [**C** → Mastercard Digital     |
|      | k} |              |      | > Enablement Service              |
|      |    |              |      | > secure]{.mark} [element         |
|      |    |              |      | > token]{.mark}                   |
|      |    |              |      | >                                 |
|      |    |              |      | > [**E** → Embossed account       |
|      |    |              |      | > number provided by              |
|      |    |              |      | > issuer]{.mark}                  |
|      |    |              |      | >                                 |
|      |    |              |      | > [**F** → Mastercard Digital     |
|      |    |              |      | > Enablement Service static       |
|      |    |              |      | > token]{.mark} [**H** →          |
|      |    |              |      | > Mastercard Digital Enablement   |
|      |    |              |      | > Service cloud-based]{.mark}     |
|      |    |              |      | > [payments token]{.mark}         |
|      |    |              |      | >                                 |
|      |    |              |      | > [**L** → Pay with rewards       |
|      |    |              |      | > loyalty program operator        |
|      |    |              |      | > \[LPO\] card]{.mark}            |
+------+----+--------------+------+-----------------------------------+

2.  [19]{.mark} [Account Number]{.mark} [PAN]{.mark}

> [Expiration Date]{.mark}
>
> [TLV]{.mark} [This Subfield contains the PAN mapping account]{.mark}
> [number.]{.mark}
>
> [This Subfield contains the expiration date of the PAN]{.mark}
> [Mapping File Information.]{.mark}

-   [**Acquirer Message** = contains the expiration date]{.mark}
    > [when]{.mark}

```{=html}
<!-- -->
```
-   [the issuer provided one for a PAN mapping record]{.mark} [added to
    > the MCC106 MDES PAN Mapping File]{.mark}

-   [A transit transaction response contains MCC 4111,]{.mark} [4131,
    > 4784, and 7523, or]{.mark}

3.  [4]{.mark}

> [Token Assurance]{.mark}
>
> [TLV]{.mark}
>
> [-- The Mastercard Digital Enablement Service was]{.mark}
> [applied.]{.mark}

-   [**Issuer Message** = contains Contactless]{.mark} [card/device
    expiration date, or virtual]{.mark} [card expiration date, or
    Mastercard Digital]{.mark}

> [Enablement Service token expiration date, only if]{.mark} [acquirer
> provided in DE 14]{.mark}

-   [**Issuer and acquirer response message** =]{.mark} [contains
    embossed Expiration date in response to]{.mark} [transit
    transactions]{.mark}

> [This Subfield contains a value indicating the]{.mark}

4.  [2]{.mark}

5.  [11]{.mark}

[Level]{.mark} [TLV]{.mark}

> [Token Requester ID]{.mark}

[TLV]{.mark}

> [confidence level of the token to PAN/cardholder]{.mark}
> [binding.]{.mark}
>
> [This Subfield contains the ID assigned by the Token]{.mark} [Service
> Provider to the Token Requestor.]{.mark}
>
> [- *Contains the ID assigned by the Token Service*]{.mark} *[Provider
> to the Token Requestor. The Token]{.mark} [Requestor ID is optional
> for all token types.]{.mark}*

6.  [19]{.mark} [PAN Account]{.mark} [Range]{.mark}

> [TLV]{.mark} [This Subfield contains the PAN Account Range.]{.mark}

7.  [2]{.mark} [Storage Technology]{.mark} [TLV]{.mark} [(Storage
    > Technology) describes the Storage]{.mark}

> [Technology of a requested or created token.]{.mark}

8.  [3]{.mark}

> [Payment Account]{.mark}
>
> [Data]{.mark} [TLV]{.mark}
>
> [(Payment Account Data) contains unique, non-]{.mark} [financial
> reference information associated with the]{.mark} [PAN or token used
> to initiate the transaction.]{.mark}
>
> ![](./image2.jpeg){width="0.8465277777777778in"
> height="0.5229658792650919in"}***[Dataset ID: 03 Token Related
> Data]{.mark}***
>
> [Token Expiration]{.mark} [Date]{.mark}
>
> [01]{.mark}
>
> [TLV]{.mark}
>
> [Expiration date that is embossed, encoded,]{.mark} [or both on the
> card that represents the]{.mark} [cardholder primary account
> number]{.mark} [(primary account number).]{.mark}
>
> [Format: YYMM]{.mark}

2.  [Token Service]{.mark} [Provider]{.mark} [Identification
    > (TCN)]{.mark}

3.  [Token Assurance]{.mark} [Level]{.mark}

> [TLV]{.mark} [M = Mastercard Digital Enablement Service]{.mark}
>
> [TLV]{.mark} [Assurance level assigned to the token (value]{.mark}
> [between 00 and 99).]{.mark}

4.  [Contactless Usage]{.mark} [TLV]{.mark} [Contains value indicating
    > if the token is]{.mark}

> [permitted for use in contactless]{.mark} [transactions.]{.mark}
>
> [Values:]{.mark}

-   [0 = Token is not permitted for use in]{.mark} [contactless
    > transactions]{.mark}

-   [1 = Token is permitted for use in]{.mark} [contactless
    > transactions]{.mark}

> [Card on file electronic]{.mark} [commerce usage]{.mark}
>
> [05]{.mark}
>
> [TLV]{.mark}
>
> [Contains value indicating if the token is]{.mark} [permitted for use
> in card on file electronic]{.mark} [commerce transactions.]{.mark}
>
> [Values:]{.mark}

-   [0 = Token is not permitted for use in Card]{.mark} [on File
    electronic commerce transactions]{.mark}

-   [1 = Token is permitted for use in card on]{.mark} [file electronic
    commerce transactions]{.mark}

6.  [Mobile / digital]{.mark} [wallet electronic]{.mark} [commerce
    > usage]{.mark}

> [Number of active]{.mark} [tokens for the PAN]{.mark}
>
> [TLV]{.mark} [Contains value indicating if the token is]{.mark}
> [permitted for use in mobile/digital wallet]{.mark} [electronic
> commerce transactions.]{.mark}
>
> [Values:]{.mark}

-   [0 = Token is not permitted for use in]{.mark} [mobile/digital
    > wallet electronic commerce]{.mark} [transactions]{.mark}

-   [1 = Token is permitted for use in mobile/]{.mark} [digital wallet
    > electronic commerce]{.mark} [transactions]{.mark}

> [Number of active or suspended tokens for]{.mark} [the primary account
> number digitized to]{.mark} [consumer devices. Space-filled when
> token]{.mark}

7.  [TLV]{.mark}

> [present in DE 48, subelement 33, subfield 2]{.mark} [(Account Number)
> in an 0100 Tokenization]{.mark} [Complete Notification message
> is]{.mark} [provisioned to a server. Presence of this field]{.mark}
> [is conditiona]{.mark}l

8.  ![](./image2.jpeg){width="0.8465277777777778in"
    > height="0.5229658792650919in"}[Issuer product]{.mark}
    > [configuration id]{.mark}

> [TLV]{.mark} [The unique product configuration identifier]{.mark}
> [applied to the token, as provided by the]{.mark} [issuer, identifying
> a particular set of card]{.mark} [art, texts, and other product
> related data,]{.mark} [that were provided during the issuer]{.mark}
> [enablement or maintenance process.]{.mark}

![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

+------+-----+-------------+------+-----------------------------------+
| >    |     |             |      | > [Presence of this field is      |
|  [09 |     |             |      | > conditional.]{.mark}            |
| ]{.m |     |             |      |                                   |
| ark} |     |             |      |                                   |
+======+=====+=============+======+===================================+
|      |     | > [Consumer | >    | > [Language preference selected   |
|      |     | > langu     | [TLV | > by the]{.mark} [consumer.       |
|      |     | age]{.mark} | ]{.m | > Presence of this field          |
|      |     |             | ark} | > is]{.mark}                      |
|      |     |             |      | > [conditional.]{.mark}           |
+------+-----+-------------+------+-----------------------------------+
| >    |     | > [Final    | >    | > [The final tokenization         |
|  [0A |     | > Tokenizat | [TLV | > decision that was]{.mark} [used |
| ]{.m |     | ion]{.mark} | ]{.m | > in the tokenization of the      |
| ark} |     | > [Decis    | ark} | > card.]{.mark}                   |
|      |     | ion]{.mark} |      |                                   |
|      |     |             |      | -   [1 = Approve]{.mark}          |
|      |     |             |      |                                   |
|      |     |             |      | -   [2 = Approve but requires     |
|      |     |             |      |     > additional]{.mark}          |
|      |     |             |      |     > [authentication]{.mark}     |
|      |     |             |      |                                   |
|      |     |             |      | > [Presence of this field is      |
|      |     |             |      | > conditional.]{.mark}            |
+------+-----+-------------+------+-----------------------------------+
| >    |     | > [Final    | >    | > [The element of the Service     |
|  [0B |     | > Tokenizat | [TLV | > that was]{.mark} [responsible   |
| ]{.m |     | ion]{.mark} | ]{.m | > for determining the             |
| ark} |     | > [Decision | ark} | > final]{.mark} [tokenization     |
|      |     | > Indica    |      | > decision:]{.mark}               |
|      |     | tor]{.mark} |      |                                   |
|      |     |             |      | -   [1 = Tokenization Eligibility |
|      |     |             |      |     > Response]{.mark}            |
|      |     |             |      |                                   |
|      |     |             |      | -   [2 = Tokenization             |
|      |     |             |      |     > Authorization               |
|      |     |             |      |     > Response]{.mark}            |
|      |     |             |      |                                   |
|      |     |             |      | -   [3 = Issuer pre-defined       |
|      |     |             |      |     > tokenization rules]{.mark}  |
|      |     |             |      |                                   |
|      |     |             |      | -   [4 = Mobile                   |
|      |     |             |      |     > Application]{.mark}         |
|      |     |             |      |                                   |
|      |     |             |      | > [Presence of this field is      |
|      |     |             |      | > conditional.]{.mark}            |
+------+-----+-------------+------+-----------------------------------+
| >    |     | > [T&C      | >    | > [Identifier associated with the |
|  [0C |     | > Identif   | [TLV | > version of]{.mark} [terms and   |
| ]{.m |     | ier]{.mark} | ]{.m | > conditions accepted by          |
| ark} |     |             | ark} | > the]{.mark} [consumer. Presence |
|      |     |             |      | > of this field is]{.mark}        |
|      |     |             |      | >                                 |
|      |     |             |      | > [conditional.]{.mark}           |
+------+-----+-------------+------+-----------------------------------+
| >    |     | > [T&C Date | >    | > [Date and time that the         |
|  [0D |     | > And       | [TLV | > consumer accepted]{.mark} [the  |
| ]{.m |     | > T         | ]{.m | > terms and conditions of the     |
| ark} |     | ime]{.mark} | ark} | > Service,]{.mark} [specified in  |
|      |     |             |      | > UTC units.]{.mark}              |
|      |     |             |      | >                                 |
|      |     |             |      | > [Format: YYMMDDhhmm]{.mark}     |
+------+-----+-------------+------+-----------------------------------+
| >    |     | > [Number   | >    | > [Number of activation code      |
|  [0E |     | >           | [TLV | > entry attempts]{.mark}          |
| ]{.m |     |  Of]{.mark} | ]{.m | >                                 |
| ark} |     | >           | ark} | > [by the cardholder.             |
|      |     | [Activation |      | > Space-filled when               |
|      |     | > Attem     |      | > DE124,]{.mark} [SF14 (Token     |
|      |     | pts]{.mark} |      | > Type) value is F. Presence      |
|      |     |             |      | > of]{.mark} [this field is       |
|      |     |             |      | > conditional.]{.mark}            |
+------+-----+-------------+------+-----------------------------------+
| >    |     | > [Token    | >    | > [Service-allocated unique       |
|  [1A |     | > Uni       | [TLV | > reference to the]{.mark}        |
| ]{.m |     | que]{.mark} | ]{.m | > [token.]{.mark}                 |
| ark} |     | >           | ark} |                                   |
|      |     |  [Reference |      |                                   |
|      |     | > (T        |      |                                   |
|      |     | CN)]{.mark} |      |                                   |
+------+-----+-------------+------+-----------------------------------+
| >    |     | > [PAN      | >    | > [Service-allocated unique       |
|  [1B |     | > Uni       | [TLV | > reference to the]{.mark}        |
| ]{.m |     | que]{.mark} | ]{.m | > [tokenized Primary Account      |
| ark} |     | > [Refere   | ark} | > Number at the]{.mark} [wallet   |
|      |     | nce]{.mark} |      | > level.]{.mark}                  |
+------+-----+-------------+------+-----------------------------------+
| >    |     | > [T        | >    | > [Value indicating the event     |
|  [1C |     | okenization | [TLV | > that has]{.mark} [occurred on   |
| ]{.m |     | > Ev        | ]{.m | > the Mastercard Digital]{.mark}  |
| ark} |     | ent]{.mark} | ark} | > [Enablement Service for the     |
|      |     | > [Indica   |      | > token]{.mark}                   |
|      |     | tor]{.mark} |      | >                                 |
|      |     |             |      | > [3 = Deactivate]{.mark}         |
|      |     |             |      | >                                 |
|      |     |             |      | > [4 = Deleted from consumer      |
|      |     |             |      | > device]{.mark}                  |
|      |     |             |      | >                                 |
|      |     |             |      | > [6 = Suspend]{.mark}            |
|      |     |             |      | >                                 |
|      |     |             |      | > [7 = Resume]{.mark}             |
|      |     |             |      | >                                 |
|      |     |             |      | > [8 = Tokenization Exception     |
|      |     |             |      | > Event]{.mark}                   |
|      |     |             |      | >                                 |
|      |     |             |      | > [9 = Replacement]{.mark}        |
+------+-----+-------------+------+-----------------------------------+

> [1D]{.mark} [Tokenization Event]{.mark} [Reason Code]{.mark}
>
> [Event Requestor]{.mark}
>
> [TLV]{.mark} [If the Tokenization Event Indicator]{.mark} [contains
> value 8 (Tokenization Exception]{.mark} [Event), this field contains a
> value]{.mark} [indicating the event reason. If the]{.mark}
> [Tokenization Event Indicator contains a]{.mark} [value of 3
> (Deactivate), 6 (Suspend), or 7]{.mark} [(Resume), this field will not
> be present.]{.mark}

-   [00 = Activation code retries exceeded]{.mark}

-   [01 = Activation code expired or]{.mark} [invalidated]{.mark}

-   [02 = Activation code entered incorrectly]{.mark} [by
    > cardholder]{.mark}

> [If the Tokenization Event Indicator]{.mark} [contains a value of 3
> (Deactivate), 6]{.mark} [(Suspend), or 7 (Resume), this field
> will]{.mark} [contain a value indicating the party that]{.mark}
> [requested the event. If the Tokenization]{.mark} [Event Indicator
> contains a value of 8]{.mark} [(Tokenization Exception Event) this
> field]{.mark} [will be space filled.]{.mark}

-   [0 = Indicates the Tokenization Event]{.mark} [was requested by the
    > Wallet Provider]{.mark} [or Token Requestor]{.mark}

-   [1 = Indicates the Tokenization Event]{.mark} [was requested by the
    > Funding Account]{.mark} [issuer]{.mark}

-   [2 = Indicates the Tokenization Event]{.mark} [was requested by the
    > Cardholder]{.mark}

> [1E]{.mark} [TLV]{.mark}

-   [3 = Indicates the Tokenization Event]{.mark} [was requested in
    relation to a]{.mark} [systematic event triggered by Mobile]{.mark}
    [PIN Validation security (applicable to]{.mark} [Tokenization Event
    Indicator value of 6]{.mark} [(Suspend), or 7 (Resume) only)]{.mark}

-   [4 = Indicates the Tokenization Event]{.mark} [was requested in
    relation to a]{.mark} [systematic event triggered by Mobile]{.mark}
    [PIN Change Validation security]{.mark} [(applicable to Tokenization
    Event]{.mark} [Indicator value of 6 (Suspend), or 7]{.mark}
    [(Resume) only)]{.mark}

-   [5 = Reserved for future use]{.mark}

-   [6 = Reserved for future use]{.mark}

-   [7 = Reserved for future use]{.mark}

-   [8 = Reserved for future use]{.mark}

-   [9 = Reserved for future use]{.mark}

> ![](./image2.jpeg){width="0.8465277777777778in"
> height="0.5229658792650919in"}***[Dataset ID: 04, PAN Mapping File
> Information]{.mark}***
>
> [01]{.mark} [Primary Account]{.mark} [TLV]{.mark} [Identifies the
> method which the cardholder is]{.mark}

+--------+------------------+----+-----------------------------------+
|        | > [Number        |    | > [attempting to tokenize a       |
|        | > Score]{.mark}  |    | > primary account]{.mark} [number |
|        |                  |    | > with one of the following       |
|        |                  |    | > values:]{.mark}                 |
|        |                  |    | >                                 |
|        |                  |    | > [1 = Card on file]{.mark}       |
|        |                  |    | >                                 |
|        |                  |    | > [2 = Card added                 |
|        |                  |    | > manually]{.mark}                |
|        |                  |    | >                                 |
|        |                  |    | > [3 = Card added via             |
|        |                  |    | > application]{.mark}             |
+========+==================+====+===================================+
| >      | >                | >  | > [Identifier associated with the |
|  [02]{ | [Payment]{.mark} | [T | > payment]{.mark} [application    |
| .mark} | > [Application   | LV | > installed onto a                |
|        | >                | ]{ | > device.]{.mark}                 |
|        | Instance]{.mark} | .m |                                   |
|        | > [ID]{.mark}    | ar |                                   |
|        |                  | k} |                                   |
+--------+------------------+----+-----------------------------------+
| >      | > [Device Source | >  | > [Variable length IP address.    |
|  [03]{ | > IP]{.mark}     | [T | > Each octet of the IP]{.mark}    |
| .mark} | >                | LV | > [address is converted to hex,   |
|        | [Address]{.mark} | ]{ | > and joined into]{.mark} [one    |
|        |                  | .m | > string, with the order          |
|        |                  | ar | > maintained.]{.mark}             |
|        |                  | k} |                                   |
+--------+------------------+----+-----------------------------------+
| >      | > [Wallet        | >  | > [When provided by the Wallet    |
|  [04]{ | >                | [T | > Provider, the]{.mark} [issuer   |
| .mark} | Provider]{.mark} | LV | > may use this hash value to      |
|        | > [Account ID    | ]{ | > match]{.mark} [against known    |
|        | > Hash]{.mark}   | .m | > identifiers for the             |
|        |                  | ar | > cardholder;]{.mark} [for        |
|        |                  | k} | > example, their email addresses  |
|        |                  |    | > on file. If]{.mark} [the hash   |
|        |                  |    | > values match, this may aid an   |
|        |                  |    | > issuer's]{.mark} [digitization  |
|        |                  |    | > decision by providing           |
|        |                  |    | > additional]{.mark} [factors to  |
|        |                  |    | > help verify that the Wallet     |
|        |                  |    | > Provider]{.mark} [account       |
|        |                  |    | > holder is indeed their          |
|        |                  |    | > cardholder, or to]{.mark}       |
|        |                  |    | > [differentiate between primary  |
|        |                  |    | > and secondary]{.mark}           |
|        |                  |    | > [cardholders.]{.mark}           |
+--------+------------------+----+-----------------------------------+
| >      | > [Cardholder    | >  | > [This field may be present and  |
|  [05]{ | > name]{.mark}   | [T | > contain the]{.mark} [name of    |
| .mark} |                  | LV | > the cardholder. The format is   |
|        |                  | ]{ | > either]{.mark}                  |
|        |                  | .m | > [LASTNAME/FIRSTNAME with the    |
|        |                  | ar | > names]{.mark} [delimited by a   |
|        |                  | k} | > slash "/" (Example:             |
|        |                  |    | > SMITH/JOE)]{.mark} [or the      |
|        |                  |    | > format is FIRSTNAME             |
|        |                  |    | > LASTNAME]{.mark} [(Example: JOE |
|        |                  |    | > SMITH).]{.mark}                 |
|        |                  |    | >                                 |
|        |                  |    | > [If the cardholder's name is    |
|        |                  |    | > longer than 27]{.mark}          |
|        |                  |    | > [positions, the data will be    |
|        |                  |    | > truncated to the]{.mark}        |
|        |                  |    | > [maximum length of 27.]{.mark}  |
+--------+------------------+----+-----------------------------------+
| >      | > [Wallet        | >  | > [Tokenization decision          |
|  [06]{ | >                | [T | > suggested by the Wallet]{.mark} |
| .mark} | provider]{.mark} | LV | > [Provider. One of the following |
|        | > [Toke          | ]{ | > values:]{.mark}                 |
|        | nization]{.mark} | .m | >                                 |
|        | > [Recomm        | ar | > [0 = Decline]{.mark}            |
|        | endation]{.mark} | k} | >                                 |
|        |                  |    | > [1 = Approve]{.mark}            |
|        |                  |    | >                                 |
|        |                  |    | > [2 = Require additional         |
|        |                  |    | > authentication]{.mark}          |
+--------+------------------+----+-----------------------------------+
| >      | > [Wallet        | >  | > [The version of the standards   |
|  [07]{ | >                | [T | > the Wallet]{.mark} [Provider is |
| .mark} | provider]{.mark} | LV | > using to determine the          |
|        | > [Toke          | ]{ | > suggested]{.mark} [tokenization |
|        | nization]{.mark} | .m | > recommendation.]{.mark}         |
|        | > [Recomm        | ar |                                   |
|        | endation]{.mark} | k} |                                   |
|        | > [Standard      |    |                                   |
|        | >                |    |                                   |
|        |  Version]{.mark} |    |                                   |
+--------+------------------+----+-----------------------------------+
| >      | > [Wallet        | >  | > [Score assigned by Wallet       |
|  [08]{ | >                | [T | > Provider for the]{.mark}        |
| .mark} | Provider]{.mark} | LV | > [device. Value between 1 and    |
|        | > [Device        | ]{ | > 5.]{.mark}                      |
|        | > Score]{.mark}  | .m |                                   |
|        |                  | ar |                                   |
|        |                  | k} |                                   |
+--------+------------------+----+-----------------------------------+

+--------+-----------------+------+----------------------------------+
| >      | > [Wallet       | [TLV | [Score assigned by Wallet        |
|  [09]{ | > P             | ]{.m | Provider for the]{.mark}         |
| .mark} | rovider]{.mark} | ark} | [primary account number. Value   |
|        | > [Account      |      | between 1 and]{.mark}            |
|        | > Score]{.mark} |      | [5.]{.mark}                      |
+========+=================+======+==================================+
| >      | > [Wallet       | [TLV | > [Code indicating the specific  |
|  [0A]{ | > P             | ]{.m | > reason the Wallet]{.mark}      |
| .mark} | rovider]{.mark} | ark} | > [Provider is suggesting the    |
|        | > [Token        |      | > tokenization]{.mark}           |
|        | ization]{.mark} |      | > [recommendation.]{.mark}       |
|        | > [Reccome      |      | >                                |
|        | ndation]{.mark} |      | > [The data of this field is a   |
|        | > [Reason       |      | > hex-encoded bitmap,]{.mark}    |
|        | > Codes]{.mark} |      | > [whereby each bit corresponds  |
|        |                 |      | > to a specific]{.mark} [Reason  |
|        |                 |      | > Code.]{.mark}                  |
|        |                 |      | >                                |
|        |                 |      | > [The bitmap is big-endian with |
|        |                 |      | > the least]{.mark} [significant |
|        |                 |      | > bit corresponding to Reason    |
|        |                 |      | > Code]{.mark} [01, with the     |
|        |                 |      | > next least significant         |
|        |                 |      | > bit]{.mark} [corresponding to  |
|        |                 |      | > Reason Code 02, and so         |
|        |                 |      | > on.]{.mark} [For example, if   |
|        |                 |      | > Reason Codes 01, 05, and       |
|        |                 |      | > 16]{.mark} [were encoded, the  |
|        |                 |      | > bitmap would be]{.mark}        |
|        |                 |      | > [0000000010000000000100001 and |
|        |                 |      | > the hex]{.mark}                |
|        |                 |      | >                                |
|        |                 |      | > [value of this field would be  |
|        |                 |      | > 008011.]{.mark}                |
|        |                 |      | >                                |
|        |                 |      | > [If the Wallet Provider has no |
|        |                 |      | > reason, this field]{.mark}     |
|        |                 |      | > [will contain spaces.]{.mark}  |
+--------+-----------------+------+----------------------------------+
| >      | > [Device       | [TLV | [Latitude and longitude where    |
|  [0B]{ | > L             | ]{.m | the device the]{.mark} [consumer |
| .mark} | ocation]{.mark} | ark} | is attempting to tokenize a      |
|        |                 |      | card]{.mark} [onto is            |
|        |                 |      | located.]{.mark}                 |
|        |                 |      |                                  |
|        |                 |      | [Device Location Latitude --     |
|        |                 |      | an-4; hexadecimal]{.mark}        |
|        |                 |      | [encoded degrees with 2 decimal  |
|        |                 |      | places]{.mark} [Device Location  |
|        |                 |      | Longitude -- an-4;               |
|        |                 |      | hexadecimal]{.mark} [encoded     |
|        |                 |      | degrees with 2 decimal           |
|        |                 |      | places]{.mark} [Device Location  |
|        |                 |      | Lat/Long Sector -- n-1 --        |
|        |                 |      | one]{.mark} [of the following    |
|        |                 |      | values:]{.mark}                  |
|        |                 |      |                                  |
|        |                 |      | [1 = Latitude = N, Longitude =   |
|        |                 |      | W]{.mark}                        |
|        |                 |      |                                  |
|        |                 |      | [2 = Latitude = N, Longitude =   |
|        |                 |      | E]{.mark}                        |
|        |                 |      |                                  |
|        |                 |      | [3 = Latitude = S, Longitude =   |
|        |                 |      | W]{.mark}                        |
|        |                 |      |                                  |
|        |                 |      | [4 = Latitude = S, Longitude =   |
|        |                 |      | E]{.mark}                        |
|        |                 |      |                                  |
|        |                 |      | [This field will contain spaces  |
|        |                 |      | if the Wallet]{.mark} [Provider  |
|        |                 |      | has not provided this            |
|        |                 |      | information.]{.mark}             |
+--------+-----------------+------+----------------------------------+

##### 125.6\* (Card on File Electronic Commerce Usage) {#card-on-file-electronic-commerce-usage .unnumbered}

> Contains value indicating if the token is permitted for use in card on
> file electronic commerce transactions.

##### Possible Values: {#possible-values-2 .unnumbered}

> 0 = Token is not permitted for use in Card on File electronic commerce
> transactions.
>
> 1 = Token is permitted for use in Card on File electronic commerce
> transactions.

+------+----+-------------+------+-----------------------------------+
| >    |    |             |      |                                   |
|  []{ |    |             |      |                                   |
| #_bo |    |             |      |                                   |
| okma |    |             |      |                                   |
| rk93 |    |             |      |                                   |
| > .  |    |             |      |                                   |
| anch |    |             |      |                                   |
| or}* |    |             |      |                                   |
| *Sub |    |             |      |                                   |
| >    |    |             |      |                                   |
| Elem |    |             |      |                                   |
| ents |    |             |      |                                   |
| > of |    |             |      |                                   |
| > DE |    |             |      |                                   |
| -125 |    |             |      |                                   |
| >    |    |             |      |                                   |
| when |    |             |      |                                   |
| >    |    |             |      |                                   |
|  DE- |    |             |      |                                   |
| 63.7 |    |             |      |                                   |
| > =  |    |             |      |                                   |
| >    |    |             |      |                                   |
| 'UNI |    |             |      |                                   |
| ONPA |    |             |      |                                   |
| Y'** |    |             |      |                                   |
+======+====+=============+======+===================================+
| >    | >  | > Value     | > Fo | > Content of Sub-Element          |
|  Tag | Le |             | rmat |                                   |
|      | ng |             |      |                                   |
|      | th |             |      |                                   |
+------+----+-------------+------+-----------------------------------+
| > ** |    |             |      |                                   |
| *Dat |    |             |      |                                   |
| aset |    |             |      |                                   |
| >    |    |             |      |                                   |
|  ID: |    |             |      |                                   |
| >    |    |             |      |                                   |
|  QR, |    |             |      |                                   |
| > T  |    |             |      |                                   |
| oken |    |             |      |                                   |
| >    |    |             |      |                                   |
|  Dat |    |             |      |                                   |
| a*** |    |             |      |                                   |
+------+----+-------------+------+-----------------------------------+
| > 01 | >  | > QRC Use   | >    | > [Valid values:]{.underline}     |
|      |  3 | > Case      |  ANS | >                                 |
|      |    | > Indicator |      | > 100- Consumer-presented QRC,    |
|      |    |             |      | > purchase transaction. 210-      |
|      |    |             |      | > Merchant-presented QRC,         |
|      |    |             |      | > purchase transaction.           |
|      |    |             |      | >                                 |
|      |    |             |      | > 211- Merchant-presented QRC,    |
|      |    |             |      | > purchase transaction, debit     |
|      |    |             |      | > card only. Example: purchasing  |
|      |    |             |      | > financial products.             |
|      |    |             |      | >                                 |
|      |    |             |      | > 220- Merchant-presented QRC,    |
|      |    |             |      | > ATM cash withdrawal.            |
|      |    |             |      | >                                 |
|      |    |             |      | > 212- Merchant-presented QRC,    |
|      |    |             |      | > purchase transaction in small   |
|      |    |             |      | > businesses.                     |
|      |    |             |      | >                                 |
|      |    |             |      | > 231- P2P QRC-based Payment,     |
|      |    |             |      | > primary credit transaction.     |
|      |    |             |      | >                                 |
|      |    |             |      | > 232- P2P QRC-based Payment,     |
|      |    |             |      | > account funding transaction,    |
+------+----+-------------+------+-----------------------------------+
| > 02 | >  | > QRC       | >    | > Generated by UnionPay system.   |
|      | 20 | > Voucher   |  ANS | > The payment index is unique     |
|      |    | > Number    |      | > permanently. It is used to      |
|      |    |             |      | > locate a transaction.           |
+------+----+-------------+------+-----------------------------------+
| > 03 | >  | > C2B       | >    | > The information contained in    |
|      | 34 | > Payment   |  ANS | > the Consumer- presented QRC.    |
|      |    | > Code      |      |                                   |
+------+----+-------------+------+-----------------------------------+
| > 04 | >  | > Wallet ID | >    | > Assigned by UPI. It indicates   |
|      | 11 | > 1         |  ANS | > the Wallet ID of payer.         |
+------+----+-------------+------+-----------------------------------+
| > 05 | >  | > Wallet ID | >    | > Assigned by UPI. It indicates   |
|      | 11 | > 2         |  ANS | > the Wallet ID of payee.         |
+------+----+-------------+------+-----------------------------------+

+------+------------+----------+--------+---+-------+---------------+---+
| > *  |            |          |        |   |       |               |   |
| *Sub |            |          |        |   |       |               |   |
| >    |            |          |        |   |       |               |   |
| Elem |            |          |        |   |       |               |   |
| ents |            |          |        |   |       |               |   |
| > of |            |          |        |   |       |               |   |
| > DE |            |          |        |   |       |               |   |
| >    |            |          |        |   |       |               |   |
|  125 |            |          |        |   |       |               |   |
| >    |            |          |        |   |       |               |   |
| when |            |          |        |   |       |               |   |
| > DE |            |          |        |   |       |               |   |
| 63.7 |            |          |        |   |       |               |   |
| > =  |            |          |        |   |       |               |   |
| >    |            |          |        |   |       |               |   |
| 'DIS |            |          |        |   |       |               |   |
| COVE |            |          |        |   |       |               |   |
| R'** |            |          |        |   |       |               |   |
+======+============+==========+========+===+=======+===============+===+
| >    | > Field    | >        | > Data | > | > F   | > Values      |   |
|  Sub | > Name     | Discover | > set  |   | ormat |               |   |
| > F  |            | > Bit No |        | T |       |               |   |
| ield |            |          |        | A |       |               |   |
| > No |            |          |        | G |       |               |   |
+------+------------+----------+--------+---+-------+---------------+---+
| > 1  | > Token    | > 106    | > 61   | > | > 16  | > This tag    |   |
| 25.1 | >          |          |        |   | > AN  | > will        |   |
|      |  Requestor |          |        | 0 |       | > contain the |   |
|      | > ID       |          |        | 2 |       | > ID of Token |   |
|      |            |          |        |   |       | >             |   |
|      |            |          |        |   |       | > Requestor.  |   |
|      |            |          |        |   |       | >             |   |
|      |            |          |        |   |       | > This tag    |   |
|      |            |          |        |   |       | > may not be  |   |
|      |            |          |        |   |       | > present to  |   |
|      |            |          |        |   |       | > all         |   |
|      |            |          |        |   |       | > Merchant /  |   |
|      |            |          |        |   |       | > Acquirers.  |   |
+------+------------+----------+--------+---+-------+---------------+---+
| > 1  | > Token    | > 106    | > 61   | > | > 2   | > This tag    |   |
| 25.2 | >          |          |        |   | > AN  | > will        |   |
|      |  Assurance |          |        | 0 |       | > contain a   |   |
|      |            |          |        | 3 |       |               |   |
+------+------------+----------+--------+---+-------+---------------+---+

+------+------------+----------+--------+---+-------+----------------+
|      | > Level    |          |        |   |       | > value that   |
|      |            |          |        |   |       | > indicates    |
|      |            |          |        |   |       | > the          |
|      |            |          |        |   |       | > confidence   |
|      |            |          |        |   |       | > level of the |
|      |            |          |        |   |       | > Payment      |
|      |            |          |        |   |       | > Token to PAN |
|      |            |          |        |   |       | > Cardholder   |
|      |            |          |        |   |       | > binding.     |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > Contact your |
|      |            |          |        |   |       | > Discover     |
|      |            |          |        |   |       | > Account      |
|      |            |          |        |   |       | > Executive    |
|      |            |          |        |   |       | > for further  |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       |  clarification |
|      |            |          |        |   |       | > on the use   |
|      |            |          |        |   |       | > of this      |
|      |            |          |        |   |       | > field.       |
+======+============+==========+========+===+=======+================+
| > 1  | > PAN Data | > 106    | > 61   | > | > 19  | > Contains     |
| 25.3 |            |          |        |   | > AN  | > Primary      |
|      |            |          |        | 0 |       | > Account data |
|      |            |          |        | 4 |       | > for the      |
|      |            |          |        |   |       | > tokenized    |
|      |            |          |        |   |       | > Account.     |
|      |            |          |        |   |       | > Acquirers    |
|      |            |          |        |   |       | > and Merchant |
|      |            |          |        |   |       | > Processors   |
|      |            |          |        |   |       | > must not     |
|      |            |          |        |   |       | > forward PAN  |
|      |            |          |        |   |       | > data to      |
|      |            |          |        |   |       | > Merchants.   |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > This tag may |
|      |            |          |        |   |       | > not be       |
|      |            |          |        |   |       | > present to   |
|      |            |          |        |   |       | > all Merchant |
|      |            |          |        |   |       | > / Acquirers. |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > Contact your |
|      |            |          |        |   |       | > Discover     |
|      |            |          |        |   |       | > Network      |
|      |            |          |        |   |       | > Account      |
|      |            |          |        |   |       | > Executive    |
|      |            |          |        |   |       | > for further  |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       |  clarification |
|      |            |          |        |   |       | > on the use   |
|      |            |          |        |   |       | > of this      |
|      |            |          |        |   |       | > field.       |
+------+------------+----------+--------+---+-------+----------------+
| > 1  | > Payment  | > 106    | > 61   | > | > 19  | > This is the  |
| 25.4 | > Token    |          |        |   | > AN  | > Payment      |
|      | > Number   |          |        | 0 |       | > Token        |
|      |            |          |        | 5 |       | > number.      |
+------+------------+----------+--------+---+-------+----------------+
| > 1  | > Token    | > 106    | > 61   | > | > 4   | > The          |
| 25.5 | > Expiry   |          |        |   | > AN  | > expiration   |
|      | > Date     |          |        | 0 |       | > date of the  |
|      |            |          |        | 6 |       | > Payment      |
|      |            |          |        |   |       | > Token.       |
|      |            |          |        |   |       | > Format       |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > = YYMM.      |
+------+------------+----------+--------+---+-------+----------------+
| > 1  | > PAN      | > 106    | > 61   | > | > 4   | > The PAN      |
| 25.6 | >          |          |        |   | > AN  | > expiration   |
|      | Expiration |          |        | 1 |       | > date for the |
|      | > Date     |          |        | 3 |       | > Primary      |
|      |            |          |        |   |       | > Account      |
|      |            |          |        |   |       | > Number.      |
|      |            |          |        |   |       | > Format =     |
|      |            |          |        |   |       | > YYMM         |
+------+------------+----------+--------+---+-------+----------------+
| > 1  | > Token    | > 106    | > 61   | > | > 64  | > This tag     |
| 25.7 | > Network  |          |        |   | > AN  | > will contain |
|      | > T        |          |        | 1 |       | > a unique     |
|      | ransaction |          |        | 4 |       | > Transaction  |
|      | >          |          |        |   |       | > ID generated |
|      | Identifier |          |        |   |       | > by Discover  |
|      |            |          |        |   |       | > Digital      |
|      |            |          |        |   |       | > Platform.    |
+------+------------+----------+--------+---+-------+----------------+
| > 1  | > Token ID | > 106    | > 61   | > | > 64  | > Ser          |
| 25.8 |            |          |        |   | > AN  | vice-allocated |
|      |            |          |        | 1 |       | > unique       |
|      |            |          |        | 8 |       | > reference to |
|      |            |          |        |   |       | > the token.   |
+------+------------+----------+--------+---+-------+----------------+
| > 1  | > Token    | > 106    | > 61   | > | > 2   | > Contains a   |
| 25.9 | > Domain   |          |        |   | > AN  | > value        |
|      | > Type     |          |        | 2 |       | > indicating   |
|      |            |          |        | 0 |       | > the type of  |
|      |            |          |        |   |       | > Payment      |
|      |            |          |        |   |       | > Token        |
|      |            |          |        |   |       | > present.     |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > 01 ECOM/COF- |
|      |            |          |        |   |       | > E-           |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > Commerc      |
|      |            |          |        |   |       | e/Card-on-File |
|      |            |          |        |   |       | > 02Secure     |
|      |            |          |        |   |       | > Element      |
|      |            |          |        |   |       | > 03HCE /      |
|      |            |          |        |   |       | > Cloud-Based  |
|      |            |          |        |   |       | > Payment      |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > 04CBP (Cloud |
|      |            |          |        |   |       | > Based        |
+------+------------+----------+--------+---+-------+----------------+

+------+------------+----------+--------+---+-------+----------------+
|      |            |          |        |   |       | > Payment)     |
+======+============+==========+========+===+=======+================+
| > 12 | > Device   | > 106    | > 62   | > | > 2   | > This tag     |
| 5.10 | > Type     |          |        |   | > AN  | > contains the |
|      |            |          |        | 0 |       | > device type. |
|      |            |          |        | 1 |       | >              |
|      |            |          |        |   |       | > Possible     |
|      |            |          |        |   |       | > values:      |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > 125.10       |
|      |            |          |        |   |       | > Possible     |
|      |            |          |        |   |       | > values of    |
|      |            |          |        |   |       | > device types |
|      |            |          |        |   |       | > 92           |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Device   | > 106    | > 62   | > | > 64  | > A stable     |
| 5.11 | > ID       |          |        |   | > AN  | > persistent   |
|      |            |          |        | 0 |       | > hardware     |
|      |            |          |        | 6 |       | > identifier   |
|      |            |          |        |   |       | > of the       |
|      |            |          |        |   |       | > device (e.g. |
|      |            |          |        |   |       | > the secure   |
|      |            |          |        |   |       | > element      |
|      |            |          |        |   |       | > identifier   |
|      |            |          |        |   |       | > (SEID)       |
|      |            |          |        |   |       | > provided by  |
|      |            |          |        |   |       | > the digital  |
|      |            |          |        |   |       | > wallet).     |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Full     | > 106    | > 62   | > | > 20  | > A full phone |
| 5.12 | > Phone    |          |        |   | > AN  | > number, if   |
|      | > Number   |          |        | 0 |       | > provided by  |
|      |            |          |        | 8 |       | > the digital  |
|      |            |          |        |   |       | > wallet.      |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Device   | > 106    | > 62   | > | > 64  | > Commercial   |
| 5.13 | > Name     |          |        |   | > ANS | > name (model) |
|      |            |          |        | 1 |       | > of the       |
|      |            |          |        | 0 |       | > device, as   |
|      |            |          |        |   |       | > defined by   |
|      |            |          |        |   |       | > the device   |
|      |            |          |        |   |       | > provider     |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Device   | > 106    | > 62   | > | > 35  | > This tag     |
| 5.14 | > Location |          |        |   | > ANS | > contains the |
|      |            |          |        | 1 |       | > geographic   |
|      |            |          |        | 2 |       | > location of  |
|      |            |          |        |   |       | > the device.  |
|      |            |          |        |   |       | > Location is  |
|      |            |          |        |   |       | > lati         |
|      |            |          |        |   |       | tude/longitude |
|      |            |          |        |   |       | > rounded to   |
|      |            |          |        |   |       | > nearest      |
|      |            |          |        |   |       | > whole digit; |
|      |            |          |        |   |       | > for example, |
|      |            |          |        |   |       | > +37/-        |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > 121\. May    |
|      |            |          |        |   |       | > present when |
|      |            |          |        |   |       | > function     |
|      |            |          |        |   |       | > code is 641  |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Device   | > 106    | > 62   | > | > 35  | > This tag     |
| 5.15 | > IP       |          |        |   | > ANS | > contains the |
|      | > Address  |          |        | 1 |       | > IP address   |
|      |            |          |        | 3 |       | > of the       |
|      |            |          |        |   |       | > device at    |
|      |            |          |        |   |       | > the time of  |
|      |            |          |        |   |       | > the          |
|      |            |          |        |   |       | > provisioning |
|      |            |          |        |   |       | > request. May |
|      |            |          |        |   |       | > present when |
|      |            |          |        |   |       | > function     |
|      |            |          |        |   |       | > code is 641. |
|      |            |          |        |   |       | > This value   |
|      |            |          |        |   |       | > will be in   |
|      |            |          |        |   |       | > the format:  |
|      |            |          |        |   |       | > 25           |
|      |            |          |        |   |       | 5.255.255.255. |
|      |            |          |        |   |       | > Each         |
|      |            |          |        |   |       | >              |
|      |            |          |        |   |       | > octet (255)  |
|      |            |          |        |   |       | > may be 1--3  |
|      |            |          |        |   |       | > digits in    |
|      |            |          |        |   |       | > length.      |
|      |            |          |        |   |       | > (align with  |
|      |            |          |        |   |       | > V+ data in   |
|      |            |          |        |   |       | > Field 63)    |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Account  | > 106    | > 63   | > | > 2   | > A value of   |
| 5.16 | > Risk     |          |        |   | > AN  | > 01--05, with |
|      |            |          |        | 0 |       | > a value of   |
|      |            |          |        | 5 |       | > 05 as the    |
|      |            |          |        |   |       | > most trusted |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Device   | > 106    | > 63   | > | > 2   | > A value of   |
| 5.17 | > Risk     |          |        |   | > AN  | > 01--05, with |
|      |            |          |        | 0 |       | > a value of   |
|      |            |          |        | 4 |       | > 05 as the    |
|      |            |          |        |   |       | > most trusted |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Risk     | > NA     | > NA   | > | > 3 N | > Identified   |
| 5.18 | > Reason   |          |        |   |       | > risk reason  |
|      |            |          |        | N |       | > code for     |
|      |            |          |        | A |       | > identifying  |
|      |            |          |        |   |       | > provision    |
|      |            |          |        |   |       | > risk color   |
+------+------------+----------+--------+---+-------+----------------+

+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Phone    | > NA     | > NA   | > | > 4 N | > User phone   |
| 5.19 | > no.      |          |        |   |       | > number if    |
|      | > (Last 4) |          |        | N |       | > available    |
|      |            |          |        | A |       | > (Last)       |
+======+============+==========+========+===+=======+================+
| > 12 | > Pr       | > NA     | > NA   | > | > 10  | > Risk rating  |
| 5.20 | ovisioning |          |        |   | > AN  | > based on     |
|      | > Risk     |          |        | N |       | > experience   |
|      |            |          |        | A |       | > with the     |
|      |            |          |        |   |       | > customer and |
|      |            |          |        |   |       | > device being |
|      |            |          |        |   |       | > provisioned. |
|      |            |          |        |   |       | > Possible     |
|      |            |          |        |   |       | > values are   |
|      |            |          |        |   |       | > GREEN YELLOW |
|      |            |          |        |   |       | > ORANGE RED   |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Token    | > NA     | > NA   | > | > 4 N | > Specific     |
| 5.21 | > No       |          |        |   |       | > operation    |
|      | tification |          |        | N |       | > that needs   |
|      | > Type     |          |        | A |       | > to performed |
|      |            |          |        |   |       | > on the Token |
|      |            |          |        |   |       | > associated   |
|      |            |          |        |   |       | > with the     |
|      |            |          |        |   |       | > tokenId      |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > C        | > NA     | > NA   | > | > 64  | > This is a    |
| 5.22 | orrelation |          |        |   | > ANS | > value that   |
|      | > Id       |          |        | N |       | > is returned  |
|      |            |          |        | A |       | > by the       |
|      |            |          |        |   |       | > Issuer. This |
|      |            |          |        |   |       | > allows the   |
|      |            |          |        |   |       | > Issuer to    |
|      |            |          |        |   |       | > tie together |
|      |            |          |        |   |       | > Verify Card  |
|      |            |          |        |   |       | > calls with   |
|      |            |          |        |   |       | > Provision    |
|      |            |          |        |   |       | > Credential   |
|      |            |          |        |   |       | > calls as     |
|      |            |          |        |   |       | > these happen |
|      |            |          |        |   |       | > a            |
|      |            |          |        |   |       | synchronously. |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > OTP      | > NA     | > NA   | > | > 8   | > OTP code     |
| 5.23 |            |          |        |   | > AN  | > entered by   |
|      |            |          |        | N |       | > user /       |
|      |            |          |        | A |       | > received     |
|      |            |          |        |   |       | > from network |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | >          | > NA     | > NA   | > | > 1 N |                |
| 5.24 | Cardholder |          |        |   |       |                |
|      | > Ve       |          |        | N |       |                |
|      | rification |          |        | A |       |                |
|      | > Method   |          |        |   |       |                |
|      | >          |          |        |   |       |                |
|      | Identifier |          |        |   |       |                |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | >          | > NA     | > NA   | > | > 64  |                |
| 5.25 | Cardholder |          |        |   | > AN  |                |
|      | > Ve       |          |        | N |       |                |
|      | rification |          |        | A |       |                |
|      | > Method   |          |        |   |       |                |
|      | > Value    |          |        |   |       |                |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Token    | > NA     | > NA   | > | > 1 N | > If 1 it      |
| 5.26 | > Aut      |          |        |   |       | > means the    |
|      | horization |          |        | N |       | > request is   |
|      | > Request  |          |        | A |       | > Token        |
|      | > (TAR)    |          |        |   |       | >              |
|      | >          |          |        |   |       |  authorization |
|      |  Indicator |          |        |   |       | > request.     |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Billing  | > NA     | > NA   | > | > 128 | > Full Billing |
| 5.27 | > Address  |          |        |   | > ANS | > Address of   |
|      |            |          |        | N |       | > the          |
|      |            |          |        | A |       | > Cardholder   |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Billing  | > NA     | > NA   | > | > 24  | > Full postal  |
| 5.28 | > Zip      |          |        |   | > ANS | > code of the  |
|      |            |          |        | N |       | > Customer     |
|      |            |          |        | A |       |                |
+------+------------+----------+--------+---+-------+----------------+
| > 1  | > Token    | > NA     | > NA   | > | > 1 N | > Token Status |
| 25.9 | > Status   |          |        |   |       |                |
|      |            |          |        | N |       |                |
|      |            |          |        | A |       |                |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > R        | > NA     | > NA   | > | > 4   | > Replacement  |
| 5.30 | eplacement |          |        |   | > ANS | > DPAN Expiry  |
|      | > DPAN     |          |        | N |       |                |
|      | > Expiry   |          |        | A |       |                |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > R        | > NA     | > NA   | > | > 19  | > Replacement  |
| 5.31 | eplacement |          |        |   | > ANS | > PAN          |
|      | > PAN      |          |        | N |       |                |
|      |            |          |        | A |       |                |
+------+------------+----------+--------+---+-------+----------------+
| > 12 | > Wallet   | > NA     | > NA   | > | > 5   | > Token Wallet |
| 5.32 | > Type     |          |        |   | > AN  | > Type         |
|      |            |          |        | N |       |                |
|      |            |          |        | A |       |                |
+------+------------+----------+--------+---+-------+----------------+

> **125.10 Possible values of device types**

![](./image15.png){width="5.348438320209974in"
height="7.6942705599300085in"}

+------+-----+-------------+------+----------------------------------+
| > ** |     |             |      |                                  |
| [Tag |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
|  [Le |     |             |      |                                  |
| ngth |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| > [V |     |             |      |                                  |
| alue |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
|  [Fo |     |             |      |                                  |
| rmat |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| [Con |     |             |      |                                  |
| tent |     |             |      |                                  |
| > of |     |             |      |                                  |
| > S  |     |             |      |                                  |
| ub-E |     |             |      |                                  |
| leme |     |             |      |                                  |
| nt]{ |     |             |      |                                  |
| .mar |     |             |      |                                  |
| k}** |     |             |      |                                  |
| >    |     |             |      |                                  |
| >    |     |             |      |                                  |
|  *** |     |             |      |                                  |
| [Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  01, |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Req |     |             |      |                                  |
| uest |     |             |      |                                  |
| > H  |     |             |      |                                  |
| eade |     |             |      |                                  |
| r]{. |     |             |      |                                  |
| mark |     |             |      |                                  |
| }*** |     |             |      |                                  |
| >    |     |             |      |                                  |
| >    |     |             |      |                                  |
| [Req |     |             |      |                                  |
| uest |     |             |      |                                  |
| > ID |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| > [A |     |             |      |                                  |
| > un |     |             |      |                                  |
| ique |     |             |      |                                  |
| > r  |     |             |      |                                  |
| efer |     |             |      |                                  |
| ence |     |             |      |                                  |
| >    |     |             |      |                                  |
|  for |     |             |      |                                  |
| >    |     |             |      |                                  |
| Requ |     |             |      |                                  |
| est. |     |             |      |                                  |
| >    |     |             |      |                                  |
| This |     |             |      |                                  |
| > sh |     |             |      |                                  |
| ould |     |             |      |                                  |
| > be |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| > [  |     |             |      |                                  |
| 1-64 |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| [TLV |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| [fre |     |             |      |                                  |
| shly |     |             |      |                                  |
| > g  |     |             |      |                                  |
| ener |     |             |      |                                  |
| ated |     |             |      |                                  |
| > by |     |             |      |                                  |
| >    |     |             |      |                                  |
|  the |     |             |      |                                  |
| > cl |     |             |      |                                  |
| ient |     |             |      |                                  |
| >    |     |             |      |                                  |
|  for |     |             |      |                                  |
| > e  |     |             |      |                                  |
| very |     |             |      |                                  |
| >    |     |             |      |                                  |
|  API |     |             |      |                                  |
| > C  |     |             |      |                                  |
| all. |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| > [  |     |             |      |                                  |
| This |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ena |     |             |      |                                  |
| bles |     |             |      |                                  |
| > ea |     |             |      |                                  |
| sier |     |             |      |                                  |
| >    |     |             |      |                                  |
|  tro |     |             |      |                                  |
| uble |     |             |      |                                  |
| shoo |     |             |      |                                  |
| ting |     |             |      |                                  |
| > of |     |             |      |                                  |
| > is |     |             |      |                                  |
| sues |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| >    |     |             |      |                                  |
| [bet |     |             |      |                                  |
| ween |     |             |      |                                  |
| >    |     |             |      |                                  |
|  the |     |             |      |                                  |
| >    |     |             |      |                                  |
|  MPP |     |             |      |                                  |
| >    |     |             |      |                                  |
|  and |     |             |      |                                  |
| >    |     |             |      |                                  |
|  the |     |             |      |                                  |
| >    |     |             |      |                                  |
|  NWP |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| > [  |     |             |      |                                  |
| 1-64 |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| [Ses |     |             |      |                                  |
| sion |     |             |      |                                  |
| > ID |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| [TLV |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| > [  |     |             |      |                                  |
| This |     |             |      |                                  |
| > is |     |             |      |                                  |
| > a  |     |             |      |                                  |
| > Un |     |             |      |                                  |
| ique |     |             |      |                                  |
| > Id |     |             |      |                                  |
| enti |     |             |      |                                  |
| fier |     |             |      |                                  |
| >    |     |             |      |                                  |
|  cre |     |             |      |                                  |
| ated |     |             |      |                                  |
| > by |     |             |      |                                  |
| >    |     |             |      |                                  |
|  the |     |             |      |                                  |
| >    |     |             |      |                                  |
|  MPP |     |             |      |                                  |
| > to |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| > [r |     |             |      |                                  |
| epre |     |             |      |                                  |
| sent |     |             |      |                                  |
| > a  |     |             |      |                                  |
| >    |     |             |      |                                  |
| prov |     |             |      |                                  |
| isio |     |             |      |                                  |
| ning |     |             |      |                                  |
| >    |     |             |      |                                  |
|  att |     |             |      |                                  |
| empt |     |             |      |                                  |
| >    |     |             |      |                                  |
|  for |     |             |      |                                  |
| > an |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Acc |     |             |      |                                  |
| ount |     |             |      |                                  |
| > on |     |             |      |                                  |
| > a  |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| [dev |     |             |      |                                  |
| ice. |     |             |      |                                  |
| > It |     |             |      |                                  |
| > is |     |             |      |                                  |
| >    |     |             |      |                                  |
| used |     |             |      |                                  |
| > to |     |             |      |                                  |
| >    |     |             |      |                                  |
|  tie |     |             |      |                                  |
| >    |     |             |      |                                  |
| toge |     |             |      |                                  |
| ther |     |             |      |                                  |
| >    |     |             |      |                                  |
|  the |     |             |      |                                  |
| >    |     |             |      |                                  |
| acti |     |             |      |                                  |
| vity |     |             |      |                                  |
| > ac |     |             |      |                                  |
| ross |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| 1.   |     |             |      |                                  |
| [the |     |             |      |                                  |
|      |     |             |      |                                  |
|  > d |     |             |      |                                  |
| iffe |     |             |      |                                  |
| rent |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| APIs |     |             |      |                                  |
|      |     |             |      |                                  |
| > up |     |             |      |                                  |
|      |     |             |      |                                  |
|  > u |     |             |      |                                  |
| ntil |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  the |     |             |      |                                  |
|      |     |             |      |                                  |
|  > p |     |             |      |                                  |
| oint |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| that |     |             |      |                                  |
|      |     |             |      |                                  |
|  > t |     |             |      |                                  |
| here |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  has |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| > [  |     |             |      |                                  |
| been |     |             |      |                                  |
| > a  |     |             |      |                                  |
| > su |     |             |      |                                  |
| cces |     |             |      |                                  |
| sful |     |             |      |                                  |
| > p  |     |             |      |                                  |
| rovi |     |             |      |                                  |
| sion |     |             |      |                                  |
| ing. |     |             |      |                                  |
| >    |     |             |      |                                  |
| Requ |     |             |      |                                  |
| ired |     |             |      |                                  |
| >    |     |             |      |                                  |
|  for |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| > [f |     |             |      |                                  |
| ollo |     |             |      |                                  |
| wing |     |             |      |                                  |
| >    |     |             |      |                                  |
| APIs |     |             |      |                                  |
| >    |     |             |      |                                  |
| only |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Acc |     |             |      |                                  |
| ount |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Eli |     |             |      |                                  |
| gibi |     |             |      |                                  |
| lity |     |             |      |                                  |
| > Ve |     |             |      |                                  |
| rify |     |             |      |                                  |
| >    |     |             |      |                                  |
| Card |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| > [P |     |             |      |                                  |
| rovi |     |             |      |                                  |
| sion |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Cre |     |             |      |                                  |
| dent |     |             |      |                                  |
| ials |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| -    |     |             |      |                                  |
| [OOB |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  Con |     |             |      |                                  |
| tact |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| Chan |     |             |      |                                  |
| nels |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| -    |     |             |      |                                  |
| [OOB |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  Con |     |             |      |                                  |
| tact |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  Cha |     |             |      |                                  |
| nnel |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| -    |     |             |      |                                  |
| [OOB |     |             |      |                                  |
|      |     |             |      |                                  |
| > Au |     |             |      |                                  |
| then |     |             |      |                                  |
| tica |     |             |      |                                  |
| tion |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| -    |     |             |      |                                  |
| [OOB |     |             |      |                                  |
|      |     |             |      |                                  |
| > Au |     |             |      |                                  |
| then |     |             |      |                                  |
| tica |     |             |      |                                  |
| tion |     |             |      |                                  |
|      |     |             |      |                                  |
| > Va |     |             |      |                                  |
| lida |     |             |      |                                  |
| tion |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| 2.   |     |             |      |                                  |
|  [16 |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| [Pro |     |             |      |                                  |
| gram |     |             |      |                                  |
|      |     |             |      |                                  |
| > ID |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| [TLV |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|  > [ |     |             |      |                                  |
| This |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  tag |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| cont |     |             |      |                                  |
| ains |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  the |     |             |      |                                  |
|      |     |             |      |                                  |
| > cu |     |             |      |                                  |
| mula |     |             |      |                                  |
| tive |     |             |      |                                  |
|      |     |             |      |                                  |
|  > c |     |             |      |                                  |
| ount |     |             |      |                                  |
|      |     |             |      |                                  |
| > of |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| > [  |     |             |      |                                  |
| tran |     |             |      |                                  |
| sact |     |             |      |                                  |
| ions |     |             |      |                                  |
| >    |     |             |      |                                  |
|  for |     |             |      |                                  |
| >    |     |             |      |                                  |
|  the |     |             |      |                                  |
| >    |     |             |      |                                  |
|  cur |     |             |      |                                  |
| rent |     |             |      |                                  |
| >    |     |             |      |                                  |
|  lim |     |             |      |                                  |
| ited |     |             |      |                                  |
| -use |     |             |      |                                  |
| >    |     |             |      |                                  |
|  key |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
|  [(L |     |             |      |                                  |
| UK). |     |             |      |                                  |
| This |     |             |      |                                  |
| > is |     |             |      |                                  |
| > a  |     |             |      |                                  |
| > un |     |             |      |                                  |
| ique |     |             |      |                                  |
| > id |     |             |      |                                  |
| enti |     |             |      |                                  |
| fier |     |             |      |                                  |
| >    |     |             |      |                                  |
| that |     |             |      |                                  |
| > id |     |             |      |                                  |
| enti |     |             |      |                                  |
| fies |     |             |      |                                  |
| >    |     |             |      |                                  |
|  the |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| [pro |     |             |      |                                  |
| duct |     |             |      |                                  |
| >    |     |             |      |                                  |
|  and |     |             |      |                                  |
| >    |     |             |      |                                  |
|  the |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ins |     |             |      |                                  |
| titu |     |             |      |                                  |
| tion |     |             |      |                                  |
| > p  |     |             |      |                                  |
| arti |     |             |      |                                  |
| cipa |     |             |      |                                  |
| ting |     |             |      |                                  |
| > in |     |             |      |                                  |
| >    |     |             |      |                                  |
|  the |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| [sch |     |             |      |                                  |
| eme. |     |             |      |                                  |
| >    |     |             |      |                                  |
|  The |     |             |      |                                  |
| > v  |     |             |      |                                  |
| alue |     |             |      |                                  |
| > to |     |             |      |                                  |
| > be |     |             |      |                                  |
| >    |     |             |      |                                  |
| sent |     |             |      |                                  |
| >    |     |             |      |                                  |
| will |     |             |      |                                  |
| > be |     |             |      |                                  |
| >    |     |             |      |                                  |
| prov |     |             |      |                                  |
| ided |     |             |      |                                  |
| > by |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| > [  |     |             |      |                                  |
| NWP. |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
| >    |     |             |      |                                  |
| >    |     |             |      |                                  |
|  *** |     |             |      |                                  |
| [Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  02, |     |             |      |                                  |
| >    |     |             |      |                                  |
| User |     |             |      |                                  |
| > Co |     |             |      |                                  |
| ntex |     |             |      |                                  |
| t]{. |     |             |      |                                  |
| mark |     |             |      |                                  |
| }*** |     |             |      |                                  |
|      |     |             |      |                                  |
| 1.   |     |             |      |                                  |
|   [1 |     |             |      |                                  |
| -100 |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  [Wa |     |             |      |                                  |
| llet |     |             |      |                                  |
|      |     |             |      |                                  |
| > ID |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| [TLV |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| [The |     |             |      |                                  |
|      |     |             |      |                                  |
| > Wa |     |             |      |                                  |
| llet |     |             |      |                                  |
|      |     |             |      |                                  |
| > ID |     |             |      |                                  |
|      |     |             |      |                                  |
| > pa |     |             |      |                                  |
| ssed |     |             |      |                                  |
|      |     |             |      |                                  |
| > in |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  the |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  req |     |             |      |                                  |
| uest |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  [02 |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|  > [ |     |             |      |                                  |
| 1-64 |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  [De |     |             |      |                                  |
| vice |     |             |      |                                  |
|      |     |             |      |                                  |
| > ID |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| [TLV |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| [The |     |             |      |                                  |
|      |     |             |      |                                  |
| > De |     |             |      |                                  |
| vice |     |             |      |                                  |
|      |     |             |      |                                  |
| > ID |     |             |      |                                  |
|      |     |             |      |                                  |
| > pa |     |             |      |                                  |
| ssed |     |             |      |                                  |
|      |     |             |      |                                  |
| > in |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  the |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  req |     |             |      |                                  |
| uest |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  [03 |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| > [1 |     |             |      |                                  |
| -100 |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|  > [ |     |             |      |                                  |
| User |     |             |      |                                  |
|      |     |             |      |                                  |
| > ID |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| [TLV |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| [The |     |             |      |                                  |
|      |     |             |      |                                  |
|   >  |     |             |      |                                  |
| User |     |             |      |                                  |
|      |     |             |      |                                  |
| > ID |     |             |      |                                  |
|      |     |             |      |                                  |
| > pa |     |             |      |                                  |
| ssed |     |             |      |                                  |
|      |     |             |      |                                  |
| > in |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  the |     |             |      |                                  |
|      |     |             |      |                                  |
|    > |     |             |      |                                  |
|  req |     |             |      |                                  |
| uest |     |             |      |                                  |
| ]{.m |     |             |      |                                  |
| ark} |     |             |      |                                  |
|      |     |             |      |                                  |
| > ** |     |             |      |                                  |
| [Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  03, |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Acc |     |             |      |                                  |
| ount |     |             |      |                                  |
| >    |     |             |      |                                  |
|  Eli |     |             |      |                                  |
| gibi |     |             |      |                                  |
| lity |     |             |      |                                  |
| > C  |     |             |      |                                  |
| onte |     |             |      |                                  |
| xt]{ |     |             |      |                                  |
| .mar |     |             |      |                                  |
| k}** |     |             |      |                                  |
+======+=====+=============+======+==================================+
| >    | > [ | > [Terms &  | >    | > [The identifier for the        |
|  [01 | 1-6 | > Condit    | [TLV | > version of the terms           |
| ]{.m | 4]{ | ion]{.mark} | ]{.m | > and]{.mark} [conditions that   |
| ark} | .ma | >           | ark} | > are to be accepted by the user |
|      | rk} | [ID]{.mark} |      | > during]{.mark} [this provision |
|      |     |             |      | > cycle. The actual T&Cs are     |
|      |     |             |      | > retrieved]{.mark} [by calling  |
|      |     |             |      | > the Resource API.]{.mark}      |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Terms &  | >    | > [This Tag Contains the Terms   |
|  [02 | 1-6 | > Condit    | [TLV | > and Condition]{.mark}          |
| ]{.m | 4]{ | ion]{.mark} | ]{.m | > [Accepted Date]{.mark}         |
| ark} | .ma | > [Accepted | ark} |                                  |
|      | rk} | > D         |      |                                  |
|      |     | ate]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [         | >    | > [The Primary Account Number    |
|  [03 |  [1 | PAN]{.mark} | [TLV | > representing the]{.mark}       |
| ]{.m | 9]{ |             | ]{.m | > [Account that is to be boarded |
| ark} | .ma |             | ark} | > onto the wallet.]{.mark}       |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [PAN      | >    |                                  |
|  [04 | 4]{ | >           | [TLV |                                  |
| ]{.m | .ma |  ID]{.mark} | ]{.m |                                  |
| ark} | rk} |             | ark} |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Expiry   | >    | > [The Expiry Date of the card   |
|  [05 | 3]{ | > D         | [TLV | > in format *MMYY.*]{.mark}      |
| ]{.m | .ma | ate]{.mark} | ]{.m |                                  |
| ark} | rk} |             | ark} |                                  |
+------+-----+-------------+------+----------------------------------+

+------+-----+-------------+------+----------------------------------+
| >    | > [ | >           | >    | > [Full name of the Cardholder.  |
|  [06 | 1-6 | [CardHolder | [TLV | > The Cardholder name]{.mark}    |
| ]{.m | 4]{ | > N         | ]{.m | > [can contain special           |
| ark} | .ma | ame]{.mark} | ark} | > characters such as             |
|      | rk} |             |      | > diacritic]{.mark} [marks       |
|      |     |             |      | > (umlauts, cedillas, accents)   |
|      |     |             |      | > or Emoji]{.mark} [characters   |
|      |     |             |      | > so it is difficult to restrict |
|      |     |             |      | > the values on]{.mark} [this.   |
|      |     |             |      | > The transport will validate    |
|      |     |             |      | > that it is a UTF-8]{.mark}     |
|      |     |             |      | > [character.]{.mark}            |
+======+=====+=============+======+==================================+
| >    | >   | > [Billing  | >    | > [Full Billing Address of the   |
|  [07 | [12 | > Addr      | [TLV | > Cardholder]{.mark}             |
| ]{.m | 8]{ | ess]{.mark} | ]{.m |                                  |
| ark} | .ma |             | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [Billing  | >    | > [Full Billing Zip of the       |
|  [08 |  [2 | > Postal    | [TLV | > Customer]{.mark}               |
| ]{.m | 4]{ | > C         | ]{.m |                                  |
| ark} | .ma | ode]{.mark} | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [Sou      | >    | > [This indicates which method   |
|  [09 |  [2 | rce]{.mark} | [TLV | > was used to capture the        |
| ]{.m | 0]{ |             | ]{.m | > user]{.mark} [information that |
| ark} | .ma |             | ark} | > is being sent.                 |
|      | rk} |             |      | > \"add-device\" - Provision     |
|      |     |             |      | > a]{.mark} [companion device    |
|      |     |             |      | > using the details of a         |
|      |     |             |      | > previously]{.mark}             |
|      |     |             |      | > [provisioned device            |
|      |     |             |      | > \"in-app\" - This is set when  |
|      |     |             |      | > the]{.mark} [provision Request |
|      |     |             |      | > is initiated from Card Mobile  |
|      |     |             |      | > app \"on-]{.mark} [file\" -    |
|      |     |             |      | > This is set when the account   |
|      |     |             |      | > is already present]{.mark}     |
|      |     |             |      | > [\"restore\" -- This is set    |
|      |     |             |      | > when is provision is initiated |
|      |     |             |      | > as a]{.mark} [result of        |
|      |     |             |      | > restore of previously          |
|      |     |             |      | > provisioned pan. E.g., a       |
|      |     |             |      | > new]{.mark} [device registered |
|      |     |             |      | > with wallet account with       |
|      |     |             |      | > previously]{.mark}             |
|      |     |             |      | > [digitalized pan.              |
|      |     |             |      | > \"user-input\" -- User         |
|      |     |             |      | > manually]{.mark}               |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [Capture  | >    | [Capture Method]{.mark}          |
|  [0A | 1]{ | > Met       | [TLV |                                  |
| ]{.m | .ma | hod]{.mark} | ]{.m | -   [Camera]{.mark}              |
| ark} | rk} |             | ark} |                                  |
|      |     |             |      | -   [Manual]{.mark}              |
+------+-----+-------------+------+----------------------------------+
| > ** |     |             |      |                                  |
| [Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  04, |     |             |      |                                  |
| > De |     |             |      |                                  |
| vice |     |             |      |                                  |
| > C  |     |             |      |                                  |
| onte |     |             |      |                                  |
| xt]{ |     |             |      |                                  |
| .mar |     |             |      |                                  |
| k}** |     |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Device bluetooth MAC address  |
|  [01 | 1-6 | > blueto    | [TLV | > (e.g., 00-16-68 or]{.mark}     |
| ]{.m | 4]{ | oth]{.mark} | ]{.m | > [00-16-68-2B-40-90 or          |
| ark} | .ma | > [         | ark} | > 00:16:68:2B:40:90 or]{.mark}   |
|      | rk} | mac]{.mark} |      | >                                |
|      |     |             |      | > [0016682B4090 or               |
|      |     |             |      | > 00.16.68.2B.40.90)]{.mark}     |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Brand of the device. Eg.      |
|  [02 | 1-6 | > br        | [TLV | > \"Google\" for nexus           |
| ]{.m | 4]{ | and]{.mark} | ]{.m | > devices]{.mark}                |
| ark} | .ma |             | ark} | >                                |
|      | rk} |             |      | > [,\"Samsung\" for Samsung      |
|      |     |             |      | > devices]{.mark}                |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Country where the device was  |
|  [03 | 2]{ | > coun      | [TLV | > purchased (iso 3166-]{.mark}   |
| ]{.m | .ma | try]{.mark} | ]{.m | > [1 alpha-2)]{.mark}            |
| ark} | rk} |             | ark} |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [device   | >    | > [Type of the device id from    |
|  [04 |  [6 | > id        | [TLV | > which it is sources. E.g.,     |
| ]{.m | 4]{ | > t         | ]{.m | > TEE]{.mark}                    |
| ark} | .ma | ype]{.mark} | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [device   | >    | > [IP Address of the             |
|  [05 |  [1 | >           | [TLV | > device]{.mark}                 |
| ]{.m | 5-3 |  ip]{.mark} | ]{.m |                                  |
| ark} | 2]{ |             | ark} |                                  |
|      | .ma |             |      |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Mobile Manufacturer (Google,  |
|  [06 | 1-6 | > manufactu | [TLV | > Samsung etc)]{.mark}           |
| ]{.m | 4]{ | rer]{.mark} | ]{.m |                                  |
| ark} | .ma |             | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Device Model (Galaxy 56,LG,   |
|  [07 | 1-6 | > mo        | [TLV | > G4, HTC etc)]{.mark}           |
| ]{.m | 4]{ | del]{.mark} | ]{.m |                                  |
| ark} | .ma |             | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [device   | >    | > [User Assigned Device          |
|  [08 |  [1 | > n         | [TLV | > Name]{.mark}                   |
| ]{.m | -10 | ame]{.mark} | ]{.m |                                  |
| ark} | 0]{ |             | ark} |                                  |
|      | .ma |             |      |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Device OS build version       |
|  [09 | 1-6 | > os        | [TLV | > (9.3.2, 4.1.1. etc)]{.mark}    |
| ]{.m | 4]{ | > bu        | ]{.m |                                  |
| ark} | .ma | ild]{.mark} | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Device OS type (Android,      |
|  [10 | 1-6 | > os        | [TLV | > Windows, Symbian etc)]{.mark}  |
| ]{.m | 4]{ | > t         | ]{.m |                                  |
| ark} | .ma | ype]{.mark} | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Mobile operating system       |
|  [11 | 1-3 | > os        | [TLV | > version (Android               |
| ]{.m | 2]{ | > vers      | ]{.m | > 4.4.2,]{.mark} [Kitkat 5.0.3,  |
| ark} | .ma | ion]{.mark} | ark} | > etc\...)]{.mark}               |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Device time zone. example:    |
|  [12 | 1-3 | > time      | [TLV | > \"GMT-08:00\"]{.mark}          |
| ]{.m | 2]{ | > z         | ]{.m |                                  |
| ark} | .ma | one]{.mark} | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+

+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [true if user lets timezone be |
|  [13 | 4-3 | > time      | [TLV | > set timezone Network,]{.mark}  |
| ]{.m | 5]{ | > z         | ]{.m | > [false if user set own         |
| ark} | .ma | one]{.mark} | ark} | > timezone.]{.mark}              |
|      | rk} | > [setti    |      |                                  |
|      |     | ngs]{.mark} |      |                                  |
+======+=====+=============+======+==================================+
| >    | >   | > [device   | >    | > [Type of device]{.mark}        |
|  [14 | [1- | > t         | [TLV | >                                |
| ]{.m | 3]{ | ype]{.mark} | ]{.m | > [1 -- Mobile]{.mark}           |
| ark} | .ma |             | ark} | >                                |
|      | rk} |             |      | > [2 -- Tablet]{.mark}           |
|      |     |             |      | >                                |
|      |     |             |      | > [3 -- Watch 2]{.mark}          |
|      |     |             |      | >                                |
|      |     |             |      | > [5 -- Phone_Tablet]{.mark}     |
|      |     |             |      | >                                |
|      |     |             |      | > [6 -- PC/Mac]{.mark}           |
|      |     |             |      | >                                |
|      |     |             |      | > [7 - Cloud]{.mark}             |
|      |     |             |      | >                                |
|      |     |             |      | > [99 -- Other]{.mark}           |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [device   | >    | > [Device User ID]{.mark}        |
|  [15 | 1-2 | > user      | [TLV |                                  |
| ]{.m | 0]{ | >           | ]{.m |                                  |
| ark} | .ma |  id]{.mark} | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [i        | >    | > [Last 2 or 4 digits. Issuer    |
|  [16 | [2- | me]{.mark}i | [TLV | > app can query for IMEI /       |
| ]{.m | 4]{ |             | ]{.m | > MEID]{.mark} [through standard |
| ark} | .ma |             | ark} | > android API. Issuer can then   |
|      | rk} |             |      | > compare]{.mark} [their         |
|      |     |             |      | > independently derived          |
|      |     |             |      | > knowledge of the               |
|      |     |             |      | > IMEI/MEID]{.mark} [to the last |
|      |     |             |      | > 2 or 4 characters that are     |
|      |     |             |      | > sent. Customer]{.mark}         |
|      |     |             |      | > [service can use IMEI last 2   |
|      |     |             |      | > or 4 characters in             |
|      |     |             |      | > support]{.mark} [scenarios to  |
|      |     |             |      | > verify they are speaking with  |
|      |     |             |      | > the holder of the]{.mark}      |
|      |     |             |      | > [device, and to disambiguate a |
|      |     |             |      | > device.]{.mark}                |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [langu    | >    | > [Code for identifying the      |
|  [17 |  [1 | age]{.mark} | [TLV | > device language. Based         |
| ]{.m | 0]{ |             | ]{.m | > on]{.mark} [IEFT BCP 47. If    |
| ark} | .ma |             | ark} | > not provided, this will be     |
|      | rk} |             |      | > defaulted]{.mark} [to          |
|      |     |             |      | > en-US.]{.mark}                 |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [latit    | >    | > [Coordinates (latitude) of the |
|  [18 | 1-1 | ude]{.mark} | [TLV | > device when it is              |
| ]{.m | 6]{ |             | ]{.m | > being]{.mark}                  |
| ark} | .ma |             | ark} | > [provisioned]{.mark}           |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [location | >    | > [Source from which location of |
|  [19 | 1-6 | > sou       | [TLV | > the device is                  |
| ]{.m | 4]{ | rce]{.mark} | ]{.m | > identified]{.mark} [e.g.,      |
| ark} | .ma |             | ark} | > WiFi, Cellular, GPS]{.mark}    |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [longit   | >    | > [Coordinates (longitude) of    |
|  [20 | 1-1 | ude]{.mark} | [TLV | > the device when it is          |
| ]{.m | 6]{ |             | ]{.m | > being]{.mark}                  |
| ark} | .ma |             | ark} | > [provisioned]{.mark}           |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [parent   | >    | > [A stable persistent hardware  |
|  [21 | 5-6 | > device    | [TLV | > identifier of the              |
| ]{.m | 4]{ | >           | ]{.m | > parent]{.mark} [device that    |
| ark} | .ma |  id]{.mark} | ark} | > survives factory resets (e.g., |
|      | rk} |             |      | > Device id of]{.mark} [the      |
|      |     |             |      | > phone when watch is            |
|      |     |             |      | > provisioned)]{.mark}           |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [phone    | >    | > [User phone number if          |
|  [22 | 4]{ | > num       | [TLV | > available (Last)]{.mark}       |
| ]{.m | .ma | ber]{.mark} | ]{.m |                                  |
| ark} | rk} |             | ark} |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [serial   | >    | > [The last 2 to 4 digits of the |
|  [23 | [2- | > num       | [TLV | > device Serial number]{.mark}   |
| ]{.m | 4]{ | ber]{.mark} | ]{.m |                                  |
| ark} | .ma |             | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| > ** |     |             |      |                                  |
| [Dat |     |             |      |                                  |
| aset |     |             |      |                                  |
| >    |     |             |      |                                  |
|  ID: |     |             |      |                                  |
| >    |     |             |      |                                  |
|  05, |     |             |      |                                  |
| >    |     |             |      |                                  |
| User |     |             |      |                                  |
| > P  |     |             |      |                                  |
| rovi |     |             |      |                                  |
| sion |     |             |      |                                  |
| > C  |     |             |      |                                  |
| onte |     |             |      |                                  |
| xt]{ |     |             |      |                                  |
| .mar |     |             |      |                                  |
| k}** |     |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [email    | >    | > [Device profile email Address. |
|  [01 |  [1 | > addr      | [TLV | > This will be                   |
| ]{.m | -30 | ess]{.mark} | ]{.m | > obfuscated]{.mark} [if         |
| ark} | 0]{ |             | ark} | > supplied.]{.mark}              |
|      | .ma |             |      |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | >   | > [email    | >    | > [Age of profile email id in    |
|  [02 | [1- | > address   | [TLV | > weeks]{.mark}                  |
| ]{.m | 4]{ | >           | ]{.m |                                  |
| ark} | .ma | age]{.mark} | ark} |                                  |
|      | rk} |             |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [email    | >    | > [Country of device at time of  |
|  [03 | 2]{ | > addr      | [TLV | > provisioning (iso              |
| ]{.m | .ma | ess]{.mark} | ]{.m | > 3166-1]{.mark}                 |
| ark} | rk} | > [coun     | ark} | > [alpha-2)]{.mark}              |
|      |     | try]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+
| >    | > [ | > [hashed   | >    | > [Hashed Email Address /        |
|  [04 | 1-6 | > em        | [TLV | > Account Id]{.mark}             |
| ]{.m | 4]{ | ail]{.mark} | ]{.m |                                  |
| ark} | .ma | > [addr     | ark} |                                  |
|      | rk} | ess]{.mark} |      |                                  |
+------+-----+-------------+------+----------------------------------+

+------+-----+--------------+----+-----------------------------------+
| > ** |     |              |    |                                   |
| [Dat |     |              |    |                                   |
| aset |     |              |    |                                   |
| >    |     |              |    |                                   |
|  ID: |     |              |    |                                   |
| >    |     |              |    |                                   |
|  06, |     |              |    |                                   |
| >    |     |              |    |                                   |
| Risk |     |              |    |                                   |
| > C  |     |              |    |                                   |
| onte |     |              |    |                                   |
| xt]{ |     |              |    |                                   |
| .mar |     |              |    |                                   |
| k}** |     |              |    |                                   |
+======+=====+==============+====+===================================+
| >    | > [ | > [account   | >  | > [MPP risk rating based on       |
|  [01 | 1]{ | >            | [T | > experience with the]{.mark}     |
| ]{.m | .ma | risk]{.mark} | LV | > [customer account. Numeric      |
| ark} | rk} |              | ]{ | > score from 1-5.]{.mark} [1 --   |
|      |     |              | .m | > Highest Risk, Lowest            |
|      |     |              | ar | > Confidence.]{.mark}             |
|      |     |              | k} | >                                 |
|      |     |              |    | > [5 -- Lowest Risk, Highest      |
|      |     |              |    | > Confidence.]{.mark}             |
+------+-----+--------------+----+-----------------------------------+
| >    | > [ | > [device    | >  | > [MPP risk rating based on       |
|  [02 | 1]{ | >            | [T | > experience with the             |
| ]{.m | .ma | risk]{.mark} | LV | > device]{.mark} [being           |
| ark} | rk} |              | ]{ | > provisioned. Numeric score from |
|      |     |              | .m | > 1-5.]{.mark}                    |
|      |     |              | ar | >                                 |
|      |     |              | k} | > [1 -- Highest Risk, Lowest      |
|      |     |              |    | > Confidence.]{.mark} [5 --       |
|      |     |              |    | > Lowest Risk, Highest            |
|      |     |              |    | > Confidence.]{.mark}             |
+------+-----+--------------+----+-----------------------------------+
| >    | > [ | > [          | >  | > [MPP risk rating based on       |
|  [03 | 1-1 | provisioning | [T | > experience with the]{.mark}     |
| ]{.m | 0]{ | >            | LV | > [customer and device being      |
| ark} | .ma | risk]{.mark} | ]{ | > provisioned. Possible]{.mark}   |
|      | rk} |              | .m | > [values are]{.mark}             |
|      |     |              | ar | >                                 |
|      |     |              | k} | > [GREEN]{.mark} [YELLOW]{.mark}  |
|      |     |              |    | > [ORANGE]{.mark} [RED]{.mark}    |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [age of    | >  | > [Number of weeks since the      |
|  [04 | [1- | > device     | [T | > device was used by the]{.mark}  |
| ]{.m | 2]{ | > u          | LV | > [wallet account. Max value is   |
| ark} | .ma | sage]{.mark} | ]{ | > 99.]{.mark}                     |
|      | rk} | > [by        | .m |                                   |
|      |     | > acc        | ar |                                   |
|      |     | ount]{.mark} | k} |                                   |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [age of    | >  | > [Number of weeks since last     |
|  [05 | [1- | > last       | [T | > activity by the wallet]{.mark}  |
| ]{.m | 2]{ | > acc        | LV | > [account (provision, refresh,   |
| ark} | .ma | ount]{.mark} | ]{ | > lifecycle events from           |
|      | rk} | > [acti      | .m | > the]{.mark} [wallet account     |
|      |     | vity]{.mark} | ar | > across Networks/Issuers). Max   |
|      |     |              | k} | > value]{.mark} [is 99.]{.mark}   |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [age of    | >  | > [Number of weeks since the last |
|  [06 | [1- | > last       | [T | > change to the wallet]{.mark}    |
| ]{.m | 2]{ | > acc        | LV | > [account. Max value is          |
| ark} | .ma | ount]{.mark} | ]{ | > 99.]{.mark}                     |
|      | rk} | > [ch        | .m |                                   |
|      |     | ange]{.mark} | ar |                                   |
|      |     |              | k} |                                   |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [age of    | >  | > [Number of weeks since another  |
|  [07 | [1- | > token      | [T | > card from the same]{.mark}      |
| ]{.m | 4]{ | ized]{.mark} | LV | > [issuer was tokenized on a      |
| ark} | .ma | > [          | ]{ | > device. Max value is]{.mark}    |
|      | rk} | card]{.mark} | .m | > [9999.]{.mark}                  |
|      |     |              | ar |                                   |
|      |     |              | k} |                                   |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [age of    | >  | > [Age of user's financial        |
|  [08 | [1- | > wa         | [T | > relationship with               |
| ]{.m | 4]{ | llet]{.mark} | LV | > mobile]{.mark} [platform (in    |
| ark} | .ma | > [acc       | ]{ | > weeks)]{.mark}                  |
|      | rk} | ount]{.mark} | .m |                                   |
|      |     |              | ar |                                   |
|      |     |              | k} |                                   |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [card on   | >  | > [Age of card on file (in        |
|  [09 | [1- | > file       | [T | > weeks). Applicable only         |
| ]{.m | 4]{ | > te         | LV | > for]{.mark} [card-on file use   |
| ark} | .ma | nure]{.mark} | ]{ | > cases]{.mark}                   |
|      | rk} |              | .m |                                   |
|      |     |              | ar |                                   |
|      |     |              | k} |                                   |
+------+-----+--------------+----+-----------------------------------+
| >    | > [ | > [country   | >  | > [Country of device at time of   |
|  [0A | 2]{ | > du         | [T | > provisioning (iso               |
| ]{.m | .ma | ring]{.mark} | LV | > 3166-1]{.mark}                  |
| ark} | rk} | > [provi     | ]{ | > [alpha-2)]{.mark}               |
|      |     | sion]{.mark} | .m |                                   |
|      |     |              | ar |                                   |
|      |     |              | k} |                                   |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [number of | >  | > [Number of Tokens for the       |
|  [0B | [1- | > to         | [T | > wallet account across]{.mark}   |
| ]{.m | 3]{ | kens]{.mark} | LV | > [devices. Max value is          |
| ark} | .ma | > [acc       | ]{ | > 999.]{.mark}                    |
|      | rk} | ount]{.mark} | .m |                                   |
|      |     |              | ar |                                   |
|      |     |              | k} |                                   |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [number of | >  | > [Number of Tokens on physical   |
|  [0C | [1- | > to         | [T | > device.]{.mark}                 |
| ]{.m | 3]{ | kens]{.mark} | LV |                                   |
| ark} | .ma | > [de        | ]{ |                                   |
|      | rk} | vice]{.mark} | .m |                                   |
|      |     |              | ar |                                   |
|      |     |              | k} |                                   |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [suspended | >  | > [Number of suspended Tokens in  |
|  [0D | [1- | > to         | [T | > the wallet account.]{.mark}     |
| ]{.m | 2]{ | kens]{.mark} | LV | > [Max value is 99.]{.mark}       |
| ark} | .ma | > [in        | ]{ |                                   |
|      | rk} | > acc        | .m |                                   |
|      |     | ount]{.mark} | ar |                                   |
|      |     |              | k} |                                   |
+------+-----+--------------+----+-----------------------------------+
| >    | >   | > [total     | >  | > [Number of provisioning         |
|  [0E | [1- | > provisio   | [T | > attempts on the device          |
| ]{.m | 2]{ | ning]{.mark} | LV | > for]{.mark}                     |
| ark} | .ma |              | ]{ |                                   |
|      | rk} |              | .m |                                   |
|      |     |              | ar |                                   |
|      |     |              | k} |                                   |
+------+-----+--------------+----+-----------------------------------+

+-----+-----+--------------+-----+-----------------------------------+
|     |     | > [atte      |     | > [the last 24 hours. Max value   |
|     |     | mpts]{.mark} |     | > is 99.]{.mark}                  |
+=====+=====+==============+=====+===================================+
| >   | >   | > [total     | >   | > [Total number of transaction    |
|  [1 | [1- | > transac    | [TL | > count by the wallet]{.mark}     |
| 1]{ | 4]{ | tion]{.mark} | V]{ | > [account in the past 12 months  |
| .ma | .ma | > [count for | .ma | > (at the account level]{.mark}   |
| rk} | rk} | >            | rk} | > [across devices, Networks,      |
|     |     | year]{.mark} |     | > partners etc). Max              |
|     |     |              |     | > value]{.mark} [is 9999.]{.mark} |
+-----+-----+--------------+-----+-----------------------------------+
| >   | >   | > [risk      | >   | > [MPP identified risk reason     |
|  [1 | [1- | > reason     | [TL | > code for identifying]{.mark}    |
| 2]{ | 3]{ | >            | V]{ | > [provision risk color.]{.mark}  |
| .ma | .ma | code]{.mark} | .ma |                                   |
| rk} | rk} |              | rk} |                                   |
+-----+-----+--------------+-----+-----------------------------------+
| > * |     |              |     |                                   |
| *[D |     |              |     |                                   |
| ata |     |              |     |                                   |
| set |     |              |     |                                   |
| >   |     |              |     |                                   |
| ID: |     |              |     |                                   |
| >   |     |              |     |                                   |
| 06, |     |              |     |                                   |
| >   |     |              |     |                                   |
|  To |     |              |     |                                   |
| ken |     |              |     |                                   |
| >   |     |              |     |                                   |
|  Co |     |              |     |                                   |
| nte |     |              |     |                                   |
| xt] |     |              |     |                                   |
| {.m |     |              |     |                                   |
| ark |     |              |     |                                   |
| }** |     |              |     |                                   |
+-----+-----+--------------+-----+-----------------------------------+
| >   | >   | > [t         | >   | > [The tokenized Account Number   |
|  [0 |  [1 | oken]{.mark} | [TL | > representing the]{.mark}        |
| 1]{ | 2-1 |              | V]{ | > [Account that is to be boarded  |
| .ma | 9]{ |              | .ma | > onto the wallet. This           |
| rk} | .ma |              | rk} | > is]{.mark} [the Account Number  |
|     | rk} |              |     | > that will used for              |
|     |     |              |     | > tokenized]{.mark}               |
|     |     |              |     | > [Transactions.]{.mark}          |
+-----+-----+--------------+-----+-----------------------------------+
| >   | > [ | > [Token     | >   | > [The expiry Date of the Token   |
|  [0 | 4]{ | > expiry     | [TL | > in format MMYY.]{.mark}         |
| 2]{ | .ma | >            | V]{ |                                   |
| .ma | rk} | Date]{.mark} | .ma |                                   |
| rk} |     |              | rk} |                                   |
+-----+-----+--------------+-----+-----------------------------------+
| >   | >   | > [Token     | >   | > [This is an opaque identifier   |
|  [0 |  [3 | > id]{.mark} | [TL | > for the Token in the]{.mark}    |
| 3]{ | 2-6 |              | V]{ | > [wallet associated with the     |
| .ma | 4]{ |              | .ma | > programId.]{.mark}              |
| rk} | .ma |              | rk} |                                   |
|     | rk} |              |     |                                   |
+-----+-----+--------------+-----+-----------------------------------+
| >   | > [ | > [Token     | >   | > [A classification of the type   |
|  [0 | 2]{ | >            | [TL | > of Token being passed]{.mark}   |
| 4]{ | .ma | type]{.mark} | V]{ | > [01 - Card on File (individual  |
| .ma | rk} |              | .ma | > Merchant)]{.mark}               |
| rk} |     |              | rk} | >                                 |
|     |     |              |     | > [04 -- CBP (Cloud Based         |
|     |     |              |     | > Payment)]{.mark}                |
+-----+-----+--------------+-----+-----------------------------------+
| >   | > [ | > [Selected  | >   | > [Unique identifier of the       |
|  [0 | 1-3 | > cha        | [TL | > out-of-band contact             |
| 5]{ | 2]{ | nnel]{.mark} | V]{ | > channel]{.mark} [selected by    |
| .ma | .ma | > [identi    | .ma | > the user. This is the value of  |
| rk} | rk} | fier]{.mark} | rk} | > one of the]{.mark} [identifiers |
|     |     |              |     | > returned in the                 |
|     |     |              |     | > getOOBContactChannels]{.mark}   |
|     |     |              |     | > [Response.]{.mark}              |
+-----+-----+--------------+-----+-----------------------------------+

# Data Element 109 -- Advice Reason Code Table {#data-element-109-advice-reason-code-table .unnumbered}

+-----------+---+------------+---+------+---+---------+---+----------------+
| > **Sub   |   |            |   |      |   |         |   |                |
| >         |   |            |   |      |   |         |   |                |
|  Elements |   |            |   |      |   |         |   |                |
| > of DE   |   |            |   |      |   |         |   |                |
| > 109     |   |            |   |      |   |         |   |                |
| > when    |   |            |   |      |   |         |   |                |
| > DE63.7  |   |            |   |      |   |         |   |                |
| > =       |   |            |   |      |   |         |   |                |
| > 'MA     |   |            |   |      |   |         |   |                |
| STERCARD' |   |            |   |      |   |         |   |                |
| > and     |   |            |   |      |   |         |   |                |
| > 48.9 =  |   |            |   |      |   |         |   |                |
| > 'SMS'** |   |            |   |      |   |         |   |                |
+===========+===+============+===+======+===+=========+===+================+
| > **Sub   |   | > **Field  | > |      |   | > **Pos |   | > **Format**   |
| > Field   |   | > Name**   |   |      |   | ition** |   |                |
| > No**    |   |            | * |      |   |         |   |                |
|           |   |            | * |      |   |         |   |                |
|           |   |            | M |      |   |         |   |                |
|           |   |            | C |      |   |         |   |                |
|           |   |            | > |      |   |         |   |                |
|           |   |            |   |      |   |         |   |                |
|           |   |            | B |      |   |         |   |                |
|           |   |            | i |      |   |         |   |                |
|           |   |            | t |      |   |         |   |                |
|           |   |            | > |      |   |         |   |                |
|           |   |            |   |      |   |         |   |                |
|           |   |            | N |      |   |         |   |                |
|           |   |            | o |      |   |         |   |                |
|           |   |            | * |      |   |         |   |                |
|           |   |            | * |      |   |         |   |                |
+-----------+---+------------+---+------+---+---------+---+----------------+
| > 109.1   |   | > Message  | > |      |   | > 1-3   |   | > 3N           |
|           |   | > Reason   |   |      |   |         |   |                |
|           |   | > Code     | 6 |      |   |         |   |                |
|           |   |            | 0 |      |   |         |   |                |
|           |   |            | . |      |   |         |   |                |
|           |   |            | 1 |      |   |         |   |                |
+-----------+---+------------+---+------+---+---------+---+----------------+
| > 109.2   |   | > Message  | > |      |   | > 4-7   |   | > 4N           |
|           |   | > Reason   |   |      |   |         |   |                |
|           |   | > Code     | 6 |      |   |         |   |                |
|           |   | > Detail   | 0 |      |   |         |   |                |
|           |   |            | . |      |   |         |   |                |
|           |   |            | 2 |      |   |         |   |                |
+-----------+---+------------+---+------+---+---------+---+----------------+
| > 109.3   |   | > Detail   | > |      |   | > 8-60  |   | > 53 ANS       |
|           |   | > Text     |   |      |   |         |   |                |
|           |   |            | 6 |      |   |         |   |                |
|           |   |            | 0 |      |   |         |   |                |
|           |   |            | . |      |   |         |   |                |
|           |   |            | 3 |      |   |         |   |                |
+-----------+---+------------+---+------+---+---------+---+----------------+
| > 109.4   |   | >          | > |      |   | >       |   | > 40 AN        |
|           |   | Additional |   |      |   |  61-100 |   |                |
|           |   | > Text     | 6 |      |   |         |   |                |
|           |   |            | 0 |      |   |         |   |                |
|           |   |            | . |      |   |         |   |                |
|           |   |            | 4 |      |   |         |   |                |
+-----------+---+------------+---+------+---+---------+---+----------------+
| > **Sub   |   |            |   |      |   |         |   |                |
| >         |   |            |   |      |   |         |   |                |
|  Elements |   |            |   |      |   |         |   |                |
| > of DE   |   |            |   |      |   |         |   |                |
| > 109     |   |            |   |      |   |         |   |                |
| > when    |   |            |   |      |   |         |   |                |
| > DE63.7  |   |            |   |      |   |         |   |                |
| > =       |   |            |   |      |   |         |   |                |
| > 'MA     |   |            |   |      |   |         |   |                |
| STERCARD' |   |            |   |      |   |         |   |                |
| > and     |   |            |   |      |   |         |   |                |
| > 48.9 =  |   |            |   |      |   |         |   |                |
| > 'DMS'** |   |            |   |      |   |         |   |                |
+-----------+---+------------+---+------+---+---------+---+----------------+
| > **Sub   | > |            |   | >    | > |         | > |                |
| > Field   |   |            |   | **MC |   |         |   |                |
| > No**    | * |            |   | >    | * |         | * |                |
|           | * |            |   |  Bit | * |         | * |                |
|           | F |            |   | >    | P |         | F |                |
|           | i |            |   | No** | o |         | o |                |
|           | e |            |   |      | s |         | r |                |
|           | l |            |   |      | i |         | m |                |
|           | d |            |   |      | t |         | a |                |
|           | > |            |   |      | i |         | t |                |
|           |   |            |   |      | o |         | * |                |
|           | N |            |   |      | n |         | * |                |
|           | a |            |   |      | * |         |   |                |
|           | m |            |   |      | * |         |   |                |
|           | e |            |   |      |   |         |   |                |
|           | * |            |   |      |   |         |   |                |
|           | * |            |   |      |   |         |   |                |
+-----------+---+------------+---+------+---+---------+---+----------------+
| > 109.1\* | > |            |   | >    | > |         | > |                |
|           |   |            |   |  N/A |   |         |   |                |
|           | M |            |   |      | 1 |         | 7 |                |
|           | e |            |   |      | - |         | N |                |
|           | s |            |   |      | 7 |         |   |                |
|           | s |            |   |      |   |         |   |                |
|           | a |            |   |      |   |         |   |                |
|           | g |            |   |      |   |         |   |                |
|           | e |            |   |      |   |         |   |                |
|           | > |            |   |      |   |         |   |                |
|           |   |            |   |      |   |         |   |                |
|           | R |            |   |      |   |         |   |                |
|           | e |            |   |      |   |         |   |                |
|           | a |            |   |      |   |         |   |                |
|           | s |            |   |      |   |         |   |                |
|           | o |            |   |      |   |         |   |                |
|           | n |            |   |      |   |         |   |                |
|           | > |            |   |      |   |         |   |                |
|           |   |            |   |      |   |         |   |                |
|           | C |            |   |      |   |         |   |                |
|           | o |            |   |      |   |         |   |                |
|           | d |            |   |      |   |         |   |                |
|           | e |            |   |      |   |         |   |                |
+-----------+---+------------+---+------+---+---------+---+----------------+

##### \*: Multi-Clearing Indicators

-   Multi-Clearing → '**1403'** (If Field 109 **contains** value '1403',
    It is a multi-clearing)

-   Final Clearing → '**1404'** (If field 109 **contains** value '1404',
    it is the last clearing in multiclearing cycle)

+-----------+-----------------+------+-----------+-------------------+
| > **Sub   |                 |      |           |                   |
| >         |                 |      |           |                   |
|  Elements |                 |      |           |                   |
| > of DE   |                 |      |           |                   |
| > 109     |                 |      |           |                   |
| > when    |                 |      |           |                   |
| > DE63.7  |                 |      |           |                   |
| > =       |                 |      |           |                   |
| > 'STAR'  |                 |      |           |                   |
| > and     |                 |      |           |                   |
| > 48.9 =  |                 |      |           |                   |
| > 'AXS'** |                 |      |           |                   |
+===========+=================+======+===========+===================+
| > **Sub   | > **Field       | > ** | > **P     | > **Format**      |
| > Field   | > Name**        | STAR | osition** |                   |
| > No**    |                 | > B  |           |                   |
|           |                 | it** |           |                   |
|           |                 | >    |           |                   |
|           |                 | > ** |           |                   |
|           |                 | No** |           |                   |
+-----------+-----------------+------+-----------+-------------------+
| > 109.1\* | >               | > 60 | > 1-6     | > AN-6            |
|           | Advice/Reversal |      |           |                   |
|           | > Reason Code   |      |           |                   |
+-----------+-----------------+------+-----------+-------------------+

##### 109.1\* {#section-3 .unnumbered}

> Represents the advice/reversal reason code. Issuers may use specific
> advice reason codes to notify acquirer of the reason for a decline on
> a recurring payment authorization.

+-----------------------------------+-----------------------------------+
| > **Position 1-2:** Indicates     | -   **80** = Reversal Reason      |
| > which reason code is present    |     > present                     |
|                                   |                                   |
|                                   | -   **40** = Advice Reason        |
|                                   |     > present                     |
|                                   |                                   |
|                                   | -   **C0** = Both reversal and    |
|                                   |     > advice reason subfields are |
|                                   |     > present.                    |
+===================================+===================================+
| > **Position 3-4:** Depending     | -   **RR** (A valid reversal      |
| > upon the previous field, this   |     > reason code)                |
| > field contains either a valid   |                                   |
| > advice/reversal reason code.    | -   **AA** (A valid advice reason |
|                                   |     > code)                       |
+-----------------------------------+-----------------------------------+
| > **Position 5-6:** Present only  | -   **C0RRAA** (where RR is       |
| > if the first two positions      |     > reversal reason code & AA   |
| > contain 'C0', then reversal     |     > is advice reason code)      |
| > code is present at position 3-4 |                                   |
| > and advice reason code in at    |                                   |
| > these two positions.            |                                   |
+-----------------------------------+-----------------------------------+

+------------+----------------+-------------+------------+------------+
| > **Sub    |                |             |            |            |
| > Elements |                |             |            |            |
| > of DE    |                |             |            |            |
| > 109 when |                |             |            |            |
| > DE63.7 = |                |             |            |            |
| > 'D       |                |             |            |            |
| ISCOVER'** |                |             |            |            |
+============+================+=============+============+============+
| > Sub      | > Field Name   | > DISCOVER  | > Position | > Format   |
| > Field No |                | > Bit No    |            |            |
+------------+----------------+-------------+------------+------------+
| > 109.1    | > Message      | > 25        | > 1-2      | > 2 N      |
|            | > Reason Code  |             |            |            |
+------------+----------------+-------------+------------+------------+

> Possible values with description:

+-----+--------------------------------------------------------------+---+
| > * |                                                              |   |
| *Re |                                                              |   |
| ver |                                                              |   |
| sal |                                                              |   |
| >   |                                                              |   |
| Rea |                                                              |   |
| son |                                                              |   |
| > C |                                                              |   |
| ode |                                                              |   |
| s** |                                                              |   |
+=====+==============================================================+===+
| > C | > Definition                                                 |   |
| ode |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Customer Cancellation                                      |   |
|  00 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Unspecified; No Action Taken                               |   |
|  01 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Suspected Malfunction                                      |   |
|  02 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Format Error; No Action Taken                              |   |
|  03 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Completed Partially                                        |   |
|  04 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Original Amount Incorrect                                  |   |
|  05 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Response Received Too Late                                 |   |
|  06 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Card Acceptor Device (POS Device) Unable to Complete       |   |
|  07 | > Transaction                                                |   |
+-----+--------------------------------------------------------------+---+
| >   | > Unable to Deliver Message to Point of Sale (POS)           |   |
|  13 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Suspected Malfunction/Card Retained                        |   |
|  14 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Suspected Malfunction/Track 3 Not Updated                  |   |
|  16 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Suspected Malfunction/No Cash Dispensed                    |   |
|  17 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Timed-Out at Taking Money/No Cash Dispensed                |   |
|  18 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Timed-Out at Taking Card/Card Retained and No Cash         |   |
|  19 | > Dispensed                                                  |   |
+-----+--------------------------------------------------------------+---+
| >   | > Invalid Response; No Action Taken                          |   |
|  20 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Timed-Out Waiting for Response                             |   |
|  21 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Invalid Card Product Code                                  |   |
|  22 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Return (of goods or services)                              |   |
|  51 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Credit Adjustment                                          |   |
|  52 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   |                                                              |   |
|  ** |                                                              |   |
| Adv |                                                              |   |
| ice |                                                              |   |
| >   |                                                              |   |
| Rea |                                                              |   |
| son |                                                              |   |
| > C |                                                              |   |
| ode |                                                              |   |
| s** |                                                              |   |
+-----+--------------------------------------------------------------+---+
| > C | > Definition                                                 |   |
| ode |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Invalid Card Product Code                                  |   |
|  62 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Merchant is not in Inclusion Table                         |   |
|  63 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Reserved                                                   |   |
|  64 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Reserved                                                   |   |
|  65 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Issuer unavailable                                         |   |
|  66 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Issuer's rules failed                                      |   |
|  67 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > AVS verification failed                                    |   |
|  68 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Reserved                                                   |   |
|  69 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Mobile Passcode not verified                               |   |
|  70 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Mobile Transaction Amount exceeds stand-in limit           |   |
|  71 |                                                              |   |
+-----+--------------------------------------------------------------+---+

+-----+--------------------------------------------------------------+---+
| >   | > Network Declined: Suspected Fraud                          |   |
|  72 |                                                              |   |
+=====+==============================================================+===+
| >   | > Automated Fuel Dispenser - final Card Sale amount          |   |
|  73 |                                                              |   |
+-----+--------------------------------------------------------------+---+
| >   | > Host Capture - final Card Sale amount                      |   |
|  74 |                                                              |   |
+-----+--------------------------------------------------------------+---+

+-----+----------------------------------------------------------------+
| > * |                                                                |
| *Ad |                                                                |
| min |                                                                |
| ist |                                                                |
| rat |                                                                |
| ive |                                                                |
| >   |                                                                |
|  Tr |                                                                |
| ans |                                                                |
| act |                                                                |
| ion |                                                                |
| > R |                                                                |
| equ |                                                                |
| est |                                                                |
| >   |                                                                |
| Rea |                                                                |
| son |                                                                |
| > C |                                                                |
| ode |                                                                |
| s** |                                                                |
+=====+================================================================+
| > C | > Definition                                                   |
| ode |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Instant Credit Support -- Consumer                           |
|  80 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Application Status -- Consumer                               |
|  81 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Authorized User Inquiry -- Consumer                          |
|  82 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Account Inquiry -- Consumer                                  |
|  83 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Account Maintenance -- Consumer                              |
|  84 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Instant Credit Support - Business                            |
|  90 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Application Status -- Business                               |
|  91 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Authorized User Inquiry -- Business                          |
|  92 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Mobile Passcode not verified Account Inquiry -- Business     |
|  93 |                                                                |
+-----+----------------------------------------------------------------+
| >   | > Account Maintenance -- Business                              |
|  94 |                                                                |
+-----+----------------------------------------------------------------+

+-----------+----------------+-------------+-----------+-------------+
| > **Sub   |                |             |           |             |
| >         |                |             |           |             |
|  Elements |                |             |           |             |
| > of DE   |                |             |           |             |
| > 109     |                |             |           |             |
| > when    |                |             |           |             |
| > DE63.7  |                |             |           |             |
| > =       |                |             |           |             |
| > '       |                |             |           |             |
| FISERV'** |                |             |           |             |
+===========+================+=============+===========+=============+
| > Sub     | > Field Name   | > FISERV    | >         | > Format    |
| > Field   |                | > Bit No    |  Position |             |
| > No      |                |             |           |             |
+-----------+----------------+-------------+-----------+-------------+
| > 109.1   | > Message      | > 25        | > 1-4     | > 4N        |
|           | > Reason Code  |             |           |             |
+-----------+----------------+-------------+-----------+-------------+

> Possible values of Field-109 with description for FISERV:

+-----+----------------------------------------------------------------+
| >   |                                                                |
|  ** |                                                                |
| Adv |                                                                |
| ice |                                                                |
| >   |                                                                |
| Rea |                                                                |
| son |                                                                |
| >   |                                                                |
|  Co |                                                                |
| des |                                                                |
| > ( |                                                                |
| For |                                                                |
| > 0 |                                                                |
| 1xx |                                                                |
| >   |                                                                |
| and |                                                                |
| > 0 |                                                                |
| 2xx |                                                                |
| >   |                                                                |
|  me |                                                                |
| ssa |                                                                |
| ges |                                                                |
| )** |                                                                |
+=====+================================================================+
| > C | > Definition                                                   |
| ode |                                                                |
+-----+----------------------------------------------------------------+
| > 1 | > Stand-in processing at the card issuer\'s option             |
| 000 |                                                                |
+-----+----------------------------------------------------------------+
| > 1 | > Stand-in because card issuer was signed off                  |
| 001 |                                                                |
+-----+----------------------------------------------------------------+
| > 1 | > Stand-in because card issuer timed out on original request   |
| 002 |                                                                |
+-----+----------------------------------------------------------------+
| > 1 | > Stand-in because card issuer was unavailable                 |
| 003 |                                                                |
+-----+----------------------------------------------------------------+
| > 1 | > Terminal processed                                           |
| 004 |                                                                |
+-----+----------------------------------------------------------------+
| > 1 | > ICC processed                                                |
| 005 |                                                                |
+-----+----------------------------------------------------------------+
| > 1 | > Under floor limit                                            |
| 006 |                                                                |
+-----+----------------------------------------------------------------+
| > 1 | > Stand-in processing at the acquirer\'s option                |
| 007 |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| > 1 | > Credit adjustment                                            |
| 008 |                                                                |
+=====+================================================================+
| > 1 | > Default value                                                |
| 376 |                                                                |
+-----+----------------------------------------------------------------+

+-----+----------------------------------------------------------------+
| >   |                                                                |
|  ** |                                                                |
| Adv |                                                                |
| ice |                                                                |
| >   |                                                                |
| Rea |                                                                |
| son |                                                                |
| >   |                                                                |
|  Co |                                                                |
| des |                                                                |
| > ( |                                                                |
| For |                                                                |
| > 0 |                                                                |
| 4xx |                                                                |
| >   |                                                                |
|  me |                                                                |
| ssa |                                                                |
| ges |                                                                |
| )** |                                                                |
+=====+================================================================+
| >   | > **Definition**                                               |
|  ** |                                                                |
| Cod |                                                                |
| e** |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Customer/Merchant cancellation                               |
| 000 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Unspecified                                                  |
| 001 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Suspected malfunction                                        |
| 002 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Format error; no action taken                                |
| 003 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Completed partially (under dispense)                         |
| 004 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Original amount incorrect                                    |
| 005 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Response received too late (late response reversal)          |
| 006 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Card acceptor device unable to complete transaction          |
| 007 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Unable to deliver message to point of service                |
| 013 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Acquirer denial suspect fraud                                |
| 014 |                                                                |
+-----+----------------------------------------------------------------+
| > 4 | > Time out waiting for response (early reversal)               |
| 021 |                                                                |
+-----+----------------------------------------------------------------+

## Appendix D -- Sample Messages {#appendix-d-sample-messages .unnumbered}

#### Sample Network Request/Response Messages (0800, 0810) {#sample-network-requestresponse-messages-0800-0810 .unnumbered}

##### Request Message \[0800\] (ASCII format) {#request-message-0800-ascii-format .unnumbered}

> 00670800822000000800000004000000000000000409111530088001909916088001081
>
> Where,
>
> Message length (4-bytes): 0067 MTI (4-bytes): 0800
>
> Bitmaps (32 bytes): 82200000080000000400000000000000
>
> Data Elements (31 bytes): 0409111530088001909916088001081

###### Parsed Data Elements: {#parsed-data-elements .unnumbered}

> DE 007 = 0409111530
>
> DE 011 = 088001
>
> DE 037 = 909916088001
>
> DE 070 = 081

##### Response Message \[0810\] (ASCII format) {#response-message-0810-ascii-format .unnumbered}

> 00690810822000000A0000000400000000000000040911153008800190991608800100081
>
> Where,
>
> Message length (4-bytes): 0069 MTI (4-bytes): 0810
>
> Bitmaps (32 bytes): 822000000A0000000400000000000000
>
> Data Elements (33 bytes): 040911153008800190991608800100081

###### Parsed Data Elements: {#parsed-data-elements-1 .unnumbered}

> DE 007 = 0409111530
>
> DE 011 = 088001
>
> DE 037 = 909916088001
>
> DE 039 = 00
>
> DE 070 = 081

##### Request Message \[0800\] (Bytes format) {#request-message-0800-bytes-format .unnumbered}

###### Request Message (represented in Hex): {#request-message-represented-in-hex .unnumbered}

> Where,
>
> Message length (2-bytes): 0033 (51 bytes)
>
> MTI (4-bytes): 30383030 (0800)
>
> Bitmaps (16 bytes): 82200000080000000400000000000000
>
> Data Elements (31 bytes):
> 30323236303932363536303838303031393035373134303838303031303831

###### Parsed Data Elements: {#parsed-data-elements-2 .unnumbered}

> DE 007 = 0226092656
>
> DE 011 = 088001
>
> DE 037 = 905714088001
>
> DE 070 = 081
>
> **Response Message \[0810\] (Bytes format)**

###### Request Message (represented in Hex): {#request-message-represented-in-hex-1 .unnumbered}

> Where,
>
> Message length (2-bytes): 0035 (53 bytes)
>
> MTI (4-bytes): 30383130 (0810)
>
> Bitmaps (16 bytes): 822000000A0000000400000000000000
>
> Data Elements (33 bytes):
> 303232363039323635363038383030313930353731343038383030313030303831

###### Parsed Data Elements: {#parsed-data-elements-3 .unnumbered}

> DE 007 = 0226092656
>
> DE 011 = 088001
>
> DE 037 = 905714088001
>
> DE 039 = 00
>
> DE 070 = 081

#### Sample Authorization Request/Response Messages (0100, 0110) {#sample-authorization-requestresponse-messages-0100-0110 .unnumbered}

##### Request Message \[0100\] (represented in Hex): {#request-message-0100-represented-in-hex .unnumbered}

###### Parsed Message \[0100\]: {#parsed-message-0100 .unnumbered}

> DE-2 \[100194868736564\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000050000\]
>
> DE-6 \[000000050100\]
>
> DE-7 \[0122132918\]
>
> DE-10 \[61002000\]
>
> DE-11 \[016372\]
>
> DE-12 \[182918\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-18 \[5541\]
>
> DE-22 \[902\]
>
> DE-25 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000\]
>
> DE-37 \[802213016372\] DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR\]
>
> DE-43 \[ACQUIRER NAME CITY NAME CAUSA\] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA\]
>
> DE-102 \[100194868736564\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0768892\]

##### Response Message \[0110\] (represented in Hex): {#response-message-0110-represented-in-hex .unnumbered}

> 01CE30313130F67A00910EC0A40A00000000040200003135313030313934383638373336353634303030
>
> 30303030303030303030353030303030303030303030353031303030313232313332393138363130303230
>
> 30303031363337323138323931383031323230313232303044303030303030303030363030303030303830
>
> 3232313330313633373230303132343535315445524D4944303143415244204143434550544F5220203834
>
> 30383430303230303037323834304430303030303030303031303030313630303030303030303034303230
>
> 30303030373030303032202020203132333435363132333435363132332020202020202020202020302020
>
> 20202020202020202020202020202020202020202056495341202020202020202031353130303139343836
>
> 38373336353634313534203132333435363132333435363132332020202020303020202020202020202020
>
> 20202020202020202020202020202020303030303030203030303030303030303020303030303030303030
>
> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

###### Parsed Message \[0110\]: {#parsed-message-0110 .unnumbered}

> DE-2 \[100194868736564\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000050000\]
>
> DE-6 \[000000050100\]
>
> DE-7 \[0122132918\]
>
> DE-10 \[61002000\]
>
> DE-11 \[016372\]
>
> DE-12 \[182918\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-25 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000
>
> DE-37 \[802213016372\]
>
> DE-38 \[001245\]
>
> DE-39 \[51\]
>
> DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR\] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA\]
>
> DE-102 \[100194868736564\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0768892\]
>
> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

#### Sample Authorization Advice Request/Response Messages (0120, 0130) {#sample-authorization-advice-requestresponse-messages-0120-0130 .unnumbered}

##### Request Message \[0120 (represented in Hex): {#request-message-0120-represented-in-hex .unnumbered}

###### Parsed Message \[0120\]: {#parsed-message-0120 .unnumbered}

> DE-2 \[100194868736564\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000050000\]
>
> DE-6 \[000000050100\]
>
> DE-7 \[0122133300\]
>
> DE-10 \[61002000\]
>
> DE-11 \[016374\]
>
> DE-12 \[183300\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-18 \[5541\]
>
> DE-22 \[902\]
>
> DE-25 \[00\]
>
> DE-26 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000\]
>
> DE-37 \[802213016374\] DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR\]
>
> DE-43 \[ACQUIRER NAME CITY NAME CAUSA\] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA\]
>
> DE-102 \[100194868736564\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0984707\]

##### Response Message \[0130\] (represented in Hex): {#response-message-0130-represented-in-hex .unnumbered}

> 01C830313330F67A00910AC0A40A000000000402000031353130303139343836383733363536343030303
>
> 03030303030303030303530303030303030303030303530313030303132323133333330303631303032303
>
> 03030313633373431383333303030313232303132323030443030303030303030303630303030303038303
>
> 232313330313633373435315445524D4944303143415244204143434550544F52202038343038343030323
>
> 03030373238343044303030303030303030313030303136303030303030303030343032303030303037303
>
> 03030322020202031323334353631323334353631323320202020202020202020203020202020202020202
>
> 02020202020202020202020202020564953412020202020202020313531303031393438363837333635363
>
> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

###### Parsed Message \[0130\]: {#parsed-message-0130 .unnumbered}

> DE-2 \[100194868736564\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000050000\]
>
> DE-6 \[000000050100\]
>
> DE-7 \[0122133300\]
>
> DE-10 \[61002000\]
>
> DE-11 \[016374\]
>
> DE-12 \[183300\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-25 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000\]
>
> DE-37 \[802213016374\]
>
> DE-39 \[51\]
>
> DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR \] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA \]
>
> DE-102 \[100194868736564\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0984707\]
>
> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

#### Sample Financial Request/Response Messages (0200, 0210) {#sample-financial-requestresponse-messages-0200-0210 .unnumbered}

##### Request Message \[0200\] (represented in Hex): {#request-message-0200-represented-in-hex .unnumbered}

###### Parsed Message \[0200\]: {#parsed-message-0200 .unnumbered}

> DE-2 \[100194868736654\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000050000\]
>
> DE-6 \[000000050100\]
>
> DE-7 \[0122133141\]
>
> DE-10 \[61002000\]
>
> DE-11 \[016373\]
>
> DE-12 \[183141\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-18 \[5541\]
>
> DE-22 \[902\]
>
> DE-25 \[00\]
>
> DE-26 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000\]
>
> DE-37 \[802213016373\] DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR \]
>
> DE-43 \[ACQUIRER NAME CITY NAME CAUSA\] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA \]
>
> DE-102 \[100194868736654\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0905440\]

##### Response Message \[0210\] (represented in Hex): {#response-message-0210-represented-in-hex .unnumbered}

> 01D230323130F67A40910EC0A40A000000000402000031353130303139343836383733363635343030303
>
> 03030303030303030303530303030303030303030303530313030303132323133333134313631303032303
>
> 03030313633373331383331343130313232303132323535343130304430303030303030303036303030303
>
> 03038303232313330313633373330303132343535315445524D4944303143415244204143434550544F522
>
> 02038343038343030323030303732383430443030303030303030303130303031363030303030303030303
>
> 43032303030303037303030303220202020313233343536313233343536313233202020202020202020202
>
> 03020202020202020202020202020202020202020202020205649534120202020202020203135313030313
>
> 93438363837333636353431353420313233343536313233343536313233202020202030302020202020202
>
> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

###### Parsed Message \[0210\]: {#parsed-message-0210 .unnumbered}

> DE-2 \[100194868736654\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000050000\]
>
> DE-6 \[000000050100\]
>
> DE-7 \[0122133141\]
>
> DE-10 \[61002000\]
>
> DE-11 \[016373\]
>
> DE-12 \[183141\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-18 \[5541\]
>
> DE-25 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000\]
>
> DE-37 \[802213016373\]
>
> DE-38 \[001245\]
>
> DE-39 \[51\]
>
> DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR \] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA \]
>
> DE-102 \[100194868736654\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0905440\]
>
> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

#### Sample Financial Advice Request/Response Messages (0220, 0230) {#sample-financial-advice-requestresponse-messages-0220-0230 .unnumbered}

##### Request Message \[0220\] (represented in Hex): {#request-message-0220-represented-in-hex .unnumbered}

###### Parsed Message \[0220\]: {#parsed-message-0220 .unnumbered}

> DE-2 \[100194868736654\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000050000\]
>
> DE-6 \[000000050100\]
>
> DE-7 \[0122133357\]
>
> DE-10 \[61002000\]
>
> DE-11 \[016375\]
>
> DE-12 \[183357\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-18 \[5541\]
>
> DE-22 \[902\]
>
> DE-25 \[00\]
>
> DE-26 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000\]
>
> DE-37 \[802213016375\] DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR \]
>
> DE-43 \[ACQUIRER NAME CITY NAME CAUSA\] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA \]
>
> DE-102 \[100194868736654\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0 \]

##### Response Message \[0230\] (represented in Hex): {#response-message-0230-represented-in-hex .unnumbered}

> 01CE30323330F67A00910EC0A40A00000000040200003135313030313934383638373336363534303030
>
> 30303030303030303030353030303030303030303030353031303030313232313333333537363130303230
>
> 30303031363337353138333335373031323230313232303044303030303030303030363030303030303830
>
> 3232313330313633373530303132343535315445524D4944303143415244204143434550544F5220203834
>
> 30383430303230303037323834304430303030303030303031303030313630303030303030303034303230
>
> 30303030373030303032202020203132333435363132333435363132332020202020202020202020302020
>
> 20202020202020202020202020202020202020202056495341202020202020202031353130303139343836
>
> 38373336363534313534203132333435363132333435363132332020202020303020202020202020202020
>
> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

###### Parsed Message \[0230\]: {#parsed-message-0230 .unnumbered}

> DE-2 \[100194868736654\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000050000\]
>
> DE-6 \[000000050100\]
>
> DE-7 \[0122133357\]
>
> DE-10 \[61002000\]
>
> DE-11 \[016375\]
>
> DE-12 \[183357\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-25 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000\]
>
> DE-37 \[802213016375\]
>
> DE-38 \[001245\]
>
> DE-39 \[51\]
>
> DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR \] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA \]
>
> DE-102 \[100194868736654\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0 \]
>
> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

#### Sample Reversal Request/Response Messages (0420, 0430) {#sample-reversal-requestresponse-messages-0420-0430 .unnumbered}

##### Request Message \[0420\] (represented in Hex): {#request-message-0420-represented-in-hex .unnumbered}

###### Parsed Message \[0420\]: {#parsed-message-0420 .unnumbered}

> DE-2 \[100194868736768\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000020000\]
>
> DE-6 \[000000020100\]
>
> DE-7 \[0122134443\]
>
> DE-10 \[61005000\]
>
> DE-11 \[016380\]
>
> DE-12 \[184443\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-18 \[5541\]
>
> DE-22 \[902\]
>
> DE-25 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000\]
>
> DE-37 \[802213016380\]
>
> DE-39 \[00\]
>
> DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR \]
>
> DE-43 \[ACQUIRER NAME CITY NAME CAUSA\] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA \]
>
> DE-102 \[100194868736768\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0686491\]

##### Response Message \[0430\] (represented in Hex): {#response-message-0430-represented-in-hex .unnumbered}

> 01F930343330F67A00910EE0A40A000000000402000031353130303139343836383733363736383030303
>
> 03030303030303030303230303030303030303030303230313030303132323133343434333631303035303
>
> 03030313633383031383434343330313232303132323030443030303030303030303630303030303038303
>
> 232313330313633383030303132343530305445524D4944303143415244204143434550544F52202041435
>
> 15549524552204E414D4520202020202020202020202043495459204E414D452020202043415553413834
>
> 30383430303230303037323834304430303030303030303031303030313630303030303030303034303230
>
> 30303030373030303032202020203132333435363132333435363132332020202020202020202020302020
>
> 20202020202020202020202020202020202020202056495341202020202020202031353130303139343836
>
> ![](./image2.jpeg){width="0.8417257217847769in" height="0.52in"}

###### Parsed Message \[0430\]: {#parsed-message-0430 .unnumbered}

> DE-2 \[100194868736768\]
>
> DE-3 \[000000\]
>
> DE-4 \[000000020000\]
>
> DE-6 \[000000020100\]
>
> DE-7 \[0122134443\]
>
> DE-10 \[61005000\]
>
> DE-11 \[016380\]
>
> DE-12 \[184443\]
>
> DE-13 \[0122\]
>
> DE-15 \[0122\]
>
> DE-25 \[00\]
>
> DE-28 \[D00000000\] DE-32 \[000000\]
>
> DE-37 \[802213016380\]
>
> DE-38 \[001245\]
>
> DE-39 \[00\]
>
> DE-41 \[TERMID01\]
>
> DE-42 \[CARD ACCEPTOR \]
>
> DE-43 \[ACQUIRER NAME CITY NAME CAUSA\] DE-49 \[840\]
>
> DE-51 \[840\]
>
> DE-54 \[0072840D000000000100\] DE-61 \[0000000004020000\]
>
> DE-63 \[0002 123456123456123 0 VISA \]
>
> DE-102 \[100194868736768\]
>
> DE-111 \[ 123456123456123 00 000000 0000000000 000000000000 0000000000
> 00020000000000000000
>
> 00 0686491\]

#### Sample Token Notification Message (0620, 0320) {#sample-token-notification-message-0620-0320 .unnumbered}

##### Request Message \[0620\] (represented in Hex): {#request-message-0620-represented-in-hex .unnumbered}

> 03D230363230C22000000A000002040000000002000831353130303134313738383635323631353038323
>
> 93132353834343031323630363632343231323031323630363030303730303030322020202020202020202
>
> 02020202020202020202020202020202020202020302020202020202020202020202020202020202020202
>
> 02056495341202020202020202038393033323320303030303030303030303030303030202020202030302
>
> 02020202020202020202020202020202020202020202020202030303030303020303030303030303030302
>
> 03030303030303030303030302020202020303030303030303030302020202020202020202020203030303
>
> 23337313130303030303030303030303020202020202020202020202020205A30302020202030202020202
>
> 02031323334353637383931323334353637383931323334353637383931323334353637383931323334353
>
> 637383931323320202020202020202020202020202020353535353030303030303030303030693263204D6
> F62696C65202020202020202020203031343036333237313132373030303131383030305A5A4130343330
> 30202020202020202030303030303030303030202020202020202020202020202020202020203030303035
>
> 30360200590220F1F2F3F4F5F6F7F8F9F1F2F3F4F5F6F7F8F9F1F2F3F4F5F6F7F8F9F1F2F3F4F50706F
>
> 0F5F0F9F0C30601F30920F7F8F9F7F8F9F7F9F8F7F7F8F9F7F8F9F7F9F8F7F7F8F9F7F8F9F7F9F8F7F
>
> 7F80301F70802F0F10A01F80100730203C5D5C7070EF5F54BF2F5F54BF2F5F54BF2F5F50404F5F5F5F
>
> 50B01F206084EF3F76160F1F2F10102F0F10901F70330F1F2F3F4F5F6F7F8F9F1F2F3F4F5F6F7F8F9F1
> F2F3F4F5F6F7F8F9F1F2F3F4F5F6F7F8F9F1F2F3F4F5F6F7F8F9F1F2F30801F50A01F8050A89F28340
> D496828993856800DE0202F2F21F3102F7F21D02F4F41B0CF7F7F7F7F7F7F7F7F7F7F7F71401F40702
> E9E91F3203F6F0F01F3305F1F0F0F0F00409F0F0F0F0F0F0F0F0F01102F8F80B19E56060F0F0F0F0F0F
> 0F0F0F0F0F0F0F0F0F0F0F1F2F3F4F5F60604F2F3F1F20110F4F0F6F3F2F7F1F1F2F7F0F0F0F1F1F813
>
> 01F20C20F0F1F2F3F4F5F6F7F8F9F0F1F2F3F4F5F6F7F8F9F0F1F2F3F4F5F6F7F8F9F0F1030BF4F0F0
> F0F0F0F0F0F0F5F50801C11001F90A01F01C02F5F51A06F6F6F6F6F6F61201F30520F1F2F3F4F5F6F7
> F8F9F1F2F3F4F5F6F7F8F9F1F2F3F4F5F6F7F8F9F1F2F3F4F5400044021AD496956B40F0F740D683A3
> 40F2F0F2F040F1F07AF2F57AF2F1F70126E38889A2C689859384E6899393C39695A3818995E3859994A
>
> 2C19584C396958489A3899695A2

##### Request Message \[0302\] (represented in Hex): {#request-message-0302-represented-in-hex .unnumbered}

> 01D130333032C2200000080000020000000000020000313635333837353731303030303034363939303833
>
> 30313633383539393731303034366465763136393731303034303730303030322020202020202020202020
>
> 20202020202020202020202020202020202020302020202020202020202020202020202020202020202020
>
> 56495341202020202020202033323320303030303030303030303030303030202020202030302020202020
>
> 20202020202020202020202020202020202020202030303030303020303030303030303030302030303030
>
> 30303030303030302020202020303030303030303030302020202020202020202020203030303230303030
>
> 30303030303030303030303020202020202020202020202020202030302020202030202020202020202020
>
> 20202020202020202020202020202020202020202020202020202020202020202020202020202020202020
>
> 20202020202020202020202020202020202030303030303030303030303030303020202020202020202020
>
> 20202020202020202020202030303030303030303030303030303030303030202020303030303020202020
>
> 20202020303030303030303030303435323031303939303030303030313920202032303132

#### Sample DE-111 -- Additional Data {#sample-de-111-additional-data .unnumbered}

##### Sample DE-111 (Fixed Format) for Visa {#sample-de-111-fixed-format-for-visa .unnumbered}

> 325Y0000000000000010000H0700000000000000000000000000000000000000000000000000000000A00
> D 01234567890000000000A 0002000090011234567800000000000000000101S0
> 000000000000000
>
> 00000 0000000000 00000

##### Sample DE-111 for MasterCard {#sample-de-111-for-mastercard .unnumbered}

> 767Z400502010 0103210 0101102010031300112345678900412000000000010
> 00000000000000MD
>
> 0000010101 010000000 C01 N52001 YA000 000000123456 0679847
> 000000000000000 00000
>
> 0000000000 0000
>
> []{#_bookmark104 .anchor}**Data Element 80 Dispute Action Information
> Tag 05 Decline Reasons**

+-----------+-------------------------+--------------------------------+
| >         | > **Reject Reason       | > **Reject Reason              |
|  **Reject | > Title**               | > Description**                |
| > Reason  |                         |                                |
| > ID**    |                         |                                |
+===========+=========================+================================+
| > **1**   | > Authenticated via OTP | > The disputed transaction(s)  |
|           | > (UCAF)                | > was/were authenticated via   |
|           |                         | > OTP, indicating the          |
|           |                         | > transactions were validated  |
|           |                         | > from profile registered      |
|           |                         | > phone number or email        |
|           |                         | >                              |
|           |                         | > address                      |
+-----------+-------------------------+--------------------------------+
| > **2**   | > Authenticated via     | > The disputed transaction(s)  |
|           | > CHIP                  | > was/were authenticated       |
|           |                         | >                              |
|           |                         | > with CHIP, indicating your   |
|           |                         | > card was physically used to  |
|           |                         | > perform these disputed       |
|           |                         | > transactions                 |
+-----------+-------------------------+--------------------------------+
| > **3**   | > Authenticated via     | > The disputed transaction(s)  |
|           | > CHIP & PIN            | > was/were authenticated with  |
|           |                         | > CHIP and PIN or Chip read    |
|           |                         | > transactions indicating your |
|           |                         | > card was physically used to  |
|           |                         | > perform                      |
|           |                         | >                              |
|           |                         | > disputed transaction(s)      |
+-----------+-------------------------+--------------------------------+
| > **4**   | > CVV Code Used         | > The disputed transaction(s)  |
|           |                         | > was/were authenticated with  |
|           |                         | > CVV code indicating your     |
|           |                         | > card information was         |
|           |                         | >                              |
|           |                         | > used to perform disputed     |
|           |                         | > transaction(s)               |
+-----------+-------------------------+--------------------------------+
| > **5**   | > Web Account Created   | > The web account was created  |
|           | > After OTP             | > after authentication with    |
|           | > Authentication        | > OTP indicating the account   |
|           |                         | > creation was validated from  |
|           |                         | > profile registered phone     |
|           |                         | > number or                    |
|           |                         | >                              |
|           |                         | > email address                |
+-----------+-------------------------+--------------------------------+
| > **6**   | > No Balance Inquiry    | > No Balance Inquiry was       |
|           |                         | > observed prior to disputed   |
|           |                         | >                              |
|           |                         | > charge                       |
+-----------+-------------------------+--------------------------------+
| > **7**   | > No Decline/Bad PIN    | > No Decline/Bad PIN was       |
|           |                         | > observed prior to disputed   |
|           |                         | >                              |
|           |                         | > charge                       |
+-----------+-------------------------+--------------------------------+
| > **8**   | > No PIN Reset          | > No Reset PIN was observed    |
|           |                         | > prior to disputed            |
|           |                         | >                              |
|           |                         | > charge                       |
+-----------+-------------------------+--------------------------------+
| > **9**   | > No NSF Declines       | > No NSF was observed after    |
|           |                         | > the disputed charge          |
+-----------+-------------------------+--------------------------------+
| > **10**  | > No Declines after     | > No declined transactions     |
|           | > Card Reported         | > observed after the card      |
|           |                         | >                              |
|           |                         | > was reported                 |
+-----------+-------------------------+--------------------------------+
| > **11**  | > No Declines after     | > No declined transactions     |
|           | > Card Reissue Request  | > observed after the card re-  |
|           |                         | >                              |
|           |                         | > issue request was initiated  |
+-----------+-------------------------+--------------------------------+
| > **12**  | > PIN Authenticated via | > Reset/Setup PIN was          |
|           | > Registered            | > authenticated from profile   |
|           | >                       | >                              |
|           | > Phone/Email           | > registered phone number or   |
|           |                         | > email address                |
+-----------+-------------------------+--------------------------------+
| > **13**  | > Trans Reviewed by CH  | > The transaction(s) & other   |
|           | > through Web           | > details were reviewed by     |
|           |                         | > cardholder through Web       |
|           |                         | > Account in disputed date     |
|           |                         | >                              |
|           |                         | > range                        |
+-----------+-------------------------+--------------------------------+
| > **14**  | > Trans Reviewed by CH  | > The transaction(s) & other   |
|           | > through Mobile        | > details were reviewed by     |
|           |                         | > cardholder through Mobile    |
|           |                         | > App in disputed date         |
|           |                         | >                              |
|           |                         | > range                        |
+-----------+-------------------------+--------------------------------+
| > **15**  | > Trans Reviewed by CH  | > The transactions & other     |
|           | > through IVR           | > details were reviewed by     |
|           |                         | >                              |
|           |                         | > cardholder through IVR in    |
|           |                         | > disputed date range          |
+-----------+-------------------------+--------------------------------+
| > **16**  | > Disputed Trans made   | > The disputed transaction(s)  |
|           | > on DD Date            | > were made on the same        |
|           |                         | >                              |
|           |                         | > day the Direct Deposit was   |
|           |                         | > received                     |
+-----------+-------------------------+--------------------------------+
| > **17**  | > Valid Presentment     | > The re-presentment           |
|           | > Received              | > document(s) received from    |
|           |                         | > the merchant was/were        |
|           |                         | > reviewed and found valid to  |
|           |                         | >                              |
|           |                         | > decline this dispute         |
+-----------+-------------------------+--------------------------------+
| > **18**  | > ATM Provided Proof    | > The ATM provided proof of    |
|           |                         | > successful withdrawal(s)     |
+-----------+-------------------------+--------------------------------+
| > **19**  | > Merch Successfully    | > The services/merchandise     |
|           | > Delivered             | > were successfully            |
|           |                         | >                              |
|           |                         | > delivered to the profile     |
|           |                         | > address                      |
+-----------+-------------------------+--------------------------------+
| > **20**  | > Merchant History      | > The account history has      |
|           |                         | > non-disputed transaction(s)  |
+-----------+-------------------------+--------------------------------+

+-----------+-------------------------+--------------------------------+
|           |                         | > of the same merchant that    |
|           |                         | > were made prior to the       |
|           |                         | >                              |
|           |                         | > disputed transaction(s)      |
+===========+=========================+================================+
| > **21**  | > Family Fraud          | > A potential Family Fraud     |
|           |                         | > case according to the        |
|           |                         | >                              |
|           |                         | > information analyzed in the  |
|           |                         | > merchant documents           |
+-----------+-------------------------+--------------------------------+
| > **22**  | > Normal Spending Trend | > The recent spending trend on |
|           |                         | > the card is observed         |
|           |                         | >                              |
|           |                         | > as normal                    |
+-----------+-------------------------+--------------------------------+
| > **23**  | > PIN Changed with      | > The same phone number which  |
|           | > Registered Phone      | > is available on              |
|           |                         | >                              |
|           |                         | > cardholder profile was used  |
|           |                         | > to change PIN                |
+-----------+-------------------------+--------------------------------+
| > **24**  | > Merch Docs have Same  | > The merchant re-presentment  |
|           | > Last Name             | > document(s) show             |
|           |                         | >                              |
|           |                         | > the same last name which is  |
|           |                         | > on cardholder profile        |
+-----------+-------------------------+--------------------------------+
| > **25**  | > Reported After 120    | > The disputed transaction(s)  |
|           | > Days                  | > are reported after 120       |
|           |                         | >                              |
|           |                         | > days of transaction date(s)  |
+-----------+-------------------------+--------------------------------+
| > **26**  | > Trans made within     | > The disputed transaction(s)  |
|           | > 7-mile Radius         | > were made within 7-mile      |
|           |                         | >                              |
|           |                         | > radius from the profile      |
|           |                         | > address                      |
+-----------+-------------------------+--------------------------------+
| > **27**  | > Cancel by Cardholder  | > The cardholder               |
|           |                         | > himself/herself called the   |
|           |                         | > customer support and         |
|           |                         | > requested for cancellation   |
|           |                         | > of reported                  |
|           |                         | >                              |
|           |                         | > dispute.                     |
+-----------+-------------------------+--------------------------------+
| > **28**  | > Credit Issued by      | > The merchant has issued the  |
|           | > Merchant/Credit       | > credit and no further        |
|           | >                       | >                              |
|           | > Adjustment by         | > action required for reported |
|           | > Merchant              | > dispute.                     |
+-----------+-------------------------+--------------------------------+
| > **29**  | > No Chargeback Rights  | > No Chargeback Rights         |
+-----------+-------------------------+--------------------------------+
| > **30**  | > Valid Document        | > The merchant has sent        |
|           | > Received (via email)  | > documentation via email/fax  |
|           |                         | >                              |
|           |                         | > to show proof of charge      |
+-----------+-------------------------+--------------------------------+
| > **31**  | > Card Activated via    | > The card was activated using |
|           | > Registered Phone      | > the registered number        |
|           |                         | >                              |
|           |                         | > on the account               |
+-----------+-------------------------+--------------------------------+
| > **32**  | > Card Still in Use     | > The card is reported as      |
|           | > (Lost/Stolen)         | > lost/stolen but is still in  |
|           |                         | > use                          |
+-----------+-------------------------+--------------------------------+
| > **33**  | > AVS Match             | > The Address on the merchant  |
|           |                         | > documents is a full          |
|           |                         | >                              |
|           |                         | > match to the registered      |
|           |                         | > address                      |
+-----------+-------------------------+--------------------------------+
| > **34**  | > Cancellation of       | > Based on merchant documents  |
|           | > Services Failed       | > cancellation of the          |
|           |                         | >                              |
|           |                         | > product/service was failed   |
+-----------+-------------------------+--------------------------------+
| > **35**  | > The card in           | > The card has not been        |
|           | > Possession not        | > reported as lost/stolen and  |
|           | > Lost/Stolen           | > is                           |
|           |                         | >                              |
|           |                         | > in possession                |
+-----------+-------------------------+--------------------------------+
| > **36**  | > No Evidence of Double | > No evidence of a double      |
|           | > Charge                | > charge is observed           |
+-----------+-------------------------+--------------------------------+
| > **37**  | > Cardholder            | > A pattern of multiple        |
|           | > Unauthorized Dispute  | > Unauthorized disputes filed  |
|           | >                       | > is                           |
|           | > Pattern               | >                              |
|           |                         | > observed                     |
+-----------+-------------------------+--------------------------------+
| > **38**  | > Additional CP         | > There are additional card    |
|           | > Transaction not       | > present transactions in the  |
|           | > Disputed              | >                              |
|           | >                       | > same time frame that are     |
|           | > (Lost/Stolen)         | > left undisputed              |
+-----------+-------------------------+--------------------------------+
| > **39**  | > Claim Filed in Error  | > The dispute was incorrectly  |
|           |                         | > filed                        |
+-----------+-------------------------+--------------------------------+
| > **40**  | > Friendly Fraud        | > A potential Friendly Fraud   |
|           |                         | > case according to the        |
|           |                         | >                              |
|           |                         | > information analyzed         |
+-----------+-------------------------+--------------------------------+

## Appendix E -- Possible Values of New Sub-fields in DE-111 {#appendix-e-possible-values-of-new-sub-fields-in-de-111 .unnumbered}

#### Stand In Trans Indicator {#stand-in-trans-indicator .unnumbered}

-   0 (Default Value)

-   1 (AuthHost Timed Out)

-   2 (AuthHost Down)

#### Token Type {#token-type .unnumbered}

-   01 (ECOM/COF- E-Commerce/Card-on-File)

-   02 (Secure Element)

-   03 (Cloud-Based Payment)

-   05 (E-Commerce Enabler)

#### Token Status {#token-status .unnumbered}

-   B (Active for payment)

-   I (Inactive for payment (not yet active))

-   S (Temporarily suspended for payments)

-   F (Permanently deactivated for payments)

-   D (Discard for payment)

#### Token Device Type {#token-device-type .unnumbered}

![](./image15.png){width="5.474232283464567in"
height="7.875311679790026in"}

#### Token Authorization Request Indicator {#token-authorization-request-indicator .unnumbered}

-   0 (Not a TAR Request)

-   1 (TAR Request)

#### Token Notification Type {#token-notification-type .unnumbered}

-   4300 (Token Completion Notification: Green Path)

-   4301 (Token Completion Notification: Yellow Path)

-   4302 (Token Completion Notification: Yellow Path Call Center)

-   4304 (Token Completion Notification: Red Path)

-   4305 (Token Creation Only Notification)

-   4401 (Token Event Notification: Deactivate Token)

-   4402 (Token Event Notification: Suspend Token)

-   4403 (Token Event Notification: Resume Token)

-   4306 (Token Event Notification: Token Data Update / Token Expiration
    Update)

-   4307 (Token Event Notification: Exception / Invalid OTP)

#### Chargeback Flag (Data Element 111.45) {#chargeback-flag-data-element-111.45 .unnumbered}

-   0 Chargeback Transaction

-   1 Chargeback Cancellation Transaction

-   2 Representment Transaction

-   3 Representment Reversal Transaction

-   4 2nd Chargeback Transaction

-   5 2nd Chargeback Cancellation Transaction

-   6 Arbitration Transaction

-   7 Arbitration Reversal Transaction

-   8 Chargeback Preauth Transaction

-   9 2nd Chargeback Preauth Transaction

-   A Chargeback Preauth Cancellation Transaction

-   B 2nd Chargeback Preauth Cancellation Transaction

-   C Chargeback Special Adjustment Transaction

-   D Chargeback Adjustment

-   E Chargeback Adjustment Reversal

##### On-behalf Service (Data Element 111.46) {#on-behalf-service-data-element-111.46 .unnumbered}

> Data Element 111.46 is mapped to Mastercard Data Element 48,
> Sub-element 71. This sub-element identifies the type of Mastercard
> on-behalf service performed on the transaction. There are 3 sub-fields
> of this sub-element.

+----+-------------------+----------+----------------------------------+
| >  | > **Field Name**  | > **     | > **Description**                |
|  * |                   | Subfield |                                  |
| *N |                   | >        |                                  |
| o. |                   | Length** |                                  |
| ** |                   |          |                                  |
+====+===================+==========+==================================+
| >  | > On-behalf       | > 2      | > It contains the on-behalf      |
|  1 | > Service         |          | > service indicator. (see below  |
|    | > Indicator       |          | > the list of possible on-behalf |
|    |                   |          | > service indicators)            |
+----+-------------------+----------+----------------------------------+
| >  | > On-behalf       | > 1      | > It indicates the results of    |
|  2 | > Result 1        |          | > the service processing.        |
+----+-------------------+----------+----------------------------------+
| >  | > On-behalf       | > 1      | > It contains the on-behalf      |
|  3 | > Result 2        |          | > result 2 indicator value.      |
+----+-------------------+----------+----------------------------------+

> Below are the possible results for Fraud Scoring On-behalf Service:

![](./image16.png){width="6.477802930883639in"
height="0.8065616797900262in"}

##### Fraud Scoring Data (Data Element 111.47) {#fraud-scoring-data-data-element-111.47 .unnumbered}

> Data Element 111.47 is mapped to Mastercard Data Element 48,
> Subelement 75. Mastercard fraud scoring solution provides customers &
> issuers an opportunity to enroll in Expert Monitoring Real time Fraud
> Scoring Service & Fraud Rules Manager respectively to assess the fraud
> scoring of a financial transactions.

+----+-----------------+------+------+--------------------------------+
| >  | > **Field       | > ** | > ** | > **Description**              |
|  * | > Name**        | Subf | Subf |                                |
| *N |                 | ield | ield |                                |
| o. |                 | >    | >    |                                |
| ** |                 | ID** | Leng |                                |
|    |                 |      | th** |                                |
+====+=================+======+======+================================+
| >  | > Fraud         | > 01 | > 03 | > Fraud Scoring System         |
|  1 | > Assessment    |      |      | > provides the risk score of   |
|    | > Score         |      |      | > 000-999 where 000 indicates  |
|    |                 |      |      | > the least likely fraudulent  |
|    |                 |      |      | > transaction and 999          |
|    |                 |      |      | > indicates the most likely    |
|    |                 |      |      | > fraudulent transaction.      |
+----+-----------------+------+------+--------------------------------+
| >  | > Score Reason  | > 02 | > 02 | > Fraud Scoring System         |
|  2 | > Code          |      |      | > provides the Score Reason    |
|    |                 |      |      | > Code, an alphanumeric code   |
|    |                 |      |      | > identifying the data used to |
|    |                 |      |      | > derive the fraud score.      |
|    |                 |      |      | >                              |
|    |                 |      |      | > **Score \| Reason Code       |
|    |                 |      |      | > Description XX** \|          |
|    |                 |      |      | > Suspicious transaction       |
|    |                 |      |      |                                |
|    |                 |      |      | Y.  \| Four or more swiped     |
|    |                 |      |      |     > transactions on a self-  |
|    |                 |      |      |     > service terminal in the  |
|    |                 |      |      |     > past two days            |
|    |                 |      |      |                                |
|    |                 |      |      | Z.  \| Suspicious activity     |
|    |                 |      |      |     > during the past three    |
|    |                 |      |      |     > days                     |
+----+-----------------+------+------+--------------------------------+
| >  | > Rules Score   | > 03 | > 03 | > Fraud Rule Manager Service   |
|  3 |                 |      |      | > provides the rule adjusted   |
|    |                 |      |      | > score of 000--999, where 000 |
|    |                 |      |      | > indicates the least likely   |
|    |                 |      |      | > fraudulent transaction and   |
|    |                 |      |      | > 999 indicates the most       |
|    |                 |      |      | > likely fraudulent            |
|    |                 |      |      | > transaction.                 |
+----+-----------------+------+------+--------------------------------+
| >  | > Rule Reason   | > 04 | > 02 | > Fraud Rule Manager Service   |
|  4 | > Code 1        |      |      | > provides the Rule Reason     |
|    |                 |      |      | > Code, an alphanumeric code   |
|    |                 |      |      | > that identifies the data     |
|    |                 |      |      | > used to derive the Rule      |
|    |                 |      |      | > Adjusted Score.              |
+----+-----------------+------+------+--------------------------------+
| >  | > Rule Reason   | > 05 | > 02 | > Fraud Rule Manager Service   |
|  5 | > Code 2        |      |      | > provides the Rule Reason     |
|    |                 |      |      | > Code, an alphanumeric code   |
|    |                 |      |      | > that identifies the data     |
|    |                 |      |      | > used to derive the Rule      |
|    |                 |      |      | > Adjusted Score.              |
+----+-----------------+------+------+--------------------------------+

> Data received in this field will be in TLV (Tag-Length-Value) format.
> Sample data: 0103049020208
>
> This will be parsed as follows: Tag:01, Length:03, Value: 049 Tag:02,
> Length:02, Value: 08

## Appendix F -- Token Activation / OTP Notification Message Identification {#appendix-f-token-activation-otp-notification-message-identification .unnumbered}

> Token Activation / OTP Notification message can be identified with
> following fields, in addition to OTP code in DE 111:
>
> MTI = 0120, Filed 32 = 746922, Field 41 = 11111111, Field 42 =
> 111111111111111.

## Appendix G -- Token Provisioning -- Send OTP Request {#appendix-g-token-provisioning-send-otp-request .unnumbered}

> Administrative request (Token Provisioning -- Send OTP) Request
> message will contain following mandatory information:
>
> MTI = 0600
>
> Field 02 = PRIMARY ACCOUNT NUMBER Field 07 = LOCAL TRANSMISSION DATE
> TIME
>
> Field 18 = 7299
>
> Field 22 = 01
>
> Field 25 = 66
>
> Field 32 = 746922
>
> Field 41 = 11111111
>
> Field 42 = 111111111111111
>
> Field 63 = VISA \[switchType at position 59 --\> total length 70\]
>
> Field 111 = Contains OTP, OTP Expiry DateTime, Cardholder Verification
> Method Identifier & Value OTP Expiry Date Time (Value will be in GMT)
>
> Expected response codes in DE39 in response. Success = 00
>
> Format Error = 30 Transaction not allowed = 57 System malfunction = 96
> Refer to Card Issuer = 01

## Appendix H -- Token Transactions Flow {#appendix-h-token-transactions-flow .unnumbered}

+-----------------------------------------------------------------------+
| > **Token Messages**                                                  |
+=======================================================================+
| > Message with **MTI 0100** with **TAR** indicator in DE 111.         |
+-----------------------------------------------------------------------+
| > **Token Activation Message** with **MTI 0120** with Access Code     |
| > (OTP) and Code Expiry in DE 111. \[Optional only if TAR qualifies   |
| > for yellow path\]                                                   |
+-----------------------------------------------------------------------+
| > **Token Complete Notification** with MTI 0620 with indication in DE |
| > 111. Token Notification Type with following values:                 |
| >                                                                     |
| > 4300 (Green Path)                                                   |
| >                                                                     |
| > 4301 (Yellow Path OTP)                                              |
| >                                                                     |
| > 4302 (Yellow Path Call Center) 4304 (Red Path)                      |
| >                                                                     |
| > 4305 (Token Creation Only)                                          |
+-----------------------------------------------------------------------+
| > **Token Event Notification** with MTI 0620 with indication in DE    |
| > 111. Token Notification Type with following values:                 |
| >                                                                     |
| > 4401 (Token Deactivate F) 4402 (Token Suspend S) 4403 (Token Resume |
| > B)                                                                  |
| >                                                                     |
| > 4306 (Token Data Update / Token Expiration Update)                  |
+-----------------------------------------------------------------------+
| > PAN replacement message (in case of PAN reissued with new number)   |
| > with MTI 0302 with indication in DE 111.                            |
| >                                                                     |
| > Replacement PAN (New PAN)                                           |
| >                                                                     |
| > Replacement PAN Expiration Date                                     |
+-----------------------------------------------------------------------+

## Appendix I -- Token Creation Green/Red/Yellow Path Identification from Issue Perspective {#appendix-i-token-creation-greenredyellow-path-identification-from-issue-perspective .unnumbered}

##### Green Path: {#green-path .unnumbered}

> TAR Message with DE 39 = 00.

##### Yellow Path: {#yellow-path .unnumbered}

> TAR Message with DE 39 = 85.

##### Red Path: {#red-path .unnumbered}

> TAR Message with DE 39 = 05.

## Appendix J -- Message Type Identifiers {#appendix-j-message-type-identifiers .unnumbered}

+------+---------------------------------------------------------------+
| >    | > **Description**                                             |
|  **M |                                                               |
| TI** |                                                               |
+======+===============================================================+
| >    | > Authorization Request                                       |
| 0100 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Authorization Response                                      |
| 0110 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Token Provisioning -- Send OTP Request                      |
| 0100 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Token Provisioning -- Send OTP Response                     |
| 0110 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Token OTP Notification                                      |
| 0120 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Token OTP Notification Response                             |
| 0130 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Advice Authorization Request                                |
| 0120 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Authorization Advice Response                               |
| 0130 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Financial Transaction Request                               |
| 0200 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Financial Transaction Response                              |
| 0210 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Financial Transaction Advice                                |
| 0220 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Financial Transaction Response                              |
| 0230 |                                                               |
+------+---------------------------------------------------------------+
| >    | > File Update Request                                         |
| 0302 |                                                               |
+------+---------------------------------------------------------------+
| >    | > File Update Request Response                                |
| 0312 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Reversal Advice                                             |
| 0420 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Reversal Advice Response                                    |
| 0430 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Administrative Request                                      |
| 0600 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Administrative Advice                                       |
| 0620 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Administrative Advice Response                              |
| 0630 |                                                               |
+------+---------------------------------------------------------------+
| >    | > Network Management Request (Mandatory for TCP/IP            |
| 0800 | > Communication)                                              |
+------+---------------------------------------------------------------+
| >    | > Network Management Response (Mandatory for TCP/IP           |
| 0810 | > Communication)                                              |
+------+---------------------------------------------------------------+

> 100 Redwood Shores Parkway, Suite 100, Redwood City, CA 94065
> +1-650-593-5400 \| <connect@i2cinc.com>
> [www.i2cinc.com](http://www.i2cinc.com/)

## Appendix K -- Anticipated Amount Transaction {#appendix-k-anticipated-amount-transaction .unnumbered}

> Anticipated amount verification transactions are Account verification
> transactions with anticipated amount which is used to confirm the
> account has availability to accept purchases.
>
> Host which are system of records or have balance maintained at their
> end must confirm the anticipated amount, and sending the appropriate
> response code. Host must not hold funds during the processing of an
> anticipated amount verification transaction.
>
> A new amount type code 44 is used to identify anticipated amounts in
> Field 54.
>
> When both the account and anticipated amount are validated by the
> host, the response message will contain the existing value of 00
> (Approved) in Field 39---Response Code.
>
> When only the account is validated, the response message will contain
> one of the following values in Field 39---Response Code:

-   85 (Approved -- Account Verification)

-   X6 (Valid account but amount not supported) Anticipated Amount
    verification transactions Identification:

-   A 0100 Account verification request

-   Field 4---Amount, Transaction contains all zeros

-   Field 25---Point-of-Service Condition Code contains the existing
    > value of **62** (Account Verification w/o Auth; product
    > eligibility inquiry without authorization)

-   Field 54---Additional Amounts contains an anticipated amount type
    > code.

-   Field 63.7 = "VISA".
