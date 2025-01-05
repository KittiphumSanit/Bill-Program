from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet
import datetime
from bahttext import bahttext
from data import readDATA


def create_pdf(m):

    dataMonth = readDATA(m)

    # Register Thai font
    pdfmetrics.registerFont(TTFont('THSarabun', './fonts/THSarabunNew.ttf'))  # Replace with the path to your Thai font file

    # Create the document
    
    elements = []

    date = datetime.datetime.now()

    for i in range(len(dataMonth.get('Room'))):
        output = "./output/ห้อง" + str(i+1) + '.pdf'
        document = SimpleDocTemplate(output, pagesize=letter)

        # Add introductory Thai text
        styles = getSampleStyleSheet()
        centered_style = styles["Normal"]
        centered_style.fontName = "THSarabun"  # Set the Thai font
        centered_style.fontSize = 16
        centered_style.alignment = 1  # Center alignment

        intro_text = "หอพักร่มเย็น"
        intro_paragraph = Paragraph(intro_text, styles["Normal"])
        elements.append(intro_paragraph)
        elements.append(Paragraph("<br/><br/>", styles["Normal"]))

        intro_text = "402 หมู่ 9 ต.โป่งผา อ.แม่สาย จ.เชียงราย"
        intro_paragraph = Paragraph(intro_text, styles["Normal"])
        elements.append(intro_paragraph)
        elements.append(Paragraph("<br/><br/>", styles["Normal"]))

        intro_text = "ใบแจ้งหนี้"
        intro_paragraph = Paragraph(intro_text, styles["Normal"])
        elements.append(intro_paragraph)

        # Add some spacing
        elements.append(Paragraph("<br/><br/>", styles["Normal"]))

        # Table data (with merged cells)
        data = [
            [f"ห้อง {dataMonth.get("Room")[i]['Number']}", "", "", "วันที่", f"{str(date.day) + '/' + str(date.month) + '/' + str(date.year+543)}"],
            ["ลำดับ", "รายการ", "จำนวนหน่อย", "ราคาต่อหน่วย", "จำนวนเงิน"],  # Merged cell text in Thai
            ["1", "ค่าเช่า", '1', f"{dataMonth.get("Rent_Price")}", f"{dataMonth.get("Rent_Price")*1}"],
            ["2", "ค่าไฟ", f"{dataMonth.get("Room")[i]['Unit']}", f"{dataMonth.get("Electricity_Price")}", f"{dataMonth.get("Room")[i]['Electricity_Value']}"],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            [f"({bahttext(dataMonth.get("Room")[i]['Debt'])})", "", "", "จำนวนเงินรวม", f"{dataMonth.get("Room")[i]['Debt']}"],
            ["หมายเหตุ กรุณาโอนเงินมาที่บัญชี \"นางสาว กรรณิกา สนิท\"", "", "", "", ""],
            ["ธนาคารเพื่อการเกษตรและสหกรณ์การเกษตร(ธกส) เลขบัญชี 020142880900", "", "", "", ""],
            ["", "", "", "", ""],
        ]

        # Create the table with custom column widths
        table = Table(data, colWidths=[50, 100, 80, 80, 80])  # Adjust widths as needed

        # Add styles, including merging cells and setting the font
        style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'THSarabun'),  # Apply Thai font
            ('FONTSIZE', (0, 0), (-1, -1), 15),  # Font size
            ('BACKGROUND', (0, 0), (2, 0), colors.yellow),
            ('BACKGROUND', (3, 0), (4, 0), colors.greenyellow),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('ALIGN', (0, 7), (-1, 7), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            # ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),

            # Merge Cells
            ('SPAN', (0, 0), (2, 0)),  # Merge cells from (1, 1) to (2, 1)
            ('SPAN', (0, 6), (2, 6)),  
            ('SPAN', (0, 7), (4, 7)),
            ('SPAN', (0, 8), (4, 8)),  
            ('SPAN', (0, 9), (4, 9)),

            # Define the outer grid lines
            ('LINEABOVE', (0, 0), (-1, 0), 0, colors.black),  # Line above header
            ('LINEBELOW', (0, 0), (-1, 0), 0, colors.black),  # Line below header
            ('LINEBELOW', (0, 1), (-1, 1), 0, colors.black),  
            ('LINEBELOW', (0, 5), (-1, 5), 0, colors.black),
            ('LINEBELOW', (0, 6), (-1, 6), 0, colors.black),
            ('LINEBELOW', (0, 9), (-1, 9), 0, colors.black),  

            # Add vertical lines for columns
            ('LINEBEFORE', (0, 0), (0, -1), 1, colors.black),  # Left column
            ('LINEBEFORE', (1, 0), (1, -1), 1, colors.black),  # Left column
            ('LINEBEFORE', (2, 0), (2, -1), 1, colors.black),  # Left column
            ('LINEBEFORE', (3, 0), (3, -1), 1, colors.black),  # Left column
            ('LINEBEFORE', (4, 0), (4, -1), 1, colors.black),  # Left column
            ('LINEAFTER', (4, 0), (4, -1), 1, colors.black),   # Right column
            
        ])
        table.setStyle(style)

        # Add the table to the document
        elements.append(table)

        elements.append(Paragraph("<br/><br/>", styles["Normal"]))

        # Add an image with specific position
        image_path = "qrcode.jpg"  # Provide the path to your image
        img = Image(image_path, width=150, height=200)
        
        # Position the image at (100, 500) coordinates
        # img.drawOn(document.canv, x=100, y=500)

        # Add the image to the list of elements
        elements.append(img)

        elements.append(Paragraph("<br/><br/>", styles["Normal"]))

        # Add introductory Thai text
        styles2 = getSampleStyleSheet()
        centered_style2 = styles2["Normal"]
        centered_style2.fontName = "THSarabun"  # Set the Thai font
        centered_style2.fontSize = 16
        centered_style2.alignment = 2  
        intro_text = "ลงชื่อ  กรรณิกา สนิท"
        intro_paragraph = Paragraph(intro_text, styles2["Normal"])
        elements.append(intro_paragraph)

        # Build the document
        document.build(elements)

    # Save the PDF
    # create_pdf_with_thai_and_merged_cells("thai_merged_cells.pdf")
