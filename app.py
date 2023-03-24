from flask import Flask,request,jsonify
from compute import qna_converter
from werkzeug.utils import secure_filename
import urllib.request
import os
import json

app = Flask(__name__)



@app.get("/")
def home():
    return "Welcome to the baseURL"

@app.route('/getAnswers', methods=['POST','GET'])
def processAnswersWithoutPdf():
    if request.method == 'POST':
        question = request.form['question']
    else:
        return "Invalid request method"
    
    resp=qna_converter(question,'MRTP.pdf')
    return resp



if __name__=="__main__":
    host = os.environ.get('FLASK_RUN_HOST')
    port = int(os.environ.get('FLASK_RUN_PORT'))
    app.run(host=host, port=port)