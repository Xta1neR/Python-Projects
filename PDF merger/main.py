import PyPDF2

pdffiles = ["sample.pdf", "sample2.pdf"]
pdfMerger = PyPDF2.PdfMerger()

for filename in pdffiles : 
	pdfFiles = open(filename, 'rb')
	pdfReader = PyPDF2.PdfReader(pdfFiles)
	pdfMerger.append(pdfReader)

pdfFiles.close()
pdfMerger.write("merged.pdf")
pdfMerger.close()