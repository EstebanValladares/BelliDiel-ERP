# Usamos una versión ligera de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los requerimientos y los instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de tu código
COPY . .

# Comando para encender el servidor en el puerto 5000
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]