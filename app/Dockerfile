FROM tensorflow/tensorflow:2.5.0

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python download_model.py

EXPOSE 8000

ENV NAME World

CMD ["python", "/server.py"]
