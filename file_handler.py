from PyPDF2 import PdfReader
def load_text(file):
    if str(file).endswith(".txt"):
        with open(file,"r",encoding="utf-8") as f:
            return f.read()
    elif str(file).endswith(".pdf"):
        reader=PdfReader(file)
        text=""
        for page in reader.pages:
            text+=page.extract_text()
        return text