# AI Project Audit Trail Policy

| Field | Value |
|-------|-------|
| **Document ID** | G4 |
| **Version** | 1.0 |
| **Effective Date** | |

---

## 1. Purpose

Ensure every AI project under the DIVE Framework maintains a complete, tamper-evident record of decisions, data, models, and governance actions for accountability, compliance, and reproducibility.

---

## 2. Required Records & Retention

| Artifact | Retention Period | Owner | Format |
|----------|-----------------|-------|--------|
| Project Charter | Project life + 7 years | PM | Signed PDF |
| Data Inventory & Quality Report | Project life + 7 years | Data Engineer | Signed PDF |
| Metric Contract (all versions) | Project life + 7 years | PM | Signed PDF |
| Experiment Logs | Project life + 3 years | Data Scientist | Markdown / Notebook |
| Model Evaluation Reports | Model life + 7 years | Data Scientist | Signed PDF |
| Model Governance Card | Model life + 7 years | PM | Living document |
| Phase Gate Review Records | Project life + 7 years | PM | Signed PDF |
| Drift Alert Logs | Model life + 3 years | ML Engineer | Database / Log |
| Deployment Manifests | Deployment life + 3 years | ML Engineer | Signed PDF |
| Ethics Reviews | Project life + 10 years | Ethics Officer | Signed PDF |
| Board Decisions | Permanent | Governance Board | Signed minutes |

---

## 3. Version Control Requirements

| Requirement | Standard |
|------------|----------|
| System | Git (or equivalent) |
| Minimum commit info | Author, timestamp, change description |
| Metric Contract | Immutable after signing. Changes = new version, full re-sign-off |
| Governance Card | Living document — all changes tracked with version history |
| Tags | Every deployment tagged with model version + data snapshot ID |

---

## 4. Reproducibility Requirements

Every model promoted to production must have:

| Component | Requirement |
|-----------|------------|
| Training code | Exact commit hash |
| Training data | Snapshot identifier (S3 path, database snapshot ID) |
| Environment | Docker image digest or conda/pip lock file |
| Random seeds | All seeds documented |
| Training config | Full configuration file (hyperparameters, architecture) |
| Evaluation code | Same commit as training code |

---

## 5. Access Control

| Artifact Class | Read | Write | Admin |
|---------------|------|-------|-------|
| Project records | Project team | PM | PM + Governance Board |
| Ethics reviews | Governance Board + Legal | Ethics Officer | Ethics Officer |
| Deployment manifests | All (read) | ML Engineering | ML Engineering Lead |
| Financial/compute data | PM + Sponsor | PM | PM |

**Access revocation:** Within 48 hours of role change or departure.

---

## 6. Compliance

This policy satisfies requirements for:
- **GDPR** Art. 5(2) — Accountability
- **ISO 42001** — AI Management System
- **EU AI Act** — Documentation obligations (Tiers 1-3)
- **NYC Local Law 144** — Bias audit records

> *Organizations operating in additional jurisdictions should consult legal counsel for supplemental requirements.*

---

*DIVE Framework™ — Governance Artifact G4*
