#!/usr/bin/env python3
"""Build the one-page job market paper front page PDF."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

OUT = Path(__file__).resolve().parents[2] / "jmp.pdf"
TITLE = "Fertility and Housing Costs"
AUTHOR = "Tommaso De Santo"
AFFILIATION = "New York University"
DATE = "October 2026"
LATEST_VERSION_URL = "https://tommasodesanto.github.io/jmp.pdf"
ABSTRACT_PARAGRAPHS = [
    "Housing costs are often blamed for low fertility, with proposed remedies ranging from easier mortgage credit to housing supply interventions. I study the potential for policies to raise fertility in a lifecycle model in which households choose whether and when to have children, how much space to occupy, and whether to rent or own. Children increase the need for a bigger house, buying requires a down payment, and earnings are subject to uninsurable idiosyncratic risk. I calibrate the model to the United States in 2007, estimate changes in fertility preferences to match the subsequent decline in birth rates, and treat 2023 as a point on a transition to a smaller population.",
    "First, I show that earnings risk can substantially discourage childbirth: reducing the standard deviation of earnings shocks by about a quarter raises completed fertility by 16 percent, consistent with precautionary behavior and the commitment to ongoing spending on children. I then investigate how earnings risk interacts with housing costs and financial constraints. Starting from the 2023 economy, a 10 percent expansion of housing supply raises completed fertility by about 5 percent for the cohort entering adulthood, with persistent effects for later cohorts. Removing down-payment requirements produces an increase in births of about 2 percent on impact, but has little effect on completed fertility: it mostly affects the timing of births, and encourages ownership of small homes which potentially dissuade further natality. However, the same credit expansion restricted to parents raises completed fertility by about 6 percent. The results highlight the difference between helping households buy a home and helping them sustain the cost of the space children require.",
]

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "PaperTitle", parent=styles["Title"], fontName="Times-Roman", fontSize=22,
    leading=27, textColor=colors.black, alignment=TA_CENTER, spaceAfter=17,
)
meta_style = ParagraphStyle(
    "PaperMetadata", parent=styles["Normal"], fontName="Times-Roman", fontSize=11,
    leading=15, textColor=colors.black, alignment=TA_CENTER,
)
link_style = ParagraphStyle(
    "LatestVersion", parent=styles["Normal"], fontName="Times-Roman", fontSize=10.5,
    leading=14, textColor=colors.black, alignment=TA_CENTER,
)
abstract_heading_style = ParagraphStyle(
    "AbstractHeading", parent=styles["Normal"], fontName="Times-Bold", fontSize=11.5,
    leading=15, textColor=colors.black, alignment=TA_CENTER, spaceAfter=10,
)
abstract_body_style = ParagraphStyle(
    "AbstractBody", parent=styles["BodyText"], fontName="Times-Roman", fontSize=11,
    leading=15.7, textColor=colors.black, alignment=TA_LEFT, spaceAfter=10,
    allowWidows=0, allowOrphans=0,
)

doc = SimpleDocTemplate(
    str(OUT), pagesize=letter, rightMargin=1*inch, leftMargin=1*inch,
    topMargin=1*inch, bottomMargin=1*inch, title=TITLE, author=AUTHOR,
    subject="Job Market Paper abstract",
)
story = [
    Spacer(1, 22),
    Paragraph(TITLE, title_style),
    Paragraph(f"{AUTHOR}<br/>{AFFILIATION}<br/>{DATE}", meta_style),
    Spacer(1, 13),
    Paragraph(
        f'<link href="{LATEST_VERSION_URL}" color="#155b8a"><u>Click here for the latest version</u></link>',
        link_style,
    ),
    Spacer(1, 29),
    Paragraph("Abstract", abstract_heading_style),
]
story.extend(Paragraph(paragraph, abstract_body_style) for paragraph in ABSTRACT_PARAGRAPHS)
doc.build(story)
print(OUT)
