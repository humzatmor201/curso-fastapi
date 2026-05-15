import mysql.connector

class gestor_bd:
    def __init__(self, host, user, password, nombre_database):
        self.host = host
        self.user = user
        self.password = password
        self.nombre_database = nombre_database

# Métodos CRUD para gestionar la información de la base de datos
    # INSERT INTO
    def insert_into(self, nombre_tabla, dict_objeto: dict):
        lista_propiedades = ""
        lista_valores = ""
        try:
            database = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.nombre_database
            )
            cursor_db = database.cursor()
            for key in dict_objeto.keys():
                lista_propiedades = lista_propiedades + str(key) + ", "
                lista_valores = lista_valores + "'" + str(dict_objeto[key]) + "'" + ", "

            cursor_db.execute(f"INSERT INTO {nombre_tabla} ({lista_propiedades.strip()[:-1]}) VALUES ({lista_valores.strip()[:-1]});")
            database.commit()
        except mysql.connector.Error as err:
            print(f"Error al agregar entidad a base de datos: {err}")
    
    # SELECT
    def select(self, nombre_tabla, condicion_where: dict = None):
        try:
            database = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.nombre_database
            )
            cursor_db = database.cursor()
            if not condicion_where:
                # Retorna toda la tabla
                cursor_db.execute(f"SELECT * FROM {nombre_tabla}")
            else:
                # Retorna solo las columnas istadas en query_keys de las filas especificadas en la condicion de WHERE
                cursor_db.execute(f"SELECT * FROM {nombre_tabla} WHERE {self.armar_filtro_where(condicion_where)}")
            return self.sql_response_2_dict_list("tabla_prueba", cursor_db.fetchall())
        except mysql.connector.Error as err:
            print(f"Error al intentar consultar la base de datos: {err}")
        
    # UPDATE
    def update(self, nombre_tabla, set: dict, condicion_where: dict):
        try:
            database = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.nombre_database
            )
            cursor_db = database.cursor()
            cursor_db.execute(f"UPDATE {nombre_tabla} SET {self.armar_set_query(set)} WHERE {self.armar_filtro_where(condicion_where)};")
            database.commit()
        except mysql.connector.Error as err:
            print(f"Error al intentar actualizar base de datos: {err}")

    # DELETE
    def delete(self, nombre_tabla, condicion_where: dict):
        try:
            database = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.nombre_database
            )
            cursor_db = database.cursor()
            cursor_db.execute(f"DELETE FROM {nombre_tabla} WHERE {self.armar_filtro_where(condicion_where)};")
            database.commit()
        except mysql.connector.Error as err:
            print(f"Error al intentar actualizar base de datos: {err}")

    # CREATE TABLE
    def create_table(self, nombre_tabla, objeto: any):
        try:
            database = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.nombre_database
            )
            cursor_db = database.cursor()
            if not self.existe(nombre_tabla, "TABLE"):
                cursor_db.execute(f"CREATE TABLE {nombre_tabla} ({self.armar_query_columnas(objeto)});")
        except mysql.connector.Error as err:
            print(f"Hubo un error al crear la tabla: {err}")

    #CREATE DATABASE
    def create_database(self):
        database = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
            )
        cursor_db = database.cursor()
        if not self.existe(self.nombre_database, "DATABASE"):
            cursor_db.execute(f"CREATE DATABASE {self.nombre_database};")

# Metodos con logica de negocio separada por responsabilidades
# Cualquier algoritmo que no sea directamente gestionar la base de datos, colocar aqui debajo
    def conectarse_a_bd(self):
        try:
            database = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.nombre_database
            )
            cursor_db = database.cursor()

            return database, cursor_db
        except mysql.connector.Error as err:
            print(f"Error al intentar conectarse a la base de datos: {err}")

    def armar_query_columnas(self, objeto: any):
        dict_parametros = self.extraer_atributos_de_clase_y_tipos(objeto)
        query_armada = ""
        for key in dict_parametros.keys():
            match str(dict_parametros.get(key)):
                case "<class 'int'>":
                    query_armada = query_armada + " " + key + " " + "int" + ", "
                case "<class 'float'>":
                    query_armada = query_armada + " " + key + " " + "float" + ", "
                case "<class 'bool'>":
                    query_armada = query_armada + " " + key + " " + "bool" + ", "
                case "<class 'str'>":
                    query_armada = query_armada + " " + key + " " + "varchar(255), "
        return query_armada.strip()[:-1]
    
    def obj_2_sql_query(self, dict: dict):
        keys_query = ""
        values_query = ""

        for key in dict.keys():
            keys_query = keys_query + str(key) + ", "
            values_query = values_query + str(dict.get(key)) + ", "
        return keys_query.strip()[:-1], values_query.strip()[:-1]
    
    def sql_response_2_dict_list(self, nombre_tabla, sql_response):
        database = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.nombre_database
            )
        cursor_db = database.cursor()
        cursor_db.execute(f"DESCRIBE {nombre_tabla}")
        nombre_columnas = []
        result = []
        for columna in cursor_db.fetchall():
            nombre_columnas.append(columna[0])
        for sub_resp in sql_response:
            result.append(dict(zip(nombre_columnas, sub_resp)))
        return result
    
    def armar_set_query(self, dict: dict):
        query = ""

        for key in dict.keys():
            if not dict[key]:
                continue
            query = query + str(key) + "=" + "'" + str(dict.get(key)) + "'" + ", "
        return query[:-2]
    
    def armar_filtro_where(self, filtros: dict):
        filtro_query = ""
        for key in filtros.keys():
            if not filtros[key]:
                continue
            filtro_query = filtro_query + str(key) + "=" + "'" + str(filtros[key]) + "'" + " AND "
        return filtro_query[:-5]

    def existe(self, nombre, tabla_o_bd):
        try:
            database = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.nombre_database
            )
            cursor_db = database.cursor()
            cursor_db.execute(f"SHOW {tabla_o_bd}" + "S")
            for obj in cursor_db:
                if nombre in obj:
                    return True
            return False
        except mysql.connector.Error as err:
            print(f"Error al comprobar existencia: {err}")
    
    def extraer_atributos_de_clase_y_tipos(self, clase: any):
        return clase.__annotations__




            
    

        
