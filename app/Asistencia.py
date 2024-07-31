from app.Conexion import Conexion
from app.CursorPOOL import CursorPOOL


class Asistencia:
    def __init__(self, id, id_usuario, id_clase):
        self._id = id
        self._id_usuario = id_usuario
        self._id_clase = id_clase

    def __str__(self):
        return f"""
                ID: {self._id}
                id_usuario: {self._id_usuario}
                id_clase: {self._id_clase}
                """
#FOREIGN KEY (id_clase) REFERENCES clases (id),
            #FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
    @staticmethod
    def crearTabla():

        tablas = (
            """
            CREATE TABLE IF NOT EXISTS asistencia (
                id SERIAL PRIMARY KEY,
                id_usuario INTEGER REFERENCES usuario(id), 
                id_clase INTEGER REFERENCES clases(id)
                
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

    @staticmethod
    def registrarAsistencia(id_usuario, id_clase):
        with CursorPOOL() as cursor:
            cursor.execute("INSERT INTO asistencia (id_usuario, id_clase) VALUES (%s, %s)", (id_usuario, id_clase))
            return cursor.rowcount

    @staticmethod
    def ActualizarAsistencia(id, id_usuario, id_clase):
        with CursorPOOL() as cursor:
            cursor.execute("UPDATE asistencia set id_usuario=%s, id_clase=%s WHERE id=%s ", (id_usuario, id_clase, id))
            return cursor.rowcount

    @staticmethod
    def eliminarAsistencia(id):
        with CursorPOOL() as cursor:
            cursor.execute("DELETE FROM asistencia WHERE id=%s", (id,))
            return cursor.rowcount

    @staticmethod
    def listarAsistencias():
        with CursorPOOL() as cursor:
            cursor.execute("SELECT * FROM asistencia")
            registros = cursor.fetchall()
            listaAsistencia = []
            for registro in registros:
                asistencia = Asistencia(registro[0], registro[1], registro[2])
                listaAsistencia.append(asistencia)

            return listaAsistencia
