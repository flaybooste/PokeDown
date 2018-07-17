from flask import Flask, render_template, url_for, request
from db import PokeUser, Pokedb
from flask_basicauth import BasicAuth
from netifaces import ifaddresses
from selenium import webdriver
#from flask_cache import Cache
app = Flask(__name__)
#Config BasicAuth
basic_auth = BasicAuth(app)
app.config['BASIC_AUTH_USERNAME'] = 'root'
app.config['BASIC_AUTH_PASSWORD'] = 'root'
#---------------------------------
app.config['CACHE_TYPE'] = 'simple'
#app.cache = Cache(app)
ip = ifaddresses('wlp2s0')[2][0]['addr']#linux automatic ip
#ip = '' WINDOWS MANUAL IP
@app.route("/")
def index():
    data = Pokedb().select_all_db()
    return render_template('index.html', data=data)

@app.route("/register", methods=['GET','POST'])
@basic_auth.required
def register():
    if request.method == "POST":
        PokeUser().inserir_users_db(request.form['id'],
                                    request.form['user'],
                                    request.form['pass'],
                                    request.form['pokeinit'])
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form['user'] == PokeUser().select_user(request.form['user'])[1] and request.form['pass'] == PokeUser().select_user(request.form['user'])[2]:
            user = PokeUser().select_user(request.form['user'])[0],PokeUser().select_user(request.form['user'])[1],PokeUser().select_user(request.form['user'])[3]
            return render_template('user.html', user=user)
        else:
            err = "Login incorreto"
            return render_template('login.html', error=err)
    else:
        return render_template('login.html')

@app.route("/battle")
def battle():
    pokes = Pokedb().select_one_db(1), Pokedb().select_one_db(4)
    return render_template('battle.html', pokes=pokes)


app.run(ip,debug=True)
