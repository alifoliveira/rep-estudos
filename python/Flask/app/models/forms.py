from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

# Formulário de login
class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()]) # Campo obrigatório
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")