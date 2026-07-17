import hashlib

orig_md5 = hashlib.md5


def md5_wrapper(*args, **kwargs):
    kwargs.pop("usedforsecurity", None)
    return orig_md5(*args, **kwargs)


hashlib.md5 = md5_wrapper

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


pdf_path = (
    r"C:\Users\YJ\Documents\python_scripts\kludge\YangJunSite\resume"
    r"\backup\Waymo\Data Scientist\Yang-Jun_Joo_Waymo_Data_Scientist_Resume.pdf"
)

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36,
)

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "NameStyle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=18,
    leading=21,
    alignment=1,
    textColor=colors.HexColor("#0f172a"),
)

headline_style = ParagraphStyle(
    "HeadlineStyle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=14,
    alignment=1,
    textColor=colors.HexColor("#1d4ed8"),
)

subtitle_style = ParagraphStyle(
    "SubtitleStyle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.5,
    leading=12.5,
    alignment=1,
    textColor=colors.HexColor("#475569"),
)

contact_style = ParagraphStyle(
    "ContactStyle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=11.5,
    alignment=1,
    textColor=colors.HexColor("#334155"),
)

summary_style = ParagraphStyle(
    "SummaryStyle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10,
    leading=13.5,
    textColor=colors.HexColor("#1e293b"),
)

section_style = ParagraphStyle(
    "SectionStyle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=14,
    textColor=colors.HexColor("#1d4ed8"),
)

meta_style = ParagraphStyle(
    "MetaStyle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.8,
    leading=12.8,
    textColor=colors.HexColor("#475569"),
)

job_style = ParagraphStyle(
    "JobStyle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10,
    leading=13,
    textColor=colors.HexColor("#0f172a"),
)

body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10,
    leading=13.2,
    textColor=colors.HexColor("#334155"),
)

bullet_style = ParagraphStyle(
    "BulletStyle",
    parent=body_style,
    leftIndent=9,
    firstLineIndent=-9,
    spaceAfter=0.6,
)

story = []


def section(title):
    table = Table([[Paragraph(title.upper(), section_style)]], colWidths=[540])
    table.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.65, colors.HexColor("#94a3b8")),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 3.5))


def bullet(text):
    story.append(Paragraph(f"- {text}", bullet_style))


def experience(role, company, dates, bullets):
    row = [
        Paragraph(role, job_style),
        Paragraph(company, meta_style),
        Paragraph(dates, meta_style),
    ]
    table = Table([row], colWidths=[280, 160, 100])
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    story.append(table)
    for item in bullets:
        bullet(item)
    story.append(Spacer(1, 3.5))


story.append(Paragraph("Yang-Jun Joo, Ph.D.", name_style))
story.append(Spacer(1, 1))
story.append(
    Paragraph(
        "Data Scientist | AV Performance Evaluation & Statistical Modeling",
        headline_style,
    )
)
story.append(
    Paragraph(
        "Autonomous Vehicle Safety | Measurement Frameworks | Large-Scale Mobility Data",
        subtitle_style,
    )
)
story.append(Spacer(1, 3))
story.append(
    Paragraph(
        "Orlando, FL | Open to relocation to Mountain View / San Francisco",
        contact_style,
    )
)
story.append(
    Paragraph(
        "<a href='mailto:yangjunjoo.phd@gmail.com'><b>yangjunjoo.phd@gmail.com</b></a> | "
        "+1 (813) 455-1392 | "
        "<a href='https://linkedin.com/in/yang-jun-joo-a8012820a'><b>LinkedIn</b></a> | "
        "<a href='https://github.com/YangJunJoo'><b>GitHub</b></a> | "
        "<a href='https://scholar.google.com/citations?user=xPJpVcMAAAAJ&hl=en'><b>Google Scholar</b></a>",
        contact_style,
    )
)
story.append(Spacer(1, 6))

