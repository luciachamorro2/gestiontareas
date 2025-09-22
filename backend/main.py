from fastapi import FastAPI
from models import engine, SessionLocal, users_table, tasks_table
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="Gestor de Tareas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URL del frontend Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------
# Inicializar datos de prueba
# ---------------------------
def init_data():
    with SessionLocal() as session:
        # Usuarios
        if not session.execute(users_table.select()).fetchall():
            session.execute(
                users_table.insert(),
                [
                    {"nombre": "Ana", "correo": "ana@mail.com", "rol": "admin"},
                    {"nombre": "Luis", "correo": "luis@mail.com", "rol": "user"},
                ],
            )
            session.commit()

        # Tareas
        if not session.execute(tasks_table.select()).fetchall():
            session.execute(
                tasks_table.insert(),
                [
                    {
                        "titulo": "Enviar informe",
                        "fecha": "2025-09-20",
                        "destinatario": "Jefe de proyecto",
                        "mensaje": "Informe semanal del avance",
                        "notificaciones": "Email",
                        "estado": "Pendiente",
                        "user_id": 1,
                    },
                    {
                        "titulo": "Revisión diseño",
                        "fecha": "2025-09-21",
                        "destinatario": "Equipo UI/UX",
                        "mensaje": "Feedback del mockup",
                        "notificaciones": "Slack",
                        "estado": "Completada",
                        "user_id": 2,
                    },
                ],
            )
            session.commit()

# Inicializar datos al arrancar
init_data()

# ---------------------------
# Endpoints
# ---------------------------
@app.get("/tasks")
def get_tasks():
    with SessionLocal() as session:
        rows = session.execute(tasks_table.select()).mappings().all()
        return list(rows)

@app.get("/users")
def get_users():
    with SessionLocal() as session:
        users = session.execute(users_table.select()).mappings().all()
        result = []

        for u in users:
            user_dict = dict(u)  # convertir RowMapping a dict
            tasks = session.execute(
                tasks_table.select().where(tasks_table.c.user_id == user_dict["id"])
            ).mappings().all()
            user_dict["tareas"] = [t["titulo"] for t in tasks]
            result.append(user_dict)

        return result
