from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer, Image, Table, TableStyle
from reportlab.platypus import PageTemplate, Frame, HRFlowable, ListFlowable, ListItem
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# API CALL HERE
json_data = {"title": "Sample Title",
             "content": "Sample Content", "date_start": "October 1, 2020", "date_end": "November 21, 2023", "name": "Timmy"}  # example json

# HEADER
custom_header_style = ParagraphStyle("CustomHeader", fontSize=10, alignment=TA_LEFT,
                                     fontName="Times-Bold", leading=11, spaceBefore=5, spaceAfter=5, textColor=colors.black)

# NAME IN HEADER
custom_name_style = ParagraphStyle("CustomHeader", fontSize=10, alignment=TA_RIGHT,
                                   fontName="Times-Bold", leading=11, spaceBefore=5, spaceAfter=5, textColor=colors.black)

# TITLE OF EACH SECTION
custom_title_style = ParagraphStyle("CustomTitle", fontSize=12, alignment=TA_LEFT,
                                    fontName="Times-Bold", leading=12, spaceBefore=6, spaceAfter=6, textColor=colors.black)

# LISTS
custom_list_style = ParagraphStyle("CustomList", fontSize=10, alignment=TA_LEFT,
                                   fontName="Times-Bold", leading=12, spaceBefore=5, spaceAfter=5, textColor=colors.black)

# BULLETS
custom_thin_list_style = ParagraphStyle("CustomThinList", fontSize=10, alignment=TA_LEFT,
                                        fontName="Times-Roman", leading=12, spaceBefore=5, spaceAfter=5, textColor=colors.black)

# NORMAL TEXT
custom_text_style = ParagraphStyle("CustomText", fontSize=10, alignment=TA_LEFT,
                                   fontName="Times-Roman", leading=12, spaceBefore=5, spaceAfter=5, textColor=colors.black)
custom_signature_style = ParagraphStyle("CustomSignature", fontSize=12, alignment=TA_LEFT,
                                   fontName="Times-Roman", leading=12, spaceBefore=5, spaceAfter=5, textColor=colors.black)

