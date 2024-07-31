import sys

from app.Usuario import *
from app.Clase import *
from app.Asistencia import *
from app.Pago import *
from app.Reporte import *


def menu():
    while True:
        print("""
        Elija un campo para realizar alguna operacion:
        
        1. Usuarios
        2. Clases
        3. Asistencias
        4. Pagos
        5. Reportes
        6. Salir
        """)

        opcion = int(input("Ingrese una opcion del menu: "))

        if opcion == 1:
            while True:
                print("""
                        Elija una opcion para realizar alguna operacion:
    
                        1. Ingresar Usuario
                        2. Actualizar Usuario
                        3. Eliminar Usuario
                        4. Listar Usuarios
                        5. Volver al Menu principal
                        6. Salir
                        """)
                opcion1 = int(input("Ingrese una opcion del menu de Usuario: "))

                if opcion1 == 1:
                    nombre = input("Ingrese el nombre del Usuario: ")
                    apellido = input("Ingrese el apellido del Usuario: ")
                    mail = input("Ingrese el email del Usuario: ")
                    tipo = input("Ingrese tipo de Usuario(Cliente o Personal): ")
                    Usuario.agregarCliente(nombre=nombre, apellido=apellido, email=mail, tipo=tipo)

                elif opcion1 == 2:
                    usuario_id = int(input("Ingrese el id del usuario al que desea actualizar: "))
                    nombre = input("Ingrese el nombre del Usuario: ")
                    apellido = input("Ingrese el apellido del Usuario: ")
                    mail = input("Ingrese el email del Usuario: ")
                    tipo = input("Ingrese tipo de Usuario(Cliente o Personal): ")
                    Usuario.ActualizarCliente(id=usuario_id, nombre=nombre, apellido=apellido, email=mail, tipo=tipo)

                elif opcion1 == 3:
                    usuario_id = int(input("Ingrese el id del usuario al que desea eliminar: "))
                    Usuario.eliminarCliente(id=usuario_id)

                elif opcion1 == 4:
                    usuarios = Usuario.listarCliente()
                    for usuario in usuarios:
                        print(f"Usuarios encontrados: {usuario}")

                elif opcion1 == 5:
                    menu()

                elif opcion1 == 6:
                    sys.exit()


                else:
                    print("Opcion invalida")



        elif opcion == 2:
            while True:
                print("""
                        Elija una opcion para realizar alguna operacion:

                        1. Ingresar Clase
                        2. Actualizar Clase
                        3. Eliminar Clase
                        4. Listar Clases
                        5. Volver al Menu principal
                        6. Salir
                        """)

                opcion2 = int(input("Ingrese una opcion del menu de Clase: "))

                if opcion2 == 1:
                    nombre = input("Ingrese el nombre de la clase: ")
                    horario = input("Horario (YYYY-MM-DD HH:MM:SS): ")
                    Clase.AgregarClase(nombre=nombre, horario=horario)

                elif opcion2 == 2:
                    clase_id = int(input("Ingrese el id de la clase que desea actualizar: "))
                    nombre = input("Ingrese el nombre de la clase: ")
                    horario = input("Horario (YYYY-MM-DD HH:MM:SS): ")
                    Clase.ActualizarClase(id=clase_id, nombre=nombre, horario=horario)

                elif opcion2 == 3:
                    clase_id = int(input("Ingrese el id de la clase que desea eliminar: "))
                    Clase.eliminarClase(id=clase_id)

                elif opcion2 == 4:
                    clases = Clase.listarClase()
                    for clase in clases:
                        print(f"Clases encontradas: {clase}")

                elif opcion2 == 5:
                    menu()

                elif opcion2 == 6:
                    sys.exit()


                else:
                    print("Opcion invalida")


        elif opcion == 3:
            while True:
                print("""
                        Elija una opcion para realizar alguna operacion:

                        1. Ingresar Asistencia
                        2. Actualizar Asistencia
                        3. Eliminar Asistencia
                        4. Listar Asistencias
                        5. Volver al Menu principal
                        6. Salir
                        """)

                opcion3 = int(input("Ingrese una opcion del menu de Asistencia: "))

                if opcion3 == 1:
                    usuario_id = int(input("Ingrese el id del usuario para registrar la asistencia: "))
                    clase_id = int(input("Ingrese el id de la clase para registrar la asistencia: "))
                    Asistencia.registrarAsistencia(id_usuario=usuario_id, id_clase=clase_id)

                elif opcion3 == 2:
                    asistencia_id = int(input("Ingrese el id de la asistencia que desea actualizar: "))
                    usuario_id = int(input("Ingrese el id del usuario para registrar la asistencia: "))
                    clase_id = int(input("Ingrese el id de la clase para registrar la asistencia: "))
                    Asistencia.ActualizarAsistencia(id=asistencia_id, id_usuario=usuario_id, id_clase=clase_id)

                elif opcion3 == 3:
                    asistencia_id = int(input("Ingrese el id de la asistencia que desea eliminar: "))
                    Asistencia.eliminarAsistencia(id=asistencia_id)

                elif opcion3 == 4:
                    asistencias = Asistencia.listarAsistencias()
                    for asistencia in asistencias:
                        print(f"Asistencias encontradas: {asistencia}")

                elif opcion3 == 5:
                    menu()

                elif opcion3 == 6:
                    sys.exit()


                else:
                    print("Opcion invalida")


        elif opcion == 4:
            while True:
                print("""
                        Elija una opcion para realizar alguna operacion:

                        1. Ingresar Pago
                        2. Actualizar Pago
                        3. Eliminar Pago
                        4. Listar Pagos
                        5. Volver al Menu principal
                        6. Salir
                        """)

                opcion4 = int(input("Ingrese una opcion del menu de Pago: "))

                if opcion4 == 1:
                    usuario_id = int(input("ID del usuario: "))
                    monto = float(input("Monto: "))
                    fecha = input("Fecha (YYYY-MM-DD HH:MM:SS): ")
                    Pago.registrarPago(id_usuario=usuario_id, monto=monto, fecha=fecha)

                elif opcion4 == 2:
                    pago_id = int(input("Ingrese el id del pago a cambiar: "))
                    usuario_id = int(input("ID del usuario: "))
                    monto = float(input("Monto: "))
                    fecha = input("Fecha (YYYY-MM-DD HH:MM:SS): ")
                    Pago.ActualizarPago(id=pago_id, id_usuario=usuario_id, monto=monto, fecha=fecha)

                elif opcion4 == 3:
                    pago_id = int(input("Ingrese el id del pago a eliminar: "))
                    Pago.eliminarPago(id=pago_id)

                elif opcion4 == 4:
                    pagos = Pago.listarPago()
                    for pago in pagos:
                        print(f"Pagos encontrados: {pago}")

                elif opcion4 == 5:
                    menu()

                elif opcion4 == 6:
                    sys.exit()

                else:
                    print("Opcion invalida")

        elif opcion == 5:
            while True:
                print("""
                        Elija una opcion para realizar alguna operacion:

                        1. Usuarios por tipo
                        2. Asistencia por clase
                        3. Pagos por usuarios
                        4. Volver al Menu principal
                        5. Salir
                        """)

                opcion5 = int(input("Ingrese una opcion del menu de Pago: "))

                if opcion5 == 1:
                    reportes = Reporte.usuarios_por_tipo()
                    for reporte in reportes:
                        print(f"Reportes de usuarios por tipo encontrados: {reporte}")

                elif opcion5 == 2:
                    reportes = Reporte.asistencias_por_clase()
                    for reporte in reportes:
                        print(f"Reportes de asistencia por clase encontrados: {reporte}")

                elif opcion5 == 3:
                    reportes = Reporte.pagos_por_usuario()
                    for reporte in reportes:
                        print(f"Reportes de pagos por usuarios encontrados: {reporte}")

                elif opcion5 == 4:
                    menu()

                elif opcion5 == 5:
                    sys.exit()

                else:
                    print("Opcion invalida")

        elif opcion == 6:
            sys.exit()


if __name__ == "__main__":
    Usuario.crearTablas()
    Clase.crearTabla()
    Asistencia.crearTabla()
    Pago.crearTabla()
    menu()
