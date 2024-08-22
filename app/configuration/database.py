from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import DBSettings


db_settings = DBSettings()


engine = create_engine(db_settings.DB_URL, connect_args={"check_same_thread": False})

SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Fournit une session de base de données aux dépendances FastAPI.
    Gère automatiquement l'ouverture et la fermeture des connexions.
    """
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

