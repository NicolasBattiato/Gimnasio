# Usar la imagen base de Python 3.12
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar git y otras dependencias del sistema
RUN apt-get update && apt-get install -y git gcc libpq-dev

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto 5432 (si es necesario)
EXPOSE 5432

# Definir el comando por defecto para ejecutar la aplicación
CMD ["python", "Main.py"]