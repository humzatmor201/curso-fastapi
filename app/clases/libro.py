class libro:
    titulo: str
    autor: str
    genero: str
    precio: float
    calificacion: int
    def __init__(self, titulo, autor, genero, precio, calificacion):
        self.titulo: str = titulo
        self.autor: str = autor
        self.genero: str = genero
        self.precio: float = precio
        self.calificacion: int = calificacion