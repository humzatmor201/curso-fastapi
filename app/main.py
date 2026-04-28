from fastapi import FastAPI
from libros.libros import LIBROS

app = FastAPI()

# Endpoint/Metodo GET, equivalente a READ en un CRUD. Usado para consultar informacion.
# Endpoint para solo consultar libros.
@app.get("/consultar-catalogo")
async def get_catalogo():
    return LIBROS