custom_table_style = TableStyle([(
    'LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black), ('FONT', (0, 0), (-1, 0), "Times-Bold"), ('FONT', (0, 1), (-1, -1), "Times-Roman")])

custom_thin_table_style = TableStyle([(
    'LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black), ('FONT', (0, 0), (-1, 0), "Times-Italic"), ('FONT', (0, 1), (-1, -1), "Times-Roman")])

custom_signature_table_style = TableStyle([
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('LINEABOVE', (0, 0), (-1, -1), 0.1, colors.black), 
            ('FONT', (0, 1), (-1, 0), "Times-Roman")])


def create_header(canvas, doc):
    # REPLACE WITH JSON
    header_text = f'ADDENDUM<br />for the review period<br />{json_data["date_start"]} through {json_data["date_end"]}'
    header_style = custom_header_style
    header = Paragraph(header_text, header_style)
    header.wrap(doc.width, doc.topMargin)
    header.drawOn(canvas, doc.leftMargin + 6, doc.height + doc.topMargin + 6)

    name_text = f"Name: {json_data['name']}"  # REPLACE WITH JSON
    name_style = custom_name_style
    name = Paragraph(name_text, name_style)
    name.wrap(doc.width, doc.topMargin)
    name.drawOn(canvas, doc.rightMargin - 6, doc.height +
                doc.topMargin + name.height + name.height + 6)  # manual but works

    line = HRFlowable(width=pdf.width, color="black",
                      thickness=2.25, spaceBefore=0, spaceAfter=6)
    line.wrapOn(canvas, pdf.width, doc.topMargin)
    line.drawOn(canvas, doc.leftMargin + 6, doc.height +
                doc.topMargin)  # Adjust the position as needed


pdf = SimpleDocTemplate("output.pdf", pagesize=letter)
elements = []  # initiate the elements list
styles = getSampleStyleSheet()  # sample style sheet in case needed

# THIS IS THE PART TO START EDITING SECTIONS


def create_section_1(section_a, section_b):
    for _ in range(2):
        elements.append(Paragraph("", custom_list_style))
    elements.append(Paragraph(
        "SECTION I – Previous Applicable Academic Employment", custom_title_style))
    elements.append(Paragraph("", custom_list_style))
    section_a_table = Table(section_a, style=custom_table_style)

    section_b_table = Table(section_b, style=custom_table_style)

    sectionlist = [
        ListItem(Paragraph("UC EMPLOYMENT HISTORY", custom_list_style),
                 value=1), ListItem(section_a_table, value=0),
        ListItem(Paragraph("OTHER APPLICABLE ACADEMIC EMPLOYMENT",
                           custom_list_style), value=2), ListItem(section_b_table, value=0)
    ]

    elements.append(ListFlowable(sectionlist,
                                 bulletType='A', bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold"))
    elements.append(PageBreak())  # Insert a page break


def create_section_2(section_a, section_b, section_c, section_d, section_e, section_f, section_g, section_h):
    for _ in range(2):
        elements.append(Paragraph("", custom_list_style))
    elements.append(Paragraph(
        "SECTION II – Teaching Activity during review period", custom_title_style))
    elements.append(Paragraph("", custom_list_style))
    section_a_table = Table(section_a, style=custom_table_style)

    section_b_table = Table(section_b[0], style=custom_table_style)
    sub_b1 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_b[1]])
    sub_b2 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_b[2]])
    sub_b3 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_b[3]])

    section_c_table = Table(section_c[0], style=custom_table_style)
    sub_c1 = ListFlowable(
        [ListItem(Paragraph(item, custom_text_style), value=0) for item in section_c[1]])
    sub_c2 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_c[2]])
    sub_c3 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_c[3]])

    sub_sub_d = ListFlowable([ListItem(Paragraph("those who received their Ph.D or PharmD.", custom_thin_list_style),
                                       value=1), ListItem(Table(section_d[0][0], style=custom_thin_table_style), value=0),
                              ListItem(Paragraph("those who advanced their candidacy", custom_thin_list_style),
                                       value=2), ListItem(Table(section_d[0][1], style=custom_thin_table_style), value=0),
                              ListItem(Paragraph("pre-disseration committees", custom_thin_list_style),
                                       value=3), ListItem(Table(section_d[0][2], style=custom_thin_table_style), value=0),
                              ListItem(Paragraph("other research supervision", custom_thin_list_style),
                                       value=4), ListItem(Table(section_d[0][3], style=custom_thin_table_style), value=0)], bulletType='a', bulletFormat='(%s)', bulletFontSize=10, bulletFontName="Times-Roman")
    
    sub_d = ListFlowable(
        [ListItem(Paragraph("(indicate dates, and whether as chair, co-chair, or committee member)", custom_list_style),
                  value=1), ListItem(sub_sub_d, value=0),
         ListItem(Paragraph("<b>Master’s Thesis Students Supervised</b> (indicate dates, and whether as chair, co-chair, or committee member)", custom_thin_list_style),
                  value=2), ListItem(Table(section_d[1], style=custom_thin_table_style), value=0),
         ListItem(Paragraph("Postdoctoral Scholars Supervised", custom_list_style),
                  value=3), ListItem(Table(section_d[2], style=custom_thin_table_style), value=0),
         ListItem(Paragraph("Undergraduate Student Research Supervision – UROP, honors courses, 199's or equivalents", custom_list_style),
                  value=4), ListItem(Table(section_d[3], style=custom_thin_table_style), value=0),
         ListItem(Paragraph("Other Research or Teaching Supervision", custom_list_style),
                  value=5), ListItem(Table(section_d[4], style=custom_thin_table_style), value=0)], bulletType='1', bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold")

    section_e_table = Table(section_e, style=custom_thin_table_style)
    section_f_table = Table(section_f, style=custom_thin_table_style)
    section_g_table = Table(section_g, style=custom_thin_table_style)
    section_h_table = Table(section_h, style=custom_thin_table_style)

    sectionlist = [
        ListItem(Paragraph("COURSES TAUGHT AT UCI", custom_list_style),
                 value=1), ListItem(section_a_table, value=0),
        ListItem(Paragraph("HEALTHCARE PROFESSIONAL STUDENTS TEACHING",
                 custom_list_style), value=2), ListItem(section_b_table, value=0),
        ListItem(Paragraph("<b>Ward Rounds</b>", custom_text_style), value=0), ListItem(sub_b1, value=0), ListItem(Paragraph("<b>Clinical Teaching</b>",
                                                                                                                             custom_text_style), value=0), ListItem(sub_b2, value=0), ListItem(Paragraph("<b>Lectures</b>", custom_text_style), value=0), ListItem(sub_b3, value=0),

        ListItem(Paragraph("GRADUATE TEACHING", custom_list_style),
                 value=3), ListItem(section_c_table, value=0),
        ListItem(Paragraph("<b>Ward Rounds</b>", custom_text_style), value=0), ListItem(sub_c1, value=0), ListItem(Paragraph("<b>Clinical Teaching</b>",
                                                                                                                             custom_text_style), value=0), ListItem(sub_c2, value=0), ListItem(Paragraph("<b>Lectures</b>", custom_text_style), value=0), ListItem(sub_c3, value=0),

        ListItem(Paragraph("ADDITIONAL ITEMS THAT RELATE TO YOUR TEACHING",
                           custom_list_style), value=4), ListItem(sub_d, value=0),
        ListItem(Paragraph("TEACHING AWARDS AND PEDGOGICAL ACTIVITIES", custom_list_style),
                 value=5), ListItem(section_e_table, value=0),
        ListItem(Paragraph("TEACHING INNOVATIONS AND CURRICULUM DEVELOPMENT", custom_list_style),
                 value=6), ListItem(section_f_table, value=0),
        ListItem(Paragraph("PROFESSIONAL DEVELOPMENT ACTIVITIES RELATED TO TEACHING", custom_list_style),
                 value=7), ListItem(section_g_table, value=0),
        ListItem(Paragraph("DIVERSITY ACTIVITIES RELATED TO TEACHING", custom_list_style),
                 value=8), ListItem(section_h_table, value=0),
    ]

    elements.append(ListFlowable(sectionlist,
                                 bulletType='A', bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold"))
    elements.append(PageBreak())  # Insert a page break


def create_section_3(t1, t2, t3, t4, t5, t6):
    for _ in range(2):
        elements.append(Paragraph("", custom_list_style))
    elements.append(Paragraph(
        "SECTION III – Research and Creative Activity during review period", custom_title_style))
    elements.append(Paragraph("", custom_list_style))
    table1 = Table(t1, style=custom_table_style)
    table2 = Table(t2, style=custom_table_style)
    table3 = Table(t3, style=custom_table_style)
    table4 = Table(t4, style=custom_thin_table_style)
    table5 = Table(t5, style=custom_thin_table_style)
    table6 = Table(t6, style=custom_table_style)

    sectionlist = [
        # Section A
        ListItem(Paragraph(
            "PUBLICATIONS AND CREATIVE ACTIVITY NOT CREDITED IN A PRIOR REVIEW", custom_list_style), value=1),
        ListItem(Paragraph("INTELLECTUAL CONTRIBUTIONS",
                 custom_list_style), value=0),
        ListItem(table1, value=0),
        ListItem(Paragraph(
            "ARTISTIC AND PROFESSIONAL PERFORMANCES AND EXHIBITS", custom_list_style), value=0),
        ListItem(table2, value=0),

        # Section B
        ListItem(Paragraph("PUBLICATIONS AND CREATIVE ACTIVITY PREVIOUSLY SUBMITTED IN A PRIOR REVIEW(do not list any work already credited for the last promotion or advancement (Professor VI, A/S)", custom_list_style), value=2),
        ListItem(Paragraph("INTELLECTUAL CONTRIBUTIONS",
                 custom_list_style), value=0),
        ListItem(table1, value=0),
        ListItem(Paragraph(
            "ARTISTIC AND PROFESSIONAL PERFORMANCES AND EXHIBITS", custom_list_style), value=0),
        ListItem(table2, value=0),

        # Section C
        ListItem(Paragraph("COMPLETED PARTS OF LARGER WORKS",
                 custom_list_style), value=3),
        ListItem(table3, value=0),

        # Section D
        ListItem(Paragraph(
            "PROFESSIONAL ONLINE & SYSTEM RESOURCES PRODUCED/MAINTAINED", custom_list_style), value=4),
        ListItem(table4, value=0),

        # Section E
        ListItem(Paragraph(
            "INTELLECTUAL PROPERTY – PATENTS, COPYRIGHTS, ETC.", custom_list_style), value=5),
        ListItem(table5, value=0),

        # Section F
        ListItem(Paragraph("CONTRACTS, GRANTS, FELLOWSHIPS",
                 custom_list_style), value=6),
        ListItem(table6, value=0),

        # Section G
        ListItem(Paragraph("ALLOCATION OF OTHER NON-FINANCIAL RESOURCES",
                 custom_list_style), value=7),
        ListItem(table6, value=0),

        # Section H
        ListItem(Paragraph(
            "PROFESSIONAL DEVELOPMENT ACTIVITIES RELATED TO RESEARCH/CREATIVE ACTIVITIES", custom_list_style), value=8),
        ListItem(table5, value=0),

        # Section I
        ListItem(Paragraph(
            "DIVERSITY ACTIVITIES RELATED TO RESEARCH/CREATIVE ACTIVITIES", custom_list_style), value=9),
        ListItem(table5, value=0),
    ]

    elements.append(ListFlowable(sectionlist, bulletType='A',
                    bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold"))
    elements.append(PageBreak())  # Insert a page break


def create_section_4(section_a, section_b, section_c, section_d, section_e, section_f):
    for _ in range(2):
        elements.append(Paragraph("", custom_list_style))
    elements.append(Paragraph(
        "SECTION IV – Professional Recognition and Activity during review period", custom_title_style))
    elements.append(Paragraph("", custom_list_style))
    section_a_table = Table(section_a, style=custom_thin_table_style)
    section_b_table = Table(section_b, style=custom_thin_table_style)
    section_e_table = Table(section_e, style=custom_thin_table_style)
    section_f_table = Table(section_f, style=custom_thin_table_style)

    sectionlist = [
        ListItem(Paragraph("HONORS AND AWARDS", custom_list_style),
                 value=1), ListItem(section_a_table, value=0),
        ListItem(Paragraph("MEMBERSHIPS", custom_list_style),
                 value=2), ListItem(section_b_table, value=0),
        ListItem(Paragraph("PROFESSIONAL ACTIVITY", custom_list_style),
                 value=3),
        ListItem(Paragraph("Invited presentations at educational, governmental institutions (or similar organizations)", custom_list_style),
                 value=0),
        ListItem(Table(section_c[0], style=custom_thin_table_style), value=0),
        ListItem(Paragraph("Invited presentations at professional meetings", custom_list_style),
                 value=0),
        ListItem(Table(section_c[1], style=custom_thin_table_style), value=0),
        ListItem(Paragraph("Accepted presentations at educational, governmental institutions (or similar organizations)", custom_list_style),
                 value=0),
        ListItem(Table(section_c[2], style=custom_thin_table_style), value=0),
        ListItem(Paragraph("Accepted presentations at professional meetings", custom_list_style),
                 value=0),
        ListItem(Table(section_c[3], style=custom_thin_table_style), value=0),
        ListItem(Paragraph("Other presentations at professional meetings", custom_list_style),
                 value=0),
        ListItem(Table(section_c[4], style=custom_thin_table_style), value=0),
        ListItem(Paragraph("Media Appearances and Interviews", custom_list_style),
                 value=0),
        ListItem(Table(section_c[5], style=custom_thin_table_style), value=0),
        ListItem(Paragraph("Professional articles in this period about you or published reviews of your work", custom_list_style),
                 value=0),
        ListItem(Table(section_c[6], style=custom_thin_table_style), value=0),
        ListItem(Paragraph("PROFESSIONAL AND PUBLIC SERVICE", custom_list_style),
                 value=4),
        ListItem(Table(section_d[0], style=custom_thin_table_style), value=0),
        ListItem(Table(section_d[1], style=custom_thin_table_style), value=0),
        ListItem(Table(section_d[2], style=custom_thin_table_style), value=0),
        ListItem(Table(section_d[3], style=custom_thin_table_style), value=0),
        ListItem(Table(section_d[4], style=custom_thin_table_style), value=0),
        ListItem(Table(section_d[5], style=custom_thin_table_style), value=0),
        ListItem(Table(section_d[6], style=custom_thin_table_style), value=0),
        ListItem(Paragraph("PROFESSIONAL DEVELOPMENT ACTIVITIES RELATED TO PROFESSIONAL AND PUBLIC SERVICE", custom_list_style),
                 value=5), ListItem(section_e_table, value=0),
        ListItem(Paragraph("DIVERSITY ACTIVITIES RELATED TO PROFESSIONAL AND PUBLIC SERVICE", custom_list_style),
                 value=6), ListItem(section_f_table, value=0),
    ]

    elements.append(ListFlowable(sectionlist,
                                 bulletType='A', bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold"))
    elements.append(PageBreak())  # Insert a page break

def create_section_5(t):
    for _ in range(2): elements.append(Paragraph("", custom_list_style))
    elements.append(Paragraph("SECTION V – University & Systemwide Service during review period", custom_title_style))
    elements.append(Paragraph("", custom_list_style))
    table = Table(t, style=custom_thin_table_style)

    sectionlist = [
        # Section A
        ListItem(Paragraph("<b>UNIVERSITY/SYSTEMWIDE</b> - Academic Senate, Administrative Service; Senate Assembly; MRU, UCOP", custom_text_style), value=1),
        ListItem(table, value=0),
 
        # Section B
        ListItem(Paragraph("<b>CAMPUS</b> - Academic Senate and Administrative Service:", custom_text_style), value=2),
        ListItem(table, value=0),

        # Section C
        ListItem(Paragraph("SCHOOL", custom_list_style), value=3),
        ListItem(table, value=0),

        # Section D
        ListItem(Paragraph("<b>DEPARTMENT</b> (other than listings in Section I)", custom_text_style), value=4),
        ListItem(table, value=0),

        # Section E
        ListItem(Paragraph("PROFESSIONAL DEVELOPMENT ACTIVITIES RELATED TO UNIVERSITY/SYSTEMWIDE SERVICE", custom_list_style), value=5),
        ListItem(table, value=0),

        # Section F
        ListItem(Paragraph("DIVERSITY ACTIVITIES RELATED TO UNIVERSITY/SYSTEMWIDE SERVICE", custom_list_style), value=6),
        ListItem(table, value=0)
    ]

    elements.append(ListFlowable(sectionlist, bulletType='A',
                    bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold"))

###
# Custom left spacing n times. 
# NOTE: The tmp must be None when called.
# ###
def _left_space(input: ListFlowable, n: int, tmp: ListFlowable = None): 
    if n == 0 and tmp == None: return input
    if n == 0: return tmp
    if tmp == None:
        tmp = ListFlowable([ListItem(input,value=0)])
    return _left_space(input, n-1, ListFlowable([ListItem(tmp,value=0)]))
    
def create_signature(s):
    for _ in range(13): elements.append(Paragraph("", custom_list_style))
    elements.append(Paragraph("I certify that the information on this form is correct:", custom_signature_style))
    for _ in range(9): elements.append(Paragraph("", custom_list_style))
    sig_field = ListFlowable([ListItem(Table(s, style=custom_signature_table_style), value=0)])
    elements.append(_left_space(sig_field, 10))

# def test_section(section_c):
#     for _ in range(2):
#         elements.append(Paragraph("", custom_list_style))
#     elements.append(Paragraph(
#         "SECTION IV – Professional Recognition and Activity during review period", custom_title_style))
#     elements.append(Paragraph("", custom_list_style))
#     section_a_table = Table(section_a, style=custom_table_style)
#     section_b_table = Table(section_b, style=custom_table_style)

#     sectionlist = [
#         ListItem(Paragraph("HONORS AND AWARDS", custom_list_style),
#                  value=1), ListItem(section_a_table, value=0),
#         ListItem(Paragraph("MEMBERSHIPS", custom_list_style),
#                  value=2), ListItem(section_b_table, value=0),
#         ListItem(Paragraph("PROFESSIONAL ACTIVITY", custom_list_style),
#                  value=3),
#         ListItem(Table(section_c[0], style=custom_thin_table_style), value=0),
#         ListItem(Table(section_c[1], style=custom_thin_table_style), value=0),
#         ListItem(Table(section_c[2], style=custom_thin_table_style), value=0),
#         ListItem(Table(section_c[3], style=custom_thin_table_style), value=0),
#         ListItem(Table(section_c[4], style=custom_thin_table_style), value=0),
#         ListItem(Table(section_c[5], style=custom_thin_table_style), value=0),
#         ListItem(Table(section_c[6], style=custom_thin_table_style), value=0),

#     ]

#     elements.append(ListFlowable(sectionlist,
#                                  bulletType='A', bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold"))
#     elements.append(PageBreak())  # Insert a page break


# TABLES OF DATA FULL OF FILLER FOR NOW AND SOME ARE SUPER COMPLEX GOOD LOOK LOL
section_1 = [[['Period                  ', 'Title & Rank', 'Step', 'Time', 'Department                                                 '],  # section A
              ['2019-2021', 'Assistant Professor', 'III OS', '100%', 'Material Science & Engineering']],
             [['Period                   ', 'Position/Description                                                                                                   '],  # section B
              ['2020-2023', 'TEEHEE all i did was goof around a shit fr but uh']]]

section_2 = [[['Qrtr/Year    ', 'Course #    ', 'Title                    ', 'Enrollment        ', '# Instructors        ', '% Taught'],
              ['Eh', 'numbero', 'titles', 'enrolldeeznuts', 'dos', 'none']],  # section A

             [[['Description                                                    ', '# of Students    ', 'Date/Date Span      ', '# Hours/Days'],
               ['swagger', 'yagger', 'tomorrow', 'infinity']],
              ['Ward rounds bruh', 'IDK MAN'],
              ['Clinical Teachings?', 'What the hell!?'],
              ['Lectures?', 'Yeaman']],  # section B

             [[['Description                                                    ', '# of Students    ', 'Date/Date Span      ', '# Hours/Days'],
               ['yappington city', '200', 'do', 'da']],
              ['Ward AHAH bruh'],
              ['Clinical PLACE?'],
              ['Lectures? BRUH']],  # section C

             [[[['Year(s)        ', 'Student Name                            ', 'Role                    ', 'Department                        '],
                ['2020', 'chaddington', 'smoker', 'swag city']],
                 [['Year(s)        ', 'Student Name                            ', 'Role                    ', 'Department                        '],
                  ['2020', 'chaddington', 'smoker', 'swag city']],
                 [['Year(s)        ', 'Student Name                            ', 'Role                    ', 'Department                        '],
                  ['2020', 'chaddington', 'smoker', 'swag city']],
                 [['Year(s)        ', 'Student Name                            ', 'Role                    ', 'Department                        '],
                  ['2020', 'chaddington', 'smoker', 'swag city']]],

              [['Year(s)        ', 'Student Name                                    ', 'Role                    ', 'Department                        '],
                 ['2020', 'chaddington', 'smoker', 'swag city']],
              [['Year(s)        ', 'Student Name                                    ', 'Role                    ', 'Department                        '],
                 ['2020', 'chaddington', 'smoker', 'swag city']],
              [['Year(s)        ', 'Student Name                                    ', 'Role                    ', 'Department                        '],
                 ['2020', 'chaddington', 'smoker', 'swag city']],
              [['Year(s)        ', 'Student Name                                    ', 'Role                    ', 'Department                        '],
                 ['2020', 'chaddington', 'smoker', 'swag city']]],  # section D

             [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', 'teehee']],  # section E
             [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', 'teehee']],  # section F
             [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', 'teehee']],  # section G
             [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', 'teehee']]  # section H
             ]
section_3 = [[['Category                                ', 'Publication                                                                                                '],
              ['N/A', 'N/A']],
             [['Category                                ', 'Creative Work                                                                                          '],
              ['N/A', 'N/A']],
             [['Category                                ', 'Publication or Creative Work                                                                '],
              ['N/A', 'N/A']],
             [['Date(s) Active     ', 'Description                                                                                                                    '],
              ['N/A', 'N/A']],
             [['Date(s)            ', 'Description                                                                                                                        '],
              ['N/A', 'N/A']],
             [['Previously Submitted', 'Funding Source', 'Number or Title', 'Role*', 'Amount**', 'Date Span of Award'],
              ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']]]

section_4 = [[['Date(s)            ', 'Description                                                                                                                           '],
              ['4a1', '4a2'],
              ['4a2', '4a3']],  # section A
             [['Date(s)            ', 'Description                                                                                                                           '],
              ['4b1', '4b2']],  # section B
             [[['Date(s)            ', 'Description                                                                                                                           '],
               ['4c11', '4c12'],
               ['4c11', '4c12']],
              [['Date(s)            ', 'Description                                                                                                                           '],
               ['4c21', '4c22']],
              [['Date(s)            ', 'Description                                                                                                                           '],
                 ['Date?', '4c32']],
              [['Date(s)            ', 'Description                                                                                                                           '],
                 ['Date?', '4c42']],
              [['Date(s)            ', 'Description                                                                                                                           '],
                 ['Date?', '4c52']],
              [['Date(s)            ', 'Description                                                                                                                           '],
                 ['Date?', '4c62']],
              [['Date(s)            ', 'Description                                                                                                                           '],
                 ['Date?', '4c72']],],
             [[['Date(s)            ', 'Description                                                                                                                           '],
               ['Date?', '4d12']],
              [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', '4d22']],
              [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', '4d32']],
              [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', '4d42']],
              [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', '4d52']],
              [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', '4d62']],
              [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', '4d72']],],
             [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', '4de2']],
             [['Date(s)            ', 'Description                                                                                                                           '],
              ['Date?', '4f2']],
             ]

section_5 = [['Date(s)            ', 'Description                                                                                                                        '],
            ['N/A', 'N/A']]
signature = [['Signature                                                    ', 'Date    ']]
            
create_section_1(section_1[0], section_1[1])
create_section_2(section_2[0], section_2[1], section_2[2], section_2[3],
                 section_2[4], section_2[5], section_2[6], section_2[7])
create_section_3(section_3[0], section_3[1], section_3[2],
                 section_3[3], section_3[4], section_3[5])
create_section_4(section_4[0], section_4[1], section_4[2],
                 section_4[3], section_4[4], section_4[5])
create_section_5(section_5)
create_signature(signature)
# test_section(section_4[2])

pdf.build(elements, onFirstPage=create_header, onLaterPages=create_header)
