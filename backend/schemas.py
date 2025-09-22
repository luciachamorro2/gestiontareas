from pydantic import BaseModel
from datetime import datetime

class NotificacionSchema(BaseModel):
    id: int
    tarea_id: int
    fecha_envio: datetime
    tipo: str

    class Config:
        orm_mode = True
