'''
Exercise # 8

Write a program to manipulate pdf files using pyPDF. Your programs 
should be able to merge multiple pdf files into a single pdf. 
You are welcome to add more functionalities

pypdf is a free and open-source pure-python PDF library capable of splitting, 
merging, cropping, and transforming the pages of PDF files. It can also add 
custom data, viewing options, and passwords to PDF files. pypdf can retrieve 
text and metadata from PDFs as well.
'''

from pypdf import PdfWriter
import os

merger = PdfWriter()
pdfs = os.listdir("./OPPs/Ex#8 Tut16/")

#? If don't exists rollback
if not pdfs == []:
  for pdf in pdfs:
    if not pdf.endswith(".pdf"):
      print("Files Not Exists!")
    else:
      merger.append(f"./OPPs/Ex#8 Tut16/{pdf}")
      merger.write("./OPPs/Ex#8 Tut16/merged-pdf.pdf")
      merger.close()
else:
  print("Files Not Exists!")