FROM tensorflow/tensorflow:2.5.0

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install gdown

RUN python /app/download_model.py

EXPOSE 8000

ENV NAME World

CMD ["python", "/app/server.py"]
