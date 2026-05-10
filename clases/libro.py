class libro:

    def __init__(self, titulo, autor, genero, descripcion, calificacion, fecha_publicacion):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__descripcion = descripcion
        self.__calificacion = calificacion
        self.__fecha_publicacion = fecha_publicacion
    

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion
    
    def set_fecha_publicacion(self, fecha_publicacion):
        self.__fecha_publicacion = fecha_publicacion
    

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo


    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor

    
    def get_genero(self):
        return self.__genero
    
    def set_genero(self, genero):
        self.__genero = genero
    

    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    

    def get_calificacion(self):
        return self.__calificacion
    
    def set_calificacion(self, calificacion):
        self.__calificacion = calificacion