from psycopg2 import pool
from psycopg2 import sql
import sys


class Conexion:
    _DATABASE = "gimnasio"
    _USERNAME = "postgres"
    _PASSWORD = "Nico0603"
    _DB_PORT = "5432"
    _HOST = "localhost"
    _MIN = 1
    _MAX = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN, cls._MAX,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                print(f"Conexion exitosa: {cls._pool}")
                return cls._pool

            except Exception as e:
                print(f"Ocurrio un problema en la conexion del pool: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        print(f"Conexion exitosa del pool: {conexion}")
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        print(f"se recupero la conexion al pool: {conexion}")

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
