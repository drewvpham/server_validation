# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")
  
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['name'])< 1:
        flash("Name cannot be blank!")
    elif len(request.form['comments'])<1:
        flash("Comments cant be blank!")
    else:
        flash("Success!")
    return redirect('/')
app.run(debug=True)
