from app.Conexion import Conexion


class CursorPOOL:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        print("se inicio el metodo with__enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipoExcep, valorExcep, detalleExcep):
        print("se inicio el metodo Exit__")
        if valorExcep:
            self._conexion.rollback()
            print(f"Se produjo un error: {valorExcep}")
        else:
            self._conexion.commit()
            print(f"commit de la transaccion exitosa...")

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
