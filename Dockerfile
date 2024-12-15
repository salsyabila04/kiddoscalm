# Gunakan image Python resmi sebagai base image
FROM python:3.13-slim

# libGL.so.1
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Set lingkungan kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke container
COPY requirements.txt /app/requirements_docker.txt

# Instal semua dependensi dari requirements.txt
RUN pip install --no-cache-dir -r requirements_docker.txt

# Salin semua file aplikasi ke container
COPY . /app

# Ekspos port Flask (default 5000)
EXPOSE 5000

# Tentukan perintah untuk menjalankan aplikasi
CMD ["python", "main.py"]
