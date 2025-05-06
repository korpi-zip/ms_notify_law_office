import pika
import json
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Leer configuración desde .env
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "admin")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "admin")

# Conectar a RabbitMQ
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
parameters = pika.ConnectionParameters('localhost', RABBITMQ_PORT, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Asegurarse de que la cola exista
channel.queue_declare(queue='email_notifications', durable=True)

# Mensaje a enviar (puedes adaptar esto según lo que necesites)
message = {
    "to": "santiago.escobar30220@ucaldas.edu.co",
    "subject": "Prueba desde el producer con cambios",
    "body": "Este es un correo de prueba enviado desde el microservicio Producer con cambios."
}

# Enviar el mensaje
channel.basic_publish(
    exchange='',
    routing_key='email_notifications',
    body=json.dumps(message),
    properties=pika.BasicProperties(delivery_mode=2)  # Hacerlo persistente
)

print("📤 Mensaje enviado a la cola.")
connection.close()
