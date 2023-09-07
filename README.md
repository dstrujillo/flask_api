# Proyecto: Desarrollo de Microservicio con Python

## ¿Qué es esto?
Es un ejercicio académico para demostrar las habilidades adquiridas durante el curso

## Framework seleccionado
Flask

## ¿Cómo usarlo?

- Clonar repo
- Crear entorno virtual con Python 3.9
- Activar entorno virtual
MAC:
```
user@host:$ source [path_to_env]/bin/activate
```
- Instalar dependencias
```
(env) user@host:$ pip install -r requirements.txt
```
- Configurar el archivo de .env.example con el nombre deseado para SQLALCHEMY_DATABASE_URI y el SECRET_KEY
- Para crear la base de datos de prueba, ejecutar:
```
(env) user@host:$ export FLASK_APP=server
(env) user@host:$ flask shell
>>> from server import db
>>> from users.models import User
>>> db.create_all()
>>> exit()
```

##Ejecución y prueba
- Para correr la aplicación ejecutar:
```
(env) user@host:$ python server.py
```
- Para acceder al swagger del API:
http://127.0.0.1:5000/api/spec.html
http://127.0.0.1:5000/api/spec.json
- Realizar prueba desde cliente Restful
-- Adicionar a los headers del POST, el valor definido en .example.env: 
```
Authorization: YOURSECRETKEY
```