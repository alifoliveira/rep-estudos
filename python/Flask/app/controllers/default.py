from flask import render_template
from app import app


@app.route("/index") # Define a rota da página (function) abaixo
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('base.html')
