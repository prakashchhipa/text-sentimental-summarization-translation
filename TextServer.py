#!flask/bin/python
from flask import Flask, render_template
from flask import request
from flask import jsonify
from TextOperation import *
from flask.ext.cors import CORS, cross_origin
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
@app.route('/')
def index():
    headers = {'Content-Type': 'text/html'}
    return render_template('samples/browser/index.html')
    #return "Text Service Running 2017 - NAT Hackathon"

@app.route('/text/<txt>', methods=['GET'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def getTextResults(txt):
    return jsonify({'response':GetTextDetails(txt)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
