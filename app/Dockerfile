FROM tensorflow/tensorflow:2.5.0

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python download_model.py

EXPOSE 8000

ENV NAME World

CMD ["python", "server.py"]
