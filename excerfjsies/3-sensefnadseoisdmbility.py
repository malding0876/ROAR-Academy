import PyPDF2
import os

path = os.path.dirname(os.path.abspath(__file__))
file_handle = open(path + '/Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(file_handle)
# page_number = len(pdfReader.pages)
page_object = pdfReader.pages[0]
whole_text = page_object.extract_text()

frequency_table = {}
# print(type(page_text.split('\n')))

for page_number in range(0, len(pdfReader.pages)):
    whole_text += 