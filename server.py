from flask import Flask, render_template, url_for
'''from selenium import webdriver'''
from db import Database
import os
app = Flask(__name__)

@app.route("/")
def index():

    data = Database().select_all_db()
    return render_template('index.html', data=data)

app.run(debug=True)
