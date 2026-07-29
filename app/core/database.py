from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


from app.core import settings


# Inicia a conexão com o banco
engine = create_engine(settings.DATABASE_URL)
# Criar sessões
SessionLocal = sessionmaker(bind=engine)

# Toda class que herdar Base será uma tabela no banco
class Base(DeclarativeBase):
    pass

# Busca a sessão no banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()