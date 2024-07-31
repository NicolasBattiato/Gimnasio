from app.Conexion import *
from app.CursorPOOL import CursorPOOL


class Reporte:

    @staticmethod
    def usuarios_por_tipo():
        with CursorPOOL() as cursor:
            cursor.execute("SELECT tipo, COUNT(*) FROM usuarios GROUP BY tipo")

            registros = cursor.fetchall()
            listaRepoUsuarios = []
            for registro in registros:
                listaRepoUsuarios.append(registro)
            return listaRepoUsuarios

    @staticmethod
    def asistencias_por_clase():
        with CursorPOOL() as cursor:
            cursor.execute("""
                SELECT clases.nombre, COUNT(*) 
                FROM asistencia 
                INNER JOIN clases ON asistencia.id_clase = clases.id 
                GROUP BY clases.nombre
                """)

            registros = cursor.fetchall()
            listaRepoAsistencia = []
            for registro in registros:
                listaRepoAsistencia.append(registro)
            return listaRepoAsistencia

    @staticmethod
    def pagos_por_usuario():
        with CursorPOOL() as cursor:
            cursor.execute("""
                SELECT usuarios.nombre, SUM(pagos.monto)
                FROM pagos 
                INNER JOIN usuarios ON pagos.id_usuario = usuarios.id
                GROUP BY usuarios.nombre
                """)

            registros = cursor.fetchall()
            listaReportes = []
            for registro in registros:

                listaReportes.append(registro)
            return listaReportes
