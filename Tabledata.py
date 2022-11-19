import tabula
import os
file = r"C:\Users\Pradeep\Desktop\Python-SK.pdf"
tables = tabula.io.read_pdf(file,pages="all")
print(tables)