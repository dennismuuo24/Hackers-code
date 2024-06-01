from fpdf import FPDF

# Create a new PDF instance
pdf = FPDF()

# Add a new page
pdf.add_page()

# Set the font and font size
pdf.set_font("Arial", size=12)

# Company information
pdf.cell(200, 10, txt="Tollo Tours & Travel Company", ln=1)
pdf.cell(200, 5, txt="Business Number +254 701 855459", ln=1)
pdf.cell(200, 5, txt="Paybill Number: 552800 Account Number: 404142", ln=1)
pdf.cell(200, 5, txt="Business Name: TOLLO TOURS AND ACCOMMODATION", ln=1)
pdf.cell(200, 5, txt="Mombasa", ln=1)
pdf.cell(200, 5, txt="80100", ln=1)
pdf.cell(200, 5, txt="+254 790 456234", ln=1)
pdf.cell(200, 5, txt="tollotours@gmail.com,Ordilliah@tollotours.com", ln=1)
pdf.cell(200, 10, txt="INVOICE", ln=1)
pdf.cell(200, 10, txt="Invoice0018", ln=1)
pdf.cell(200, 10, txt="DATE", ln=1)
pdf.cell(200, 10, txt="May 31, 2024", ln=1)
pdf.cell(200, 10, txt="BALANCE DUE", ln=1)
pdf.cell(200, 10, txt="KES KSh8,000.00", ln=1)
pdf.cell(200, 10, txt="BILL TO", ln=1)
pdf.cell(200, 10, txt="Lang'at", ln=1)
pdf.cell(200, 10, txt="No of Nights: 6", ln=1)
pdf.cell(200, 10, txt="Rate Per Night: Ksh 4,500", ln=1)
pdf.cell(200, 10, txt="House No: shanzu Siloam B01", ln=1)
pdf.cell(200, 10, txt="+254 726 619549", ln=1)
pdf.cell(200, 10, txt="Check In Date:24/5/2024", ln=1)
pdf.cell(200, 10, txt="Ckeck-out -Date:30/5/2024", ln=1)
pdf.cell(200, 10, txt="DESCRIPTION RATE QTY AMOUNT", ln=1)
pdf.cell(200, 10, txt="Accommodation Fee", ln=1)
pdf.cell(200, 10, txt="Rate per Night Ksh 4,500 KSh4,500.00 6 KSh27,000.00", ln=1)
pdf.cell(200, 10, txt="Paybill Number: 552800", ln=1)
pdf.cell(200, 10, txt="Account Number: 404142", ln=1)
pdf.cell(200, 10, txt="Business Name: TOLLO TOURS AND ACCOMMODATION KSh0.00 0 KSh0.00", ln=1)
pdf.cell(200, 10, txt="SUBTOTAL KSh27,000.00", ln=1)
pdf.cell(200, 10, txt="TAX (0%) KSh0.00", ln=1)
pdf.cell(200, 10, txt="TOTAL KSh27,000.00", ln=1)
pdf.cell(200, 10, txt="PAID -KSh19,000.00", ln=1)
pdf.cell(200, 10, txt="May 31, 2024", ln=1)
pdf.cell(200, 10, txt="BALANCE DUE KES KSh8,000.00", ln=1)
pdf.cell(200, 10, txt="Thank You Lang'at", ln=1)
pdf.cell(200, 10, txt="#Karibu Tena", ln=1)

# Preview the PDF
pdf.output("invoice.pdf", "F")

import os
os.system("invoice.pdf")