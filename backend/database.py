from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de la base de datos SQLite
DATABASE_URL = "sqlite:///./gestor_tareas.db"

# Engine de SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para los modelos
Base = declarative_base()
