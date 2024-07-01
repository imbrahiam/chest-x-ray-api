FROM tensorflow/tensorflow:2.5.0

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/server.py .
COPY app/download_model.py .

RUN python download_model.py

EXPOSE 8000

ENV NAME World

CMD ["python", "server.py"]
