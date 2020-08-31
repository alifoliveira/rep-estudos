from flask import Flask
from flask_sqlalchemy import SQLAlchemy # ORM do flask
from flask_script import Manager # Gerencia execução
from flask_migrate import Migrate, MigrateCommand # Gerencia migração de db

app = Flask(__name__)
app.config.from_object('config') # Seleciona configurações do server da aplicação (arquivo)

db = SQLAlchemy(app)
migrate = Migrate(app, db) # Migrate irá gerenciar as migrações do database da aplicação

manager = Manager(app) # Migrade irá gerencias os comandos da aplicação
manager.add_command('db', MigrateCommand)

from app.models import tables
from app.controllers import default
