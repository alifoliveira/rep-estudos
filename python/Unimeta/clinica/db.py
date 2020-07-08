import sqlite3

c = sqlite3.connect('clinica.db')
conexao = c.cursor()

conexao.execute("""
CREATE table if not exists cliente(
    id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR NOT NULL,
    telefone VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    cep VARCHAR NOT NULL,
    numero VARCHAR NOT NULL
);
""")

conexao.execute("""
CREATE TABLE IF NOT EXISTS animal(
    id_animal INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR NOT NULL,
    raca VARCHAR NOT NULL,
    peso VARCHAR NOT NULL
);
""")

conexao.execute("""
CREATE TABLE IF NOT EXISTS cliente_animal(
    id_cliente_animal INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    fk_cliente INTEGER,
    fk_animal INTEGER,
    FOREIGN KEY(fk_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY(fk_animal) REFERENCES animal(id_animal)
);
""")

conexao.execute("""
CREATE TABLE IF NOT EXISTS veterinarios(
    id_veterinario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR NOT NULL,
    telefone VARCHAR NOT NULL,
    email VARCHAR NOT NULL

);
""")

conexao.execute("""
CREATE TABLE IF NOT EXISTS exames(
    id_exame INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR NOT NULL,
    tipo VARCHAR NOT NULL,
    dia VARCHAR NOT NULL,
    horario VARCHAR NOT NULL
    
);
""")

conexao.execute("""
CREATE TABLE IF NOT EXISTS consulta(
    id_consulta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR NOT NULL,
    dia VARCHAR NOT NULL,
    horario VARCHAR NOT NULL
);
""")

c.commit()
conexao.close()