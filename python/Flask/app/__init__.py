from flask import Flask
from flask_sqlalchemy import SQLAlchemy # ORM do Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' # config: Definição da URI do DB
db = SQLAlchemy(app)

from app.controllers import default
