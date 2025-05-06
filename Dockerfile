FROM python:3.12-slim

WORKDIR /app

COPY ./app /app
COPY ./.env /app/.env

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "/app/consumer.py"]
