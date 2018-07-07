from flask import Flask, render_template, url_for
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
#adm = Admin(app, name="PokeDown", template_mode='bootstrap3')
#adm.add_view(ModelView(Database().select_all_db()))

@app.route("/")
def index():
    data = Database().select_all_db()
    return render_template('index.html', data=data)

app.run(debug=True)

