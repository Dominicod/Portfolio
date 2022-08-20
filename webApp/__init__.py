from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
import requests

app = Flask(__name__)

# Configures variables for mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '#'
app.config['MAIL_PASSWORD'] = '#'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['CAPTCHA_API'] = '#'
mail = Mail(app)

app.config['SECRET_KEY'] = '#'
SECRET_KEY = app.config['SECRET_KEY']


# Main route to portfolio
@app.route('/', methods=['GET'])
def index():
    title = 'Portfolio'

    return render_template('index.html', title=title)


# Route for contacted, receives form information and returns the user to /contacted and sends the emails
@app.route('/contacted', methods=['GET', 'POST'])
def contacted():
    title = 'Contacted'
    name = request.form.get('name')
    email = request.form.get('email')
    company = request.form.get('company')
    text = request.form.get('text')
    captcha = request.form.get('g-recaptcha-response')

    if not captcha:
        flash('Captcha not selected', 'error')
        return redirect('/#contact')

    if not name or not email or not company or not text:
        flash('All fields not provided', 'error')
        return redirect('/#contact')

    # Email spam filter

    recaptcha_url = f"https://www.google.com/recaptcha/api/siteverify?response={captcha}&secret={app.config['CAPTCHA_API']}"
    response = requests.get(recaptcha_url)
    json_data = response.json()

    # If email exists, continue to send, else throw exception
    if json_data['success']:
        message = "Thank you for contacting Dominic O'Donnell. Extremely excited for this opportunity to reach out " \
                  "and I will be in touch with you as soon as possible! My personal email is: " \
                  "dominicodonnell99@gmail.com if you wish to reach out further. "
        msg = Message('Thank you for contacting!', sender=app.config['MAIL_USERNAME'], recipients=[email])
        msg.body = message

        # Attempts to send message to receiver.
        try:
            mail.send(msg)
        except:
            print("Exception thrown. Receiver")

        message = f"Hello, my name is {name}, and I work for {company}. My email is {email}. I'd like to say: {text}"
        msg = Message('Contacted from Portfolio', sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = message

        # Attempts to send message to sender.
        try:
            mail.send(msg)
        except:
            print("Exception thrown. Sender")

        return render_template('contacted.html', title=title, name=name)
    else:
        flash('Captcha Failed', 'error')
        return redirect('/#contact')


if __name__ == '__main__':
    app.run()
