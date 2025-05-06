import pika
import json
import yagmail
import os
from dotenv import load_dotenv
import time

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Ahora puedes acceder a las variables de entorno
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Conexión a RabbitMQ
credentials = pika.PlainCredentials('admin', 'admin')
rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")
rabbitmq_port = int(os.getenv("RABBITMQ_PORT", 5672))
parameters = pika.ConnectionParameters(rabbitmq_host, rabbitmq_port, '/', credentials, socket_timeout=2)

# Conexión a RabbitMQ con reintentos
while True:
    try:
        print("Intentando conectar a RabbitMQ...")
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        break
    except pika.exceptions.AMQPConnectionError:
        print("RabbitMQ no está listo. Reintentando en 5 segundos...")
        time.sleep(5)

# Asegurarse de que la cola exista
channel.queue_declare(queue='email_notifications', durable=True)

# Configurar yagmail con tu cuenta registrada
yag = yagmail.SMTP(EMAIL, PASSWORD)

# Función que se ejecuta al recibir un mensaje
def callback(ch, method, properties, body):
    try:
        data = json.loads(body)

        print("📬 Mensaje recibido:")
        print(f"  Para: {data['to']}")
        print(f"  Asunto: {data['subject']}")
        print(f"  Cuerpo: {data['body']}")

        # Enviar el correo real
        yag.send(
            to=data['to'],
            subject=data['subject'],
            contents=data['body']
        )
        print("✅ Correo enviado exitosamente.\n")

        # Confirmar procesamiento del mensaje
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print("❌ Error al procesar mensaje:", str(e))
        ch.basic_nack(delivery_tag=method.delivery_tag)

# Configurar el consumidor
channel.basic_consume(queue='email_notifications', on_message_callback=callback)

print("👂 Escuchando mensajes en 'email_notifications'... Presiona CTRL+C para salir.")
channel.start_consuming()
