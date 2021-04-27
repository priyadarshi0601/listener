from os import environ
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/listen')
def home():
    print(request.get_json)
    return('Hello')
    