FROM python:3.9-slim-bullseye

WORKDIR /app

# COPY requirements.txt requirements.txt
COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]

EXPOSE 8080