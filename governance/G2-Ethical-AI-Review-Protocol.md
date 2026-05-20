# Ethical AI Review Board Protocol

| Field | Value |
|-------|-------|
| **Document ID** | G2 |
| **Version** | 1.0 |
| **Effective Date** | |
| **Approved By** | |

---

## 1. Scope

This protocol applies to all AI projects classified as **Medium** or **High Risk** by the AI Ethics Screening Checklist (Template T9). Low Risk projects follow standard governance only.

---

## 2. Review Triggers

| Trigger | Timing | Lead | Required Participants |
|---------|--------|------|---------------------|
| **Initial Screening** | Day 0 of Diagnose phase | Ethics Officer | Ethics Officer + PM |
| **Full Ethics Review** | Before Validate gate | Review Board | Full Board (5 members) |
| **Pre-Deployment Review** | Before Evolve gate | Review Board | Full Board (5 members) |
| **Incident Review** | Within 48 hours of critical incident | Chair | Emergency session |
| **Annual Review** | Every 12 months post-deployment | Ethics Officer | Ethics Officer + Model Owner |

---

## 3. Review Dimensions

| # | Dimension | Key Questions |
|---|-----------|--------------|
| 1 | **Fairness** | Does the model have disparate impact across protected groups? Are fairness metrics within thresholds? |
| 2 | **Transparency** | Is the explainability method appropriate for the use case? Can stakeholders understand model behavior? |
| 3 | **Accountability** | Is there clear ownership? Are escalation paths defined and tested? |
| 4 | **Privacy** | Is data minimized? Is consent obtained? Are retention limits enforced? |
| 5 | **Robustness** | How does the model perform under distribution shift? Adversarial conditions? |
| 6 | **Human Oversight** | Are escalation tiers defined? Are override mechanisms in place? |
| 7 | **Remediation** | Is there a mechanism for harmed individuals to seek redress? Is there an appeal process? |

---

## 4. Decision Categories

| Decision | Meaning | Required Vote |
|----------|---------|-------------|
| ✅ **Approved** | May proceed without conditions | Majority |
| ⚠️ **Conditional** | May proceed with specified mitigations | Majority |
| 🔄 **Return** | Insufficient information — resubmit with additions | Majority |
| ❌ **Rejected** | Must not proceed in current form | Supermajority (2/3) |
| 🛑 **Decommission** | Existing model must be taken down | Supermajority (2/3) |

---

## 5. Documentation Requirements

All reviews must produce:
1. Completed Ethics Review Checklist
2. Minutes of Board discussion
3. Decision rationale
4. Mitigation conditions (if Conditional)
5. Follow-up schedule

**Retention:** Minimum 7 years (or as required by applicable regulations).

---

## 6. Escalation

If the project team disagrees with a Board decision:
1. Written appeal to Board Chair within 14 days
2. Chair may convene an appellate panel (3 independent members)
3. Appellate decision is final

---

*DIVE Framework™ — Governance Artifact G2*
