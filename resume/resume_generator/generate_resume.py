import hashlib
orig_md5 = hashlib.md5
def md5_wrapper(*args, **kwargs):
    kwargs.pop('usedforsecurity', None)
    return orig_md5(*args, **kwargs)
hashlib.md5 = md5_wrapper

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = r"c:\Users\YJ\Documents\python_scripts\kludge\YangJunSite\public\YangJunJoo_CV.pdf"

# Page layout: Letter (612 x 792 points)
# Tight margins to fit everything on exactly one page.
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Custom styles for a clean, professional, 1-page layout (Fonts scaled slightly up for premium readability)
name_style = ParagraphStyle(
    'NameStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=21,
    alignment=1, # Center
    textColor=colors.HexColor('#0f172a') # Slate-900
)

headline_title_style = ParagraphStyle(
    'HeadlineTitleStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    alignment=1, # Center
    textColor=colors.HexColor('#1e3a8a') # Blue-900
)

headline_subtitle_style = ParagraphStyle(
    'HeadlineSubtitleStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9.5,
    leading=12.5,
    alignment=1, # Center
    textColor=colors.HexColor('#475569') # Slate-600
)

contact_style = ParagraphStyle(
    'ContactStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=12,
    alignment=1, # Center
    textColor=colors.HexColor('#334155')
)

summary_style = ParagraphStyle(
    'SummaryStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#1e293b') # Slate-800
)

section_heading_style = ParagraphStyle(
    'SectionHeadingStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=colors.HexColor('#1e3a8a'), # Blue-900
    spaceBefore=0,
    spaceAfter=0
)

job_title_style = ParagraphStyle(
    'JobTitleStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#0f172a')
)

job_meta_style = ParagraphStyle(
    'JobMetaStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#475569')
)

bullet_style = ParagraphStyle(
    'BulletStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    leftIndent=12,
    firstLineIndent=-12,
    textColor=colors.HexColor('#334155') # Slate-700
)

skills_style = ParagraphStyle(
    'SkillsStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#334155')
)

pub_style = ParagraphStyle(
    'PubStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    leftIndent=12,
    firstLineIndent=-12,
    textColor=colors.HexColor('#334155')
)

edu_style = ParagraphStyle(
    'EduStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#334155')
)

story = []

# --- HEADER ---
story.append(Paragraph("Yang-Jun Joo, Ph.D.", name_style))
story.append(Spacer(1, 2))
story.append(Paragraph("Data Scientist | Quantitative Risk Assessment", headline_title_style))
story.append(Paragraph("Autonomous Vehicle Safety | Statistical & Probabilistic Modeling | Large-Scale Driving Data", headline_subtitle_style))
story.append(Spacer(1, 4))

# Clickable contacts inline - split into 2 lines for clean, ATS-friendly layout
contact_html_1 = "Orlando, FL &nbsp;|&nbsp; Open to relocation to Foster City, CA"
contact_html_2 = (
    "<a href='mailto:yangjunjoo.phd@gmail.com'><b>yangjunjoo.phd@gmail.com</b></a> &nbsp;|&nbsp; "
    "+1 (813) 455-1392 &nbsp;|&nbsp; "
    "<a href='https://linkedin.com/in/yang-jun-joo-a8012820a'><b>LinkedIn</b></a> &nbsp;|&nbsp; "
    "<a href='https://github.com/YangJunJoo'><b>GitHub</b></a> &nbsp;|&nbsp; "
    "<a href='https://scholar.google.com/citations?user=xPJpVcMAAAAJ&hl=en'><b>Google Scholar</b></a>"
)
story.append(Paragraph(contact_html_1, contact_style))
story.append(Spacer(1, 2))
story.append(Paragraph(contact_html_2, contact_style))
story.append(Spacer(1, 8))

def add_divider(title):
    p = Paragraph(title.upper(), section_heading_style)
    t = Table([[p]], colWidths=[540])
    t.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 0.75, colors.HexColor('#94a3b8')), # Slate-400 line
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t)
    story.append(Spacer(1, 5))

# --- PROFESSIONAL SUMMARY ---
summary_text = (
    "<b>Professional Summary:</b> Quantitative risk assessment data scientist with 8+ years of experience, "
    "including 3+ years of post-Ph.D. experience, developing probabilistic safety metrics, "
    "uncertainty-aware models, and automated safety risk-assessment tools for autonomous vehicle systems. Author/co-author "
    "of 15 peer-reviewed papers, with hands-on experience in Python, SQL, multi-terabyte driving data, and human behavior analysis."
)
story.append(Paragraph(summary_text, summary_style))
story.append(Spacer(1, 8))

