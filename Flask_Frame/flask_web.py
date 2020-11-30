# PS C:\Users\User\git\Flask_Frame> $env:FLASK_APP = "flask_web.py"
# PS C:\Users\User\git\Flask_Frame> python -m flask run

from flask import render_template
from flask import Flask
app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# def root():
#     title = 'My super site'
#     return f'<html><body><h1>{title}</h1></body></html>'

