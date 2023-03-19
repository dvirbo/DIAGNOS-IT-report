from fpdf import FPDF


# page 1 params:
title = "DIAGNOS-IT"
year = "2022"
month = "Juin 5"
child_name = "name 1"
authored = "name 2"
logo_path = 'images/logo_DI.png'
logo_name = "Dvir"
path = 'DejaVuSansCondensed.ttf'  # notebooks/DejaVuSansCondensed.ttf

# page 2 params:
title_heading = "הסבר על הדוח"[::-1]
sub_title = "מטרת האבחון היא לבדוק היכן נמצא הילד במדדים השונים יחסית לבני גילו ויחסית לבני גילו מאותה" \
            "הכיתה/גן."[::-1]

paragraph_1 = ""
paragraph_2 = paragraph_3 = paragraph_4 = paragraph_1

# pdf destination
pdf_dest = 'Report3.pdf'


def pdf_generator(title, year, month, child_name, authored, logo_path, logo_name, title_heading, sub_title, paragraph_1,
                  paragraph_2, paragraph_3, paragraph_4):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # ======================= first page ==============================
    # Set the font and font size
    pdf.set_font('Arial', size=12)

    # Get the width of the text
    text_width = pdf.get_string_width("Hello, world!")

    # Calculate the x-coordinate for centering the text
    x = (pdf.w - text_width) / 2

    # Set the x-coordinate and y-coordinate for the cell
    y = pdf.h / 2
    pdf.set_xy(x, y)

    # Add the text to the cell
    pdf.cell(text_width, 0, "Hello, world!", align='C')

    # add year + line
    pdf.set_xy(20, 55)
    # year = "2022"
    pdf.cell(20, 10, txt=year, ln=1, align='L')
    pdf.line(21, 65, 50, 65)

    # add month + line
    pdf.set_font("arial", "", 13.0)
    pdf.set_text_color(0, 0, 150)
    pdf.set_xy(20, 230)
    # month = "Juin 5"
    pdf.cell(20, 10, txt=month, ln=1, align='L')
    pdf.line(21, 240, 50, 240)

    # add child name + authored by
    pdf.set_font("arial", "B", 10.0)
    pdf.set_text_color(0, 0, 150)
    pdf.set_xy(20, 243)
    # child_name = "name 1"
    pdf.cell(20, 10, txt="Child Name: " + child_name, ln=1, align='L')
    pdf.set_xy(20, 248)
    # authored = "name 2"
    pdf.cell(20, 10, txt="Authored by: " + authored, ln=1, align='L')

    # add logo + logo name
    # logo_path = 'logo.PNG'
    pdf.image(logo_path, x=150, y=250, w=20, h=20)

    pdf.set_font("arial", "B", 13.0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(172, 251)
    # logo_name = "FreeuuuLance"
    if ' ' in logo_name and len(logo_name) > 6:
        str_list = logo_name.rsplit(' ', 2)
        pdf.cell(20, 10, txt=str_list[0], ln=1, align='L')
        pdf.set_xy(172, 256)
        pdf.cell(20, 10, txt=str_list[1], ln=1, align='L')
    else:
        pdf.multi_cell(20, 5, txt=logo_name, align='L')

    # ======================= second page ==============================
    pdf.add_page()
    pdf.line(21, 20, 180, 20)

    # heading title
    pdf.add_font('DejaVu', '', path, uni=True)
    pdf.set_font('DejaVu', '', 16)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(85, 25)
    # title_heading = "Title Heading"
    pdf.cell(20, 10, txt=title_heading, ln=1, align='L')

    # sub title
    pdf.add_font('DejaVu', '', path, uni=True)
    pdf.set_font('DejaVu', '', 8)
    pdf.set_text_color(0, 0, 150)
    pdf.set_xy(80, 35)
    # sub_title = "Sub Title Text"
    pdf.cell(20, 10, txt=sub_title, ln=1, align='L')

    # paragraph_1  "הסבר על הדו"ח"
    hebrew_str = "שלום כולם"[::-1]
    pdf.add_font('DejaVu', '', path, uni=True)
    pdf.set_font('DejaVu', '', 16)
    pdf.set_text_color(0, 0, 130)
    pdf.set_xy(170, 55)
    pdf.multi_cell(180, 7, txt=hebrew_str, align='L')

    # paragraph_2
    pdf.set_xy(21, 75)
    pdf.multi_cell(180, 7, txt=paragraph_2, align='L')

    # add some image
   # pdf.image('images/logo_DI.png', x=52, y=95, w=100, h=20)

    # paragraph_3
    pdf.set_xy(21, 130)
    paragraph_3 = "iii"
    pdf.multi_cell(180, 7, txt=paragraph_3, align='L')

    # paragraph_4
    pdf.set_xy(21, 150)
    pdf.multi_cell(180, 7, txt=paragraph_4, align='L')

    # add plots
    pdf.image('images/race_dist.png', x=30, y=180, w=75, h=65)

    pdf.image('images/race_dist.png', x=110, y=180, w=75, h=65)

    # add page number
    pdf.set_font("arial", "B", 10.0)
    pdf.set_text_color(0, 0, 130)
    pdf.set_xy(100, 265)
    pdf.multi_cell(180, 7, txt="2", align='L')

    # ======================= third page ==============================
    pdf.add_page()
    pdf.line(21, 20, 180, 20)
    pdf.set_font("arial", "B", 10.0)
    # 1- add pdf title
    pdf.set_text_color(0, 0, 130)
    pdf.set_xy(100, 265)
    pdf.multi_cell(180, 7, txt="3", align='L')

    # Note :
    # you can add more page just add pdf.add_page()
    # if there is problem with text position try to ajust x and y position

    pdf.output(pdf_dest)


pdf_generator(title, year, month, child_name, authored, logo_path, logo_name,
              title_heading, sub_title, paragraph_1, paragraph_2, paragraph_3, paragraph_4)


