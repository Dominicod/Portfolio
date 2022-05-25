from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail=Mail(app)

# Configures varibles for mail server
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
SECRET_KEY = app.config['SECRET_KEY']

# Main route to portfolio
@app.route('/', methods=['GET'])
def index():
    title = 'Portfolio'

    return render_template('index.html', title=title)

# Route for contacted, recieves form information and returns the user to /contacted and sends the emails
@app.route('/contacted', methods=['GET', 'POST'])
def contacted():
    title = 'Contacted'

    name = request.form.get('name')
    email = request.form.get('email')
    company = request.form.get('company')
    text = request.form.get('text')

    if not name or not email or not company or not text:
        flash('All fields not provided', 'error')
        return redirect('/#contact')

    message = "Thank you for contacting Dominic O'Donnell. Extremely excited for this opportunity to reach out and I will be in touch with you as soon as possible! My personal email is: dominicodonnell99@gmail.com if you wish to reach out further."
    
    msg = Message('Thank you for contacting!', sender = app.config['MAIL_USERNAME'], recipients = [email])
    msg.body = message
    mail.send(msg)

    message = f"Hello, my name is {name}, and I work for {company}. My email is {email}. I'd like to say: {text}"

    msg = Message('Contacted from Portfolio', sender = app.config['MAIL_USERNAME'], recipients = [app.config['MAIL_USERNAME']])
    msg.body = message
    mail.send(msg)

    return render_template('contacted.html', title=title, name=name)

if __name__ == '__main__':
    app.run()