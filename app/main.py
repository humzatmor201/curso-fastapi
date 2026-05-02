from fastapi import FastAPI, Body
from libros.libros import catalogo_libros

app = FastAPI()

catalogo = catalogo_libros()

# Endpoint/Metodo GET, equivalente a READ en un CRUD. Usado para consultar informacion.
# Endpoint para solo consultar libros.
@app.get("/consultar-catalogo")
async def consultar_catalogo():
    return catalogo.get_catalogo()

# Endpoint GET que busca un libro por id y retorna su informacion
@app.get("/consultar-catalogo/{id}")
async def buscar_libro_por_id(id: int):
    if id > catalogo.get_tamano_catalogo() - 1:
        return {
            "mensaje": "no encontrado"
        }
    return catalogo.get_libro_por_id(id)


@app.get("/consultar-catalogo")
async def filtrar_libros_por_categoria(categoria: str):
    lista_libros = []
    for libro in catalogo.get_catalogo():
        if libro.get('categoria').casefold() == categoria.casefold():
            lista_libros.append(libro)
    if not lista_libros:
        return {
            "mensaje": "no se encontraron libros"
        }
    return lista_libros


@app.get("/consultar-catalogo/{autor}")
async def filtrar_libros_por_autor(autor: str):
    lista_libros = []
    for libro in catalogo.get_catalogo():
        if libro.get('autor').casefold() == autor.casefold():
            lista_libros.append(libro)
    if not lista_libros:
        return {
            "mensaje": "no se encontraron libros"
        }
    
    return lista_libros


@app.get("/consultar-catalogo/{autor}")
async def filtrar_libros_por_autor_y_categoria(autor: str, categoria: str):
    lista_libros = []
    for libro in catalogo.get_catalogo():
        if libro.get('categoria').casefold() == categoria.casefold() and libro.get('autor').casefold() == autor.casefold():
            lista_libros.append(libro)
    if not lista_libros:
        return {
            "mensaje": "no se encontraron libros"
        }
    return lista_libros


@app.post("/agregar-libro")
async def agregar_libro(libro = Body()):
    catalogo.agregar_libro(libro)


@app.delete("/eliminar-libro/{libro}")
async def eliminar_libro_por_titulo(titulo_libro: str):
    for libro in catalogo.get_catalogo():
        if libro.get('titulo').casefold() == titulo_libro.casefold():
            libro.pop()
            return {
                "mensaje": "libro borrado"
            }
    
    return {
        "mensaje": "libro no encontrado"
    }