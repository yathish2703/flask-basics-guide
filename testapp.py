from flask import Flask ,request
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World!</h1> <br> yathish"

@app.route('/diff/<int:var1>/<int:var2>')
def sub(var1, var2):
    diff = var1 - var2
    return "<h1>" + str(diff) + "</h1>"

@app.route('/<int:a>/<int:b>')
def sum(a,b):
    sum = a+b
    return str(sum)

@app.route("/yathish")
def func1():   
    a = 10 
    b=20 
    return str((a+b))

@app.route('/methods-demo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def methods_demo():
    # Get the HTTP method used
    method = request.method
    
    # Different logic for each method
    if method == 'GET':
        return 'Reading data'
    elif method == 'POST':
        return 'Creating new data gkugkjggkgkh'
    elif method == 'PUT':
        return 'Updating data'
    elif method == 'DELETE':
        return 'Deleting data'
app.run()