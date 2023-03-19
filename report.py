from fpdf import FPDF
import os
import shutil


class PDF(FPDF):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add a Unicode font that supports the characters you need
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)

    def cover_page(self, logo_path, title, ageStr, serialNo, dateCeck):
        # Add the logo to the upper middle of the page
        x_center = self.w / 2.0
        y_center = self.h / 4.0
        self.image(logo_path, x_center - 50, y_center - 50, 100)

        # Add the next text to the right side below the logo:

        # title
        self.set_font('DejaVu', '', 14)
        self.set_xy(x_center + 60, y_center + 30)
        self.cell(0, 10, title, align='R', border='B')

        # age
        self.set_xy(x_center + 60, y_center + 50)
        self.cell(0, 10, ageStr, align='R')

        # serial
        self.set_xy(x_center + 60, y_center + 60)
        self.cell(0, 10, serialNo, align='R')

        # date
        self.set_xy(x_center + 60, y_center + 70)
        self.cell(0, 10, dateCeck, align='R')

    def regular_page(self, info , sub_info):
        # Add the logo
        self.image('images/logo.jpg', x=10, y=10, w=50)

        # Add a Unicode font that supports the characters you need
        x_center = self.w / 2.0
        y_center = self.h / 4.0
        self.set_xy(x_center + 60, y_center - 30)

        # Add the title
        self.cell(0, 10, info, ln=1, align='R', border='B')

        self.set_xy(x_center + 60, y_center - 5)

        # Add the title
        self.cell(0, 10, sub_info, ln=1, align='R', border='B')


    def footer(self):
        # Add the page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')



# Create a new PDF object
pdf = PDF()

# Set the document properties
pdf.set_author('Dvir Borochov')
pdf.set_creator('FPDF')
pdf.set_title('Doc')

# Add the cover page
pdf.add_page()
title_heading = "דו\"ח הערכה עבור "[::-1]
ageStr = "גיל הילד: "[::-1]
serialNo = "מספר סידורי: "[::-1]
dataCeck = "תאריך אבחון: "[::-1]

pdf.cover_page('images/logo.jpg', title_heading, ageStr, serialNo, dataCeck)

# Add the cover page
pdf.add_page()
info = "הסבר על הדו\"ח:  "[::-1]
sub_info = "איך לקרוא את הדו\"ח: "[::-1]


pdf.regular_page(info, sub_info)

# Add the footer
pdf.footer()

# Save the PDF file
pdf.output('document.pdf', 'F')

# Set the paths to the source executable file and destination folder
src_path = r"C:\Users\dvir.bo\PycharmProjects\DIAGNOS-IT\document.pdf"
dest_folder = r"C:\Users\dvir.bo\PycharmProjects\DIAGNOS-IT\src"

# Use shutil to copy the file to the destination folder
shutil.move(src_path, dest_folder)