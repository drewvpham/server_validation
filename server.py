# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NOMBERS = re.compile(r'[0-9]')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():

  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    session['email']=request.form['email']
    session['first_name']=request.form['first_name']
    session['last_name']=request.form['last_name']
    session['password']=request.form['password']
    session['confirm_password']=request.form['confirm_password']
    message=[]
    if len(session['email'])==0 or len(session['first_name'])==0 or len(session['last_name'])==0 or len(session['password'])==0 or len(session['confirm_password'])==0:
        message.append("All fields are required and must not be blank!")
        print len(session['email']), len(session['first_name']), len(session['last_name']), len(session['password']), len(session['confirm_password'])
    if not EMAIL_REGEX.match(session['email']):
        message.append("Invalid Email Address!")
    if len(session['password'])<8:
        message.append("Password should be more than 8 characters!")
    if session['password'] is not session['confirm_password']:
        message.append("Password and Password Confirmation should match")
    if NOMBERS.match(session['first_name']) or NOMBERS.match(session['last_name']):
        message.append("Why the fuck is there a number in your name?")
    flash(message)

    return redirect('/')
app.run(debug=True)
