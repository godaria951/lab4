FROM python:3.12.3
LABEL org.opencontainers.image.source="https://github.com/godaria951/lab4"

RUN mkdir /Scripts
WORKDIR /Scripts

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn mysite.wsgi:application -b 0.0.0.0:8000
