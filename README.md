# GIMNASIO

Esta aplicación conecta con PostgreSQL mediante un pool de conexiones en Python para gestionar una base de datos. Permite la creación, inserción, modificación, eliminación y selección de datos a través de un menú interactivo que facilita la interacción con el usuario según la operación que desee realizar.

## Funcionalidades de la Aplicación:

- **Gestión de Usuarios**: Administra clientes y personal.
- **Programación de Clases y Entrenamientos**: Organiza y programa clases y sesiones de entrenamiento.
- **Seguimiento de Asistencias**: Monitorea y registra la asistencia de los usuarios.
- **Gestión de Pagos y Membresías**: Maneja los pagos y las membresías de los usuarios.
- **Reporte y Análisis de Datos**: Genera informes y analiza datos relevantes.

## Herramientas y Programas necesarios:

- PostgreSQL: 16.1
- Python:3.12: En este aplicacion se usa la blibloteca de python; DATETIME
- Docker:
  - Docker file
  - Requirements.txt:

      - psycopg2-binary==2.9.9
      - SQLAlchemy==2.0.31
    
  - Docker-compose.yml

## Uso
### Ejemplo

```Python
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

if __name__ == "__main__":
    Usuario.crearTablas()
    Clase.crearTabla()
    Asistencia.crearTabla()
    Pago.crearTabla()
    menu()
```
## Contacto:
nicolasgabrielbatti@gmail.com
