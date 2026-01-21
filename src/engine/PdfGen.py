from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


try:
    pdfmetrics.registerFont(TTFont('HindiFont', '..\\fonts\\Poppins-Regular.ttf'))
except:
    print("Font file not found. Please provide a valid .ttf file path.")

def generate_filled_cheque( name, amount_num, amount_words, date_val, acc_num, filename="..\\pdfs\\bank_cheque.pdf"):
    # Standard dimensions: 8.25" x 3.0"
    width, height = 8.25 * inch, 3.0 * inch
    c = canvas.Canvas(filename, pagesize=(width, height))

    # --- 1. Background ---
    c.setFillColorRGB(0.98, 0.97, 0.95)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # --- 2. Bank Header ---
    c.setFillColor(colors.darkslategray)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(0.4 * inch, height - 0.6 * inch, "🏛 BANK NAME")
    
    c.setFont("Helvetica", 8)
    c.drawString(0.4 * inch, height - 0.8 * inch, "Street, 00, Town Name")
    c.drawString(0.4 * inch, height - 0.95 * inch, "Tel: (000) 000 0000")

    # --- 3. Right Header (Cheque No & Date) ---
    c.setFont("Helvetica", 10)
    c.drawRightString(7.8 * inch, height - 0.4 * inch, "0000000")
    
    c.setFont("Helvetica", 9)
    c.drawString(5.3 * inch, height - 0.8 * inch, "DATE")
    c.line(5.8 * inch, height - 0.82 * inch, 7.8 * inch, height - 0.82 * inch)
    
    c.setFont("Courier-Bold", 11)
    c.drawString(6.0 * inch, height - 0.78 * inch, date_val)

    # --- 4. Payee and Amount Section ---
    c.setFont("Helvetica", 9)
    c.drawString(0.4 * inch, height - 1.3 * inch, "YOUR NAME")
    c.line(1.4 * inch, height - 1.32 * inch, 5.8 * inch, height - 1.32 * inch)
    
    c.setFont("HindiFont", 12)
    c.drawString(1.5 * inch, height - 1.28 * inch, name)

    # Dollar Box & Numeric Amount
    c.setFont("Helvetica", 16)
    c.drawString(6.0 * inch, height - 1.3 * inch, "$")
    c.rect(6.2 * inch, height - 1.45 * inch, 1.6 * inch, 0.35 * inch)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(6.3 * inch, height - 1.35 * inch, f"{amount_num:,.2f}")

    # "Pay to the Order of" Line
    c.setFont("Helvetica", 9)
    c.drawString(0.4 * inch, height - 1.65 * inch, "PAY TO THE ORDER OF")
    c.line(1.9 * inch, height - 1.67 * inch, 7.8 * inch, height - 1.67 * inch)

    # Amount in Words Line
    c.line(0.4 * inch, height - 2.0 * inch, 6.7 * inch, height - 2.0 * inch)
    c.drawString(6.8 * inch, height - 1.98 * inch, "DOLLARS 🔒")
    
    c.setFont("Times-Italic", 11)
    c.drawString(0.5 * inch, height - 1.95 * inch, amount_words)

    # --- 5. Adjusted Account Number (Shifted Bottom) ---
    # Moved from height - 2.2 to height - 2.45
    c.setFont("Helvetica", 9)
    c.drawString(0.4 * inch, height - 2.45 * inch, "ACC. NO")
    c.rect(1.0 * inch, height - 2.50 * inch, 1.8 * inch, 0.25 * inch)
    
    c.setFont("Courier-Bold", 10)
    c.drawString(1.1 * inch, height - 2.43 * inch, acc_num)

    # --- 6. Bottom Row (Memo & Signature) ---
    # Adjusted these to align with the new Account Number height
    c.setFont("Helvetica", 9)
    c.drawString(3.2 * inch, height - 2.45 * inch, "MEMO")
    c.line(3.7 * inch, height - 2.47 * inch, 5.3 * inch, height - 2.47 * inch)

    c.drawRightString(7.8 * inch, height - 2.45 * inch, "AUTHORIZED SIGNATURE")
    c.line(5.8 * inch, height - 2.47 * inch, 7.8 * inch, height - 2.47 * inch)

    c.showPage()
    c.save()

if __name__ == "__main__":
    generate_filled_cheque(
        filename=".\\pdfs\\bank_cheque.pdf",
        name="Nikhil Bardeja",
        amount_num=100.00,
        amount_words="One Hundred Dollars Only",
        date_val="11/11/2011",
        acc_num="0123456789"
    )
    