# --- TECHNICAL SKILLS ---
add_divider("Technical Skills")
skills_data = [
    [
        Paragraph("<b>Programming & Data:</b>", job_title_style),
        Paragraph("Python, SQL, R, scikit-learn, PyTorch, Git, Linux, ETL pipelines.", skills_style)
    ],
    [
        Paragraph("<b>Risk & Statistics:</b>", job_title_style),
        Paragraph("Probabilistic modeling, Bayesian networks, reliability analysis, surrogate safety measures, causal inference, uncertainty quantification, conformal prediction.", skills_style)
    ],
    [
        Paragraph("<b>Safety & Mobility:</b>", job_title_style),
        Paragraph("AV risk assessment, safety-performance metrics, naturalistic driving video, connected-vehicle and trajectory data, traffic-conflict analysis, human factors.", skills_style)
    ]
]
skills_table = Table(skills_data, colWidths=[130, 410])
skills_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ('TOPPADDING', (0, 0), (-1, -1), 1),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
]))
story.append(skills_table)
story.append(Spacer(1, 8))

# --- PROFESSIONAL EXPERIENCE ---
add_divider("Professional Experience")

def add_experience(role, company, period, bullets):
    header_data = [
        Paragraph(f"<b>{role}</b>", job_title_style),
        Paragraph(f"<b>{company}</b>", job_meta_style),
        Paragraph(period, job_meta_style)
    ]
    t = Table([header_data], colWidths=[290, 145, 105])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    story.append(t)
    story.append(Spacer(1, 2))
    for bullet in bullets:
        story.append(Paragraph(f"&bull; {bullet}", bullet_style))
    story.append(Spacer(1, 6))

add_experience(
    "Postdoctoral Scholar (Quantitative Safety Analytics)",
    "University of Central Florida",
    "Mar 2024 – Present",
    [
        "Led cross-functional safety analytics workstreams for the Florida Department of Transportation, defining and standardizing safety-performance metrics using connected-vehicle and naturalistic driving data.",
        "Secured KRW 73.5 million in competitive funding as principal investigator and used causal forests to quantify heterogeneous effects of vehicle automation on risk perception across 926 participants and 1,325 near-miss clips.",
        "Built and automated Python and SQL ETL and analytics pipelines for multi-terabyte datasets from 1,000+ intersections, standardizing risk-metric generation and reporting.",
        "Developed uncertainty-aware evaluation for autonomous-driving vision-language models (VLM) using conformal prediction, identifying context-specific calibration failures in safety-critical driving QA."
    ]
)

add_experience(
    "Postdoctoral Researcher (AV Safety Systems)",
    "Seoul National University",
    "Mar 2023 – Feb 2024",
    [
        "Led research on real-time infrastructure-to-vehicle (V2I) safety information systems for the Korean National Police Agency, defining safety-critical scenarios and operational safety criteria."
    ]
)

add_experience(
    "Graduate Research Assistant",
    "Seoul National University",
    "Mar 2018 – Feb 2023",
    [
        "Developed generalized quantitative risk assessment methods for autonomous vehicle lane changes and collision avoidance using field theory, Bayesian networks, reliability analysis, and surrogate safety measures.",
        "Secured and led a KRW 96.1 million Global Ph.D. Fellowship, developing and validating probabilistic AV risk-assessment methods for lane changes, collision avoidance, and driver-level crash risk."
    ]
)

# --- SELECTED PUBLICATIONS ---
add_divider("Selected Publications")
story.append(Paragraph(
    "&bull; Joo et al. (2023), \"A Generalized Driving Risk Assessment Method for Autonomous Vehicles Using Field Theory,\" <i>Analytic Methods in Accident Research</i>.",
    pub_style
))
story.append(Paragraph(
    "&bull; Joo et al. (2022), \"A Data-Driven Bayesian Network for Probabilistic Crash Risk Assessment,\" <i>Accident Analysis & Prevention</i>.",
    pub_style
))
story.append(Paragraph(
    "&bull; Joo et al. (2026), \"Context-Aware Conformal Prediction for VLM-Based Driving Scene QA,\" <i>ICML Workshop EMM-QA</i>.",
    pub_style
))
story.append(Spacer(1, 10))

# --- EDUCATION ---
add_divider("Education")
story.append(Paragraph("<b>Ph.D., Civil & Environmental Engineering (Transportation)</b>, Seoul National University, 2023", edu_style))
story.append(Spacer(1, 3))
story.append(Paragraph("<b>B.S., Civil & Environmental Engineering</b>, Seoul National University, 2018", edu_style))

# Build PDF
doc.build(story)
print("PDF Generated successfully at:", pdf_path)
