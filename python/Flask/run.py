from app import manager


# Verificação de execução
if __name__ == "__main__":
    manager.run()

# python run.py runserver (rodar aplicação)
# python run.py db init (cria estrutura de migração)

# Necessário após toda alteração estrutural do banco
#    python run.py db migrate (prepara migração)
#    python run.py db upgrade (realiza migração)
