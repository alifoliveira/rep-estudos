from flask import render_template
from app import app


@app.route("/index/<user>") # Define a rota da página (function) abaixo
@app.route("/", defaults={"user":None})
def index(user):
    return render_template('index.html', user=user)
