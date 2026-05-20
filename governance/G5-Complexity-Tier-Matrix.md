# Project Complexity & Governance Tier Matrix

| Field | Value |
|-------|-------|
| **Document ID** | G5 |
| **Version** | 1.0 |
| **Effective Date** | |

---

## 1. Tier Classification Overview

| Tier | Label | Governance Requirements |
|------|-------|----------------------|
| **Tier 1** | Low | Light: Charter + Risk Register + Governance Card |
| **Tier 2** | Medium | Standard: All templates + Bi-weekly board review |
| **Tier 3** | High | Full: All templates + Ethics review + Full board sign-off |
| **Tier 4** | Critical | Maximum: All of Tier 3 + External audit + Regulatory notification |

---

## 2. Classification Factors

| Factor | Tier 1 (Low) | Tier 2 (Medium) | Tier 3 (High) | Tier 4 (Critical) |
|--------|-------------|-----------------|--------------|-------------------|
| **Autonomy Level** | Advisory | Assisted | Automated | Full autonomy |
| **Decision Impact** | Low (inconvenience) | Medium (financial loss) | High (health/safety/rights) | Critical (life-threatening) |
| **Regulation** | None | Some | Heavily regulated | Multiple jurisdictions |
| **Data Sensitivity** | Internal only | Internal + some PII | Extensive PII/sensitive | Highly restricted/classified |
| **Scale (users)** | < 100 | 100 - 10K | 10K - 1M | > 1M |
| **Failure Cost** | < $10K | $10K - $100K | $100K - $1M | > $1M |

---

## 3. Classification Method

1. Score each factor on a scale of 1-4 (matching the tier numbers)
2. Calculate the **average score**
3. Round to the nearest integer to determine the tier

| Average Score | Tier |
|-------------|------|
| 1.0 - 1.5 | Tier 1 — Low |
| 1.6 - 2.5 | Tier 2 — Medium |
| 2.6 - 3.5 | Tier 3 — High |
| 3.6 - 4.0 | Tier 4 — Critical |

---

## 4. Governance Requirements by Tier

### Tier 1 — Low (Light)

| Requirement | Required? |
|------------|-----------|
| AI Project Charter | ✅ |
| Data Inventory & Quality Report | ✅ |
| Metric Contract | ✅ |
| AI Risk Register | ✅ |
| Model Governance Card | ✅ |
| Ethics Screening | ✅ |
| Phase Gate Reviews | ✅ |
| Full templates (all 14) | ❌ — subset only |
| Board review | ❌ |
| External audit | ❌ |

### Tier 2 — Medium (Standard)

All Tier 1 requirements, plus:

| Requirement | Required? |
|------------|-----------|
| All 14 templates | ✅ |
| Bi-weekly board review | ✅ |
| Bias audit | ✅ |
| Explainability analysis | ✅ |
| Shadow deployment | Recommended |
| Drift monitoring | ✅ |

### Tier 3 — High (Full)

All Tier 2 requirements, plus:

| Requirement | Required? |
|------------|-----------|
| Full ethics review board | ✅ |
| Board sign-off at all gates | ✅ |
| External bias audit | ✅ |
| Public disclosure documentation | ✅ |
| Quarterly governance review | ✅ |
| Dedicated compliance officer | ✅ |

### Tier 4 — Critical (Maximum)

All Tier 3 requirements, plus:

| Requirement | Required? |
|------------|-----------|
| Independent external audit | ✅ |
| Regulatory authority notification | ✅ |
| Full-time model governance team | ✅ |
| Continuous monitoring (real-time) | ✅ |
| Mandatory human-in-the-loop | ✅ |
| Monthly board reporting | ✅ |
| Insurance/indemnity review | ✅ |

---

## 5. Tier Escalation & De-escalation

| Action | Process | Approval |
|--------|---------|---------|
| **Escalation** | PM petitions Board at any time | Majority vote |
| **De-escalation** | PM petitions Board after 6 months of stable production (zero drift incidents) | Supermajority (2/3) |

---

## 6. Tier Assignment Record

| Project | Assigned Tier | Date | Classified By | Review Date |
|---------|-------------|------|-------------|-----------|
| | | | | |
| | | | | |

---

*DIVE Framework™ — Governance Artifact G5*
