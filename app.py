from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

data_list=[]

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    content = request.get_json()
    data_list.append(content)
    return 'JSON Posted'

@app.route('/getjson', methods = ['GET'])
def getJsonHandler():
    global data_list
    json = jsonify(data_list[-1])
    data_list=[]
    return json

