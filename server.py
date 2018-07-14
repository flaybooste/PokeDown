from flask import Flask, render_template, url_for, request
from db import Database
from flask_basicauth import BasicAuth
import os
from netifaces import ifaddresses
from flask_admin.contrib.sqla import ModelView
app = Flask(__name__)
#Config BasicAuth
basic_auth = BasicAuth(app)
app.config['BASIC_AUTH_USERNAME'] = 'root'
app.config['BASIC_AUTH_PASSWORD'] = 'root'
#---------------------------------
ip = ifaddresses('wlp2s0')[2][0]['addr'] 
#ip = '192.168.0.2'  
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
            user = Database().select_user(request.form['user'])[0],Database().select_user(request.form['user'])[1],Database().select_user(request.form['user'])[3]
            return render_template('user.html', user=user)
        else:
            print("login incorreto")
    else:
        return render_template('login.html')
@app.route("/battle")
def battle():
    pokes = Database().select_one_db(1), Database().select_one_db(4)
    return render_template('battle.html', pokes=pokes)

app.run(ip,debug=True)
