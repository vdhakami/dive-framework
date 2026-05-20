# Model Governance Card

| Field | Value |
|-------|-------|
| **Model ID** | |
| **Project** | |
| **Created** | |
| **Last Reviewed** | |
| **Status** | Development / Validation / Production / Deprecated / Decommissioned |

---

## 1. Model Identity

| Field | Value |
|-------|-------|
| Model Name | |
| Version | |
| Type | Classification / Regression / GenAI / Other: |
| Framework | PyTorch / TensorFlow / sklearn / Other: |
| Training Date | |
| Deployment Date | |
| Owner | |
| Maintainer | |

---

## 2. Intended Use

**Purpose:**
> What is the model designed to do?

**Valid Use Cases:**
> When is it appropriate to use this model?

**Invalid Use Cases:**
> When should this model NOT be used?

**Supported Input Distribution:**
> Description of valid input domain

---

## 3. Performance Characteristics

| Metric | Value at Validation | Current Value | Drift Detected? |
|--------|--------------------|--------------|-----------------|
| | | | ☐ Yes ☐ No |
| | | | ☐ Yes ☐ No |
| | | | ☐ Yes ☐ No |

| Event | Date |
|-------|------|
| Last full evaluation | |
| Next scheduled evaluation | |

---

## 4. Fairness & Bias

| Protected Attribute | Metric at Validation | Current Metric | Threshold | Pass? |
|--------------------|--------------------|--------------|----------|-------|
| | | | | ☐ Yes ☐ No |
| | | | | ☐ Yes ☐ No |

---

## 5. Explainability

| Method | Available? |
|--------|-----------|
| Feature importance (global) | ☐ Yes ☐ No |
| SHAP/LIME (per-instance) | ☐ Yes ☐ No |
| Decision tree surrogate | ☐ Yes ☐ No |
| Reasoning trace (GenAI) | ☐ Yes ☐ No |
| Not applicable (low-risk only) | ☐ |

---

## 6. Monitoring Configuration

| Monitor | Enabled? | Alert Threshold | Last Alert |
|---------|---------|----------------|-----------|
| Data drift | ☐ Yes ☐ No | | |
| Concept drift | ☐ Yes ☐ No | | |
| Performance drift | ☐ Yes ☐ No | | |
| Latency | ☐ Yes ☐ No | | |
| Error rate | ☐ Yes ☐ No | | |
| Cost per inference | ☐ Yes ☐ No | | |

---

## 7. Audit Trail

| Date | Event | Performed By | Notes |
|------|-------|-------------|-------|
| | Model created | | |
| | Validation passed | | |
| | Deployed to production | | |
| | Drift alert triggered | | |
| | Retrained (v___) | | |
| | Decommissioned | | |

---

## 8. Dependencies

| Dependency | Version | Critical? | Alternative |
|-----------|---------|-----------|-------------|
| Python | | ☐ Yes ☐ No | |
| ML Framework | | ☐ Yes ☐ No | |
| API Service | | ☐ Yes ☐ No | |
| External data source | | ☐ Yes ☐ No | |

---

## 9. Approvals

| Role | Name | Date |
|------|------|------|
| Data Scientist | | |
| ML Engineer | | |
| Ethics Officer | | |
| PM | | |

---

*DIVE Framework™ — Template T8*
