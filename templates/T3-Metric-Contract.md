# Metric Contract

| Field | Value |
|-------|-------|
| **Project** | |
| **Contract Version** | |
| **Status** | Draft / Proposed / Signed |
| **Date** | |

> **⚠️ IMPORTANT:** This contract is immutable after signing. Changes require full stakeholder re-sign-off.

---

## 1. Primary Metrics (Phase Exit Criteria)

| Metric | Definition | Target | Minimum Acceptable | Baseline | Measurement Method |
|--------|-----------|--------|-------------------|----------|-----------------|
| | | | | | |
| | | | | | |
| | | | | | |

*All primary metrics must meet or exceed Minimum Acceptable for phase exit.*

---

## 2. Secondary Metrics (Monitor Only — Not Gates)

| Metric | Warning Threshold | Alert Threshold |
|--------|------------------|----------------|
| | | |
| | | |

---

## 3. Constraint Gates (Hard Boundaries)

| Constraint | Threshold | Violation Consequence |
|------------|-----------|----------------------|
| Inference latency (p95) | ≤ ___ ms | Redesign |
| Cost per inference | ≤ $___ | Redesign |
| Model size | ≤ ___ MB | Redesign |
| Training time | ≤ ___ hours | Descope |
| | | |

*Any violation of a constraint gate triggers the specified consequence automatically.*

---

## 4. Test Set Specification

| Parameter | Value |
|-----------|-------|
| Test set source | |
| Test set size (# samples) | |
| Test set collection date | |
| Stratification strategy | |
| Hold-out method | ☐ Random split ☐ Time-based split ☐ Group-based split |
| Is test set independent from training data? | ☐ Yes ☐ No — explain: |

---

## 5. Fairness Requirements

| Protected Attribute | Metric | Minimum Threshold |
|--------------------|--------|-----------------|
| | Disparate impact ratio | ≥ 0.80 |
| | Equal opportunity difference | ≤ 0.05 |
| | Equalized odds (max diff) | ≤ 0.05 |
| | | |

---

## 6. Signatures

*By signing, each party agrees that the metrics and thresholds defined above constitute the sole criteria for project phase completion.*

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Sponsor | | | |
| PM | | | |
| Data Science Lead | | | |
| Product Owner | | | |
| Ethics Officer | | | |

---

*DIVE Framework™ — Template T3*
