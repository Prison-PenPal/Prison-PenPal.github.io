from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_mail import Mail
import pyrebase

import flask
import io

from flask_mail import Message





app = Flask(__name__)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'mohammad1.choudhury@gmail.com',
    MAIL_DEFAULT_SENDER = 'mohammad1.choudhury@gmail.com',
    MAIL_PASSWORD = 'xbmqliagmpxqwmnv',
))


mail = Mail(app)

config = {
    "apiKey": "AIzaSyCqkiwYAvaHqZSNfgaTAB00TiXgrlNw4A4",
    "authDomain": "penpals-adf5f.firebaseapp.com",
    "databaseURL": "https://penpals-adf5f.firebaseio.com",
    "projectId": "penpals-adf5f",
    "storageBucket": "penpals-adf5f.appspot.com",
    "messagingSenderId": "104129085421",
    "appId": "1:104129085421:web:4625291f08f058601831e4",
    "measurementId": "G-FKFT0CHD00"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()









@app.route("/home")
def index():

    return render_template("index.html")



@app.route("/send")
def homes():    
    return render_template("Home.html")

@app.route("/send", methods = ["POST"])
def sum():
    email = request.form["Email"]
    mess = request.form["Message"]
    msg = Message("Hi! you have just submitted your message which was " + mess,
                  sender="mohammad1.choudhury@gmail.com",
                  recipients=[email])
    
    new_event = dict(request.form)
    db.child("events").push(new_event) #replaces appending to events variable with firebase db call.
    mail.send(msg)
    return redirect("/home")



@app.route("/send", methods=["POST"])
def background_process_test():

        new_event = request.form['text']
        db.child("events").push(new_event) #replaces appending to events variable with firebase db call.
        return redirect("/send")


if __name__ == "__main__":
    app.run(debug=True)
