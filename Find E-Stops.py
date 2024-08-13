import PyPDF2, os
#WHen you open a file in python it will default to read mode (text).
#For pdfs you need to pass the string 'rb' to indicate read binary mode
#pdfFile = open('meetingminutes1.pdf', 'rb')
#reader = PyPDF2.PdfReader(pdfFile)
#print(len(reader.pages))

print(os.getcwd())

#page  = reader.pages[0]
#print(page)
#print(page.extract_text())

#for pagenum in range(len(reader.pages)):
#    print(reader.pages[pagenum].extract_text())
'''
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfReader(pdf1File)
reader2 = PyPDF2.PdfReader(pdf2File)

writer = PyPDF2.PdfWriter()
for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)

for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

outputFile = open('combinedMinutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
'''
