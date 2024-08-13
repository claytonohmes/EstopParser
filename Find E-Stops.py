import PyPDF2, os, re
from tqdm import tqdm

#Print the current working directory
print(os.getcwd())

#insert the text you want to search for here
searched_text = 'PB'

#function to search a pdf for unique values and combine them into a single list.
def search_pdf(filename, text):

    # define a regular expression to find the text you'd like to search
    regex = re.compile(r'PB\d{3}')

    #open the file and create a PDF object
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        #set up a set to be initally combined
        temp_list = []
        Unique_Set = set(temp_list)

        #for each page in the PDF, extract the text and store that in page content. This will also do the set combination.
        for page_num in tqdm(range(len(pdf_reader.pages))):

            #temp object to store the page text.
            page_content = pdf_reader.pages[page_num].extract_text()

            #Set Combination.
            Temp2 = set(regex.findall(page_content))
            Unique_Set = Unique_Set.union(Temp2)
        
        #Convert the set to a list.
        Unique_List = list(Unique_Set)

    return(Unique_List)

# call the funciton and print out the list for the user to copy.
final_List = search_pdf('TBB12V13.pdf', searched_text)
print(final_List)

#Old Code for reference
'''
#page  = pdf_reader.pages[1456]
#print(page)
#print(page.extract_text())

#for pagenum in range(len(reader.pages)):
#    print(reader.pages[pagenum].extract_text())


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
