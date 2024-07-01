FROM python:3.8-slim

RUN apt-get update && apt-get install -y libglib2.0-0

WORKDIR /app

EXPOSE 8000

COPY app/requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install opencv-python

COPY app/ .

ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

CMD ["sh", "-c", "python download_model.py && python server.py"]
