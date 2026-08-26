# 🏢 GreyBits Technologies — Complete Business Documentation

## Gymex Platform | MediFlow Platform | GymexGlobal Platform

**Version:** 1.0  
**Date:** 26 August 2026  
**Company:** GreyBits Technologies  
**Founders:** Hammad Kadiwala, Rohit, Imran  

---

# TABLE OF CONTENTS

1. [Company Overview](#1-company-overview)
2. [Platform 1: Gymex (India)](#2-platform-1-gymex-india)
3. [Platform 2: MediFlow (Clinic/Hospital)](#3-platform-2-mediflow-clinichospital)
4. [Platform 3: GymexGlobal (International)](#4-platform-3-gymexglobal-international)
5. [Technical Architecture](#5-technical-architecture)
6. [Revenue Model](#6-revenue-model)
7. [Launch Plan](#7-launch-plan)
8. [Team & Work Distribution](#8-team--work-distribution)

---

# 1. COMPANY OVERVIEW

## 1.1 Vision
Build software platforms that simplify fitness and healthcare management across India and globally.

## 1.2 Mission
- **Gymex**: Help gym owners manage their business efficiently
- **MediFlow**: Help clinics run paperless with smart prescription management
- **GymexGlobal**: Take Gymex to international markets (Middle East, Africa, SE Asia)

## 1.3 Products

| Product | Target | Market | Status |
|---------|--------|--------|--------|
| Gymex | Gyms, Fitness Studios, Yoga Studios | India | Live (500+ customers) |
| MediFlow | Clinics, Hospitals, Pharmacies, Labs | India | Backend Complete |
| GymexGlobal | Gyms, Fitness Studios (International) | Global | Website Live |

---

# 2. PLATFORM 1: GYMEX (INDIA)

## 2.1 Overview
Gymex is a SaaS-based gym management software that helps gym owners manage memberships, billing, staff, marketing, and member engagement from one platform.

## 2.2 Website
- **India**: https://www.gymex.online
- **Global**: https://gymexglobalwebsite.vercel.app

## 2.3 Customer Journey

### Step 1: Discovery
```
Customer finds Gymex via:
├── Google Search ("gym management software")
├── Facebook/Instagram Ads
├── Referral from another gym owner
├── LinkedIn outreach
└── Website: gymex.online
```

### Step 2: Demo Request
```
Customer clicks "Get Your Free Demo":
├── Fills form: Name, Last Name, Company, Email, Phone, Message
├── Form submitted via EmailJS → Sales team gets email
├── Sales calls within 24 hours
└── Demo scheduled (video call or in-person)
```

### Step 3: Onboarding
```
After demo, customer chooses plan:
├── Starter: ₹999/month
├── Pro: ₹1,999/month
└── Enterprise: ₹3,999/month

Onboarding steps:
├── Account creation
├── Gym profile setup (name, logo, address)
├── Add staff members
├── Create membership plans
├── Import existing members (CSV)
├── Set up payment gateway (Razorpay)
├── Training session (1 hour)
└── Go live!
```

### Step 4: Daily Usage
```
OWNER DASHBOARD:
├── Revenue Today: ₹XX,XXX
├── Active Members: XXX
├── New Leads: XX
├── Expiring Memberships: XX
└── Staff Attendance: XX/XX

MODULES:
├── Lead Management
├── Member Management
├── Billing & Payments
├── Staff Management
├── Class Scheduling
├── POS (Point of Sale)
├── Marketing & Campaigns
├── Reports & Analytics
├── Biometric/Access Control
├── Member Mobile App
└── Intelligent Alerts
```

## 2.4 Module Details

### A. Lead Management
```
FLOW:
New Inquiry → Call → Follow-up → Demo → Convert → Onboard

FEATURES:
├── Lead capture from website form
├── Lead capture from walk-in
├── Lead status tracking (New → Contacted → Demo → Converted/Lost)
├── Follow-up reminders
├── Lead source tracking (Website, Referral, Walk-in, Ad)
├── WhatsApp integration
└── Lead conversion report
```

### B. Member Management
```
FLOW:
Registration → Membership Purchase → Access → Renewal → Retention

FEATURES:
├── Member registration (Name, Phone, Email, Aadhaar/PAN/Passport)
├── Photo upload
├── Membership plans (Monthly, Quarterly, Yearly)
├── Auto-renewal reminders (7 days before expiry)
├── Member check-in/check-out (QR/Biometric)
├── Member app (attendance, classes, payments)
├── Family member linking
├── Medical conditions/allergies
└── Member retention tracking
```

### C. Billing & Payments
```
FLOW:
Invoice Generation → Payment Collection → Reconciliation → Reports

FEATURES:
├── Auto invoice generation (GST compliant)
├── Multiple payment modes (Cash, Card, UPI, Net Banking)
├── Payment gateway integration (Razorpay)
├── Auto-debit (UPI Mandate / Card)
├── Pending payment reminders (SMS/Email)
├── Refund management
├── Revenue reports (Daily/Weekly/Monthly)
└── Expense tracking
```

### D. Staff Management
```
FLOW:
Hire → Attendance → Shift → Performance → Salary

FEATURES:
├── Staff profiles (Name, Role, Phone, Salary)
├── Attendance tracking (Biometric)
├── Shift scheduling
├── Commission tracking (trainer per session)
├── Salary/Payroll management
├── Staff performance reports
└── Staff mobile app
```

### E. Class Scheduling
```
FLOW:
Create Class → Set Time → Open Booking → Manage Capacity → Track

FEATURES:
├── Class types (Yoga, Zumba, Spinning, CrossFit, etc.)
├── Trainer assignment
├── Time slot management
├── Member booking (via app)
├── Waitlist management
├── Capacity control
├── Class reminders (1 hour before)
└── Attendance tracking
```

### F. Marketing & Campaigns
```
FLOW:
Plan → Create Campaign → Execute → Track Results

FEATURES:
├── SMS campaigns
├── Email campaigns
├── WhatsApp broadcasts
├── Referral program (member refers friend)
├── Birthday/Anniversary wishes
├── Inactive member re-engagement
├── Festival/seasonal offers
└── Campaign analytics
```

### G. POS (Point of Sale)
```
FLOW:
Select Item → Add to Cart → Payment → Receipt

FEATURES:
├── Supplements sales (Protein, Creatine, etc.)
├── Accessories sales (Gloves, Bands, etc.)
├── Barcode scanning
├── Inventory management
├── Low stock alerts
├── Sales reports
└── GST invoice generation
```

### H. Reports & Analytics
```
AVAILABLE REPORTS:
├── Revenue Report (Daily/Weekly/Monthly/Yearly)
├── Member Report (Active, Expired, New, Cancelled)
├── Lead Report (New, Converted, Lost)
├── Staff Report (Attendance, Performance)
├── Class Report (Attendance, Revenue)
├── POS Report (Sales, Inventory)
├── Expense Report
├── Profit & Loss Statement
├── GST Report
└── Custom date range reports
```

### I. Member Mobile App
```
FEATURES:
├── Login (Mobile OTP)
├── View membership status
├── Check-in/check-out (QR code)
├── Book classes
├── View workout plans
├── Make payments
├── View progress
├── Refer friends
├── Push notifications
└── Profile management
```

### J. Intelligent Alerts
```
ALERT TYPES:
├── Membership expiring (7 days before)
├── Birthday wish
├── Payment due reminder
├── Class reminder (1 hour before)
├── Inactive member (30 days no visit)
├── New offer/promotion
├── Staff attendance alert
├── Low stock alert (POS)
├── Revenue target achieved
└── Lead follow-up reminder
```

## 2.5 Pricing

| Plan | Price | Members | Staff | Features |
|------|-------|---------|-------|----------|
| Starter | ₹999/month | Up to 100 | 1 | Basic features |
| Pro | ₹1,999/month | Up to 500 | 5 | All features |
| Enterprise | ₹3,999/month | Unlimited | Unlimited | All features + API |

---

# 3. PLATFORM 2: MEDIFLOW (CLINIC/HOSPITAL)

## 3.1 Overview
MediFlow is a comprehensive clinic management platform that digitizes patient registration, doctor consultations, prescriptions, pharmacy, diagnostics, and billing — all in one system.

## 3.2 Codebase Stats
- **Entities**: 61
- **Services**: 74
- **Controllers**: 25
- **Build**: ✅ 0 Errors
- **Tests**: ✅ 35/35 Passed
- **Git Commits**: 45+

## 3.3 User Roles

| Role | Access Level | Primary Functions |
|------|-------------|-------------------|
| **Clinic Owner** | Full | Dashboard, Reports, Settings, Staff Management |
| **Doctor** | Patient + Prescription | Consultation, Rx, Video Call, Schedule |
| **Receptionist** | Front Desk | Patient Registration, Visits, Billing, Queue |
| **Pharmacist** | Pharmacy Module | Dispensing, Stock, Returns, H1 Register |
| **Lab Technician** | Diagnostics | Test Orders, Results, Reports |

## 3.4 Complete User Flows

### A. CLINIC OWNER FLOW
```
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
├── Morning: Review schedule, check stock
├── Throughout Day: Monitor queue, revenue
├── Evening: Day-end tally, cash reconciliation
└── Weekly: Reports, staff review, reorder stock

MANAGEMENT:
├── Add/Remove Doctors
├── Add/Remove Staff
├── Configure GST
├── Set Payment Gateway
├── Import Patient Data (CSV)
├── Set Subscription Plan
└── View Analytics
```

### B. RECEPTIONIST FLOW (Walk-in First, <20 seconds)
```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Patient Arrives                                     │
│  ├── Click "New Visit"                                       │
│  └── Enter phone number                                      │
│                                                              │
│  STEP 2: Phone Lookup (Instant)                              │
│  ├── EXISTING PATIENT → Load details automatically           │
│  └── NEW PATIENT → Quick form: Name + Phone (save)           │
│                                                              │
│  STEP 3: Create Visit                                        │
│  ├── Select Doctor (dropdown)                                │
│  ├── Visit Type: Consultation (₹500)                         │
│  ├── Token Number: Auto-assigned (#015)                      │
│  └── Queue Position: 3rd in line                             │
│                                                              │
│  STEP 4: Patient Waits                                       │
│  ├── TV Display: "Token #015 - Your turn in ~15 minutes"     │
│  ├── Doctor Delayed Alert (if >20 min)                       │
│  └── SMS notification when turn near                         │
│                                                              │
│  STEP 5: Billing (After consultation)                        │
│  ├── Consultation Fee: ₹500                                  │
│  ├── Medicines: ₹XXX (from pharmacy)                         │
│  ├── Lab Tests: ₹XXX (from diagnostics)                      │
│  ├── Total: ₹XXX                                             │
│  ├── Payment: Cash/Card/UPI                                  │
│  └── Receipt Printed (Thermal/A4)                            │
└─────────────────────────────────────────────────────────────┘

KEY FEATURES:
├── Patient search by phone (instant)
├── Auto-fill for returning patients
├── Token system with queue display
├── Quick billing (2 taps)
├── Multi-doctor support
└── Day-end cash reconciliation
```

### C. DOCTOR CONSULTATION FLOW
```
┌─────────────────────────────────────────────────────────────┐
│  LOGIN → DASHBOARD                                           │
│                                                              │
│  Today's Schedule:                                           │
│  ├── Walk-ins: 15 patients                                   │
│  ├── Video Consults: 5 patients                              │
│  └── Follow-ups: 3 patients                                  │
│                                                              │
│  ─── CONSULTATION FLOW ───                                   │
│                                                              │
│  1. Patient calls/arrives                                    │
│     └── Receptionist creates visit                           │
│                                                              │
│  2. Doctor opens patient file                                │
│     ├── Previous Visits (full history)                       │
│     ├── Allergies (highlighted RED)                          │
│     ├── Current Medications                                  │
│     ├── Lab Reports (if any)                                 │
│     └── Vitals History                                       │
│                                                              │
│  3. Enter Vitals                                             │
│     ├── Blood Pressure: 120/80                               │
│     ├── Temperature: 98.6°F                                  │
│     ├── Weight: 70 kg                                        │
│     ├── Height: 5'10"                                        │
│     ├── Pulse: 72 bpm                                        │
│     └── SpO2: 98%                                            │
│                                                              │
│  4. Chief Complaint                                          │
│     └── "Fever, body ache, sore throat for 3 days"           │
│                                                              │
│  5. Diagnosis                                                │
│     ├── Primary: Acute Pharyngitis (ICD-10: J02.9)           │
│     └── Secondary: Viral Fever (ICD-10: B34.9)               │
│                                                              │
│  6. Prescription Entry                                       │
│     ├── Drug: Amoxicillin 500mg                              │
│     │   ├── Dosage: 1-0-1 (3 times/day)                      │
│     │   ├── Duration: 5 days                                 │
│     │   └── CDSS: ✅ No interaction                          │
│     │                                                        │
│     ├── Drug: Paracetamol 650mg                              │
│     │   ├── Dosage: SOS (as needed)                          │
│     │   ├── Duration: 5 days                                 │
│     │   └── CDSS: ✅ No interaction                          │
│     │                                                        │
│     ├── Drug: Cetirizine 10mg                                │
│     │   ├── Dosage: 0-0-1 (at bedtime)                       │
│     │   ├── Duration: 5 days                                 │
│     │   └── CDSS: ⚠️ May cause drowsiness                   │
│     │                                                        │
│     └── Auto-save draft (every 5 seconds)                    │
│                                                              │
│  7. CDSS Alerts (Real-time)                                  │
│     ├── Drug-Drug Interaction: ✅ Clear                      │
│     ├── Drug-Allergy Alert: ✅ Clear                         │
│     ├── Drug-Food Interaction: ✅ Clear                      │
│     ├── Dosage Validation: ✅ Within range                   │
│     └── Generic Substitute: 💡 Suggestion available          │
│                                                              │
│  8. Finalize Rx                                              │
│     ├── Print: Thermal/A4/A5                                 │
│     ├── WhatsApp: PDF to patient                             │
│     ├── SMS: PWA link (feature phones)                       │
│     └── Save: Cloud (AES-256 encrypted)                      │
│                                                              │
│  9. Order Lab Tests (if needed)                              │
│     ├── CBC, Lipid Profile, Thyroid                          │
│     └── Auto-sync to lab                                     │
│                                                              │
│  10. Follow-up                                               │
│      └── "Come back in 7 days" → Auto reminder               │
└─────────────────────────────────────────────────────────────┘

VIDEO CONSULTATION:
├── Patient joins via WhatsApp link
├ Doctor admits from waiting room
├── WebRTC video call (TURN server)
├── Short-TTL join token (5 min expiry)
├── Doctor can share screen (reports)
├── Record call (with consent)
└── E-prescription after consultation
```

### D. PHARMACIST FLOW
```
┌─────────────────────────────────────────────────────────────┐
│  LOGIN → PHARMACY DASHBOARD                                  │
│                                                              │
│  Today's Summary:                                            │
│  ├── Prescriptions Received: XX                              │
│  ├── Dispensed: XX                                           │
│  ├── Pending: XX                                             │
│  ├── Revenue: ₹XX,XXX                                        │
│  └── Stock Alerts: XX                                        │
│                                                              │
│  ─── DISPENSING FLOW ───                                     │
│                                                              │
│  1. Receive prescription                                     │
│     ├── From doctor's Rx                                     │
│     └── Shows: Patient name, drugs, dosages                  │
│                                                              │
│  2. Select prescription                                      │
│     └── Click "Dispense"                                     │
│                                                              │
│  3. Auto-select batch (FEFO)                                 │
│     ├── Amoxicillin 500mg                                    │
│     │   ├── Batch: AMP-2026-03                               │
│     │   ├── MRP: ₹85                                         │
│     │   ├── Expiry: Dec 2026                                 │
│     │   └── Stock: 150 tabs                                  │
│     │                                                        │
│     ├── Paracetamol 650mg                                    │
│     │   ├── Batch: PCM-2026-05                               │
│     │   ├── MRP: ₹25                                         │
│     │   ├── Expiry: Mar 2027                                 │
│     │   └── Stock: 300 tabs                                  │
│     │                                                        │
│     └── Cetirizine 10mg                                      │
│         ├── Batch: CTZ-2026-02                               │
│         ├── MRP: ₹35                                         │
│         ├── Expiry: Nov 2026                                 │
│         └── Stock: 80 tabs                                   │
│                                                              │
│  4. Partial dispensing (if stock low)                        │
│     └── "Only 4 of 10 tablets available"                     │
│                                                              │
│  5. Scan barcode → Auto-add to bill                          │
│                                                              │
│  6. Print label                                              │
│                                                              │
│  7. Collect payment                                          │
│     ├── Cash/Card/UPI                                        │
│     └── Receipt printed                                      │
│                                                              │
│  ─── STOCK MANAGEMENT ───                                    │
│                                                              │
│  Receive Stock:                                              │
│  ├── From distributor                                        │
│  ├── Enter: Drug name, batch, MRP, expiry, quantity          │
│  └── Auto-update stock                                       │
│                                                              │
│  Return Stock:                                               │
│  ├── Near-expiry (3 months before)                           │
│  ├── Select batch → Return                                   │
│  └── Distributor credit note generated                       │
│                                                              │
│  Stock Reports:                                              │
│  ├── Current stock value                                     │
│  ├── Expiry-wise stock                                       │
│  ├── Slow-moving items                                       │
│  └── Stock valuation (FIFO)                                  │
│                                                              │
│  ─── SCHEDULE H1 REGISTER ───                                │
│                                                              │
│  Auto-generated register for antibiotics:                    │
│  ├── Patient name                                            │
│  ├── Drug name                                               │
│  ├── Prescribing doctor                                      │
│  ├── Date & time                                             │
│  └── Export as PDF (for drug inspector)                       │
│                                                              │
│  ─── ALERTS ───                                              │
│                                                              │
│  ├── Stock below reorder level                               │
│  ├── Batch expiring in 30 days                               │
│  ├── MRP mismatch warning                                    │
│  └── Drug interaction alert (if pharmacist overrides)        │
└─────────────────────────────────────────────────────────────┘
```

### E. DIAGNOSTIC LAB FLOW
```
┌─────────────────────────────────────────────────────────────┐
│  LAB INTEGRATION FLOW                                        │
│                                                              │
│  1. Doctor prescribes test                                   │
│     ├── CBC, Lipid Profile, Thyroid                          │
│     └── Auto-sync to lab module                              │
│                                                              │
│  2. Lab receives order                                       │
│     ├── Patient registration (if new)                        │
│     ├── Sample collection                                    │
│     │   ├── Blood draw                                       │
│     │   ├── Urine sample                                     │
│     │   └── Other specimens                                  │
│     │                                                        │
│     ├── Test performed                                       │
│     │   ├── Hematology analyzer                              │
│     │   ├── Biochemistry analyzer                            │
│     │   └── Manual microscopy                                │
│     │                                                        │
│     └── Results entered                                      │
│         ├── Manual entry                                     │
│         ├── Auto-import from analyzer                        │
│         └── Reference range comparison                       │
│                                                              │
│  3. Auto-sync to doctor                                      │
│     ├── Doctor sees results in dashboard                     │
│     ├── Abnormal values HIGHLIGHTED                          │
│     ├── Compare with previous results                        │
│     └── Add notes/comments                                   │
│                                                              │
│  4. Patient receives report                                  │
│     ├── WhatsApp PDF                                         │
│     ├── Email PDF                                            │
│     ├── Print (A4)                                           │
│     └── PWA link (feature phones)                            │
│                                                              │
│  5. Billing                                                  │
│     ├── Test charges added to bill                           │
│     ├── GST invoice generated                                │
│     └── Payment collected                                    │
│                                                              │
│  ─── REVENUE TRACKING ───                                    │
│                                                              │
│  ├── Lab revenue: ₹XX,XXX                                    │
│  ├── Tests performed: XX                                     │
│  ├── Average test value: ₹XXX                                │
│  ├── Doctor referral commission: ₹XX,XXX                     │
│  └── Pending payments: ₹XX,XXX                               │
└─────────────────────────────────────────────────────────────┘
```

### F. DAY-END FLOW (Cash Tally)
```
┌─────────────────────────────────────────────────────────────┐
│  DAY-END "HISAAB-KITAAB" (Reconciliation)                    │
│                                                              │
│  1. Auto-calculate                                           │
│     ├── Cash collected: ₹XX,XXX                              │
│     ├── Card payments: ₹XX,XXX                               │
│     ├── UPI payments: ₹XX,XXX                                │
│     ├── Total revenue: ₹XX,XXX                               │
│     └── Pending: ₹XX,XXX                                     │
│                                                              │
│  2. Physical cash count                                      │
│     └── Enter actual cash in drawer                          │
│                                                              │
│  3. Variance check                                           │
│     ├── Match: ✅ "Hisaab barabar hai"                       │
│     └── Mismatch: ❌ "₹500 kam zyada hai"                   │
│                                                              │
│  4. Sign-off                                                 │
│     ├── Doctor signs                                         │
│     ├── Receptionist signs                                   │
│     └── Owner reviews (next morning)                         │
│                                                              │
│  5. Export                                                   │
│     ├── PDF report                                           │
│     ├── Excel export                                         │
│     └── Email to owner                                       │
└─────────────────────────────────────────────────────────────┘
```

## 3.5 MediFlow Features Summary

### P0 (Launch Blockers) — ALL DONE ✅
| Feature | Description |
|---------|-------------|
| Mobile SMS OTP Login | Phone number se login, OTP via SMS |
| Walk-in Flow (<20s) | Patient arrives → 20 seconds mein registered |
| Thermal/A4/A5 Printing | Token slip, Rx, Invoice — sab print |
| GST Engine | Consultation exempt, medicine taxable |
| Credit Notes | Invoice cancel pe auto credit note |
| Clinical Dosage Model | Weekly, ml, units — flexible dosage |
| Patient Dedup + Family | Phone se auto-merge, family linking |
| Idempotency + Concurrency | Double-submit nahi, parallel edit detect |
| Subscription Billing | Clinic se monthly SaaS fee collect |
| CSV Patient Import | Purana data 1-click import |
| Video Consult + TURN | WhatsApp link se video call |

### P1 (Competitiveness) — ALL DONE ✅
| Feature | Description |
|---------|-------------|
| Drug Interaction + Allergy CDSS | Real-time drug safety alerts |
| Rx Templates | Doctor ke top 30 drugs ki 1-click shortlist |
| Local Language Rx | Hindi/Marathi/Gujarati/Tamil dosage print |
| ABDM/ABHA Integration | Ayushman Bharat Digital Mission |
| Waiting Room + Live ETA | Patient ko pata hai kitna wait |
| Staff PIN Switch | Staff ek click mein switch |
| Supplier Ledger + Purchase Orders | Distributor ke saath accounts |
| Day-End Cash Tally | "Hisaab-Kitaab" reconciliation |
| Schedule H1 Register | Antibiotics ka auto-register |
| Consumables Tracking | Syringes, cotton track |

### P2 (Expansion) — DONE ✅
| Feature | Description |
|---------|-------------|
| Visiting Consultant Revenue Split | Bahar ke doctor ka hissa auto-calc |
| Export Tool (CSV/PDF) | Data export kahi bhi le jao |
| Offline Mode | Internet nahi hai toh queue mein save |
| Emergency Chat Red-Flag | "Heart attack" type keywords → auto-reply |
| Generic Substitute Suggestion | Brand ki jagah generic dikhao |
| Return to Supplier | Near-expiry wapas karo |
| Doctor Registration Expiry | License expiry tracking + alerts |
| Doctor Delayed TV Broadcast | "Dr. Sharma running 20 min late" |

## 3.6 Database Schema (61 Entities)

| Entity | Purpose |
|--------|---------|
| Patient | Patient demographics, contact, family |
| Doctor | Doctor profiles, speciality, schedule |
| Staff | Receptionist, pharmacist, nurse profiles |
| Visit | Patient visit record (walk-in/video) |
| Prescription | Doctor's prescription header |
| PrescriptionItem | Individual drug in prescription |
| Diagnosis | ICD-10 diagnosis codes |
| Vitals | BP, Temp, Weight, Height, Pulse, SpO2 |
| Invoice | Billing header |
| InvoiceItem | Individual bill line item |
| Payment | Payment record (cash/card/UPI) |
| CreditNote | Invoice cancellation credit |
| DrugInventory | Drug master (name, salt, category) |
| StockBatch | Batch-wise stock (MRP, expiry, qty) |
| StockTransaction | Stock movement log |
| ScheduleH1Register | Antibiotics register |
| Supplier | Distributor details |
| SupplierLedger | Distributor account ledger |
| PurchaseOrder | Stock purchase order |
| PurchaseOrderItem | PO line items |
| LabOrder | Diagnostic test order |
| LabResult | Test results with values |
| FamilyGroup | Family member grouping |
| FamilyMember | Family member details |
| ConsentRecord | Patient consent (DPDP) |
| MedicalRecordAudit | Audit trail for medical records |
| IdempotencyKey | Prevent duplicate submissions |
| OfflineSync | Offline queue sync |
| EmergencyChat | Red-flag keyword detection |
| DrugScheduleRegistry | Schedule H/X/NDPS drug list |
| DoctorRegistration | License expiry tracking |
| ConsumableItem | Syringes, cotton tracking |
| DoctorDelayBroadcast | TV display for delays |
| QueueEta | Live queue position + ETA |
| StaffPin | Quick switch PIN |
| DayEndTally | Cash reconciliation header |
| DayEndTallyDetail | Cash reconciliation detail |
| PrescriptionDraft | Auto-save Rx drafts |
| PatientMergeLog | Profile merge audit trail |
| VideoJoinToken | Short-TTL video room tokens |
| PaymentRefund | Refund tracking |
| DataExportLog | Data export audit |
| SubscriptionPlan | Clinic subscription plans |
| PatientImportBatch | CSV import tracking |
| RxTemplate | Doctor's drug shortlist |
| LocalLanguageRx | Multi-language Rx output |
| AbhaRecord | ABHA number linking |
| VisitingConsultantPayout | Consultant revenue split |
| DrugInteraction | Drug-drug interaction rules |
| DrugAllergy | Drug-allergy mapping |

## 3.7 CDSS (Clinical Decision Support System)

```
REAL-TIME ALERTS DURING PRESCRIPTION:

1. Drug-Drug Interaction
   ├── Warfarin + Aspirin → "Bleeding risk!"
   ├── Metformin + Alcohol → "Lactic acidosis risk!"
   └── SSRI + Tramadol → "Serotonin syndrome risk!"

2. Drug-Allergy Alert
   ├── Patient allergic to Penicillin → "Avoid Amoxicillin!"
   ├── Patient allergic to Sulfa → "Avoid Co-trimoxazole!"
   └── Patient allergic to NSAID → "Avoid Ibuprofen!"

3. Drug-Food Interaction
   ├── Warfarin + Green leafy vegetables → "Reduced efficacy"
   ├── Statins + Grapefruit → "Increased side effects"
   └── Tetracycline + Dairy → "Reduced absorption"

4. Dosage Validation
   ├── Pediatric dose exceeds max → "Dose too high!"
   ├── Elderly dose not reduced → "Consider dose reduction"
   └── Renal impairment → "Dose adjustment needed"

5. Schedule Drug Block
   ├── Schedule X via teleconsult → "Not allowed!"
   ├── NDPS drug → "Requires special prescription"
   └── Habit-forming drug → "Duration limit exceeded"

6. Generic Substitute Suggestion
   ├── Brand: Augmentin 625 (₹180)
   │   └── Generic: Amoxicillin + Clavulanate (₹45)
   └── Savings: ₹135 per strip
```

## 3.8 Security Features

```
├── JWT Authentication (15 min expiry)
├── MFA (TOTP - Google Authenticator)
├── AES-256 encryption for medical records
├── Rate limiting (5 OTP/10 min, 5 login/10 min)
├── Idempotency keys (prevent duplicate submissions)
├── Optimistic concurrency (RowVersion for parallel edits)
├── Audit trail (who changed what, when)
├── RBAC (Role-based access control)
├── DPDP compliance (Two-tier deletion)
├── Session timeout (auto-save drafts)
└── HTTPS everywhere
```

## 3.9 Background Services (8 Auto-jobs)

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

# 4. PLATFORM 3: GYMEXGLOBAL (INTERNATIONAL)

## 4.1 Overview
GymexGlobal is the international version of Gymex, targeting gyms and fitness studios in Middle East, Africa, and Southeast Asia.

## 4.2 Website
- **URL**: https://gymexglobalwebsite.vercel.app
- **Pages**: 18+ pages
- **Demo Modal**: EmailJS + intl-tel-input
- **Deployment**: Vercel (auto-deploy from GitHub)

## 4.3 Target Markets

| Region | Countries | Currency | Payment Gateway |
|--------|-----------|----------|-----------------|
| Middle East | UAE, Saudi, Oman, Qatar, Bahrain | AED/SAR | Stripe |
| Africa | Nigeria, Kenya, South Africa | NGN/KES/ZAR | Stripe |
| SE Asia | Philippines, Indonesia, Malaysia | PHP/IDR/MYR | Stripe |

## 4.4 Differentiation from Indian Gymex

| Feature | Indian Gymex | Global Gymex |
|---------|-------------|--------------|
| Language | English/Hindi | English/Arabic |
| Currency | INR (₹) | USD/AED/SAR |
| Payment | Razorpay | Stripe |
| Support | India office | Middle East office |
| Culture | Indian | Arabic/Islamic |
| Compliance | Indian GST | VAT (Middle East) |

## 4.5 Website Pages

| Page | URL | Purpose |
|------|-----|---------|
| Home | / | Hero, Stats, Features, Testimonials |
| About | /about | Company story, team |
| Features | /features | All software features |
| Pricing | /pricing | 3 plans (Starter/Growth/Enterprise) |
| Contact | /contact | Sales inquiry form |
| Blog | /blog | Articles, guides |
| Career | /career | Job openings |
| Privacy Policy | /privacy-policy | Legal |
| Refund Policy | /refund-policy | Legal |
| Gym Management | /gym-management-software | Industry page |
| Yoga Studio | /yoga-studio | Industry page |
| Dance Studio | /dance-studio | Industry page |
| Swim School | /swim-school | Industry page |
| Sports Academy | /sport-academies | Industry page |
| Martial Arts | /martial-arts-studio | Industry page |
| PT Studio | /pt-studio | Industry page |
| Pilates | /pilates | Industry page |
| Aerobics | /aerobics | Industry page |
| Health & Fitness | /health-and-fitness-centers | Industry page |
| Blog Article | /blog/article | Article template |

## 4.6 Pricing (International)

| Plan | Price | Members | Staff | Features |
|------|-------|---------|-------|----------|
| Starter | $29/month | Up to 100 | 1 | Basic features |
| Growth | $49/month | Up to 500 | 5 | All features |
| Enterprise | $99/month | Unlimited | Unlimited | All + API + White-label |

## 4.7 Website Tech Stack

```
├── HTML5 + CSS3
├── Bootstrap 5
├── JavaScript (Vanilla)
├── EmailJS (Form submission)
├── intl-tel-input (Phone with country code)
├── AOS.js (Scroll animations)
├── Slick Slider (Testimonials)
├── Vercel (Hosting + Auto-deploy)
└── Google Analytics
```

## 4.8 Website Features

```
HOME PAGE:
├── Hero Section with animated stats counter
├── Client Testimonials (slow scroll + arrows)
├── Awards & Recognition (6 logos)
├── Business Types (10 industry pages)
├── Features Section
├── Why Gym Owners Choose Us
├── Get Your Free Demo modal
└── Footer (all links)

DEMO MODAL (same across all pages):
├── Name, Last Name, Company
├── Email, Phone (intl-tel-input)
├── Message
├── EmailJS submission → Sales team
├── Success: "Thank you" message
└── Error: Retry option

NAVIGATION:
├── Home
├── About
├── Business Types (mega menu)
│   ├── Gym Management
│   ├── Yoga Studio
│   ├── Dance Studio
│   ├── Swim School
│   ├── Sports Academy
│   ├── Martial Arts
│   ├── PT Studio
│   ├── Pilates
│   ├── Aerobics
│   └── Health & Fitness
├── Features (mega menu)
│   ├── Member Management
│   ├── Staff Management
│   ├── Billing & Payments
│   ├── Marketing & CRM
│   ├── Data Analysis
│   ├── Mobile Apps
│   ├── Lead Management
│   ├── Appointment & Class
│   ├── Payroll & Commission
│   ├── Intelligent Alerts
│   ├── Expense Management
│   └── POS
├── Pricing
├── Blog
├── Contact
└── Get Your Free Demo

FOOTER:
├── Links: Home, About, Pricing, Blog, Contact
├── Legal: Terms, Privacy, Refund
├── About Us: Company description
├── Contact Us: Address, Phone, Email
├── Follow Us: Facebook, Instagram, LinkedIn
└── Copyright: © 2024 GreyBits Technologies
```

---

# 5. TECHNICAL ARCHITECTURE

## 5.1 Backend (MediFlow)

```
┌─────────────────────────────────────────────────────────────────┐
│                    MEDIFLOW ARCHITECTURE                         │
└─────────────────────────────────────────────────────────────────┘

LAYER 1: API Layer (Controllers)
├── 25 Controllers
├── REST API endpoints (100+)
├── JWT Authentication
├── Rate Limiting
└── Request Validation

LAYER 2: Application Layer (Services)
├── 74 Services
├── Business Logic
├── Validation Rules
├── CDSS Engine
└── Background Jobs

LAYER 3: Domain Layer (Entities)
├── 61 Entities
├── Value Objects
├── Domain Events
└── Business Rules

LAYER 4: Infrastructure Layer
├── PostgreSQL Database
├── Redis Cache
├── File Storage (S3/Azure)
├── Email (SendGrid)
├── SMS (Twilio/MSG91)
├── WhatsApp (Twilio)
└── Payment Gateway (Razorpay/Stripe)

LAYER 5: Cross-Cutting
├── Logging (Serilog)
├── Monitoring (Application Insights)
├── Caching (Redis)
├── Background Jobs (Hangfire)
└── Security (AES-256, JWT, MFA)
```

## 5.2 Frontend (Gymex App)

```
┌─────────────────────────────────────────────────────────────────┐
│                    GYMEX FRONTEND                                │
└─────────────────────────────────────────────────────────────────┘

WEB APP:
├── React.js
├── Tailwind CSS
├── Redux Toolkit (State)
├── React Router (Navigation)
├── Axios (API calls)
├── Chart.js (Analytics)
├── React Query (Data fetching)
└── Formik + Yup (Forms + Validation)

MOBILE APP:
├── React Native
├── Expo
├── Async Storage (Offline)
├── Push Notifications (FCM/APNs)
├── QR Code Scanner
├── Biometric Auth
└── Camera (Photo upload)

ADMIN PANEL:
├── React.js
├── Material UI
├── DataGrid (Tables)
├── Role-based routing
└── Real-time updates (SignalR)
```

## 5.3 Infrastructure

```
HOSTING:
├── AWS / Azure
├── Docker containers
├── Kubernetes (production)
├── Auto-scaling
└── Multi-region deployment

DATABASE:
├── PostgreSQL (primary)
├── Redis (cache + sessions)
├── S3/Azure Blob (files)
└── Elasticsearch (search)

CI/CD:
├── GitHub Actions
├── Automated testing
├── Code quality checks
├── Security scanning
└── Auto-deploy to production

MONITORING:
├── Application Insights
├── Sentry (error tracking)
├── Grafana (dashboards)
├── PagerDuty (alerts)
└── ELK Stack (logs)
```

---

# 6. REVENUE MODEL

## 6.1 Gymex Revenue Streams

| Stream | Price | Model |
|--------|-------|-------|
| SaaS Subscription | ₹999-3,999/month | Recurring |
| Transaction Fees | 2% on payments | Per transaction |
| White-label App | ₹10,000 one-time | One-time |
| Training & Setup | ₹5,000 one-time | One-time |
| API Access | ₹2,000/month | Recurring |

## 6.2 MediFlow Revenue Streams

| Stream | Price | Model |
|--------|-------|-------|
| SaaS Subscription | ₹999-3,999/month | Recurring |
| Transaction Fees | 1.5% on payments | Per transaction |
| API Access | ₹2,000/month | Recurring |
| Custom Integrations | Project-based | One-time |
| Data Migration | ₹10,000 one-time | One-time |

## 6.3 GymexGlobal Revenue Streams

| Stream | Price | Model |
|--------|-------|-------|
| SaaS Subscription | $29-99/month | Recurring |
| Transaction Fees | 2.5% on payments | Per transaction |
| White-label App | $500 one-time | One-time |
| Consulting | Project-based | One-time |

## 6.4 Revenue Projections

```
YEAR 1 (12 months):
├── Gymex: 100 customers × ₹2,000 avg = ₹24 Lakhs/year
├── MediFlow: 20 customers × ₹2,000 avg = ₹4.8 Lakhs/year
├── GymexGlobal: 10 customers × $50 avg = $6,000/year
└── Total: ~₹30 Lakhs/year

YEAR 2 (24 months):
├── Gymex: 300 customers × ₹2,000 avg = ₹72 Lakhs/year
├── MediFlow: 80 customers × ₹2,000 avg = ₹19.2 Lakhs/year
├── GymexGlobal: 40 customers × $50 avg = $24,000/year
└── Total: ~₹1 Crore/year

YEAR 3 (36 months):
├── Gymex: 800 customers × ₹2,000 avg = ₹1.92 Crores/year
├── MediFlow: 200 customers × ₹2,000 avg = ₹48 Lakhs/year
├── GymexGlobal: 100 customers × $50 avg = $60,000/year
└── Total: ~₹3 Crores/year
```

---

# 7. LAUNCH PLAN

## 7.1 Pre-Launch (Week 1-2)

```
├── Deploy GymexGlobal website ✅
├── Set up payment gateways (Razorpay, Stripe)
├── Create demo videos (2-3 minutes)
├── Set up sales CRM (HubSpot/Zoho)
├── Prepare marketing materials
│   ├── Brochure (PDF)
│   ├── Pitch deck (PDF)
│   ├── Case study template
│   └── Email templates
├── Set up customer support (Zendesk/Freshdesk)
├── Legal: Terms of Service, Privacy Policy
└── Insurance: Business liability
```

## 7.2 Pilot Launch (Week 3-4)

```
├── Onboard 3-5 pilot gyms (FREE for 1 month)
├── Onboard 1-2 pilot clinics (FREE for 1 month)
├── Collect feedback (weekly surveys)
├── Fix bugs (daily standup)
├── Refine onboarding flow
├── Create case studies from pilots
└── Prepare testimonials
```

## 7.3 Public Launch (Week 5-6)

```
├── Launch on Product Hunt
├── LinkedIn/Facebook ads (₹500/day)
├── Google Ads (₹500/day)
│   ├── "gym management software"
│   ├── "gym billing software"
│   ├── "clinic management software"
│   └── "prescription software"
├── Cold calling to gyms (100/day)
├── Email outreach (500/week)
├── Referral program live (₹500 per referral)
├── Partner with gym consultants
└── Attend fitness expos
```

## 7.4 Scale (Week 7-12)

```
├── Hire 2 sales reps
├── Hire 1 customer success manager
├── Launch MediFlow pilot
├── Start global expansion (Middle East)
├── Partner with accounting firms
├── Partner with gym equipment vendors
├── Content marketing (blog, YouTube)
├── Webinars for gym owners
└── Case studies + testimonials
```

## 7.5 Growth (Month 3-6)

```
├── 50 paying customers
├── ₹5 Lakhs MRR
├── Hire 2 developers
├── Launch mobile app
├── API marketplace
├── White-label option
└── Series A preparation
```

## 7.6 Scale (Month 6-12)

```
├── 200+ customers
├── ₹20 Lakhs MRR
├── 10+ team members
├── Global expansion (3 countries)
├── Series A funding
├── Enterprise clients
└── Platform ecosystem
```

---

# 8. TEAM & WORK DISTRIBUTION

## 8.1 Team Structure

| Role | Person | Responsibilities |
|------|--------|------------------|
| **CEO/Founder** | Hammad | Strategy, Sales, Fundraising |
| **CTO/Founder** | Rohit | Tech, Architecture, Development |
| **COO/Founder** | Imran | Operations, Customer Success |
| **Developer** | TBD | Frontend, Backend, Mobile |
| **Sales** | TBD | Lead gen, Demo, Closing |
| **Support** | TBD | Customer support, Onboarding |

## 8.2 Work Distribution

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

## 8.3 Sprint Plan (2-week sprints)

### Sprint 1 (Week 1-2)
```
├── Deploy GymexGlobal website ✅
├── Set up payment gateways
├── Create demo videos
├── Set up sales CRM
└── Prepare marketing materials
```

### Sprint 2 (Week 3-4)
```
├── Onboard pilot gyms (3-5)
├── Onboard pilot clinics (1-2)
├── Collect feedback
├── Fix bugs
└── Refine onboarding
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
├── Launch MediFlow pilot
├── Global expansion prep
└── Partnership outreach
```

---

# APPENDIX

## A. API Endpoints (MediFlow — 100+)

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
