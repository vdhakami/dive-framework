# Model Drift Response Protocol

| Field | Value |
|-------|-------|
| **Document ID** | G3 |
| **Version** | 1.0 |
| **Effective Date** | |

---

## 1. Detection

Drift is detected through automated monitoring (configured per Model Governance Card — Template T8) on the following dimensions:

| Dimension | Typical Metric | Description |
|-----------|---------------|-------------|
| **Data Drift** | PSI, KL divergence | Change in input data distribution |
| **Concept Drift** | Metric degradation | Change in relationship between inputs and targets |
| **Performance Drift** | Online metrics vs. baseline | Degradation of model accuracy/quality over time |

*Monitoring thresholds are established during the Evolve phase (Drift Baseline).*

---

## 2. Severity Classification

| Level | Label | Definition | Color |
|-------|-------|-----------|-------|
| 1 | **Green** | Within normal variation (< 1σ from baseline) | 🟢 |
| 2 | **Yellow** | Moderate drift (1-2σ from baseline) | 🟡 |
| 3 | **Orange** | Significant drift (2-3σ from baseline) | 🟠 |
| 4 | **Red** | Critical drift (> 3σ from baseline) | 🔴 |

---

## 3. Response Actions

### Level 2 — Yellow (Response: 1 week)

| Step | Action | Owner |
|------|--------|-------|
| 1 | Notify model owner and data science lead | Automated |
| 2 | Root cause analysis | Data Scientist |
| 3 | Document findings in Drift Alert Log | Data Scientist |
| 4 | Decision: continue monitoring or prepare retraining | PM + Data Scientist |

### Level 3 — Orange (Response: 48 hours)

| Step | Action | Owner |
|------|--------|-------|
| 1 | Notify model owner, PM, and Governance Board | Automated |
| 2 | Halt non-critical inference decisions (if applicable) | ML Engineer |
| 3 | Prepare retraining pipeline | Data Scientist |
| 4 | Deploy shadow mode if feasible | ML Engineer |
| 5 | Decision: retrain, rollback, or accept documented risk | PM + Governance Board |

### Level 4 — Red (Response: Immediate)

| Step | Action | Owner |
|------|--------|-------|
| 1 | Notify entire project team, Governance Board, sponsor | Automated |
| 2 | Halt model inference — switch to fallback | ML Engineer |
| 3 | Roll back to previous model version (if available) | ML Engineer |
| 4 | Emergency root cause analysis | Data Scientist |
| 5 | File incident report within 24 hours | PM |
| 6 | Decision: retrain, replace, or decommission | Governance Board |

---

## 4. Retraining Decision Tree

```
Drift detected?
├── Root cause = data distribution change (legitimate shift)
│   ├── Sufficient new labeled data? → Retrain
│   └── Insufficient data → Deploy fallback, collect data
├── Root cause = data quality issue (pipeline failure)
│   ├── Pipeline fix possible? → Fix and retrain
│   └── Permanent quality issue → Redesign
├── Root cause = environment change (new API, regulation, etc.)
│   ├── Adapt model possible? → Modify and retrain
│   └── No adaptation possible → Decommission
└── Root cause = unknown
    └── Monitor 1 week, escalate if persistent → Level 3
```

---

## 5. Post-Incident Review

| Requirement | Detail |
|------------|--------|
| Incident report | Filed within 24 hours of Red event |
| Root cause | Documented in Drift Alert Log |
| Preventative measures | Identified and assigned |
| Governance Card | Updated with incident record |
| Board notification | Summary presented at next meeting |
| Lessons learned | Shared with all project teams |

---

*DIVE Framework™ — Governance Artifact G3*
