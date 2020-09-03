from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm


@app.route("/index") # Define a rota da página (function) abaixo
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm() # instancia do flask form (formulario de login)
    if form.validate_on_submit(): # Verifica se o formulario de login foi enviado
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)
