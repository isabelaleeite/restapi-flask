FROM python:3.13.3-alpine3.21@sha256:18159b2be11db91f84b8f8f655cd860f805dbd9e49a583ddaac8ab39bf4fe1a7

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY wsgi.py .
COPY config.py .
COPY application application


CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000"]