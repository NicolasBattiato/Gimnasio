from app.Conexion import Conexion
from app.CursorPOOL import CursorPOOL


class Clase:
    def __init__(self, id, nombre, horario):
        self._id = id
        self._nombre = nombre
        self._horario = horario

    def __str__(self):
        return f"""
                ID: {self._id}
                Nombre: {self._nombre}
                Horario: {self._horario}
                """

    @staticmethod
    def crearTabla():

        tablas = (
            """
            CREATE TABLE IF NOT EXISTS clases (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                horario TIMESTAMP NOT NULL
            )
            """
            ,
        )
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            for tabla in tablas:
                cursor.execute(tabla)
            conexion.commit()
            cursor.close()
            print(f"Tablas creadas exitosamente...")
        except Exception as e:
            print(f"Ocurrio un error: {e}...")
        finally:
            if conexion:
                Conexion.liberarConexion(conexion)



    # OPERACIONES CRUD

    @staticmethod
    def AgregarClase(nombre, horario):
        with CursorPOOL() as cursor:
            cursor.execute("INSERT INTO clases (nombre, horario) VALUES (%s, %s)", (nombre, horario))
            return cursor.rowcount

    @staticmethod
    def ActualizarClase(id, nombre, horario):
        with CursorPOOL() as cursor:
            cursor.execute("UPDATE clases set nombre=%s, horario=%s WHERE id=%s ", (nombre, horario, id))
            return cursor.rowcount

    @staticmethod
    def eliminarClase(id):

        with CursorPOOL() as cursor:
            cursor.execute("DELETE FROM clases WHERE id=%s", (id, ))
            return cursor.rowcount

    @staticmethod
    def listarClase():
        with CursorPOOL() as cursor:
            cursor.execute("SELECT * FROM clases")
            registros = cursor.fetchall()
            listaClases = []
            for registro in registros:
                clase = Clase(registro[0], registro[1], registro[2])
                listaClases.append(clase)

            return listaClases



