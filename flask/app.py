from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload.html', error='No file selected')

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return render_template('upload.html', error='No file selected')

        # Check if the file is a PDF
        if file and file.filename.lower().endswith('.pdf'):
            filename = secure_filename(file.filename)
            file.save(filename)
            # os.remove(filename)
            return 'File uploaded successfully'
        else:
            return render_template('upload.html', error='Invalid file format. Only PDF files are allowed.')
    else:
        return render_template('upload.html')
    

if __name__ == '__main__':
    app.run(debug=True)

