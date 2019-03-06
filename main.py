from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import geocoder
from datetime import datetime
import pickle


app = Flask(__name__)


def login():
    geocode = geocoder.ip('me')
    lat, lng = geocode.latlng
    now = datetime.now()
    time = int((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds())
    return "You've logged in from {lat}, {lng} at {time}".format(lat=lat, lng=lng, time=time)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return login()


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


if __name__ == "__main__":
    # model_file = open('classifier.pkl','rb')
    # classifier = pickle.load(model_file)
    # print("Imported knowledge")
    # model_file.close()

    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
