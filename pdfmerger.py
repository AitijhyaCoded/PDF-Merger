import PyPDF2

print("Enter names of pdf files or q to quit:")
files=[]
while True:
    filename=input()
    if filename=='q':
        break
    files.append(filename)

# files=['file1.pdf','file2.pdf','file3.pdf']

merger = PyPDF2.PdfMerger()

for file in files:
    pdfFile=open(file, 'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write('merged.pdf')