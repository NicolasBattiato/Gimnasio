from app.Conexion import Conexion
from psycopg2 import sql
from datetime import datetime

from app.CursorPOOL import CursorPOOL


class Usuario:
    def __init__(self, id, nombre, apellido, email, tipo):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._tipo = tipo  #cliente o personal

    # CREACION DE TABLA

    @staticmethod
    def crearTablas():

        tablas = (
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                apellido VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                tipo VARCHAR(255) NOT NULL
            );
            """
            ,
        )
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            print(cursor)
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
    def agregarCliente(nombre, apellido, email, tipo):
        with CursorPOOL() as cursor:
            cursor.execute("INSERT INTO usuarios (nombre, apellido, email, tipo) VALUES (%s, %s, %s, %s)",
                           (nombre, apellido, email, tipo))

            return cursor.rowcount



    @staticmethod
    def ActualizarCliente(id, nombre, apellido, email, tipo):
        with CursorPOOL() as cursor:
            cursor.execute("UPDATE usuarios set nombre=%s, apellido=%s, email=%s, tipo=%s WHERE id=%s ",
                           (nombre, apellido, email, tipo, id))
            return cursor.rowcount

    @staticmethod
    def eliminarCliente(id):
        with CursorPOOL() as cursor:
            cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
            return cursor.rowcount

    @staticmethod
    def listarCliente():
        with CursorPOOL() as cursor:
            cursor.execute("SELECT * FROM usuarios")
            registros = cursor.fetchall()
            listaUsuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2], registro[3], registro[4])
                listaUsuarios.append(usuario)
            return listaUsuarios

    def __str__(self):
        return f"""
                ID: {self._id}
                Nombre: {self._nombre}
                Apellido: {self._apellido}
                email: {self._email}
                tipo: {self._tipo}"""

    # Metodos GET & SET

    @property
    def id(self):
        return self._id

    @id.setter
    def id_usuario(self, id_usuario):
        self._id = id_usuario

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
