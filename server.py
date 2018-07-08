from flask import Flask, render_template, url_for, request
from db import Database
from flask_admin import Admin
from flask_basicauth import BasicAuth
import os
from flask_admin.contrib.sqla import ModelView
app = Flask(__name__)
#Config BasicAuth
basic_auth = BasicAuth(app)
app.config['BASIC_AUTH_USERNAME'] = 'root'
app.config['BASIC_AUTH_PASSWORD'] = 'root'
#---------------------------------

@app.route("/")
def index():
    data = Database().select_all_db()
    return render_template('index.html', data=data)

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == "POST":
        print(request.form['user'])
    return render_template("register.html")

app.run(debug=True)

