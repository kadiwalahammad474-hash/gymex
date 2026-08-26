# 🏥 MediFlow — Complete Business Documentation

## Clinic Management Platform | Pharmacy Module | Diagnostic Integration

**Version:** 1.0  
**Date:** 26 August 2026  
**Company:** GreyBits Technologies  
**Founders:** Hammad Kadiwala, Rohit, Imran  

---

# TABLE OF CONTENTS

1. [Company Overview](#1-company-overview)
2. [Platform Overview](#2-platform-overview)
3. [User Roles](#3-user-roles)
4. [Complete User Flows](#4-complete-user-flows)
5. [Features Summary](#5-features-summary)
6. [Database Schema](#6-database-schema)
7. [CDSS Engine](#7-cdss-engine)
8. [Security Features](#8-security-features)
9. [Technical Architecture](#9-technical-architecture)
10. [Revenue Model](#10-revenue-model)
11. [Launch Plan](#11-launch-plan)
12. [Team & Work Distribution](#12-team--work-distribution)

---

# 1. COMPANY OVERVIEW

## 1.1 Vision
Build software platforms that simplify healthcare management across India and globally.

## 1.2 Mission
- **MediFlow**: Help clinics run paperless with smart prescription management
- Digitize patient registration, doctor consultations, prescriptions, pharmacy, diagnostics, and billing
- Make healthcare accessible, efficient, and affordable

## 1.3 Target Customers

| Customer Type | Size | Monthly Fee |
|--------------|------|-------------|
| Single Doctor Clinic | 1 doctor | ₹999/month |
| Small Clinic | 2-5 doctors | ₹1,999/month |
| Medium Clinic | 6-15 doctors | ₹3,999/month |
| Hospital | 15+ doctors | ₹7,999/month |
| Pharmacy Chain | Multi-location | Custom pricing |
| Diagnostic Lab | Multi-test | Custom pricing |

## 1.4 Target Locations

| Region | Focus | Timeline |
|--------|-------|----------|
| Mumbai | Pilot (10 clinics) | Month 1-2 |
| Maharashtra | Scale (50 clinics) | Month 3-6 |
| Tier 1 Cities | Expand (200 clinics) | Month 6-12 |
| Pan India | Growth (1000+ clinics) | Year 2-3 |

---

# 2. PLATFORM OVERVIEW

## 2.1 What is MediFlow?

MediFlow is a comprehensive clinic management platform that digitizes:
- Patient registration and records
- Doctor consultations (walk-in + video)
- Prescription management with CDSS alerts
- Pharmacy dispensing and stock management
- Diagnostic lab integration
- Billing and payments
- Compliance (GST, DPDP, Schedule H1)

## 2.2 Codebase Stats

| Metric | Count |
|--------|-------|
| Entities | 61 |
| Services | 74 |
| Controllers | 25 |
| API Endpoints | 100+ |
| Background Jobs | 8 |
| Build Status | ✅ 0 Errors |
| Test Status | ✅ 35/35 Passed |
| Git Commits | 45+ |

## 2.3 Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | ASP.NET Core 8.0 (C#) |
| **Database** | PostgreSQL |
| **Cache** | Redis |
| **Auth** | JWT + MFA (TOTP) |
| **File Storage** | AWS S3 / Azure Blob |
| **Real-time** | SignalR (WebSocket) |
| **Background Jobs** | Hangfire |
| **Logging** | Serilog → ELK Stack |
| **Monitoring** | Application Insights |

---

# 3. USER ROLES

## 3.1 Role Definitions

| Role | Access Level | Primary Functions | Login Method |
|------|-------------|-------------------|--------------|
| **Clinic Owner** | Full | Dashboard, Reports, Settings, Staff Management | Email + Password + MFA |
| **Doctor** | Patient + Prescription | Consultation, Rx, Video Call, Schedule | Email + Password + MFA |
| **Receptionist** | Front Desk | Patient Registration, Visits, Billing, Queue | Staff PIN (4-digit) |
| **Pharmacist** | Pharmacy Module | Dispensing, Stock, Returns, H1 Register | Staff PIN (4-digit) |
| **Lab Technician** | Diagnostics | Test Orders, Results, Reports | Staff PIN (4-digit) |

## 3.2 Role Permissions

```
CLINIC OWNER:
├── Full access to all modules
├── View all reports and analytics
├── Manage staff (add/remove/roles)
├── Configure settings (GST, payment gateway)
├── Export data (CSV/PDF)
├── Manage subscription
└── View audit logs

DOCTOR:
├── View own patients
├── Create/edit prescriptions
├── View patient history
├── Order lab tests
├── Conduct video consultations
├── View own schedule
├── View own revenue
└── Cannot: billing, stock, reports

RECEPTIONIST:
├── Register new patients
├── Create visits
├── Assign tokens
├── Collect payments
├── Print receipts
├── View queue
└── Cannot: prescriptions, reports, settings

PHARMACIST:
├── View prescriptions
├── Dispense medicines
├── Manage stock
├── Return to supplier
├── View H1 register
├── Print labels
└── Cannot: patient registration, billing

LAB TECHNICIAN:
├── View test orders
├── Enter test results
├── Print reports
├── View lab revenue
└── Cannot: prescriptions, billing, stock
```

---

# 4. COMPLETE USER FLOWS

## 4.1 Clinic Owner Flow

```
┌─────────────────────────────────────────────────────────────┐
│  CLINIC OWNER — DAILY FLOW                                   │
└─────────────────────────────────────────────────────────────┘

LOGIN → DASHBOARD
├── Today's Revenue: ₹XX,XXX
├── Patients Today: XX
├── Pending Bills: ₹XX,XXX
├── Stock Alerts: XX
├── Doctor Performance
├── Revenue Trends (graph)
└── Quick Actions:
    ├── Add Patient
    ├── Create Visit
    ├── View Reports
    └── Settings

DAILY TASKS:
├── Morning (9 AM)
│   ├── Review today's schedule
│   ├── Check stock alerts
│   ├── Review pending payments
│   └── Staff attendance
│
├── Throughout Day
│   ├── Monitor queue status
│   ├── Check revenue
│   ├── Review doctor performance
│   └── Handle escalations
│
├── Evening (6 PM)
│   ├── Day-end cash tally
│   ├── Review day's revenue
│   ├── Check pending tasks
│   └── Plan for tomorrow
│
└── Weekly
    ├── Revenue reports
    ├── Staff review
    ├── Stock reorder
    ├── Patient feedback
    └── Business planning

MANAGEMENT TASKS:
├── Add/Remove Doctors
├── Add/Remove Staff
├── Configure GST rates
├── Set up payment gateway
├── Import patient data (CSV)
├── Set subscription plan
├── View analytics dashboard
└── Export reports
```

## 4.2 Receptionist Flow (Walk-in First, <20 seconds)

```
┌─────────────────────────────────────────────────────────────┐
│  RECEPTIONIST — WALK-IN PATIENT FLOW                         │
│  Target: <20 seconds from entry to registered                │
└─────────────────────────────────────────────────────────────┘

STEP 1: Patient Arrives (0-2 seconds)
├── Click "New Visit" button
├── Enter phone number in search box
└── Press Enter

STEP 2: Phone Lookup (2-3 seconds)
├── EXISTING PATIENT:
│   ├── Auto-load: Name, Age, Gender
│   ├── Show: Last visit date
│   ├── Show: Allergies (if any)
│   └── Go to Step 3
│
└── NEW PATIENT:
    ├── Quick form appears
    ├── Enter: Name (required)
    ├── Enter: Age (required)
    ├── Select: Gender (required)
    └── Click "Save" (1 second)

STEP 3: Create Visit (3-5 seconds)
├── Select Doctor (dropdown)
├── Visit Type: Consultation (₹500)
├── Token Number: Auto-assigned (#015)
├── Queue Position: 3rd in line
└── Click "Create Visit"

STEP 4: Patient Waits
├── TV Display: "Token #015 - Your turn in ~15 minutes"
├── Doctor Delayed Alert (if >20 min)
└── SMS notification when turn near

STEP 5: After Consultation
├── Doctor finalizes prescription
├── Receptionist collects payment
├── Print receipt (thermal/A4)
└── Patient leaves

TOTAL TIME: <20 seconds ✅
```

### Receptionist Dashboard:

```
┌─────────────────────────────────────────────────────────────┐
│  RECEPTIONIST DASHBOARD                                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─ TODAY'S STATS ─────────────────────────────────────────┐ │
│  │  Patients Today: 24    │  Pending Bills: ₹8,500         │ │
│  │  Queue Length: 5       │  Revenue Today: ₹12,000         │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ CURRENT QUEUE ─────────────────────────────────────────┐ │
│  │  Token │ Patient      │ Doctor    │ Status    │ Time     │ │
│  │  #012  │ Rahul Kumar  │ Dr. Shah  │ With Doc  │ 10:45 AM │ │
│  │  #013  │ Priya Patel  │ Dr. Shah  │ Waiting   │ --       │ │
│  │  #014  │ Amit Singh   │ Dr. Gupta │ Waiting   │ --       │ │
│  │  #015  │ Neha Reddy   │ Dr. Shah  │ Waiting   │ --       │ │
│  │  #016  │ Vikram Rao   │ Dr. Gupta │ Waiting   │ --       │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ QUICK ACTIONS ─────────────────────────────────────────┐ │
│  │  [+ New Visit]  [Search Patient]  [Collect Payment]      │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ PENDING PAYMENTS ──────────────────────────────────────┐ │
│  │  Patient      │ Amount  │ Due Date  │ Status             │ │
│  │  Rahul Kumar  │ ₹500    │ Today     │ [Collect]          │ │
│  │  Priya Patel  │ ₹1,200  │ Yesterday │ [Remind]           │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 4.3 Doctor Consultation Flow

```
┌─────────────────────────────────────────────────────────────┐
│  DOCTOR — CONSULTATION FLOW                                  │
└─────────────────────────────────────────────────────────────┘

LOGIN → DASHBOARD
├── Today's Schedule
│   ├── Walk-ins: 15 patients
│   ├── Video Consults: 5 patients
│   └── Follow-ups: 3 patients
│
├── Current Queue
│   ├── #012 Rahul Kumar - Waiting 10 min
│   ├── #013 Priya Patel - Waiting 5 min
│   └── #014 Amit Singh - Just arrived
│
└── Quick Actions
    ├── [View Next Patient]
    ├── [Start Video Call]
    └── [View Schedule]

═══════════════════════════════════════════════════════════════

CONSULTATION FLOW:

1. Patient calls/arrives
   └── Receptionist creates visit

2. Doctor opens patient file
   ├── Previous Visits (full history)
   │   ├── Visit on 15 Aug: Fever, prescribed Paracetamol
   │   ├── Visit on 10 Jul: Check-up, all normal
   │   └── Visit on 5 May: Back pain, prescribed Ibuprofen
   │
   ├── Allergies (highlighted RED)
   │   └── ⚠️ Allergic to Penicillin
   │
   ├── Current Medications
   │   ├── Amlodipine 5mg (for BP)
   │   └── Metformin 500mg (for Diabetes)
   │
   ├── Lab Reports (if any)
   │   ├── CBC (15 Aug): Normal
   │   ├── Lipid Profile (1 Jul): Cholesterol high
   │   └── Blood Sugar (1 Jul): Slightly elevated
   │
   └── Vitals History
       ├── BP: 130/85 (15 Aug)
       ├── Weight: 75 kg (15 Aug)
       └── Temperature: 98.6°F (15 Aug)

3. Enter Vitals
   ├── Blood Pressure: 120/80
   ├── Temperature: 101°F
   ├── Weight: 74 kg
   ├── Height: 5'10"
   ├── Pulse: 88 bpm
   └── SpO2: 97%

4. Chief Complaint
   └── "Fever, body ache, sore throat for 3 days"

5. Diagnosis
   ├── Primary: Acute Pharyngitis (ICD-10: J02.9)
   └── Secondary: Viral Fever (ICD-10: B34.9)

6. Prescription Entry
   │
   ├── Drug 1: Amoxicillin 500mg
   │   ├── Dosage: 1-0-1 (3 times/day)
   │   ├── Duration: 5 days
   │   ├── Quantity: 15 tablets
   │   └── CDSS: ⚠️ ALERT! Patient allergic to Penicillin!
   │
   ├── Drug 2: Paracetamol 650mg
   │   ├── Dosage: SOS (as needed)
   │   ├── Duration: 5 days
   │   ├── Quantity: 10 tablets
   │   └── CDSS: ✅ No interaction
   │
   ├── Drug 3: Cetirizine 10mg
   │   ├── Dosage: 0-0-1 (at bedtime)
   │   ├── Duration: 5 days
   │   ├── Quantity: 5 tablets
   │   └── CDSS: ⚠️ May cause drowsiness
   │
   └── Auto-save draft (every 5 seconds)

7. CDSS Alerts (Real-time)
   ├── Drug-Drug Interaction: ✅ Clear
   ├── Drug-Allergy Alert: ⚠️ Amoxicillin + Penicillin allergy!
   ├── Drug-Food Interaction: ✅ Clear
   ├── Dosage Validation: ✅ Within range
   └── Generic Substitute: 💡 Suggestion available

8. Doctor Action (on CDSS alert)
   ├── Option A: Override alert (with reason)
   ├── Option B: Change drug (recommended)
   └── Option C: Stop prescription

9. Finalize Rx
   ├── Print: Thermal/A4/A5
   ├── WhatsApp: PDF to patient
   ├── SMS: PWA link (feature phones)
   └── Save: Cloud (AES-256 encrypted)

10. Order Lab Tests (if needed)
    ├── CBC, Lipid Profile, Thyroid
    └── Auto-sync to lab module

11. Follow-up
    └── "Come back in 7 days" → Auto reminder SMS
```

### Doctor Dashboard:

```
┌─────────────────────────────────────────────────────────────┐
│  DOCTOR DASHBOARD — Dr. Rajesh Shah                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─ TODAY'S SCHEDULE ──────────────────────────────────────┐ │
│  │  Walk-ins: 15    │  Video: 5    │  Follow-ups: 3        │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ CURRENT QUEUE ─────────────────────────────────────────┐ │
│  │  Token │ Patient      │ Wait Time │ Chief Complaint      │ │
│  │  #012  │ Rahul Kumar  │ 10 min    │ Fever, body ache     │ │
│  │  #013  │ Priya Patel  │ 5 min     │ Headache             │ │
│  │  #014  │ Amit Singh   │ 2 min     │ Back pain            │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ QUICK ACTIONS ─────────────────────────────────────────┐ │
│  │  [View #012 Rahul]  [Start Video Call]  [View History]   │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ TODAY'S PATIENTS ──────────────────────────────────────┐ │
│  │  Patient      │ Time    │ Diagnosis        │ Revenue     │ │
│  │  Amit Singh   │ 9:30 AM │ Migraine         │ ₹500       │ │
│  │  Suresh Nair  │ 10:00 AM│ Diabetes         │ ₹500       │ │
│  │  (3 more)     │         │                  │             │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 4.4 Video Consultation Flow

```
┌─────────────────────────────────────────────────────────────┐
│  VIDEO CONSULTATION FLOW                                     │
└─────────────────────────────────────────────────────────────┘

STEP 1: Doctor Initiates
├── Select patient from queue
├── Click "Start Video Consult"
├── System generates WhatsApp link
└── Link sent to patient via WhatsApp/SMS

STEP 2: Patient Joins
├── Patient clicks WhatsApp link
├── Browser opens (no app needed)
├── Waiting room appears
└── "Dr. Shah will be with you shortly"

STEP 3: Doctor Admits
├── Doctor sees "Patient waiting" notification
├── Click "Admit" or "Reject"
├── If admit: Video call starts
└── If reject: "Doctor unavailable, please reschedule"

STEP 4: Video Call
├── WebRTC peer-to-peer connection
├── TURN server for NAT traversal
├── HD video + audio
├── Screen sharing (for reports)
├── Chat (text)
└── Record (with patient consent)

STEP 5: Consultation
├── Doctor asks symptoms
├── Views patient history (shared screen)
├── Discusses diagnosis
├── Explains prescription
├── Answers questions
└── Schedules follow-up

STEP 6: End Call
├── Doctor clicks "End Call"
├── Prescription auto-generated
├── Rx sent via WhatsApp
├── Bill generated
├── Payment collected (online)
└── Call recording saved (encrypted)
```

## 4.5 Pharmacist Flow

```
┌─────────────────────────────────────────────────────────────┐
│  PHARMACIST — DISPENSING FLOW                                │
└─────────────────────────────────────────────────────────────┘

LOGIN → PHARMACY DASHBOARD
├── Today's Summary
│   ├── Prescriptions Received: 24
│   ├── Dispensed: 18
│   ├── Pending: 6
│   ├── Revenue: ₹12,500
│   └── Stock Alerts: 3

═══════════════════════════════════════════════════════════════

DISPENSING FLOW:

1. Receive prescription
   ├── From doctor's Rx
   ├── Shows: Patient name, drugs, dosages
   └── Status: "Pending Dispensing"

2. Select prescription
   └── Click "Dispense"

3. Auto-select batch (FEFO - First Expiry First Out)
   │
   ├── Amoxicillin 500mg
   │   ├── Batch: AMP-2026-03
   │   ├── MRP: ₹85
   │   ├── Expiry: Dec 2026
   │   ├── Stock: 150 tabs
   │   └── Selected: 15 tabs
   │
   ├── Paracetamol 650mg
   │   ├── Batch: PCM-2026-05
   │   ├── MRP: ₹25
   │   ├── Expiry: Mar 2027
   │   ├── Stock: 300 tabs
   │   └── Selected: 10 tabs
   │
   └── Cetirizine 10mg
       ├── Batch: CTZ-2026-02
       ├── MRP: ₹35
       ├── Expiry: Nov 2026
       ├── Stock: 80 tabs
       └── Selected: 5 tabs

4. Partial dispensing (if stock low)
   ├── "Only 4 of 10 tablets available"
   ├── System notifies doctor
   ├── Doctor approves partial
   └── Bill adjusted

5. Scan barcode → Auto-add to bill
   ├── Barcode scanner reads batch
   ├── Auto-adds to bill
   └── Stock deducted

6. Print label
   ├── Patient name
   ├── Drug name + dosage
   ├── Instructions
   └── Pharmacy details

7. Collect payment
   ├── Cash/Card/UPI
   └── Receipt printed

═══════════════════════════════════════════════════════════════

STOCK MANAGEMENT:

Receive Stock:
├── From distributor
├── Enter: Drug name, batch, MRP, expiry, quantity
├── Scan barcode (optional)
└── Auto-update stock

Return Stock:
├── Near-expiry (3 months before)
├── Select batch → Return
├── Distributor credit note generated
└── Stock deducted

Stock Reports:
├── Current stock value
├── Expiry-wise stock
├── Slow-moving items
├── Stock valuation (FIFO)
└── Reorder alerts

═══════════════════════════════════════════════════════════════

SCHEDULE H1 REGISTER:

Auto-generated register for antibiotics:
├── Patient name
├── Drug name
├── Prescribing doctor
├── Date & time
├── Quantity dispensed
└── Export as PDF (for drug inspector)

═══════════════════════════════════════════════════════════════

ALERTS:

├── Stock below reorder level
│   └── "Amoxicillin: Only 20 tabs left, reorder!"
│
├── Batch expiring in 30 days
│   └── "CTZ-2026-02 expires in 25 days"
│
├── MRP mismatch warning
│   └── "Batch MRP differs from master MRP"
│
└── Drug interaction alert
    └── "Pharmacist override noted in audit"
```

### Pharmacist Dashboard:

```
┌─────────────────────────────────────────────────────────────┐
│  PHARMACY DASHBOARD                                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─ TODAY'S SUMMARY ───────────────────────────────────────┐ │
│  │  Rx Received: 24   │  Dispensed: 18   │  Pending: 6     │ │
│  │  Revenue: ₹12,500  │  Stock Alerts: 3                    │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ PENDING PRESCRIPTIONS ─────────────────────────────────┐ │
│  │  Token │ Patient      │ Doctor    │ Drugs │ Amount       │ │
│  │  #012  │ Rahul Kumar  │ Dr. Shah  │ 3     │ ₹425        │ │
│  │  #013  │ Priya Patel  │ Dr. Shah  │ 2     │ ₹180        │ │
│  │  #014  │ Amit Singh   │ Dr. Gupta │ 1     │ ₹85         │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ STOCK ALERTS ──────────────────────────────────────────┐ │
│  │  ⚠️ Amoxicillin 500mg: Only 20 tabs left               │ │
│  │  ⚠️ Paracetamol 650mg: Expires in 25 days               │ │
│  │  ⚠️ Cetirizine 10mg: MRP mismatch detected              │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌─ QUICK ACTIONS ─────────────────────────────────────────┐ │
│  │  [Dispense Rx]  [Receive Stock]  [Return Stock]          │ │
│  │  [View H1 Register]  [Stock Report]                      │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 4.6 Diagnostic Lab Flow

```
┌─────────────────────────────────────────────────────────────┐
│  DIAGNOSTIC LAB FLOW                                         │
└─────────────────────────────────────────────────────────────┘

1. Doctor prescribes test
   ├── CBC, Lipid Profile, Thyroid
   └── Auto-sync to lab module

2. Lab receives order
   ├── Patient registration (if new)
   ├── Sample collection
   │   ├── Blood draw
   │   ├── Urine sample
   │   └── Other specimens
   │
   ├── Test performed
   │   ├── Hematology analyzer
   │   ├── Biochemistry analyzer
   │   └── Manual microscopy
   │
   └── Results entered
       ├── Manual entry
       ├── Auto-import from analyzer
       └── Reference range comparison

3. Auto-sync to doctor
   ├── Doctor sees results in dashboard
   ├── Abnormal values HIGHLIGHTED
   ├── Compare with previous results
   └── Add notes/comments

4. Patient receives report
   ├── WhatsApp PDF
   ├── Email PDF
   ├── Print (A4)
   └── PWA link (feature phones)

5. Billing
   ├── Test charges added to bill
   ├── GST invoice generated
   └── Payment collected

═══════════════════════════════════════════════════════════════

REVENUE TRACKING:

├── Lab revenue: ₹XX,XXX
├── Tests performed: XX
├── Average test value: ₹XXX
├── Doctor referral commission: ₹XX,XXX
└── Pending payments: ₹XX,XXX
```

## 4.7 Day-End Flow (Cash Tally)

```
┌─────────────────────────────────────────────────────────────┐
│  DAY-END "HISAAB-KITAAB" (Reconciliation)                    │
└─────────────────────────────────────────────────────────────┘

1. Auto-calculate
   ├── Cash collected: ₹15,000
   ├── Card payments: ₹8,000
   ├── UPI payments: ₹5,000
   ├── Total revenue: ₹28,000
   └── Pending: ₹3,500

2. Physical cash count
   └── Enter actual cash in drawer: ₹15,200

3. Variance check
   ├── Expected: ₹15,000
   ├── Actual: ₹15,200
   └── Variance: +₹200 (over)

4. Investigation
   ├── Why ₹200 extra?
   ├── Check: Advance payments?
   ├── Check: Refund not given?
   └── Owner reviews

5. Sign-off
   ├── Doctor signs
   ├── Receptionist signs
   └── Owner reviews (next morning)

6. Export
   ├── PDF report
   ├── Excel export
   └── Email to owner

═══════════════════════════════════════════════════════════════

DAY-END REPORT EXAMPLE:

┌─────────────────────────────────────────────────────────────┐
│  DAY-END REPORT — 26 August 2026                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  REVENUE:                                                    │
│  ├── Consultation Fees: ₹8,000 (16 patients)                │
│  ├── Pharmacy Sales: ₹12,500                                │
│  ├── Lab Tests: ₹5,000                                      │
│  ├── Other: ₹2,500                                          │
│  └── TOTAL: ₹28,000                                         │
│                                                              │
│  PAYMENT BREAKDOWN:                                          │
│  ├── Cash: ₹15,000                                          │
│  ├── Card: ₹8,000                                           │
│  ├── UPI: ₹5,000                                            │
│  └── Pending: ₹3,500                                         │
│                                                              │
│  CASH RECONCILIATION:                                        │
│  ├── Expected: ₹15,000                                       │
│  ├── Actual: ₹15,200                                         │
│  └── Variance: +₹200                                         │
│                                                              │
│  PATIENTS:                                                   │
│  ├── Walk-ins: 18                                            │
│  ├── Video Consults: 5                                       │
│  └── Follow-ups: 3                                           │
│                                                              │
│  STOCK:                                                      │
│  ├── Items dispensed: 45                                     │
│  ├── Revenue: ₹12,500                                        │
│  └── Low stock alerts: 3                                     │
│                                                              │
│  SIGN-OFF:                                                   │
│  ├── Dr. Rajesh Shah: _________                              │
│  ├── Receptionist: _________                                 │
│  └── Owner: _________                                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

# 5. FEATURES SUMMARY

## 5.1 P0 Features (Launch Blockers) — ALL DONE ✅

| Feature | Description | Files |
|---------|-------------|-------|
| **Mobile SMS OTP Login** | Phone number se login, OTP via SMS | SmsOtpService |
| **Walk-in Flow (<20s)** | Patient arrives → 20 seconds mein registered | WalkInController |
| **Thermal/A4/A5 Printing** | Token slip, Rx, Invoice — sab print | PrintService |
| **GST Engine** | Consultation exempt, medicine taxable | GstService |
| **Credit Notes** | Invoice cancel pe auto credit note | CreditNoteService |
| **Clinical Dosage Model** | Weekly, ml, units — flexible dosage | PrescriptionItem |
| **Patient Dedup + Family** | Phone se auto-merge, family linking | PatientDedupService |
| **Idempotency + Concurrency** | Double-submit nahi, parallel edit detect | IdempotencyKey, RowVersion |
| **Subscription Billing** | Clinic se monthly SaaS fee collect | SubscriptionService |
| **CSV Patient Import** | Purana data 1-click import | PatientImportService |
| **Video Consult + TURN** | WhatsApp link se video call | VideoSecurityService |

## 5.2 P1 Features (Competitiveness) — ALL DONE ✅

| Feature | Description | Files |
|---------|-------------|-------|
| **Drug Interaction + Allergy CDSS** | Real-time drug safety alerts | CdssService |
| **Rx Templates** | Doctor ke top 30 drugs ki 1-click shortlist | RxTemplateService |
| **Local Language Rx** | Hindi/Marathi/Gujarati/Tamil dosage print | LocalLanguageRxService |
| **ABDM/ABHA Integration** | Ayushman Bharat Digital Mission | AbdmService |
| **Waiting Room + Live ETA** | Patient ko pata hai kitna wait | QueueEtaService |
| **Staff PIN Switch** | Staff ek click mein switch | StaffPinService |
| **Supplier Ledger + Purchase Orders** | Distributor ke saath accounts | SupplierLedgerService |
| **Day-End Cash Tally** | "Hisaab-Kitaab" reconciliation | DayEndTallyService |
| **Schedule H1 Register** | Antibiotics ka auto-register | ScheduleH1Service |
| **Consumables Tracking** | Syringes, cotton track | ConsumableTrackingService |

## 5.3 P2 Features (Expansion) — DONE ✅

| Feature | Description | Files |
|---------|-------------|-------|
| **Visiting Consultant Revenue Split** | Bahar ke doctor ka hissa auto-calc | VisitingConsultantService |
| **Export Tool (CSV/PDF)** | Data export kahi bhi le jao | DataExportService |
| **Offline Mode** | Internet nahi hai toh queue mein save | OfflineSyncService |
| **Emergency Chat Red-Flag** | "Heart attack" type keywords → auto-reply | EmergencyChatService |
| **Generic Substitute Suggestion** | Brand ki jagah generic dikhao | GenericSubstituteService |
| **Return to Supplier** | Near-expiry wapas karo | ReturnToSupplierService |
| **Doctor Registration Expiry** | License expiry tracking + alerts | DoctorRegistrationService |
| **Doctor Delayed TV Broadcast** | "Dr. Sharma running 20 min late" | DoctorDelayBroadcastService |

## 5.4 Complete Feature List

```
PATIENT MANAGEMENT:
├── Patient registration (Name, Phone, Age, Gender)
├── Patient search (by phone, name, ID)
├── Patient history (visits, prescriptions, reports)
├── Family member linking
├── Medical conditions/allergies
├── Photo upload
├── Consent records (DPDP)
└── Patient dedup + auto-merge

DOCTOR MANAGEMENT:
├── Doctor profiles (Name, Speciality, Schedule)
├── Doctor registration expiry tracking
├── Doctor availability calendar
├── Video consultation setup
├── Prescription templates
└── Doctor performance reports

RECEPTIONIST FEATURES:
├── Walk-in patient flow (<20 seconds)
├── Token/queue management
├── Quick billing
├── Payment collection (Cash/Card/UPI)
├── Receipt printing (Thermal/A4)
└── Day-end reconciliation

PRESCRIPTION FEATURES:
├── Drug entry with dosage
├── CDSS alerts (Drug-Drug, Drug-Allergy)
├── Generic substitute suggestions
├── Local language dosage (Hindi/Marathi/Gujarati/Tamil)
├── Rx templates (doctor's shortlist)
├── Auto-save drafts (every 5 seconds)
├── Print (Thermal/A4/A5)
├── WhatsApp PDF delivery
├── SMS PWA link (feature phones)
└── Schedule H1 register (antibiotics)

PHARMACY FEATURES:
├── Drug inventory management
├── Batch-wise stock (MRP, expiry)
├── FEFO dispensing (First Expiry First Out)
├── Partial dispensing
├── Barcode scanning
├── Return to supplier
├── Stock valuation (FIFO)
├── Consumables tracking
└── Schedule H1 register

DIAGNOSTIC FEATURES:
├── Test order management
├── Result entry (manual/auto-import)
├── Abnormal value highlighting
├── Previous result comparison
├── Report generation (PDF)
├── Doctor auto-sync
└── Revenue tracking

BILLING FEATURES:
├── Auto invoice generation (GST)
├── Multiple payment modes
├── Payment gateway (Razorpay/Stripe)
├── Credit notes
├── Refund tracking
├── Revenue reports
└── Day-end cash tally

COMPLIANCE FEATURES:
├── GST engine (exempt + taxable)
├── Schedule H1 register
├── DPDP two-tier deletion
├── Audit trail
├── Consent records
└── Data retention enforcement

COMMUNICATION FEATURES:
├── SMS notifications
├── Email notifications
├:// WhatsApp PDF delivery
├── Emergency chat red-flag
├── Doctor delay broadcast
└── Follow-up reminders

REPORTS & ANALYTICS:
├── Revenue reports (Daily/Weekly/Monthly)
├── Patient reports
├── Prescription reports
├── Stock reports
├── Doctor performance reports
├── Export (CSV/Excel/PDF)
└── Custom date range
```

---

# 6. DATABASE SCHEMA

## 6.1 Entity Overview (61 Entities)

### Core Entities

| Entity | Purpose | Key Fields |
|--------|---------|------------|
| **Patient** | Patient demographics | Id, Name, Phone, Age, Gender, Address, Allergies |
| **Doctor** | Doctor profiles | Id, Name, Speciality, Schedule, RegistrationNo |
| **Staff** | Staff members | Id, Name, Role, Phone, Pin, Salary |
| **Visit** | Patient visit record | Id, PatientId, DoctorId, Type, Token, Status |
| **Prescription** | Doctor's prescription | Id, VisitId, DoctorId, Notes, Status |
| **PrescriptionItem** | Individual drug | Id, PrescriptionId, DrugName, Dosage, Duration |

### Billing Entities

| Entity | Purpose | Key Fields |
|--------|---------|------------|
| **Invoice** | Billing header | Id, VisitId, PatientId, Total, Status |
| **InvoiceItem** | Bill line item | Id, InvoiceId, Description, Amount, GST |
| **Payment** | Payment record | Id, InvoiceId, Amount, Mode, Status |
| **CreditNote** | Invoice cancellation | Id, InvoiceId, Amount, Reason |
| **PaymentRefund** | Refund tracking | Id, PaymentId, Amount, Reason, Status |

### Pharmacy Entities

| Entity | Purpose | Key Fields |
|--------|---------|------------|
| **DrugInventory** | Drug master | Id, Name, Salt, Category, MRP |
| **StockBatch** | Batch-wise stock | Id, DrugId, BatchNo, MRP, Expiry, Qty |
| **StockTransaction** | Stock movement | Id, DrugId, BatchId, Type, Qty, Date |
| **ScheduleH1Register** | Antibiotics log | Id, DrugId, PatientId, DoctorId, Date |
| **Supplier** | Distributor details | Id, Name, Phone, Address, Balance |
| **SupplierLedger** | Distributor account | Id, SupplierId, Type, Amount, Date |
| **PurchaseOrder** | Stock purchase | Id, SupplierId, Total, Status |
| **PurchaseOrderItem** | PO line items | Id, POId, DrugId, Qty, Rate |
| **ConsumableItem** | Syringes, cotton | Id, Name, Stock, ReorderLevel |

### Diagnostic Entities

| Entity | Purpose | Key Fields |
|--------|---------|------------|
| **LabOrder** | Test order | Id, VisitId, Tests, Status |
| **LabResult** | Test results | Id, LabOrderId, TestName, Value, Unit, Range |

### Compliance Entities

| Entity | Purpose | Key Fields |
|--------|---------|------------|
| **ConsentRecord** | Patient consent | Id, PatientId, Type, Date, Status |
| **MedicalRecordAudit** | Audit trail | Id, RecordId, Action, UserId, Date |
| **DrugScheduleRegistry** | Schedule H/X/NDPS list | Id, DrugName, Schedule, Restrictions |

### System Entities

| Entity | Purpose | Key Fields |
|--------|---------|------------|
| **IdempotencyKey** | Prevent duplicates | Id, Key, ExpiresAt |
| **OfflineSync** | Offline queue | Id, EntityType, Payload, Status |
| **DataExportLog** | Export audit | Id, UserId, Type, Date, Rows |

### Feature Entities

| Entity | Purpose | Key Fields |
|--------|---------|------------|
| **FamilyGroup** | Family grouping | Id, Name, PrimaryPatientId |
| **FamilyMember** | Family members | Id, GroupId, PatientId, Relation |
| **PatientMergeLog** | Profile merge audit | Id, SourceId, TargetId, Date |
| **PrescriptionDraft** | Auto-save Rx | Id, DoctorId, PatientId, DraftJson |
| **RxTemplate** | Doctor's shortlist | Id, DoctorId, DrugName, Frequency |
| **LocalLanguageRx** | Multi-language Rx | Id, PrescriptionId, Language, Text |
| **AbhaRecord** | ABHA number linking | Id, PatientId, AbhaNumber, Status |
| **VideoJoinToken** | Short-TTL video tokens | Id, RoomId, Token, ExpiresAt |
| **EmergencyChat** | Red-flag keyword detection | Id, ThreadId, Message, Keywords |
| **DoctorRegistration** | License expiry tracking | Id, DoctorId, ExpiryDate, Status |
| **DoctorDelayBroadcast** | TV display for delays | Id, DoctorId, DelayMinutes, Message |
| **QueueEta** | Live queue position + ETA | Id, VisitId, Position, EtaMinutes |
| **StaffPin** | Quick switch PIN | Id, StaffId, Pin, ExpiresAt |
| **DayEndTally** | Cash reconciliation header | Id, Date, Expected, Actual, Variance |
| **DayEndTallyDetail** | Cash reconciliation detail | Id, TallyId, PaymentMode, Amount |
| **SubscriptionPlan** | Clinic subscription plans | Id, Name, Price, Features |
| **PatientImportBatch** | CSV import tracking | Id, FileName, Rows, Status |
| **VisitingConsultantPayout** | Consultant revenue split | Id, DoctorId, VisitId, Amount |

### Background Service Entities

| Entity | Purpose | Key Fields |
|--------|---------|------------|
| **DrugInteraction** | Drug-drug interaction rules | Id, Drug1, Drug2, Severity |
| **DrugAllergy** | Drug-allergy mapping | Id, DrugName, AllergyType |

---

# 7. CDSS ENGINE

## 7.1 Clinical Decision Support System

```
REAL-TIME ALERTS DURING PRESCRIPTION:

1. Drug-Drug Interaction
   ├── Warfarin + Aspirin → "Bleeding risk!"
   ├── Metformin + Alcohol → "Lactic acidosis risk!"
   ├── SSRI + Tramadol → "Serotonin syndrome risk!"
   └── Severity: Critical / Major / Moderate / Minor

2. Drug-Allergy Alert
   ├── Patient allergic to Penicillin → "Avoid Amoxicillin!"
   ├── Patient allergic to Sulfa → "Avoid Co-trimoxazole!"
   ├── Patient allergic to NSAID → "Avoid Ibuprofen!"
   └── Severity: Critical (blocks prescription)

3. Drug-Food Interaction
   ├── Warfarin + Green leafy vegetables → "Reduced efficacy"
   ├── Statins + Grapefruit → "Increased side effects"
   ├── Tetracycline + Dairy → "Reduced absorption"
   └── Severity: Moderate (warning)

4. Dosage Validation
   ├── Pediatric dose exceeds max → "Dose too high!"
   ├── Elderly dose not reduced → "Consider dose reduction"
   ├── Renal impairment → "Dose adjustment needed"
   └── Severity: Major (warning)

5. Schedule Drug Block
   ├── Schedule X via teleconsult → "Not allowed!"
   ├── NDPS drug → "Requires special prescription"
   ├── Habit-forming drug → "Duration limit exceeded"
   └── Severity: Critical (blocks prescription)

6. Generic Substitute Suggestion
   ├── Brand: Augmentin 625 (₹180)
   │   └── Generic: Amoxicillin + Clavulanate (₹45)
   ├── Savings: ₹135 per strip
   └── Severity: Info (suggestion)
```

## 7.2 CDSS Implementation

```
CdssService Methods:

1. CheckDrugInteraction(drug1, drug2)
   └── Returns: InteractionResult { Severity, Description }

2. CheckDrugAllergy(patientId, drugName)
   └── Returns: AllergyResult { IsAllergic, Allergen }

3. CheckDosage(drugName, dosage, patientAge, patientWeight)
   └── Returns: DosageResult { IsValid, MaxDose, Warning }

4. CheckScheduleDrug(drugName, isTeleconsult)
   └── Returns: ScheduleResult { IsBlocked, Reason }

5. SuggestGeneric(drugName)
   └── Returns: GenericSuggestion { GenericName, Price, Savings }
```

---

# 8. SECURITY FEATURES

## 8.1 Authentication & Authorization

```
├── JWT Authentication
│   ├── 15 minute expiry
│   ├── Refresh token (7 days)
│   └── Revocation on logout
│
├── Multi-Factor Authentication (MFA)
│   ├── TOTP (Google Authenticator)
│   ├── Backup codes
│   └── Required for: Owner, Doctor
│
├── Staff PIN (4-digit)
│   ├── Quick switch for staff
│   ├── 8 hour expiry
│   └── Required for: Receptionist, Pharmacist
│
├── Role-Based Access Control (RBAC)
│   ├── 5 roles with specific permissions
│   ├── Endpoint-level authorization
│   └── Data-level filtering
│
└── Session Management
    ├── Auto-logout (30 min idle)
    ├── Concurrent session limit
    └── Device tracking
```

## 8.2 Data Security

```
├── AES-256 Encryption
│   ├── Medical records at rest
│   ├── Prescription data
│   └── Patient PII
│
├── HTTPS Everywhere
│   ├── TLS 1.3
│   ├── HSTS headers
│   └── Certificate pinning (mobile)
│
├── Input Validation
│   ├── SQL injection prevention
│   ├── XSS prevention
│   ├── CSRF protection
│   └── File upload validation
│
├── Rate Limiting
│   ├── 5 OTP requests per 10 minutes
│   ├── 5 login attempts per 10 minutes
│   ├── 100 API requests per minute
│   └── Custom limits per endpoint
│
├── Idempotency
│   ├── Duplicate submission prevention
│   ├── Idempotency key in header
│   └── 24 hour key expiry
│
└── Audit Trail
    ├── Who changed what
    ├── When it was changed
    ├── What was changed (before/after)
    └── IP address + device info
```

## 8.3 Compliance

```
├── DPDP (Digital Personal Data Protection)
│   ├── Two-tier deletion (soft + hard)
│   ├── Consent records
│   ├── Data retention policies
│   └── Right to erasure
│
├── GST Compliance
│   ├── Consultation exempt (0%)
│   ├── Medicine taxable (5%/12%/18%)
│   ├── Invoice format
│   └── GST reports
│
├── Schedule H1 Register
│   ├── Auto-generated
│   ├── 3 year retention
│   └── Export as PDF
│
└── Medical Record Retention
    ├── 3 years (minor)
    ├── 5 years (adult)
    └── 8 years (after death)
```

---

# 9. TECHNICAL ARCHITECTURE

## 9.1 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MEDIFLOW ARCHITECTURE                         │
└─────────────────────────────────────────────────────────────────┘

LAYER 1: Client Layer
├── Web App (React/Next.js)
├── Mobile App (React Native)
├── Admin Panel (React.js)
└── TV Display (for queue)

LAYER 2: API Gateway
├── Load Balancer (AWS ALB)
├── Rate Limiting
├── Authentication (JWT)
└── Request Validation

LAYER 3: Application Layer (25 Controllers)
├── AuthController
├── PatientController
├── DoctorController
├── VisitController
├── PrescriptionController
├── InvoiceController
├── PaymentController
├── PharmacyController
├── LabController
├── ReportController
└── 15 more controllers...

LAYER 4: Business Layer (74 Services)
├── AuthService
├── PatientService
├── DoctorService
├── VisitService
├── PrescriptionService
├── CdssService
├── InvoiceService
├── PaymentService
├── PharmacyService
├── LabService
├── SmsOtpService
├── VideoSecurityService
├── OfflineSyncService
├── EmergencyChatService
├── DayEndTallyService
└── 59 more services...

LAYER 5: Domain Layer (61 Entities)
├── Core: Patient, Doctor, Staff, Visit, Prescription
├── Billing: Invoice, Payment, CreditNote, Refund
├── Pharmacy: DrugInventory, StockBatch, Supplier
├── Diagnostic: LabOrder, LabResult
├── Compliance: ConsentRecord, AuditTrail
└── System: IdempotencyKey, OfflineSync

LAYER 6: Infrastructure Layer
├── PostgreSQL Database
├── Redis Cache
├── S3/Azure Blob (files)
├── SendGrid (email)
├── Twilio (SMS/WhatsApp)
├── Razorpay/Stripe (payments)
└── Hangfire (background jobs)

LAYER 7: Cross-Cutting
├── Logging (Serilog → ELK)
├── Monitoring (Application Insights)
├── Caching (Redis)
├── Background Jobs (Hangfire)
└── Security (AES-256, JWT, MFA)
```

## 9.2 API Endpoints (100+)

### Authentication
- POST /api/auth/login
- POST /api/auth/verify-otp
- POST /api/auth/refresh-token
- POST /api/auth/logout

### Patients
- GET /api/patients
- GET /api/patients/{id}
- POST /api/patients
- PUT /api/patients/{id}
- DELETE /api/patients/{id}
- GET /api/patients/{id}/visits
- GET /api/patients/{id}/prescriptions

### Doctors
- GET /api/doctors
- GET /api/doctors/{id}
- POST /api/doctors
- PUT /api/doctors/{id}
- GET /api/doctors/{id}/schedule
- GET /api/doctors/{id}/patients

### Visits
- GET /api/visits
- GET /api/visits/{id}
- POST /api/visits
- PUT /api/visits/{id}
- GET /api/visits/today

### Prescriptions
- GET /api/prescriptions
- GET /api/prescriptions/{id}
- POST /api/prescriptions
- PUT /api/prescriptions/{id}
- POST /api/prescriptions/{id}/finalize
- POST /api/prescriptions/{id}/print

### Billing
- GET /api/invoices
- GET /api/invoices/{id}
- POST /api/invoices
- POST /api/invoices/{id}/payment
- POST /api/invoices/{id}/refund

### Pharmacy
- GET /api/pharmacy/drugs
- GET /api/pharmacy/stock
- POST /api/pharmacy/dispense
- GET /api/pharmacy/h1-register

### Diagnostics
- GET /api/lab/orders
- GET /api/lab/results
- POST /api/lab/results

### Reports
- GET /api/reports/revenue
- GET /api/reports/patients
- GET /api/reports/prescriptions
- GET /api/reports/stock

### And 60+ more endpoints...

## 9.3 Background Services (8 Auto-jobs)

| Service | Schedule | Purpose |
|---------|----------|---------|
| ExpiryAlertService | Daily 9 AM | Alert for batches expiring in 30 days |
| AppointmentReminderService | Every hour | SMS reminder 1 hour before appointment |
| PendingPaymentReminderService | Daily 10 AM | Remind pending payments |
| SubscriptionRenewalService | Daily 8 AM | Auto-renew clinic subscriptions |
| StaleSessionCleanupService | Every 6 hours | Clean abandoned sessions |
| DailyDigestService | Daily 8 PM | Email digest to clinic owner |
| H1RegisterReminderService | Daily 6 PM | Remind pharmacist to update H1 register |
| DataRetentionEnforcementService | Weekly | DPDP compliance - delete old data |

---

# 10. REVENUE MODEL

## 10.1 Pricing Plans

| Plan | Price | Doctors | Members | Features |
|------|-------|---------|---------|----------|
| **Starter** | ₹999/month | 1 | 500 | Basic features, 1 doctor |
| **Growth** | ₹1,999/month | 5 | 2,000 | All features, 5 doctors |
| **Professional** | ₹3,999/month | 15 | 5,000 | All features + API |
| **Enterprise** | ₹7,999/month | Unlimited | Unlimited | Custom features |

## 10.2 Revenue Streams

| Stream | Price | Model |
|--------|-------|-------|
| SaaS Subscription | ₹999-7,999/month | Recurring |
| Transaction Fees | 1.5% on payments | Per transaction |
| API Access | ₹2,000/month | Recurring |
| Custom Integrations | ₹50,000-2,00,000 | One-time |
| Data Migration | ₹10,000-25,000 | One-time |
| Training | ₹5,000-10,000 | One-time |

## 10.3 Revenue Projections

```
YEAR 1 (12 months):
├── Month 1-2: 5 pilot clinics (FREE)
├── Month 3-4: 20 paying clinics × ₹1,500 avg = ₹30,000/month
├── Month 5-6: 50 paying clinics × ₹1,500 avg = ₹75,000/month
├── Month 7-9: 100 paying clinics × ₹2,000 avg = ₹2,00,000/month
├── Month 10-12: 150 paying clinics × ₹2,000 avg = ₹3,00,000/month
└── Total Year 1: ₹15-20 Lakhs

YEAR 2 (24 months):
├── Month 13-18: 300 clinics × ₹2,000 avg = ₹6,00,000/month
├── Month 19-24: 500 clinics × ₹2,500 avg = ₹12,50,000/month
└── Total Year 2: ₹60-80 Lakhs

YEAR 3 (36 months):
├── Month 25-36: 1000 clinics × ₹3,000 avg = ₹30,00,000/month
└── Total Year 3: ₹3-4 Crores
```

## 10.4 Unit Economics

```
Customer Acquisition Cost (CAC):
├── Marketing: ₹5,000 per clinic
├── Sales: ₹3,000 per clinic
├── Onboarding: ₹2,000 per clinic
└── Total CAC: ₹10,000 per clinic

Lifetime Value (LTV):
├── Average Monthly Fee: ₹2,000
├── Average Retention: 24 months
├── LTV: ₹48,000

LTV/CAC Ratio: 4.8x ✅ (Target: >3x)

Payback Period:
├── ₹10,000 / ₹2,000 = 5 months ✅
```

---

# 11. LAUNCH PLAN

## 11.1 Pre-Launch (Week 1-2)

```
├── Finalize product (backend complete ✅)
├── Set up payment gateway (Razorpay)
├── Create demo videos (2-3 minutes)
├── Set up sales CRM (HubSpot/Zoho)
├── Prepare marketing materials
│   ├── Brochure (PDF)
│   ├── Pitch deck (PDF)
│   ├── Case study template
│   └── Email templates
├── Set up customer support (Zendesk)
├── Legal: Terms of Service, Privacy Policy
└── Insurance: Business liability
```

## 11.2 Pilot Launch (Week 3-4)

```
├── Onboard 3-5 pilot clinics (FREE for 1 month)
│   ├── Clinic 1: Single doctor (General Practice)
│   ├── Clinic 2: Multi-doctor (Speciality)
│   ├── Clinic 3: Clinic with pharmacy
│   └── Clinic 4: Clinic with diagnostics
│
├── Collect feedback (weekly surveys)
│   ├── What's working?
│   ├── What's not working?
│   ├── What's missing?
│   └── Would you pay for this?
│
├── Fix bugs (daily standup)
├── Refine onboarding flow
├── Create case studies from pilots
└── Prepare testimonials
```

## 11.3 Public Launch (Week 5-6)

```
├── Launch on Product Hunt
├── LinkedIn/Facebook ads (₹500/day)
├── Google Ads (₹500/day)
│   ├── "clinic management software"
│   ├── "prescription software"
│   ├── "pharmacy software"
│   └── "clinic billing software"
│
├── Cold calling to clinics (100/day)
├── Email outreach (500/week)
├── Referral program live (₹500 per referral)
├── Partner with clinic consultants
└── Attend healthcare expos
```

## 11.4 Scale (Week 7-12)

```
├── Hire 2 sales reps
├── Hire 1 customer success manager
├── Partner with pharmacy chains
├── Partner with diagnostic labs
├── Content marketing (blog, YouTube)
├── Webinars for clinic owners
├── Case studies + testimonials
└── Enterprise sales (hospital chains)
```

## 11.5 Growth (Month 3-6)

```
├── 100 paying clinics
├── ₹2 Lakhs MRR
├── Hire 2 developers
├── Launch mobile app
├── API marketplace
├── White-label option
└── Series A preparation
```

## 11.6 Scale (Month 6-12)

```
├── 500+ clinics
├── ₹10 Lakhs MRR
├── 15+ team members
├── Pan India expansion
├── Series A funding
├── Enterprise clients (hospital chains)
└── Platform ecosystem
```

---

# 12. TEAM & WORK DISTRIBUTION

## 12.1 Team Structure

| Role | Person | Responsibilities |
|------|--------|------------------|
| **CEO/Founder** | Hammad | Strategy, Sales, Fundraising |
| **CTO/Founder** | Rohit | Tech, Architecture, Development |
| **COO/Founder** | Imran | Operations, Customer Success |
| **Developer** | TBD | Frontend, Backend, Mobile |
| **Sales** | TBD | Lead gen, Demo, Closing |
| **Support** | TBD | Customer support, Onboarding |

## 12.2 Work Distribution

### Hammad (CEO)
```
├── Business strategy
├── Sales calls
├── Investor relations
├── Partnerships
├── Marketing campaigns
└── Customer relationships
```

### Rohit (CTO)
```
├── Architecture decisions
├── Backend development (MediFlow)
├── Code reviews
├── DevOps (deployment, CI/CD)
├── Security audits
└── Technical documentation
```

### Imran (COO)
```
├── Operations management
├── Customer onboarding
├── Support management
├── Process optimization
├── Quality assurance
└── Vendor management
```

### Developer (TBD)
```
├── Frontend development (React/Next.js)
├── Mobile app development (React Native)
├── API integration
├── Bug fixes
├── Testing
└── Documentation
```

## 12.3 Sprint Plan (2-week sprints)

### Sprint 1 (Week 1-2)
```
├── Backend complete ✅
├── Set up payment gateway
├── Create demo videos
├── Set up sales CRM
└── Prepare marketing materials
```

### Sprint 2 (Week 3-4)
```
├── Onboard pilot clinics (3-5)
├── Collect feedback
├── Fix bugs
├── Refine onboarding
└── Create case studies
```

### Sprint 3 (Week 5-6)
```
├── Public launch
├── Marketing campaigns
├── Sales outreach
├── Referral program
└── Customer support setup
```

### Sprint 4 (Week 7-8)
```
├── Hire sales reps
├── Hire customer success
├── Partner outreach
├── Content marketing
└── Enterprise sales
```

## 12.4 Developer Assignment

### Week 1-2: Frontend Setup
```
├── Create React/Next.js project
├── Set up Tailwind CSS
├── Create component library
├── Set up routing
└── Create authentication pages
```

### Week 3-4: Core Pages
```
├── Dashboard (Owner, Doctor, Receptionist)
├── Patient management pages
├── Doctor management pages
├── Visit management pages
└── Prescription pages
```

### Week 5-6: Pharmacy & Billing
```
├── Pharmacy dashboard
├── Stock management pages
├── Billing pages
├── Payment pages
└── Day-end tally pages
```

### Week 7-8: Reports & Settings
```
├── Reports dashboard
├── Export functionality
├── Settings pages
├── User management
└── Audit logs
```

---

# APPENDIX

## A. Environment Variables

```
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/mediflow
REDIS_URL=redis://localhost:6379

# Authentication
JWT_SECRET=your-secret-key
JWT_EXPIRY=15
REFRESH_TOKEN_EXPIRY=7

# SMS
TWILIO_SID=your-sid
TWILIO_AUTH_TOKEN=your-token
TWILIO_PHONE=+1234567890

# Email
SENDGRID_API_KEY=your-key
SENDGRID_FROM=noreply@mediflow.com

# WhatsApp
TWILIO_WHATSAPP_SID=your-sid
TWILIO_WHATSAPP_TOKEN=your-token

# Payments
RAZORPAY_KEY=your-key
RAZORPAY_SECRET=your-secret
STRIPE_KEY=your-key
STRIPE_SECRET=your-secret

# Storage
AWS_S3_BUCKET=your-bucket
AWS_ACCESS_KEY=your-key
AWS_SECRET_KEY=your-secret

# Monitoring
APPLICATION_INSIGHTS_KEY=your-key
SENTRY_DSN=your-dsn
```

## B. Running Locally

```bash
# Clone repository
git clone https://github.com/greybits/mediflow.git
cd mediflow

# Restore dependencies
dotnet restore

# Run database migrations
dotnet ef database update

# Run application
dotnet run --project src/Mediflow.API

# Run tests
dotnet test

# Access API
# https://localhost:5001/swagger
```

## C. Business Rules

1. **Walk-in First**: Receptionist flow must be <20 seconds
2. **Cash Dominant**: Most clinics are cash-based
3. **GST Compliance**: Consultation exempt, medicine taxable
4. **Schedule H1**: Antibiotics require strict register
5. **DPDP Compliance**: Two-tier deletion (soft + hard)
6. **Offline Support**: Queue requests when internet is down
7. **Multi-language**: Hindi/Marathi/Gujarati/Tamil support
8. **Video Security**: Short-TTL tokens, waiting room
9. **CDSS Critical**: Drug interactions must block prescription
10. **Day-End Mandatory**: Cash tally must be done daily

---

**Document Version:** 1.0  
**Last Updated:** 26 August 2026  
**Company:** GreyBits Technologies  
**Contact:** support@gymex.online
