from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

width, height = A4
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
styleN.alignment = TA_LEFT
styleBH = styles["Normal"]
styleBH.alignment = TA_CENTER

username = "John Doe"
comments = [("This is a great product.loeoiehaofhou adhfouadhfuivhadsiu fvhaiodscvoidsbvioshbd vi ohbais dvhbiohdsbvoishabdvihob disbffdsifbidoashf idsf iodsf oisdufho isdfiou sdiuhfs", "JD001"), ("I wish lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem it had more features.", "JD002"), ("Excellent customer service.", "JD001")]

def coord(x, y, unit=1):
    x, y = x * unit, height -  y * unit
    return x, y

# Headers
hdescrpcion = Paragraph('''<b>UserId</b>''', styleBH)
hpartida = Paragraph('''<b>Comments</b>''', styleBH)

# Texts
descrpcion = Paragraph('vldnlnva soidhcoa cho adfhoa doufah uasihf hoapsf hpasoufh sapofu saphofu pdavhuo hpavuod', styleN)
partida = Paragraph('1', styleN)

data = [['User ID', 'Comments']]
for comment in comments:
        data.append([Paragraph(comment[1], styleN), Paragraph(comment[0], styleN)])



table = Table(data, colWidths=[2 * cm,15* cm])

table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))

c = canvas.Canvas("a.pdf", pagesize=A4)
table.wrapOn(c, width, height)
table.drawOn(c, *coord(1.8, 9.6, cm))
c.save()
