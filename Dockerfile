# Usa una imagen base de Python
FROM python:3.12-slim


# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos a la ubicación actual del contenedor
COPY requirements.txt .

# Instala las dependencias del sistema necesarias para psycopg2 y otras librerías
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Expone el puerto en el que la aplicación correrá
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "Main.py"]



