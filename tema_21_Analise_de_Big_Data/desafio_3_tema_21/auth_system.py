from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração da conexão com o banco de dados SQLite
DATABASE_URL = 'sqlite:///./test.db'

# Criar engine e base
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Definir o modelo User


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)


# Criar todas as tabelas
Base.metadata.create_all(bind=engine)

# Configurar a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Função para adicionar um novo usuário


def add_user(username: str, password: str):
    db_user = User(username=username, password=password)
    session.add(db_user)
    session.commit()
    return db_user

# Função para autenticar um usuário


def authenticate_user(username: str, password: str):
    db_user = session.query(User).filter(
        User.username == username, User.password == password).first()
    return db_user


# Exemplo de uso
if __name__ == "__main__":
    # Adicionar usuários
    add_user('alice', 'password123')
    add_user('bob', 'password456')

    # Autenticar usuários
    user = authenticate_user('alice', 'password123')
    if user:
        print(f'User {user.username} authenticated successfully!')
    else:
        print('Authentication failed!')
