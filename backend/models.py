from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, Enum, DateTime
from sqlalchemy.orm import relationship
from database import Base  # Importamos la Base desde database.py

class Rol(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    rol_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    google_id = Column(String(100), unique=True, nullable=True)

    rol = relationship('Rol')

class Estado(Base):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)

class Tarea(Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=True)
    fecha_creacion = Column(Date, nullable=False)
    fecha_limite = Column(Date, nullable=True)
    estado_id = Column(Integer, ForeignKey('estados.id'), nullable=False)
    creador_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    asignado_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    estado = relationship('Estado')
    creador = relationship('Usuario', foreign_keys=[creador_id])
    asignado = relationship('Usuario', foreign_keys=[asignado_id])

class Notificacion(Base):
    __tablename__ = 'notificaciones'
    id = Column(Integer, primary_key=True)
    tarea_id = Column(Integer, ForeignKey('tareas.id'), nullable=False)
    fecha_envio = Column(DateTime, nullable=False)
    tipo = Column(Enum('diaria', 'semanal', 'última semana', name='tipo_notificacion'), nullable=False)

    tarea = relationship('Tarea')
