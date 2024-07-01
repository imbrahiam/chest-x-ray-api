FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx   # Install libGL.so.1

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["sh", "-c", "python download_model.py && python server.py"]
