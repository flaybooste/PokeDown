from flask import Flask, render_template, url_for, request
from db import Database
from flask_basicauth import BasicAuth
import os
from flask_admin.contrib.sqla import ModelView
app = Flask(__name__)
#Config BasicAuth
basic_auth = BasicAuth(app)
app.config['BASIC_AUTH_USERNAME'] = 'root'
app.config['BASIC_AUTH_PASSWORD'] = 'root'
#---------------------------------
import socket
ip = socket.gethostbyname(socket.gethostname())

@app.route("/")
def index():
    data = Database().select_all_db()
    return render_template('index.html', data=data)

@app.route("/register", methods=['GET','POST'])
@basic_auth.required
def register():
    if request.method == "POST":
        print(request.form['id'])
        print(request.form['user'])
        print(request.form['pass'])
        print(request.form['pokeinit'])
    return render_template("register.html")

app.run(ip,debug=True)
