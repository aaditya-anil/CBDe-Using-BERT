import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

# Sample username and comments data
username = "John Doe"
comments = [("This is a great product.", "JD001"), ("I wish it had more features.", "JD002"), ("Excellent customer service.", "JD001")]


# Create a new PDF file
pdf_writer = PyPDF2.PdfWriter()

# Create a new canvas and set its font and size
c = canvas.Canvas("output.pdf", pagesize=letter)
c.setFont("Helvetica", 12)

# Draw the username at the top of the page
c.drawString(1 * inch, 10.5 * inch, "Username: " + username)

# Add a paragraph of Lorem Ipsum
text = "Dear Higher Authority,\nWe are submitting this report regarding the recent feedback and comments received\n from our users. Unfortunately, we have come across some disturbing and hateful comments\n directed towards one of our users, which we take very seriously. The user's name is \nmentioned at the top of this report.We have compiled a list of these hateful comments\n and included them in a table along with the user ID. We understand that this type of\n behavior is unacceptable and goes against our policies and values. We want to assure you\n that we are taking this matter very seriously, and we are determined to take \nnecessary actions against the users who posted these comments.\nWe would like to request that appropriate actions be taken against the users who posted these comments. \nWe believe that this will send a strong message to our user base that we do not \ntolerate any form of hate speech or harassment on our platform. We are committed to \nmaintaining a safe and respectful environment for all of our users.\nThank you for your attention to this matter. We are looking forward to hearing back from you soon.\nSincerely,\n"+username

textobject = c.beginText(1 * inch, 10 * inch)
textobject.setFont("Helvetica", 12)
textobject.setTextOrigin(1 * inch, 10 * inch)
textobject.setWordSpace(1)
textobject.textLines(text)
c.drawText(textobject)

# Add a table for the comments
table_data = [['User ID', 'Comments']]
for comment in comments:
    table_data.append([comment[1], comment[0]])

# Create a table object and set its style
table = Table(table_data)
table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))]))

# Set the table position and size
table.wrapOn(c, 1 * inch, 5 * inch)
table.drawOn(c, 1 * inch, 5 * inch)

# Add the disclaimer
c.drawString(1 * inch, 0.5 * inch, "This PDF report has been generated using Python code developed by CBDe.\n The information contained in this report is intended solely for informational purposes \nand should not be relied upon as legal, business, or professional advice.\n CBDe does not assume any liability or responsibility for any errors or omissions in the content of this\n report or for any actions taken in reliance on the information contained herein.")


# Save the canvas to the PDF file
c.save()

# Add the PDF file to the output
with open("output.pdf", "rb") as f:
    pdf_writer.add_page(PyPDF2.PdfReader(f).pages[0])

# Write the output to a new file
with open("result.pdf", "wb") as f:
    pdf_writer.write(f)
