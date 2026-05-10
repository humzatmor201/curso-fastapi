from fastapi import FastAPI
from clases.catalogo_libros import catalogo_libros
from schemas_pydantic.esquema_libro import esquema_libro
from clases.libro import libro
from clases.enum_filtro import enum_filtro


app = FastAPI()

catalogo = catalogo_libros()


@app.get("/consultar-catalogo/")
async def consultar_catalogo_completo():
    return catalogo.get_catalogo()


@app.get("/consultar-catalogo/{filtro}/")
async def filtrar_libros_por_informacion_especifica(filtro: enum_filtro, info: str):
    return catalogo.adjuntar_libros_filtrados(filtro, info)


@app.post("/agregar-libro/")
async def agregar_libro(libro_request: esquema_libro):
    nuevo_libro = libro(**libro_request.model_dump())
    catalogo.agregar_libro(nuevo_libro)


@app.put("/actualizar-libro/")
async def actualizar_informacion_de_libro_buscando_por_id(id: int, libro_request: esquema_libro):
    if id <= catalogo.get_tamano_catalogo() and id > 0:
        libro_previo = catalogo.get_libro_por_id(id - 1)
        catalogo.get_catalogo()[id - 1] = libro(**libro_request.model_dump())
        return {
            "mensaje": "informacion actualizada",
            "info_previa": libro_previo,
            "info_nueva": catalogo.get_libro_por_id(id - 1)
        }
    
    return {
        "mensaje": "id no valido"
    }


@app.put("/actualizar-libro/{titulo}/")
async def actualizar_informacion_de_libro_buscando_por_titulo(titulo: str, libro_request: esquema_libro):
    for libro_ in catalogo.get_catalogo():
        if libro_.get_titulo().casefold() == titulo.casefold():
            libro_previo = libro_
            catalogo.get_catalogo()[catalogo.get_catalogo().index(libro) - 1] = libro(**libro_request.model_dump())
            return {
            "mensaje": "informacion actualizada",
            "info_previa": libro_previo,
            "info_nueva": catalogo.get_libro_por_id(id - 1)
        }
    
    return {
        "mensaje": "libro no encontrado"
    }


@app.delete("/eliminar-libro/{titulo}/")
async def eliminar_libro_buscando_por_titulo(titulo: str):
    for libro in catalogo.get_catalogo():
        if libro.get_titulo().casefold() == titulo.casefold():
            libro.pop()
            return {
                "mensaje": "libro borrado"
            }
    
    return {
        "mensaje": "libro no encontrado"
    }