# import re
# from pdfminer.high_level import extract_pages,extract_text
# text = extract_text("Results sem.pdf")

# pattern = re.compile(r"^[A-Z]{1}\+?")
# matches = pattern.findall(text)



import tabula
tables = tabula.read_pdf("Results sem.pdf",pages='all')
print(tables)
df = tables[0]
gc = df[['GRADE','CREDITS(C)']]
gc = gc.dropna()
print(gc.iloc[2,:])