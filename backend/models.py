from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, ForeignKey
from sqlalchemy.orm import sessionmaker

# ---------------------------
# Configuración de la base de datos
# ---------------------------
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
SessionLocal = sessionmaker(bind=engine)

# ---------------------------
# Tablas
# ---------------------------
users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String, nullable=False),
    Column("correo", String, unique=True, nullable=False),
    Column("rol", String, nullable=False),
)

tasks_table = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("titulo", String),
    Column("fecha", String),
    Column("destinatario", String),
    Column("mensaje", String),
    Column("notificaciones", String),
    Column("estado", String),
    Column("user_id", Integer, ForeignKey("users.id")),  # Relación con usuario
)

# Crear tablas si no existen
metadata.create_all(engine)
