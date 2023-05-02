import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from pypdf import PdfMerger

def firstpage():
    # Sample username and comments data
    username = "John Doe"
    comments = [("This is a great product.loeoiehaofhou adhfouadhfuivhadsiu fvhaiodscvoidsbvioshbd vi ohbais dvhbiohdsbvoishabdvihob disbffdsifbidoashf idsf iodsf oisdufho isdfiou sdiuhfs", "JD001"), ("I wish it had more features.", "JD002"), ("Excellent customer service.", "JD001")]

    # Create a new PDF file
    pdf_writer = PyPDF2.PdfWriter()

    # Create a new canvas and set its font and size
    c = canvas.Canvas("output.pdf", pagesize=letter)
    c.setFont("Helvetica", 12)

    # Draw the username at the top of the page
    c.drawString(1 * inch, 10.5 * inch, "Username: " + username)

    # Add a paragraph of text
    text = "Dear Higher Authority,\n\nWe are submitting this report regarding the recent feedback and comments received from our\n users. Unfortunately, we have come across some disturbing and hateful comments directed\n towards one of our users, which we take very seriously. The user's name is mentioned at the\n top of this report.\n\nWe have compiled a list of these hateful comments and included them in a table along with\n the user ID. We understand that this type of behavior is unacceptable and goes against our\n policies and values. We want to assure you that we are taking this matter very seriously,\n and we are determined to take necessary actions against the users who posted these \ncomments.\n\nWe would like to request that appropriate actions be taken against the users who posted\n these comments. We believe that this will send a strong message to our user base that we do\n not tolerate any form of hate speech or harassment on our platform. We are committed\n to maintaining a safe and respectful environment for all of our users.\n\nThank you for your attention to this matter. We are looking forward to hearing back from you \nsoon.\n\nSincerely,\n"+username

    textobject = c.beginText(1 * inch, 6 * inch)
    textobject.setFont("Helvetica", 12)
    textobject.setLeading(16)
    textobject.setTextOrigin(1 * inch, 10 * inch)
    textobject.setWordSpace(1)
    textobject.textLines(text)
    c.drawText(textobject)

    # Add a disclaimer at the bottom
    disclaimer_text = "This is a generated PDF from CBDe."
    c.drawString(1 * inch, 0.5 * inch, disclaimer_text)

    # Save the canvas to the PDF file
    c.save()

    # Add the PDF file to the output
    with open("output.pdf", "rb") as f:
        pdf_writer.add_page(PyPDF2.PdfReader(f).pages[0])

    # Write the output to a new file
    with open("result.pdf", "wb") as f:
        pdf_writer.write(f)

def maketable():
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
    table.drawOn(c, *coord(1.8, 20.6, cm))
    c.save()

firstpage()
maketable()

def mergepdf():
    

    pdfs = ['result.pdf', 'a.pdf']

    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("finalresult.pdf")
    merger.close()

mergepdf()