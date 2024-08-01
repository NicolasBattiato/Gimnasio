
FROM python:3.12-slim

WORKDIR /users/Nico/Documentos/GimnasioApp

RUN apt-get update && apt-get install -y git gcc libpq-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --verbose

COPY . /users/Nico/Documentos/GimnasioApp



CMD ["python", "/users/Nico/Documentos/GimnasioApp/Main.py"]