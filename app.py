import PyPDF2

PDF_FILE_PATH = 'D:\\Descargas\\some.pdf'


# creating a pdf file object 
pdfFileObj = open(PDF_FILE_PATH, 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page)
    # extracting text from page
    results = pageObj.extractText().split('TRAILER PERSONAL')[1]
    i = 0
    while 'NO DETECTABLE' in results[0: 13] or 'DETECTABLE' in results[0:10]:
        i += 1
        if results[0:13] == 'NO DETECTABLE':
            results = results.split('NO DETECTABLE', 1)[1]
        elif results[0:10] == 'DETECTABLE':
            print(f'Patient {i} was DETECTABLE')
            results = results.split('DETECTABLE', 1)[1]

# closing the pdf file object
pdfFileObj.close()