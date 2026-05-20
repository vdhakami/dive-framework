# DIVE Framework — Complete Methodology Reference

**Version 1.0 | May 2026**

Diagnose >> Iterate >> Validate >> Evolve

---

## Table of Contents

1. Executive Summary
2. Core Principles (7)
3. The DIVE Lifecycle
4. Templates Overview (14)
5. Governance Artifacts Overview (5)
6. Glossary

---

## 1. Executive Summary

The DIVE Framework (Diagnose >> Iterate >> Validate >> Evolve) is a project management methodology purpose-built for Artificial Intelligence and Machine Learning initiatives. Unlike traditional frameworks (PMBOK, PRINCE2, Agile) that assume deterministic outputs and known solution paths, DIVE addresses the fundamental uncertainty inherent in AI development.

### Why AI Needs a New Framework

| Characteristic | Traditional Software | AI Projects |
|----------------|-------------------|-------------|
| Output | Deterministic | Probabilistic |
| Spec | Known upfront | Discovered through data |
| Failure mode | Bug >> fix | Data/model degradation |
| Estimation | Possible with history | High uncertainty |
| Quality check | Pass/fail tests | Metric thresholds |
| Main cost | Engineering hours | Compute + data + talent |

---

## 2. Core Principles

### Principle 1: Data First, Code Second
No AI project begins with architecture. It begins with data audit. If the data does not exist, is not accessible, or does not contain the signal -- the project cannot succeed regardless of model sophistication. Every DIVE project has a mandatory Data Feasibility Gate before any model development.

### Principle 2: Parallel Exploration Beats Sequential Certainty
AI is research-like by nature. The winning approach is unknown at project start. DIVE mandates parallel experimentation tracks (typically 3-5) in the Iterate phase, each exploring a different algorithmic approach, prompt strategy, or data representation.

### Principle 3: Metric Contracts Replace Requirements Documents
A "requirement" in AI is meaningless until quantified. DIVE replaces traditional requirements with Metric Contracts: precise, measurable definitions of success (e.g., "F1 >= 0.87 on held-out test set, latency <= 200ms p95").

### Principle 4: Fail Fast, Fail Quantitatively
DIVE defines quantitative Feasibility Gates at phase boundaries. If gate criteria are unmet after the allocated exploration budget, the project is redesigned, descoped, or killed -- not extended.

### Principle 5: Governance Is Continuous, Not Periodic
AI models degrade post-deployment (data drift, concept drift). DIVE mandates permanent monitoring and governance as a project phase. Every model has a Governance Card for its entire lifetime.

### Principle 6: Human-in-the-Loop Is a Design Constraint
Three escalation tiers designed pre-deployment: Advisory (human reviews), Assisted (human confirms), and Automated (no human in loop -- highest governance requirement).

### Principle 7: Compute Is a First-Class Resource
GPU time, API tokens, and data storage costs dominate AI project budgets. DIVE tracks compute burn rate alongside schedule and budget variance.

---

## 3. The DIVE Lifecycle

### Phase 1: Diagnose (2-4 weeks)

**Purpose:** Validate the problem is AI-suitable, data is available, and success is measurable.

**Activities:**
- Problem framing workshop
- Data landscape audit
- Feasibility baseline (simplest possible model)
- Metric Contract negotiation
- AI Ethics screening
- Risk identification
- Build vs. buy analysis

**Exit Gate -- Feasibility Review:**
- Data exists, accessible, contains signal above noise floor
- Metric Contract signed by all stakeholders
- Baseline model shows results better than random/heuristic
- Ethics screening passes (or mitigations documented)
- Decision: Go / No-Go / Redesign

### Phase 2: Iterate (4-8 weeks)

**Purpose:** Explore multiple technical approaches in parallel.

**Activities:**
- Parallel experiment design (3-5 tracks)
- Track execution with fixed compute budgets
- Weekly comparison on shared dashboard
- Compute burn rate tracking
- Mid-phase pivot decision
- Top candidate selection

**Exit Gate -- Candidate Selection:**
- At least one track meets Metric Contract thresholds
- Top candidate(s) reproducible and documented
- Compute budget variance < 20%
- Risk register updated

