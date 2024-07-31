from app.Conexion import Conexion
from app.CursorPOOL import CursorPOOL


class Pago:
    def __init__(self, id, id_usuario, monto, fecha):
        self._id = id
        self._id_usuario = id_usuario
        self._monto = monto
        self._fecha = fecha

    def __str__(self):
        return f"""
                ID: {self._id}
                id_usuario: {self._id_usuario}
                Monto: {self._monto}
                Fecha: {self._fecha}
                """
#FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
    @staticmethod
    def crearTabla():

        tablas = (
            """
            CREATE TABLE IF NOT EXISTS pagos(
                id SERIAL PRIMARY KEY,
                id_usuario INTEGER REFERENCES usuarios(id),
                monto DECIMAL NOT NULL,
                fecha TIMESTAMP NOT NULL
                
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
    def registrarPago(id_usuario, monto, fecha):
        with CursorPOOL() as cursor:
            cursor.execute("INSERT INTO pagos (id_usuario, monto, fecha) VALUES (%s, %s, %s)", (id_usuario, monto, fecha))
            return cursor.rowcount

    @staticmethod
    def ActualizarPago(id, id_usuario, monto, fecha):
        with CursorPOOL() as cursor:
            cursor.execute("UPDATE pagos set id_usuario=%s, monto=%s, fecha=%s WHERE id=%s", (id_usuario, monto, fecha, id))
            return cursor.rowcount

    @staticmethod
    def eliminarPago(id):
        with CursorPOOL() as cursor:
            cursor.execute("DELETE FROM pagos WHERE id=%s", (id, ))
            return cursor.rowcount
    @staticmethod
    def listarPago():
        with CursorPOOL() as cursor:
            cursor.execute("SELECT * FROM pagos")
            registros = cursor.fetchall()
            listaPagos = []
            for registro in registros:
                pago = Pago(registro[0], registro[1], registro[2], registro[3])
                listaPagos.append(pago)
            return listaPagos
