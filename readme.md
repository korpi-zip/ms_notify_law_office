📧 Microservicio de Notificaciones - Consultorio Jurídico
Este microservicio está diseñado para enviar notificaciones por correo electrónico en eventos clave dentro de la plataforma de gestión de casos del consultorio jurídico.

📦 Estructura del Proyecto

<pre><code>📁<strong>ms_notify_law_office/</strong> 
  ├── 📂 <strong>app/</strong> │ 
  ├── 🐍 <code>consumer.py</code> │ 
  ├── 🐍 <code>producer.py</code> │ └── 📄 <code>requirements.txt</code>
  ├── 📂 <strong>templates/</strong> │ └── 📄 <code>notification.html</code> ├── 📄 <code>.gitignore</code> ├── 🐳 <code>Dockerfile</code> ├── 🐳 <code>docker-compose.yml</code> ├── 🔐 <code>.env</code> └── 📄 <code>README.md</code> </code></pre>

🛠️ Requisitos

-Python 3.12+
-Docker + Docker Compose
-Cuenta de correo (Gmail, con contraseña de aplicación)

🔐 Archivo .env

EMAIL=tu_correo@gmail.com
PASSWORD=tu_contraseña_de_aplicacion
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672

🐳 Ejecución con Docker

cd docker
docker compose up --build -d

RabbitMQ GUI en: http://localhost:15672
Usuario: admin, Contraseña: admin

📤 Prueba con Producer

python app/producer.py

🧪 Pruebas

Por implementar (pytest, mocks).

📬 Contacto

Desarrollado por estudiantes de Ingeniería de Computación - Universidad de Caldas.
