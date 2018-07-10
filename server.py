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
        Database().inserir_users_db(request.form['id'],
        request.form['user'],
        request.form['pass'],
        request.form['pokeinit'])
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form['user'] == Database().select_user(request.form['user'])[1] and request.form['pass'] == Database().select_user(request.form['user'])[2]:
            print("logado")
            return "logado"
    return render_template('login.html')
app.run(ip,debug=True)
