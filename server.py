from os import environ
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/listen',methods=['GET','POST'])
def home():
    print(request.get_json)
    print('FORM DATA',request.form)
    return('Hello')
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
