from flask import Flask, render_template

# windows setup ____
# pip install flask
# set FLASK_APP=app
# set FLASK_ENV=development
# flask run
# visit page given



# This is a template for Flask ( a Python module for developing web apps )

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/otherPage')
def other_page():
    return render_template('otherPage.html')