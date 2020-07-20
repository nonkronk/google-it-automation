#! /usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate

report = SimpleDocTemplate("Processed.pdf")

from reportlab.platypus import Paragraph, Spacer, Table, Image
from datetime import date
import run
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
flowables = []
paragraph_t = Paragraph("Processed Update on "+ str(date.today), styles["h1"])
flowables.append(paragraph_t)
fruits = run.dict_list
#print(fruits)
all_txt = ''
for dct in fruits:
    text = '\nname: '+dct['name']+'\nweight: '+str(dct['weight'])+' lbs'
    paragraph_f = Paragraph(text, styles['BodyText'])
    flowables.append(paragraph_f)
    all_text += text

report.build(flowables)