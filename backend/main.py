from fastapi import FastAPI, HTTPException
from datetime import date
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Rol, Usuario, Estado, Tarea
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel




class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    rol: str

app = FastAPI(title="Gestor de Tareas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # puerto de Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Crear todas las tablas
Base.metadata.create_all(bind=engine)

# ---------------------------
# Función para inicializar datos de prueba
# ---------------------------
def init_data():
    with Session(engine) as session:
        # Roles
        if not session.query(Rol).first():
            admin = Rol(nombre="Admin")
            user = Rol(nombre="User")
            session.add_all([admin, user])
            session.commit()

        # Estados
        if not session.query(Estado).first():
            pendiente = Estado(nombre="Pendiente")
            completada = Estado(nombre="Completada")
            boceto = Estado(nombre="Boceto")
            session.add_all([pendiente, completada, boceto])
            session.commit()

        # Usuarios
        if not session.query(Usuario).first():
            admin_role = session.query(Rol).filter_by(nombre="Admin").first()
            user_role = session.query(Rol).filter_by(nombre="User").first()
            u1 = Usuario(nombre="Ana", email="ana@mail.com", rol=admin_role)
            u2 = Usuario(nombre="Luis", email="luis@mail.com", rol=user_role)
            session.add_all([u1, u2])
            session.commit()

        # Tareas
        if not session.query(Tarea).first():
            u1 = session.query(Usuario).filter_by(nombre="Ana").first()
            u2 = session.query(Usuario).filter_by(nombre="Luis").first()
            pendiente = session.query(Estado).filter_by(nombre="Pendiente").first()
            completada = session.query(Estado).filter_by(nombre="Completada").first()

            t1 = Tarea(
                titulo="Enviar informe",
                descripcion="Informe semanal del avance",
                fecha_creacion=date(2025, 9, 20),
                fecha_limite=date(2025, 9, 21),
                estado=pendiente,
                creador=u1,
                asignado=u2
            )
            t2 = Tarea(
                titulo="Revisión diseño",
                descripcion="Feedback del mockup",
                fecha_creacion=date(2025, 9, 21),
                fecha_limite=date(2025, 9, 22),
                estado=completada,
                creador=u2,
                asignado=u1
            )
            session.add_all([t1, t2])
            session.commit()

# Inicializar datos
init_data()

# ---------------------------
# Endpoints
# ---------------------------

@app.get("/users")
def get_users():
    with SessionLocal() as session:
        usuarios = session.query(Usuario).all()
        result = []
        for u in usuarios:
            tareas = [t.titulo for t in session.query(Tarea).filter(Tarea.asignado_id == u.id).all()]
            result.append({
                "id": u.id,
                "nombre": u.nombre,
                "correo": u.email,
                "rol": u.rol.nombre,
                "tareas": tareas
            })
        return result
    

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with SessionLocal() as session:
        usuario = session.query(Usuario).filter(Usuario.id == user_id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        session.delete(usuario)
        session.commit()
        return {"detail": f"Usuario {user_id} eliminado correctamente"}


@app.get("/tasks")
def get_tasks():
    with SessionLocal() as session:
        tareas = session.query(Tarea).all()
        result = []
        for t in tareas:
            estado_nombre = t.estado.nombre if t.estado else None
            asignado_nombre = t.asignado.nombre if t.asignado else None
            result.append({
                "id": t.id,
                "titulo": t.titulo,
                "descripcion": t.descripcion,
                "fecha_creacion": str(t.fecha_creacion),
                "fecha_limite": str(t.fecha_limite) if t.fecha_limite else None,
                "estado": estado_nombre,
                "asignado": asignado_nombre,
                "creador": t.creador.nombre if t.creador else None
            })
        return result

@app.post("/users")
def create_user(usuario: UsuarioCreate):
    with SessionLocal() as session:
        rol = session.query(Rol).filter_by(nombre=usuario.rol).first()
        if not rol:
            raise HTTPException(status_code=400, detail="Rol no válido")
        
        nuevo_usuario = Usuario(
            nombre=usuario.nombre,
            email=usuario.email,
            rol=rol
        )
        session.add(nuevo_usuario)
        session.commit()
        session.refresh(nuevo_usuario)
        return {
            "id": nuevo_usuario.id,
            "nombre": nuevo_usuario.nombre,
            "email": nuevo_usuario.email,
            "rol": nuevo_usuario.rol.nombre
        }