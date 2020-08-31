from app import db

# Definição de Banco de Dados

class User(db.Model): # Model: Modelo de tabela padrão do SQLAlchemy
    __tablename__ = "users" # Definindo do nome da tabela
    
    id = db.Column(db.Integer, primary_key=True) # Definindo coluna(chave primária)
    username = db.Column(db.String, unique=True) # Definindo coluna(campo único)
    password = db.Column(db.String) # Definindo coluna(campo não único)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        
    def __repr__(self):
        return f"<User {self.username}>"
    

class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) # Definindo chave estrangeira
    
    user = db.relationship('User', foreign_keys=user_id) # Definindo relação da chave estrangeira
    
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
        
    def __repr__(self):
        return f"<Post {self.id}"
    
    
class Follow(db.Model):
    __tablename__ = "follow"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)
    