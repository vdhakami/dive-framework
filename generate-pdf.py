# -*- coding: utf-8 -*-
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(160, 160, 160)
            self.cell(0, 6, 'DIVE Framework -- White Paper', align='L')
            self.cell(0, 6, f'Page {self.page_no()}', align='R', new_x='LMARGIN', new_y='NEXT')
            self.line(10, 14, 200, 14)
            self.ln(6)

    def title_page(self):
        self.add_page()
        self.ln(50)
        self.set_font('Helvetica', 'B', 32)
        self.set_text_color(26, 60, 110)
        self.cell(0, 14, 'DIVE', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_font('Helvetica', '', 18)
        self.set_text_color(74, 110, 165)
        self.cell(0, 10, 'A Project Management Framework for', align='C', new_x='LMARGIN', new_y='NEXT')
        self.cell(0, 10, 'Artificial Intelligence Initiatives', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(10)
        self.set_draw_color(74, 158, 111)
        self.set_line_width(0.5)
        self.line(90, self.get_y(), 120, self.get_y())
        self.ln(10)
        self.set_font('Helvetica', '', 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, 'Diagnose >> Iterate >> Validate >> Evolve', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(20)
        self.set_font('Helvetica', '', 11)
        self.cell(0, 7, 'Vahid Hakami', align='C', new_x='LMARGIN', new_y='NEXT')
        self.cell(0, 7, 'May 2026 | Version 1.0', align='C', new_x='LMARGIN', new_y='NEXT')

    def section_title(self, title):
        self.ln(6)
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(26, 60, 110)
        self.cell(0, 10, title, new_x='LMARGIN', new_y='NEXT')
        self.set_draw_color(74, 158, 111)
        self.line(10, self.get_y(), 60, self.get_y())
        self.ln(4)

    def sub_title(self, title):
        self.ln(4)
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(42, 76, 130)
        self.cell(0, 8, title, new_x='LMARGIN', new_y='NEXT')
        self.ln(2)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def add_table(self, headers, rows, col_widths=None):
        if col_widths is None:
            col_widths = [190 / len(headers)] * len(headers)
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(26, 60, 110)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1, align='C', fill=True)
        self.ln()
        self.set_font('Helvetica', '', 9)
        self.set_text_color(30, 30, 30)
        fill = False
        for row in rows:
            if fill:
                self.set_fill_color(245, 247, 250)
            else:
                self.set_fill_color(255, 255, 255)
            max_h = 7
            for i, cell_text in enumerate(row):
                lines = self.multi_cell(col_widths[i], 7, cell_text, dry_run=True, output='LINES')
                h = len(lines) * 7
                if h > max_h:
                    max_h = h
            x_start = self.get_x()
            y_start = self.get_y()
            for i, cell_text in enumerate(row):
                self.set_xy(x_start + sum(col_widths[:i]), y_start)
                if fill:
                    self.set_fill_color(245, 247, 250)
                    self.rect(self.get_x(), self.get_y(), col_widths[i], max_h, 'F')
                self.set_xy(x_start + sum(col_widths[:i]) + 1, y_start + 1)
                self.multi_cell(col_widths[i] - 2, 5, cell_text)
            self.set_xy(x_start, y_start + max_h)
            fill = not fill
        self.ln(4)


pdf = PDF()

# Title Page
pdf.title_page()

# Abstract
pdf.add_page()
pdf.section_title('Abstract')
pdf.body_text(
    'Artificial Intelligence (AI) projects face fundamental challenges that traditional project '
    'management methodologies (PMBOK, PRINCE2, Agile, SAFe) were not designed to address: '
    'non-deterministic outputs, data-dependent feasibility, model drift, compute cost uncertainty, '
    'and ethical risk. Existing approaches assume deterministic outcomes and known solution paths, '
    'leading to high failure rates in AI initiatives. This paper introduces the DIVE Framework '
    '(Diagnose >> Iterate >> Validate >> Evolve), a purpose-built methodology for managing '
    'AI and machine learning projects. DIVE introduces seven novel principles including Metric '
    'Contracts, parallel experimentation tracks, feasibility gates, and continuous governance as '
    'a lifecycle phase. The framework includes 14 templates and 5 governance artifacts. We present '
    'the complete methodology and discuss its differentiation from existing approaches.'
)

# 1. Introduction
pdf.section_title('1. Introduction')
pdf.body_text(
    'The Project Management Institute reports that over 70% of AI projects fail to deliver '
    'expected value [1]. Root cause analyses consistently point to the same factors: unclear '
    'success criteria, insufficient data quality, unrealistic timelines, and failure to account '
    'for model degradation post-deployment. These are not failures of execution -- they are '
    'failures of methodology.'
)
pdf.body_text(
    'Traditional project management frameworks were designed for deterministic environments. '
    'A software feature either works or it does not; requirements can be specified upfront; '
    'quality is binary. AI projects operate in fundamentally different conditions:'
)

pdf.add_table(
    ['Characteristic', 'Traditional Software', 'AI Projects'],
    [
        ['Output', 'Deterministic', 'Probabilistic'],
        ['Spec', 'Known upfront', 'Discovered through data'],
        ['Failure mode', 'Bug -> fix', 'Data/model degradation'],
        ['Estimation', 'Possible with history', 'High uncertainty'],
        ['Quality check', 'Pass/fail tests', 'Metric thresholds'],
        ['Main cost', 'Engineering hours', 'Compute + data + talent'],
    ],
    [42, 70, 78]
)

pdf.body_text('The DIVE Framework was designed from first principles to address these differences.')

# 2. The Seven Principles
pdf.section_title('2. The Seven Principles')

principles = [
    ('Principle 1: Data First, Code Second',
     'No AI project begins without a data feasibility audit. If the data does not exist, is '
     'inaccessible, or lacks signal, the project cannot succeed regardless of model sophistication.'),
    ('Principle 2: Parallel Exploration Beats Sequential Certainty',
     'AI development is research-like; the optimal approach is unknown at project start. DIVE '
     'mandates 3-5 parallel experimentation tracks with fixed compute budgets.'),
    ('Principle 3: Metric Contracts Replace Requirements Documents',
     'Success criteria are defined as measurable, signed contracts (e.g., "F1 >= 0.87, '
     'latency <= 200ms p95") before development begins. These are the sole criteria for phase exit.'),
    ('Principle 4: Fail Fast, Fail Quantitatively',
     'Pre-defined quantitative kill criteria prevent indefinite "one more iteration" cycles. '
     'A kill decision is a success -- it preserves resources.'),
    ('Principle 5: Governance Is Continuous, Not Periodic',
     'Post-deployment drift (data drift, concept drift, performance drift) means models degrade '
     'even if code does not change. Continuous monitoring and governance are a permanent lifecycle phase.'),
    ('Principle 6: Human-in-the-Loop Is a Design Constraint',
     'Three escalation tiers (Advisory, Assisted, Automated) are designed pre-deployment, with '
     'confidence thresholds and fallback routing.'),
    ('Principle 7: Compute Is a First-Class Resource',
     'GPU time, API tokens, and storage costs are tracked alongside scope, schedule, and budget. '
     'Each experiment track has a fixed compute budget.'),
]

for title, body in principles:
    pdf.sub_title(title)
    pdf.body_text(body)

# 3. The Lifecycle
pdf.section_title('3. The Lifecycle')
pdf.body_text('The DIVE lifecycle consists of four phases:')
pdf.set_font('Courier', 'B', 12)
pdf.set_text_color(26, 60, 110)
pdf.cell(0, 10, '   Diagnose  >>  Iterate  >>  Validate  >>  Evolve', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(4)

phases = [
    ('Phase 1 -- Diagnose (2-4 weeks)',
     'Problem validation, data audit, feasibility baseline, Metric Contract negotiation, '
     'ethics screening, risk registration, build/buy assessment. '
     'Exit gate: Feasibility Review (Go/No-Go/Redesign).'),
    ('Phase 2 -- Iterate (4-8 weeks)',
     '3-5 parallel experiment tracks with fixed compute budgets. Weekly comparison on a shared '
     'dashboard. Compute burn rate tracking. Mid-phase pivot allowed. '
     'Exit gate: Candidate Selection.'),
    ('Phase 3 -- Validate (2-4 weeks)',
     'Hold-out evaluation, robustness testing, bias audit, performance benchmarking, shadow '
     'deployment (optional), stakeholder sign-off. '
     'Exit gate: Validation Sign-Off.'),
    ('Phase 4 -- Evolve (ongoing)',
     'Production deployment, monitoring configuration, drift detection, feedback pipeline, '
     'quarterly governance reviews, retraining as needed. '
     'Exit gate: Decommissioning.'),
]

for title, body in phases:
    pdf.sub_title(title)
    pdf.body_text(body)

# 4. Differentiation
pdf.section_title('4. Differentiation from Existing Approaches')
pdf.add_table(
    ['Dimension', 'PMBOK', 'PRINCE2', 'Agile', 'DIVE'],
    [
        ['AI-native', 'No', 'No', 'No', 'Yes'],
        ['Data feasibility gate', 'No', 'No', 'No', 'Yes'],
        ['Parallel exploration', 'No', 'No', 'No', 'Yes'],
        ['Metric Contracts', 'No', 'No', 'No', 'Yes'],
        ['Compute as resource', 'No', 'No', 'No', 'Yes'],
        ['Continuous governance', 'No', 'No', 'No', 'Yes'],
        ['Explicit kill criteria', 'No', 'No', 'No', 'Yes'],
    ],
    [40, 30, 30, 30, 50]
)

# 5. Conclusion
pdf.section_title('5. Conclusion')
pdf.body_text(
    'The DIVE Framework provides a structured, AI-native approach to project management that '
    'addresses the unique challenges of data-driven, non-deterministic, continuously evolving '
    'AI systems. By replacing false certainty with measurable gates, parallel exploration, and '
    'continuous governance, DIVE aims to improve the success rate of AI initiatives across '
    'industries. The framework is vendor-agnostic, tool-agnostic, and designed to scale from '
    'small teams to enterprise AI programs.'
)

# References
pdf.section_title('References')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(30, 30, 30)
pdf.cell(5, 5, '[1]')
pdf.multi_cell(175, 5, 'Project Management Institute. "AI Project Success Rates and Root Causes." PMI White Paper, 2024.')

# Save
output_path = os.path.expandvars('%USERPROFILE%\\Downloads\\DIVE-Framework-Assets\\DIVE-White-Paper.pdf')
pdf.output(output_path)
print(f'PDF saved to: {output_path}')
