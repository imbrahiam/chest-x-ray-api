FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install Flask flask_cors opencv-python tensorflow numpy gdown
RUN pip install opencv-python

COPY app/ .

ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

CMD ["sh", "-c", "python download_model.py && python server.py"]
