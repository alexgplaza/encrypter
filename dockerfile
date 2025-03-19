# Imagen base ligera de Python
FROM python:3.11-slim 

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de la app
WORKDIR /app

# Copiar los archivos de la aplicación
COPY requirements.txt .
COPY app.py .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./bin/nom-proxy-encrypt /bin/nom-proxy-encrypt

# Dar permisos de ejecución al binario
RUN chmod +x /bin/nom-proxy-encrypt

# Segunda etapa: imagen final minimizada

# Exponer el puerto Flask
EXPOSE 5000

# Comando de ejecución
CMD ["python", "app.py"]
