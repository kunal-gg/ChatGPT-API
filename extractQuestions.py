import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('design_credit.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the first page of the PDF document
page = pdf_reader.pages[0]

# Extract the text from the page
text = page.extract_text()

# Open a text file in write mode
text_file = open('example.txt', 'w')

# Write the extracted text to the text file
text_file.write(text)

# Close the text file and PDF file
text_file.close()
pdf_file.close()
