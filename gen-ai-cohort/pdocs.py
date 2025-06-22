from docx import Document
import os

content = input("Enter your content for Word doc:\n")


doc = Document()
doc.add_paragraph(content)


filename = "output.docx"
doc.save(filename)

os.startfile(filename)
