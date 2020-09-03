DEBUG = True # Ativa/Desativa report de debug da ablicação | ↓
# Server reinicia automaticamente após alteração    ←

SQLALCHEMY_DATABASE_URI = ('sqlite+pysqlite:///storage.db') # Definição da URI do DB
SQLALCHEMY_TRACK_MODIFICATIONS = True # Desabilita Warning de rastreio de modificações

SECRET_KEY = 'A1B-J82-532-137'
