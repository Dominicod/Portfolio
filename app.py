from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacted')
def contacted():
    return "<h1>Thank you!</h1>"