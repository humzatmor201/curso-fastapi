from app.servicios.bd import gestor_bd
from fastapi import FastAPI

bd = gestor_bd("localhost", "root", "root", "prueba_bd")

app = FastAPI()

@app.post("/agregar-libro/")
def agregar_libro(titulo: str = None,
                     autor: str = None,
                     genero: str = None,
                     precio: float = None,
                     calificacion: int = None):
    bd.insert_into("tabla_prueba", {"titulo": titulo,
                                    "autor": autor,
                                    "genero": genero,
                                    "precio": precio,
                                    "calificacion": calificacion})

@app.get("/consultar-catalogo/")
def consultar_catalogo_completo():
    return bd.select("tabla_prueba")

@app.get("/filtrar-catalogo/")
def filtrar_catalogo(titulo: str = None,
                     autor: str = None,
                     genero: str = None,
                     precio: float = None,
                     calificacion: int = None):
    return bd.select("tabla_prueba", {"titulo": titulo,
                                      "autor": autor,
                                      "genero": genero,
                                      "precio": precio,
                                      "calificacion": calificacion})

@app.put("/actualizar-catalogo/{titulo}/")
def actualizar_info_de_libro_filtrando_por_titulo(titulo: str, titulo_nuevo: str = None,
                                                               autor: str = None,
                                                               genero: str = None,
                                                               precio: float = None,
                                                               calificacion: int = None):
    
    bd.update("tabla_prueba", {"titulo": titulo_nuevo,
                               "autor": autor,
                               "genero": genero,
                               "precio": precio,
                               "calificacion": calificacion}, {"titulo": titulo})

@app.delete("/eliminar-libro/{titulo}/")
def eliminar_libro(titulo: str):
    bd.delete("tabla_prueba", {"titulo": titulo})