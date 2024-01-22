#generating PDF report from the arguments passed in function

#! /usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)    
    report_title = Paragraph(title, styles["h1"])
    report_data = Paragraph(paragraph, styles["BodyText"])
    blank_line = Spacer(1,20)
    report.build([report_title, blank_line, report_data])