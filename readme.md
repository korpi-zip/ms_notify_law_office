📧 Microservicio de Notificaciones - Consultorio Jurídico
Este microservicio está diseñado para enviar notificaciones por correo electrónico en eventos clave dentro de la plataforma de gestión de casos del consultorio jurídico.

📦 Estructura del Proyecto

  📁 ms_notify_law_office/
├── 📂 app/                  
│   ├── 🐍 consumer.py       
│   ├── 🐍 producer.py       
│   └── 📄 requirements.txt  
├── 📂 templates/           
│   └── 📄 notification.html 
├── 📄 .gitignore           
├── 🐳 Dockerfile           
├── 🐳 docker-compose.yml   
├── 🔐 .env                 
└── 📄 README.md            


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
