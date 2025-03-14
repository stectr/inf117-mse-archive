from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer, Image, Table, TableStyle
from reportlab.platypus import PageTemplate, Frame, HRFlowable, ListFlowable, ListItem
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "mse_faculty_db.settings")
django.setup()
from staff_data.models import *

# Initial header data
header_data = {"date_start": "NULL", "date_end": "NULL",
               "name": "printer"}  # example json

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

custom_signature_table_style = TableStyle(
    [('FONTSIZE', (0, 0), (-1, 0), 11), ('LINEABOVE', (0, 0), (-1, -1), 0.1, colors.black), ('FONT', (0, 0), (-1, -1), "Times-Roman")])


def create_header(canvas, doc):
    # REPLACE WITH JSON
    header_text = f'ADDENDUM<br />for the review period<br />{header_data["date_start"]} through {header_data["date_end"]}'
    header_style = custom_header_style
    header = Paragraph(header_text, header_style)
    header.wrap(doc.width, doc.topMargin)
    header.drawOn(canvas, doc.leftMargin + 6, doc.height + doc.topMargin + 6)

    name_text = f"Name: {header_data['name']}"  # REPLACE WITH JSON
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
    section_a_table = Table(section_a, style=custom_table_style, colWidths=[
                            60, 90, 100, 40, 150])

    section_b_table = Table(
        section_b, style=custom_table_style, colWidths=[100, 340])

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
    section_a_table = Table(section_a, style=custom_table_style, colWidths=[
                            70, 70, 100, 70, 80, 50])

    section_b_table = Table(
        section_b[0], style=custom_table_style, colWidths=[230, 70, 70, 70])
    sub_b1 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_b[1]])
    sub_b2 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_b[2]])
    sub_b3 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_b[3]])

    section_c_table = Table(
        section_c[0], style=custom_table_style, colWidths=[230, 70, 70, 70])
    sub_c1 = ListFlowable(
        [ListItem(Paragraph(item, custom_text_style), value=0) for item in section_c[1]])
    sub_c2 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_c[2]])
    sub_c3 = ListFlowable([
        ListItem(Paragraph(item, custom_text_style), value=0) for item in section_c[3]])

    sub_sub_d = ListFlowable([ListItem(Paragraph("those who received their Ph.D or PharmD.", custom_thin_list_style),
                                       value=1), ListItem(Table(section_d[0][0], style=custom_thin_table_style, colWidths=[70, 140, 70, 120]), value=0),
                              ListItem(Paragraph("those who advanced their candidacy", custom_thin_list_style),
                                       value=2), ListItem(Table(section_d[0][1], style=custom_thin_table_style, colWidths=[70, 140, 70, 120]), value=0),
                              ListItem(Paragraph("pre-disseration committees", custom_thin_list_style),
                                       value=3), ListItem(Table(section_d[0][2], style=custom_thin_table_style, colWidths=[70, 140, 70, 120]), value=0),
                              ListItem(Paragraph("other research supervision", custom_thin_list_style),
                                       value=4), ListItem(Table(section_d[0][3], style=custom_thin_table_style, colWidths=[70, 140, 70, 120]), value=0)], bulletType='a', bulletFormat='(%s)', bulletFontSize=10, bulletFontName="Times-Roman")

    sub_d = ListFlowable(
        [ListItem(Paragraph("(indicate dates, and whether as chair, co-chair, or committee member)", custom_list_style),
                  value=1), ListItem(sub_sub_d, value=0),
         ListItem(Paragraph("<b>Master’s Thesis Students Supervised</b> (indicate dates, and whether as chair, co-chair, or committee member)", custom_thin_list_style),
                  value=2), ListItem(Table(section_d[1], style=custom_thin_table_style, colWidths=[70, 160, 70, 120]), value=0),
         ListItem(Paragraph("Postdoctoral Scholars Supervised", custom_list_style),
                  value=3), ListItem(Table(section_d[2], style=custom_thin_table_style, colWidths=[70, 160, 70, 120]), value=0),
         ListItem(Paragraph("Undergraduate Student Research Supervision – UROP, honors courses, 199's or equivalents", custom_list_style),
                  value=4), ListItem(Table(section_d[3], style=custom_thin_table_style, colWidths=[70, 160, 70, 120]), value=0),
         ListItem(Paragraph("Other Research or Teaching Supervision", custom_list_style),
                  value=5), ListItem(Table(section_d[4], style=custom_thin_table_style, colWidths=[70, 160, 70, 120]), value=0)], bulletType='1', bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold")

    section_e_table = Table(
        section_e, style=custom_thin_table_style, colWidths=[100, 340])
    section_f_table = Table(
        section_f, style=custom_thin_table_style, colWidths=[100, 340])
    section_g_table = Table(
        section_g, style=custom_thin_table_style, colWidths=[100, 340])
    section_h_table = Table(
        section_h, style=custom_thin_table_style, colWidths=[100, 340])

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


def create_section_3(t1, t2, t3, t4, t5, t6, t7, t8, t9):
    for _ in range(2):
        elements.append(Paragraph("", custom_list_style))
    elements.append(Paragraph(
        "SECTION III – Research and Creative Activity during review period", custom_title_style))
    elements.append(Paragraph("", custom_list_style))
    table1_a = Table(t1[0], style=custom_table_style, colWidths=[130, 310])
    table1_b = Table(t1[1], style=custom_table_style, colWidths=[130, 310])
    table2_a = Table(t2[0], style=custom_table_style, colWidths=[130, 310])
    table2_b = Table(t2[1], style=custom_table_style, colWidths=[130, 310])
    table3 = Table(t3, style=custom_table_style, colWidths=[130, 310])
    table4 = Table(t4, style=custom_thin_table_style, colWidths=[130, 310])
    table5 = Table(t5, style=custom_thin_table_style, colWidths=[130, 310])
    table6 = Table(t6, style=custom_table_style,
                   colWidths=[50, 100, 140, 50, 50, 50])
    table7 = Table(t7, style=custom_table_style,
                   colWidths=[50, 100, 140, 50, 50, 50])
    table8 = Table(t8, style=custom_thin_table_style, colWidths=[130, 310])
    table9 = Table(t9, style=custom_thin_table_style, colWidths=[130, 310])

    sectionlist = [
        # Section A
        ListItem(Paragraph(
            "PUBLICATIONS AND CREATIVE ACTIVITY NOT CREDITED IN A PRIOR REVIEW", custom_list_style), value=1),
        ListItem(Paragraph("INTELLECTUAL CONTRIBUTIONS",
                 custom_list_style), value=0),
        ListItem(table1_a, value=0),
        ListItem(Paragraph(
            "ARTISTIC AND PROFESSIONAL PERFORMANCES AND EXHIBITS", custom_list_style), value=0),
        ListItem(table1_b, value=0),

        # Section B
        # <br />(do not list any work already credited for the last promotion or advancement (Professor VI, A/S)
        ListItem(Paragraph(
            "PUBLICATIONS AND CREATIVE ACTIVITY PREVIOUSLY SUBMITTED IN A PRIOR REVIEW", custom_list_style), value=2),
        ListItem(Paragraph("INTELLECTUAL CONTRIBUTIONS",
                 custom_list_style), value=0),
        ListItem(table2_a, value=0),
        ListItem(Paragraph(
            "ARTISTIC AND PROFESSIONAL PERFORMANCES AND EXHIBITS", custom_list_style), value=0),
        ListItem(table2_b, value=0),

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
        ListItem(table7, value=0),

        # Section H
        ListItem(Paragraph(
            "PROFESSIONAL DEVELOPMENT ACTIVITIES RELATED TO RESEARCH/CREATIVE ACTIVITIES", custom_list_style), value=8),
        ListItem(table8, value=0),

        # Section I
        ListItem(Paragraph(
            "DIVERSITY ACTIVITIES RELATED TO RESEARCH/CREATIVE ACTIVITIES", custom_list_style), value=9),
        ListItem(table9, value=0),
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
    section_a_table = Table(
        section_a, style=custom_thin_table_style, colWidths=[100, 340])
    section_b_table = Table(
        section_b, style=custom_thin_table_style, colWidths=[100, 340])
    section_e_table = Table(
        section_e, style=custom_thin_table_style, colWidths=[100, 340])
    section_f_table = Table(
        section_f, style=custom_thin_table_style, colWidths=[100, 340])

    sectionlist = [
        ListItem(Paragraph("HONORS AND AWARDS", custom_list_style),
                 value=1), ListItem(section_a_table, value=0),
        ListItem(Paragraph("MEMBERSHIPS", custom_list_style),
                 value=2), ListItem(section_b_table, value=0),
        ListItem(Paragraph("PROFESSIONAL ACTIVITY", custom_list_style),
                 value=3),
        ListItem(Paragraph("Invited presentations at educational, governmental institutions (or similar organizations)", custom_list_style),
                 value=0),
        ListItem(Table(section_c[0], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Paragraph("Invited presentations at professional meetings", custom_list_style),
                 value=0),
        ListItem(Table(section_c[1], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Paragraph("Accepted presentations at educational, governmental institutions (or similar organizations)", custom_list_style),
                 value=0),
        ListItem(Table(section_c[2], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Paragraph("Accepted presentations at professional meetings", custom_list_style),
                 value=0),
        ListItem(Table(section_c[3], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Paragraph("Other presentations at professional meetings", custom_list_style),
                 value=0),
        ListItem(Table(section_c[4], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Paragraph("Media Appearances and Interviews", custom_list_style),
                 value=0),
        ListItem(Table(section_c[5], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Paragraph("Professional articles in this period about you or published reviews of your work", custom_list_style),
                 value=0),
        ListItem(Table(section_c[6], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Paragraph("PROFESSIONAL AND PUBLIC SERVICE", custom_list_style),
                 value=4),
        ListItem(Table(section_d[0], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Table(section_d[1], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Table(section_d[2], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Table(section_d[3], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Table(section_d[4], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Table(section_d[5], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Table(section_d[6], style=custom_thin_table_style, colWidths=[
                 100, 340]), value=0),
        ListItem(Paragraph("PROFESSIONAL DEVELOPMENT ACTIVITIES RELATED TO PROFESSIONAL AND PUBLIC SERVICE", custom_list_style),
                 value=5), ListItem(section_e_table, value=0),
        ListItem(Paragraph("DIVERSITY ACTIVITIES RELATED TO PROFESSIONAL AND PUBLIC SERVICE", custom_list_style),
                 value=6), ListItem(section_f_table, value=0),
    ]

    elements.append(ListFlowable(sectionlist,
                                 bulletType='A', bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold"))
    elements.append(PageBreak())  # Insert a page break


def create_section_5(sa, sb, sc, sd, se, sf):
    for _ in range(2):
        elements.append(Paragraph("", custom_list_style))
    elements.append(Paragraph(
        "SECTION V – University & Systemwide Service during review period", custom_title_style))
    elements.append(Paragraph("", custom_list_style))
    section_a_table = Table(sa, style=custom_table_style, colWidths=[100, 340])
    section_b_table = Table(sb, style=custom_table_style, colWidths=[100, 340])
    section_c_table = Table(sc, style=custom_table_style, colWidths=[100, 340])
    section_d_table = Table(sd, style=custom_table_style, colWidths=[100, 340])
    section_e_table = Table(se, style=custom_table_style, colWidths=[100, 340])
    section_f_table = Table(sf, style=custom_table_style, colWidths=[100, 340])

    sectionlist = [
        # Section A
        ListItem(Paragraph(
            "<b>UNIVERSITY/SYSTEMWIDE</b> - Academic Senate, Administrative Service; Senate Assembly; MRU, UCOP", custom_text_style), value=1),
        ListItem(section_a_table, value=0),

        # Section B
        ListItem(Paragraph(
            "<b>CAMPUS</b> - Academic Senate and Administrative Service:", custom_text_style), value=2),
        ListItem(section_b_table, value=0),

        # Section C
        ListItem(Paragraph("SCHOOL", custom_list_style), value=3),
        ListItem(section_c_table, value=0),

        # Section D
        ListItem(Paragraph(
            "<b>DEPARTMENT</b> (other than listings in Section I)", custom_text_style), value=4),
        ListItem(section_d_table, value=0),

        # Section E
        ListItem(Paragraph(
            "PROFESSIONAL DEVELOPMENT ACTIVITIES RELATED TO UNIVERSITY/SYSTEMWIDE SERVICE", custom_list_style), value=5),
        ListItem(section_e_table, value=0),

        # Section F
        ListItem(Paragraph(
            "DIVERSITY ACTIVITIES RELATED TO UNIVERSITY/SYSTEMWIDE SERVICE", custom_list_style), value=6),
        ListItem(section_f_table, value=0)
    ]

    elements.append(ListFlowable(sectionlist, bulletType='A',
                    bulletFormat='%s.', bulletFontSize=10, bulletFontName="Times-Bold"))

###
# Custom left spacing n times.
# NOTE: The tmp must be None when called.
# ###


def _left_space(input: ListFlowable, n: int, tmp: ListFlowable = None):
    if n == 0 and tmp == None:
        return input
    if n == 0:
        return tmp
    if tmp == None:
        tmp = ListFlowable([ListItem(input, value=0)])
    return _left_space(input, n-1, ListFlowable([ListItem(tmp, value=0)]))


def create_signature():
    for _ in range(13):
        elements.append(Paragraph("", custom_list_style))
    elements.append(Paragraph(
        "I certify that the information on this form is correct:", custom_signature_style))
    for _ in range(9):
        elements.append(Paragraph("", custom_list_style))
    sig_field = ListFlowable(
        [ListItem(Table([['Signature', 'Date']], style=custom_signature_table_style, colWidths=[260, 40]), value=0)])
    elements.append(_left_space(sig_field, 7))


# TABLES OF DATA FULL OF FILLER FOR NOW AND SOME ARE SUPER COMPLEX GOOD LOOK LOL
section_1 = [
            [
                ['Period', 'Title & Rank', 'Step', 'Time', 'Department'],  # [0]
            ],  # section A

    [
                ['Period', 'Position/Description'],  # [1]
            ]  # section B
]

section_2 = [[['Qrtr/Year', 'Course #', 'Title', 'Enrollment', '# Instructors', '% Taught'],  # [0]
              ],  # section A

             [[['Description', '# of Students', 'Date/Date Span', '# Hours/Days'],
               ['not implemented', 'not implemented', 'not implemented', 'not implemented']],
              ['not implemented', 'not implemented'],
              ['not implemented', 'not implemented'],
              ['not implemented', 'not implemented']
              ],  # section B

             [[['Description', '# of Students', 'Date/Date Span', '# Hours/Days'],
               ['not implemented', 'not implemented', 'not implemented', 'not implemented']],
              ['not implemented'],
              ['not implemented'],
              ['not implemented']
              ],  # section C

             [[[['Year(s)', 'Student Name', 'Role', 'Department'],  # [3][0][0]
                ],
                 [['Year(s)', 'Student Name', 'Role', 'Department'],  # [3][0][1]
                  ],
                 [['Year(s)', 'Student Name', 'Role', 'Department'],  # [3][0][2]
                  ],
                 [['Year(s)', 'Student Name', 'Role', 'Department'],  # [3][0][3]
                  ]],

              [['Year(s)', 'Student Name', 'Role', 'Department'],  # [3][0]
               ],
              [['Year(s)', 'Student Name', 'Role', 'Department'],  # [3][1]
               ],
              [['Year(s)', 'Student Name', 'Role', 'Department'],  # [3][2]
               ],
              [['Year(s)', 'Student Name', 'Role', 'Department'],  # [3][3]
               ]],  # section D

             [['Date(s)', 'Description'],  # [4]
              ],  # section E
             [['Date(s)', 'Description'],  # [5]
              ],  # section F
             [['Date(s)', 'Description'],  # [6]
              ],  # section G
             [['Date(s)', 'Description'],  # [7]
              ]  # section H
             ]

section_3 = [
            [
                [['Category', 'Publication'], ],  # [0][0]
                [['Category', 'Creative Work'], ]  # [0][1]
            ],  # section A

    [
                [['Category', 'Publication'], ],  # [1][0]
                [['Category', 'Creative Work'], ]  # [1][1]
            ],  # section B

    [
                ['Category', 'Publication or Creative Work'],  # [2]
            ],  # section C

    [
                ['Date(s) Active', 'Description'],  # [3]
            ],  # section D

    [
                ['Date(s)', 'Description'],  # [4]
            ],  # section E

    [
                ['Previously\nSubmitted', 'Funding Source', 'Number or Title',
                 'Role*', 'Amount**', 'Date Span of\nAward'],  # [5]
            ],  # section F

    [
                ['Previously\nSubmitted', 'Funding Source', 'Number or Title',
                 'Role*', 'Amount**', 'Date Span of\nAward'],  # [6]
            ],  # section G

    [
                ['Date(s)', 'Description'],  # [7]
            ],  # section H

    [
                ['Date(s)', 'Description'],  # [8]
            ],  # section I
]

section_4 = [[['Date(s)', 'Description'],   # section_4[0].append
              ],  # section A
             [['Date(s)', 'Description'],   # section_4[1].append
              ],  # section B
             [[['Date(s)', 'Description'],  # section_4[2][0].append
               ],
              [['Date(s)', 'Description'],  # section_4[2][1].append
               ],
              [['Date(s)', 'Description'],  # section_4[2][2].append
               ],
              [['Date(s)', 'Description'],  # section_4[2][3].append
               ],
              [['Date(s)', 'Description'],  # section_4[2][4].append
               ],
              [['Date(s)', 'Description'],  # section_4[2][5].append
               ],
              [['Date(s)', 'Description'],  # section_4[2][6].append
               ],
              ],
             [[['Date(s)', 'Description'],  # section_4[3][0].append
               ],
              [['Date(s)', 'Description'],  # section_4[3][1].append
               ],
              [['Date(s)', 'Description'],  # section_4[3][2].append
               ],
              [['Date(s)', 'Description'],  # section_4[3][3].append
               ],
              [['Date(s)', 'Description'],  # section_4[3][4].append
               ],
              [['Date(s)', 'Description'],  # section_4[3][5].append
               ],
              [['Date(s)', 'Description'],  # section_4[3][6].append
               ],],
             [['Date(s)', 'Description'],  # section_4[4].append
              ],
             [['Date(s)', 'Description'],  # section_4[5].append
              ],
             ]

section_5 = [[['Date(s)', 'Description'],  # section_5[0].append
              ],
             [['Date(s)', 'Description'],  # section_5[1].append
              ],
             [['Date(s)', 'Description'],  # section_5[2].append
              ],
             [['Date(s)', 'Description'],  # section_5[3].append
              ],
             [['Date(s)', 'Description'],  # section_5[4].append
              ],
             [['Date(s)', 'Description'],  # section_5[5].append
              ],
             ]


# SECTION 1 APPENDING DATA
section1a = EmploymentHistory.objects.filter(
    faculty_id__name=header_data['name'])
section1b = OtherEmployment.objects.filter(
    faculty_id__name=header_data['name'])
for i in section1a:
    section_3[0].append([f'{i.period_start.strftime("%Y")} - {i.period_end.strftime("%Y")}',
                        i.title_rank, i.step, i.time_percentage, i.department])
for i in section1b:
    section_3[1].append(
        [f'{i.period_start.strftime("%Y")} - {i.period_end.strftime("%Y")}', i.position_description])

# SECTION 2 APPENDING DATA
section2a = UCICourse.objects.filter(faculty_id__name=header_data['name'])
section2d1 = DoctoralStudent.objects.filter(
    faculty_id__name=header_data['name'])
section2d2 = MasterStudent.objects.filter(faculty_id__name=header_data['name'])
section2d3 = PostdocStudent.objects.filter(
    faculty_id__name=header_data['name'])
section2d4 = UndergradResearch.objects.filter(
    faculty_id__name=header_data['name'])
section2d5 = OtherResearch.objects.filter(faculty_id__name=header_data['name'])
section2e = TeachingAward.objects.filter(faculty_id__name=header_data['name'])
section2f = TeachingInnovation.objects.filter(
    faculty_id__name=header_data['name'])
section2g = ProfDevelopmentTeaching.objects.filter(
    faculty_id__name=header_data['name'])
section2h = DiversityTeaching.objects.filter(
    faculty_id__name=header_data['name'])

for i in section2a:
    section_2[0].append([f'{i.quarter} {i.year}', i.courseNumber,
                        i.courseTitle, i.enrollment, i.numInstructors, i.percentTaught])
for i in section2d1:
    if i.receivedPHD:
        section_2[3][0][0].append(
            [i.startyear, i.studentName, i.role, i.department])
    elif i.candidacy:
        section_2[3][0][1].append(
            [i.startyear, i.studentName, i.role, i.department])
    elif i.preDissComm:
        section_2[3][0][2].append(
            [i.startyear, i.studentName, i.role, i.department])
    else:
        section_2[3][0][3].append(
            [i.startyear, i.studentName, i.role, i.department])
for i in section2d2:
    section_2[3][1].append([i.startyear, i.studentName, i.role, i.department])
for i in section2d3:
    section_2[3][2].append([i.startyear, i.studentName, i.role, i.department])
for i in section2d4:
    section_2[3][3].append([i.startyear, i.studentName, i.role, i.department])
for i in section2d5:
    section_2[3][4].append([i.startyear, i.studentName, i.role, i.department])
for i in section2e:
    section_2[4].append([i.startdate.strftime("%Y"), i.description])
for i in section2f:
    section_2[5].append([i.startdate.strftime("%Y"), i.description])
for i in section2g:
    section_2[6].append([i.startdate.strftime("%Y"), i.description])
for i in section2h:
    section_2[7].append([i.startdate.strftime("%Y"), i.description])

# SECTION 3 APPENDING DATA
section3a1 = IntellectualContributions.objects.filter(
    faculty_id__name=header_data['name'])
section3a2 = NotCreditedArtistic.objects.filter(
    faculty_id__name=header_data['name'])
section3b1 = PreviousContributions.objects.filter(
    faculty_id__name=header_data['name'])
section3b2 = CreditedArtistic.objects.filter(
    faculty_id__name=header_data['name'])
section3c = CompletedPartsOfWorks.objects.filter(
    faculty_id__name=header_data['name'])
section3d = ProfessionalResources.objects.filter(
    faculty_id__name=header_data['name'])
section3e = IntellectualProperty.objects.filter(
    faculty_id__name=header_data['name'])
section3f = ContractsGrantsFellowships.objects.filter(
    faculty_id__name=header_data['name'])
section3g = NonFinancialResources.objects.filter(
    faculty_id__name=header_data['name'])
section3h = ProfDevResearchActivities.objects.filter(
    faculty_id__name=header_data['name'])
section3i = DiversityResearchActivities.objects.filter(
    faculty_id__name=header_data['name'])

for i in section3a1:
    section_3[0][0].append([i.category, i.publication_citation])
for i in section3a2:
    section_3[0][1].append([i.category, i.creativeWork])
for i in section3b1:
    section_3[1][0].append([i.category, i.publication_citation])
for i in section3b2:
    section_3[1][1].append([i.category, i.creativeWork])
for i in section3c:
    section_3[2].append([i.category, i.work_detail])
for i in section3d:
    section_3[3].append([i.dates_active, i.description])
for i in section3e:
    section_3[4].append([i.dates, i.description])
for i in section3f:
    section_3[5].append([i.previously_submitted, i.funding_source,
                        i.number_or_title, i.role, i.amount, i.date_span])
for i in section3g:
    section_3[6].append([i.previously_submitted, i.funding_source,
                        i.number_or_title, i.role, i.perks_description, i.date_span])
for i in section3h:
    section_3[7].append([i.dates, i.description])
for i in section3i:
    section_3[8].append([i.dates, i.description])

# SECTION 4 APPENDING DATA
section4a = HonorsAward.objects.filter(faculty_id__name=header_data['name'])
section4b = Membership.objects.filter(faculty_id__name=header_data['name'])
section4c = ProfessionalActivity.objects.filter(
    faculty_id__name=header_data['name'])
section4d = ProfPublicService.objects.filter(
    faculty_id__name=header_data['name'])
section4e = ProfDevService.objects.filter(faculty_id__name=header_data['name'])
section4f = DiversityService.objects.filter(
    faculty_id__name=header_data['name'])

for i in section4a:
    section_4[0].append(
        [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
for i in section4b:
    section_4[1].append(
        [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
for i in section4c:
    if i.invitedEduGov:
        section_4[2][0].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.invitedProf:
        section_4[2][1].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.acceptedEduGov:
        section_4[2][2].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.acceptedProf:
        section_4[2][3].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.otherPresent:
        section_4[2][4].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.mediaInterview:
        section_4[2][5].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.articlesReviews:
        section_4[2][6].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
for i in section4d:
    if i.profSocOutsideInst:
        section_4[3][0].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.journalEdit:
        section_4[3][1].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.reviewer:
        section_4[3][2].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.memberReviewBoard:
        section_4[3][3].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.adhocService:
        section_4[3][4].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.consulting:
        section_4[3][5].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
    elif i.communityService:
        section_4[3][6].append(
            [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
for i in section4e:
    section_4[4].append(
        [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])
for i in section4f:
    section_4[5].append(
        [f'{i.startdate.strftime("%Y")} - {i.enddate.strftime("%Y")}', i.description])

# SECTION 5 APPENDING DATA
section5a = UniversitySystemwide.objects.filter(
    faculty_id__name=header_data['name'])
section5b = Campus.objects.filter(faculty_id__name=header_data['name'])
section5c = School.objects.filter(faculty_id__name=header_data['name'])
section5d = Department.objects.filter(faculty_id__name=header_data['name'])
section5e = ProfessionalDevelopement.objects.filter(
    faculty_id__name=header_data['name'])
section5f = DiversityAcitivites.objects.filter(
    faculty_id__name=header_data['name'])

for i in section5a:
    section_5[0].append(
        [f'{i.period_start.strftime("%Y")} - {i.period_end.strftime("%Y")}', i.position_description])
for i in section5b:
    section_5[1].append(
        [f'{i.period_start.strftime("%Y")} - {i.period_end.strftime("%Y")}', i.position_description])
for i in section5c:
    section_5[2].append(
        [f'{i.period_start.strftime("%Y")} - {i.period_end.strftime("%Y")}', i.position_description])
for i in section5d:
    section_5[3].append(
        [f'{i.period_start.strftime("%Y")} - {i.period_end.strftime("%Y")}', i.position_description])
for i in section5e:
    section_5[4].append(
        [f'{i.period_start.strftime("%Y")} - {i.period_end.strftime("%Y")}', i.position_description])
for i in section5f:
    section_5[5].append(
        [f'{i.period_start.strftime("%Y")} - {i.period_end.strftime("%Y")}', i.position_description])

create_section_1(section_1[0], section_1[1])
create_section_2(section_2[0], section_2[1], section_2[2], section_2[3],
                 section_2[4], section_2[5], section_2[6], section_2[7])
create_section_3(section_3[0], section_3[1], section_3[2],
                 section_3[3], section_3[4], section_3[5],
                 section_3[6], section_3[7], section_3[8])
create_section_4(section_4[0], section_4[1], section_4[2],
                 section_4[3], section_4[4], section_4[5])
create_section_5(section_5[0], section_5[1], section_5[2],
                 section_5[3], section_5[4], section_5[5])
create_signature()

pdf.build(elements, onFirstPage=create_header, onLaterPages=create_header)
