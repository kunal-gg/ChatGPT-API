import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('./pdf-files/design_credit-aerospace.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Open a text file in write mode
text_file = open('./text-files/example.txt', 'a', encoding="utf-8",)

# iterating over the pages and appending them to the file
for page_number in range(9, 33):
    page = pdf_reader.pages[page_number]
    text = page.extract_text()
    text_file.write(text)


# Close the text file and PDF file
text_file.close()
pdf_file.close()
