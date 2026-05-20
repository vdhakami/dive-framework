# Deployment Manifest

| Field | Value |
|-------|-------|
| **Model ID** | |
| **Version** | |
| **Deployment Date** | |
| **Deployed By** | |

---

## 1. Deployment Target

☐ Cloud — Provider: _____ Region: _____
☐ On-premises — Location: _____
☐ Edge — Device type: _____
☐ Hybrid — Describe: _____

---

## 2. Infrastructure

| Resource | Specification | Autoscaling? | Min / Max |
|----------|--------------|-------------|-----------|
| Instance type | | ☐ Yes ☐ No | / |
| GPU | | ☐ Yes ☐ No | / |
| Memory | | ☐ Yes ☐ No | / |
| Storage | | ☐ Yes ☐ No | / |

---

## 3. Serving Configuration

| Parameter | Value |
|-----------|-------|
| Batch size | |
| Max concurrency | |
| Timeout | ___ ms |
| Retry policy | |
| Fallback behavior | |
| Warm-up requests | ☐ Yes ☐ No — count: ___ |

---

## 4. Release Strategy

☐ **Blue/Green** — two identical environments, instant switch
☐ **Canary** — % traffic: ___ → ___ → 100%
☐ **Shadow mode** — parallel run, no user-facing output
☐ **Rolling update** — instance by instance
☐ **Feature flag** — controlled rollout
☐ **Other:** _____

---

## 5. Rollback Plan

**Trigger conditions for rollback:**
> e.g., error rate > 5%, latency p95 > 500ms

**Rollback steps:**
1.
2.
3.

**Expected rollback time:** ___ minutes

**Has rollback been tested?** ☐ Yes ☐ No

---

## 6. Monitoring & Alerts (Post-Deployment)

| Monitor | Tool / Method | Alert Recipients |
|---------|--------------|-----------------|
| Latency p95 > threshold | | |
| Error rate > threshold | | |
| Drift detected | | |
| | | |

---

## 7. Approvals

| Role | Name | Date |
|------|------|------|
| ML Engineer | | |
| PM | | |
| Operations | | |

---

*DIVE Framework™ — Template T10*