summary = (
    "<b>Professional Summary:</b> Applied data scientist with 8+ years of quantitative research and "
    "applied data science experience, including 3+ years post-Ph.D. Developed AV performance evaluation "
    "and measurement frameworks, new safety metrics, and Python/SQL analytics pipelines for large-scale "
    "on-road and mobility data. Expertise in rare-event rate estimation, combining real and synthetic data, "
    "experimental design, anomaly investigation, and uncertainty-aware evaluation of large-scale ML models."
)
story.append(Paragraph(summary, summary_style))
story.append(Spacer(1, 6))

section("Technical Skills")
skills = [
    [
        Paragraph("<b>Programming & Data:</b>", job_style),
        Paragraph(
            "Python, SQL, R, scikit-learn, PyTorch, deep learning, Git, Linux, ETL pipelines, data visualization.",
            body_style,
        ),
    ],
    [
        Paragraph("<b>Statistics & ML Evaluation:</b>", job_style),
        Paragraph(
            "Probabilistic modeling, Bayesian networks, reliability analysis, causal inference, "
            "experimental design, rare-event rate estimation, real and synthetic data integration, "
            "uncertainty quantification, model calibration.",
            body_style,
        ),
    ],
    [
        Paragraph("<b>AV & Mobility Analytics:</b>", job_style),
        Paragraph(
            "AV performance evaluation, traffic modeling, safety evaluation and prediction, trajectory prediction, "
            "on-road/naturalistic driving, connected-vehicle event data.",
            body_style,
        ),
    ],
]
skills_table = Table(skills, colWidths=[158, 382])
skills_table.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0.3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0.3),
        ]
    )
)
story.append(skills_table)
story.append(Spacer(1, 6))

section("Professional Experience")
experience(
    "Postdoctoral Scholar, Quantitative Safety Analytics",
    "University of Central Florida",
    "Mar 2024-Present",
    [
        "Collaborated across agency and technical teams to develop evaluation frameworks and standardized safety-performance metrics using connected-vehicle, naturalistic-driving, and high-resolution event data.",
        "Built Python/SQL ETL and analytics pipelines for multi-terabyte data from 1,000+ intersections, enabling standardized metric generation, trend interpretation, and anomaly investigation for operational decisions.",
        "Designed and analyzed near-miss risk-judgment experiments across 926 participants and 1,325 crash/near-miss clips, applying causal forests to quantify effects of vehicle automation.",
        "Developed synthetic data generation methods for class-imbalanced crash severity estimation, supporting safety prediction under sparse-event conditions.",
        "Evaluated large-scale driving-scene VLMs with conformal prediction, identifying context-specific calibration failures for safety-critical model evaluation.",
    ],
)

experience(
    "Postdoctoral Researcher (AV Safety Systems)",
    "Seoul National University",
    "Mar 2023-Feb 2024",
    [
        "Led research on real-time infrastructure-to-vehicle (V2I) safety information systems for the Korean National Police Agency, defining safety-critical scenarios and operational safety criteria.",
    ],
)

experience(
    "Graduate Research Assistant",
    "Seoul National University",
    "Mar 2018-Feb 2023",
    [
        "Developed new risk-field and reliability-based metrics for AV lane-change and collision-avoidance evaluation using trajectory prediction, Bayesian networks, and surrogate safety measures.",
    ],
)
section("Selected Publications")
bullet(
    "Kim, Kim, and Joo* (2026), \"Generative AI for Class Imbalance in Crash Severity Estimation with Mixed Data Types,\" Transportation Research Record."
)
bullet(
    "Joo et al. (2023), \"A Generalized Driving Risk Assessment Method for Autonomous Vehicles Using Field Theory,\" Analytic Methods in Accident Research."
)
bullet(
    "Joo et al. (2021), \"Reliability-Based Assessment of Potential Risk for Lane-Changing Maneuvers,\" Transportation Research Record."
)
story.append(Spacer(1, 4))

section("Education")
story.append(
    Paragraph(
        "<b>Ph.D., Civil & Environmental Engineering (Transportation)</b>, Seoul National University, 2023",
        body_style,
    )
)
story.append(
    Paragraph(
        "<b>B.S., Civil & Environmental Engineering</b>, Seoul National University, 2018",
        body_style,
    )
)

doc.build(story)
print(f"PDF generated: {pdf_path}")
