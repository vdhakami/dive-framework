# Model Evaluation Report

| Field | Value |
|-------|-------|
| **Project** | |
| **Model ID** | |
| **Evaluator** | |
| **Date** | |
| **Status** | Draft / Final |

---

## 1. Final Metrics vs. Contract

| Metric | Target | Minimum Acceptable | Achieved | Pass? |
|--------|--------|-------------------|----------|-------|
| | | | | ☐ Yes ☐ No |
| | | | | ☐ Yes ☐ No |
| | | | | ☐ Yes ☐ No |

---

## 2. Test Set Information

| Parameter | Value |
|-----------|-------|
| Total samples | |
| Positive class samples | |
| Negative class samples | |
| Time period covered | |
| Distribution matches production? | ☐ Yes ☐ No — describe: |

---

## 3. Confusion Matrix (Classification Only)

| | Predicted Positive | Predicted Negative |
|----------------|-------------------|-------------------|
| **Actual Positive** | TP = ___ | FN = ___ |
| **Actual Negative** | FP = ___ | TN = ___ |

**Derived:** Precision = ___ | Recall = ___ | F1 = ___ | Accuracy = ___

---

## 4. Performance by Segment

| Segment | Sample Size | Metric Value | vs. Overall |
|---------|------------|-------------|-------------|
| Overall | | | — |
| Segment A | | | |
| Segment B | | | |
| Edge case 1 | | | |
| Edge case 2 | | | |

---

## 5. Error Analysis

| Error Mode | Frequency | Root Cause | Severity |
|-----------|-----------|-----------|----------|
| | | | H / M / L |
| | | | H / M / L |
| | | | H / M / L |

**Overall error rate:** ___% (threshold: ___%)

**Unacceptable errors identified?** ☐ Yes ☐ No

---

## 6. Efficiency Benchmarks

| Measure | Achieved | Required | Pass? |
|---------|---------|----------|-------|
| Latency p50 | | | ☐ Yes ☐ No |
| Latency p95 | | | ☐ Yes ☐ No |
| Latency p99 | | | ☐ Yes ☐ No |
| Throughput (req/s) | | | ☐ Yes ☐ No |
| Memory usage (MB) | | | ☐ Yes ☐ No |
| Model size (MB) | | | ☐ Yes ☐ No |

---

## 7. Recommendation

☐ **Pass** — meets all thresholds — proceed to deployment
☐ **Conditional Pass** — meets primary metrics, secondary waived (attach waiver)
☐ **Fail** — does not meet Metric Contract — return to Iterate

**Comments:**

---

*DIVE Framework™ — Template T6*