### Phase 3: Validate (2-4 weeks)

**Purpose:** Rigorously evaluate the selected model against production conditions.

**Activities:**
- Hold-out evaluation
- Robustness & edge case testing
- Bias audit
- Performance benchmarking (latency, throughput, cost)
- Shadow deployment (optional)
- Stakeholder demo & sign-off

**Validation dimensions:** Accuracy, Fairness, Robustness, Efficiency, Explainability

**Exit Gate -- Validation Sign-Off:**
- All Metric Contract thresholds met
- Bias audit clean or mitigations accepted
- Edge case handling documented
- Stakeholder sign-off obtained

### Phase 4: Evolve (ongoing)

**Purpose:** Deploy, monitor, and continuously improve the model in production.

**Activities:**
- Production deployment (Blue/Green, Canary, Rolling)
- Configure monitoring (data drift, concept drift, performance drift)
- Initialize Governance Card
- Establish drift baselines
- Set up feedback pipeline
- Continuous monitoring & response
- Quarterly governance review
- Retraining as needed

**Drift Response Protocol:**
| Level | Label | Definition | Response | Action |
|-------|-------|-----------|----------|--------|
| 1 | Green | < 1 sigma | None | Continue monitoring |
| 2 | Yellow | 1-2 sigma | 1 week | Investigate, alert team |
| 3 | Orange | 2-3 sigma | 48 hours | Halt non-critical, prepare retraining |
| 4 | Red | > 3 sigma | Immediate | Halt model, fallback, incident report |

**Exit Gate -- Decommissioning:**
- Model permanently retired
- Governance Card finalized and archived
- Downstream consumers notified

---

## 4. Templates (14)

| ID | Template | Phase |
|----|----------|-------|
| T1 | AI Project Charter | Diagnose |
| T2 | Data Inventory & Quality Report | Diagnose |
| T3 | Metric Contract | Diagnose |
| T4 | Experiment Log | Iterate |
| T5 | Track Comparison Dashboard | Iterate |
| T6 | Model Evaluation Report | Validate |
| T7 | AI Risk Register | All |
| T8 | Model Governance Card | Evolve |
| T9 | AI Ethics Screening Checklist | Diagnose |
| T10 | Deployment Manifest | Validate |
| T11 | Drift Alert & Response Log | Evolve |
| T12 | Phase Gate Review Checklist | All |
| T13 | Retrospective / Lessons Learned | All |
| T14 | Compute Budget Tracker | Iterate |

---

## 5. Governance Artifacts (5)

| ID | Artifact | Purpose |
|----|----------|---------|
| G1 | AI Governance Board Charter | Board structure, authority, and operating model |
| G2 | Ethical AI Review Board Protocol | Formal review process for high-risk AI |
| G3 | Model Drift Response Protocol | Severity-classified drift response procedures |
| G4 | AI Project Audit Trail Policy | Retention, versioning, reproducibility standards |
| G5 | Project Complexity & Governance Tier Matrix | Risk-based tier classification (4 tiers) |

---

## 6. Glossary

| Term | Definition |
|------|-----------|
| **Baseline** | Performance of the simplest reasonable model |
| **Compute Budget** | Fixed allocation of GPU/CPU/token resources |
| **Concept Drift** | Change in relationship between inputs and target |
| **Data Drift** | Change in input data distribution over time |
| **Escalation Tier** | Level of human involvement (Advisory/Assisted/Automated) |
| **Feasibility Gate** | Quantitative Go/No-Go decision point |
| **Governance Card** | Living document for model identity and monitoring |
| **Metric Contract** | Signed measurable success criteria |
| **Parallel Track** | One of multiple simultaneous experiment approaches |
| **Performance Drift** | Degradation of evaluation metrics over time |
| **RPN** | Risk Priority Number (Likelihood x Impact) |
| **Shadow Deployment** | Parallel run without serving user-facing output |
| **Signal** | Measurable correlation between features and target |

---

*DIVE Framework -- Copyright (c) 2026 Vahid Hakami. All rights reserved.*
*SSRN Abstract ID: 6806018 — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6806018*
