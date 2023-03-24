from flask import Flask,request,jsonify
from compute import qna_converter
from werkzeug.utils import secure_filename
import urllib.request
import os
import json
from dotenv import load_dotenv

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['pdf'])
UPLOAD_FOLDER=os.environ.get('UPLOAD_FOLDER')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get("/")
def home():
    return "Welcome to QNA System"



@app.route('/getAnswers', methods=['POST','GET'])
def processAnswersWithoutPdf():
    if request.method == 'POST':
        question = request.form['question']
    else:
        return "Invalid request method"
    filename='MRTP.pdf'
    
    resp=qna_converter(question,filename)
    return resp



@app.route('/getAnswersFromPdf', methods=['POST','GET'])
def processAnswersWithPdf():
    # check if the post request has the file part
    if 'document' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['document']

    success=False
    errors = {}

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        success = True
    else:
        errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

    if success:
        question = request.form['question']
        pdfpath=os.path.join(UPLOAD_FOLDER, filename)
        resp=qna_converter(question,pdfpath)

        #deleting the PDF after the task is complete
        os.remove(pdfpath)


        return resp

    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp




if __name__=="__main__":
    load_dotenv()
    host = os.environ.get('FLASK_RUN_HOST')
    port = int(os.environ.get('FLASK_RUN_PORT'))
    app.run(host=host, port=port)