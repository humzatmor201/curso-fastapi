from clases.libro import libro

class catalogo_libros:

    __LIBROS = [
        libro('1984', 'George Orwell', 'Distopia', 'Una Inglaterra post-Segunda Guerra Mundial vive bajo el yugo del Gran Hermano', 10, 1949),
        libro('Un Mundo Feliz', 'Aldous Huxley', 'Distopia', 'Conceptos como La Caja Del Placer mantienen sumisa a la sociedad', 9, 1932),
        libro('Rebelion en la Granja', 'George Orwell', 'Distopia', 'Cualquier parecido con la realidad no es coincidencia', 10, 1945),
        libro('Buscando a Alaska', 'John Green', 'Misterio', 'La misteriosa muerte de Alaska pone a todo el grupo de amigos de El Flaco en entredicho', 8, 2005),
        libro('El Manifiesto Comunista', 'Karl Marx', 'Politica', 'Karl Marx expone su idea de como la economia de una sociedad debe evolucionar', 8, 1848),
        libro('Los Carteles No Existen', 'Oswaldo Zavala', 'Politica', 'Oswaldo expone como la clase politica es culpable del narcotrafico', 10, 2018),
        libro('Cronica de una muerte anunciada', 'Gabriel Garcia Marquez', 'Suspenso', 'No se, no lo he leido', 9, 1981),
        libro('Algebra de Baldor', 'Aurelio Baldor', 'Matematicas', 'Un clasico para aprender algebra basica', 10, 1941)
    ]

    def __init__(self):
        pass

    def get_catalogo(self):
        return self.__LIBROS
    
    def get_libro_por_id(self, id: int):
        return self.__LIBROS[id - 1]
    
    def get_tamano_catalogo(self):
        return len(self.__LIBROS)
    
    def agregar_libro(self, libro):
        self.__LIBROS.append(libro)

    def ajustar_filtro(self, filtro: str, info: str, libro: libro):
        match filtro:
            case 'autor':
                return libro.get_autor().casefold() == info.casefold()
            case 'genero':
                return libro.get_genero().casefold() == info.casefold()
            case 'calificacion':
                return libro.get_calificacion() == int(info)
            case 'fecha_publicacion':
                return libro.get_fecha_publicacion() == int(info)

    def filtrar_libros_de_lista(self, filtro: str, info: str, libros):
        libros_filtrados = []
        for libro in libros:
            if self.ajustar_filtro(filtro, info, libro):
                libros_filtrados.append(libro)
        return libros_filtrados
                
    def adjuntar_libros_filtrados(self, filtro: str, info: str, lista_libros = [None]):
        if lista_libros == None:
            return self.filtrar_libros_de_lista(filtro, info, self.get_catalogo())
        else:
            return self.filtrar_libros_de_lista(filtro, info, lista_libros)
