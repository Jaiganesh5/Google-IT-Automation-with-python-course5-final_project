#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, body):

  """ generates the pdf using reportlab module"""
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title,styles["h1"])
  report_body = Paragraph(body,styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_body])
