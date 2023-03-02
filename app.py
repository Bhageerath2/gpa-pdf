from flask import Flask, request, render_template,redirect,url_for
from werkzeug.utils import secure_filename
import os
from PyPDF2 import PdfReader
import tabula
from tabula import read_pdf
import pandas


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', error='No file selected')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', error='No file selected')
        if file and file.filename.lower().endswith('.pdf'):
            filename = secure_filename(file.filename)
            filepath=file.save(os.path.join('./static/uploads', filename))
            # reader = PdfReader(filepath)
            # if reader is not None and len(reader.pages) > 0:
            #     page = reader.pages[0]
            #     text = page.extract_text(0)
            tables = tabula.read_pdf(filepath,pages='all')
            df = tables[0]
            gc = df[['GRADE','CREDITS(C)']]
            gc = gc.dropna()
            

            
            
            
            

            return redirect(url_for('./templates/calculate.html',text=filepath))
        else:
            return render_template('upload.html', error='Invalid file format. Only PDF files are allowed.')
    else:
        return render_template('upload.html')
    

if __name__ == '__main__':
    app.run(debug=True)



