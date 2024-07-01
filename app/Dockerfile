FROM tensorflow/tensorflow:2.5.0

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gdown

RUN python download_model.py

EXPOSE 8000

CMD ["python", "server.py"]