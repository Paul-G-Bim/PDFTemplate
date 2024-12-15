from fpdf import FPDF

# Configure the pdf document
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Create a page
pdf.add_page()

# Output the document to a file
pdf.output("template.pdf")
