class catalogo_libros:

    LIBROS = [
        {'titulo': '1984', 'autor': 'george orwell', 'categoria': 'distopia'},
        {'titulo': 'Un mundo feliz', 'autor': 'aldous huxley', 'categoria': 'distopia'},
        {'titulo': 'Rebelion en la granja', 'autor': 'george orwell', 'categoria': 'distopia'},
        {'titulo': 'Buscando a Alaska', 'autor': 'john green', 'categoria': 'misterio'},
        {'titulo': 'Manifiesto comunista', 'autor': 'karl marx', 'categoria': 'politica'},
        {'titulo': 'Los carteles no existen', 'autor': 'oswaldo zavala', 'categoria': 'politica'},
        {'titulo': 'Cronica de una muerte anunciada', 'autor': 'gabriel garcía márquez', 'categoria': 'suspenso'},
        {'titulo': 'Algebra de Baldor', 'autor': 'aurelio baldor', 'categoria': 'matematicas'},
    ]

    def __init__(self):
        pass

    def get_catalogo(self):
        return self.LIBROS
    
    def get_libro_por_id(self, id: int):
        return self.LIBROS[id]
    
    def get_tamano_catalogo(self):
        return len(self.LIBROS)
    
    def agregar_libro(self, libro):
        self.LIBROS.append(libro)
