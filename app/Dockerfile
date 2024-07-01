FROM tensorflow/tensorflow:2.5.0

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN python download_model.py

EXPOSE 8000

CMD ["python", "server.py"]
