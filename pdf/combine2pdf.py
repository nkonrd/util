from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileMerger, PdfFileReader

pagesTotal = 0
folderName = ""

for page in range(0, pagesTotal):
  svg = svg2rlg(f"{folderName}/{page}.svg")
  renderPDF.drawToFile(svg, f"{folderName}/{page}.pdf")

merger = PdfFileMerger()
for page in range(0, pagesTotal):
  merger.append(PdfFileReader(open(f"{folderName}/{page}.pdf", 'rb')))

pdfOut = open(f"{folderName}.pdf", "wb")
merger.write(pdfOut)
pdfOut.close()
merger.close()
