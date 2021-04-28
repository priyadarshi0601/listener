from os import environ
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/listen',methods=['GET','POST'])
def home():
    print(request.json)
    result = request.form.to_dict(flat=False)
    print('FORM DATA',result)
    return('Hello')
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
