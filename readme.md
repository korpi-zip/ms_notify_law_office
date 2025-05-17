# 📧 Microservicio de Notificaciones - Consultorio Jurídico

Este microservicio está diseñado para enviar notificaciones por correo electrónico en eventos clave dentro de la plataforma de gestión de casos del consultorio jurídico.

---

## 📦 Estructura del Proyecto

<pre><code>📁 ms_notify_law_office/
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
</code></pre>

---

## 🛠️ Requisitos

- Python 3.12+  
- Docker + Docker Compose  
- Cuenta de correo (Gmail, con contraseña de aplicación)  

---

## 🔐 Archivo <code>.env</code>

<pre><code>EMAIL=tu_correo@gmail.com
PASSWORD=tu_contraseña_de_aplicacion
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
</code></pre>

---

## 🚀 Guía de Instalación

1. <strong>Clona el repositorio:</strong>  
<pre><code>git clone https://github.com/tu_usuario/ms_notify_law_office.git
cd ms_notify_law_office
</code></pre>

2. <strong>Crea y configura el archivo <code>.env</code>:</strong>  
Asegúrate de incluir tus credenciales de correo y la configuración de RabbitMQ.

<pre><code>EMAIL=tu_correo@gmail.com
PASSWORD=tu_contraseña_de_aplicacion
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
</code></pre>

3. <strong>(Opcional) Ejecuta localmente sin Docker:</strong>  
Instala las dependencias y ejecuta el consumidor manualmente.

<pre><code>pip install -r app/requirements.txt
python app/consumer.py
</code></pre>

4. <strong>Verifica que tienes Docker y Docker Compose instalados:</strong>  
<pre><code>docker --version
docker compose version
</code></pre>

---

## 🐳 Ejecución con Docker

<pre><code>docker compose up --build -d
</code></pre>

Accede a la interfaz de RabbitMQ:  
<code>http://localhost:15672</code>  
<strong>Usuario:</strong> admin  
<strong>Contraseña:</strong> admin

---

## 📤 Prueba con Producer

<pre><code>python app/producer.py
</code></pre>

---

## 🧪 Pruebas

Por implementar (<code>pytest</code>, <code>mocks</code>).

---

## 📬 Contacto

Desarrollado por estudiantes de Ingeniería de Computación - Universidad de Caldas.

