from pydantic import BaseModel, Field
from clases.libro import libro

class esquema_libro(BaseModel, libro):
    titulo: str
    autor: str
    genero: str
    descripcion: str
    calificacion: int = Field(gt = -1, lt = 11)
    fecha_publicacion: int