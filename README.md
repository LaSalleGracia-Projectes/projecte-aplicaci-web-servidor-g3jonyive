ConnectYourCoach Backend
==========================

ConnectYourCoach es la API que da soporte al backend de la plataforma ConnectYourCoach, diseñada para conectar entrenadores y clientes a través posts. Este backend está desarrollado con Flask y sigue principios RESTful, autenticación JWT y uso de una base de datos relacional.

## Tabla de Contenidos
- [Descripción del Proyecto](#descripcion-del-proyecto)
- [Características](#caracteristicas)
- [Arquitectura y Tecnologías](#arquitectura-y-tecnologias)
- [Instalación y Configuración](#instalacion-y-configuracion)
- [Variables de Entorno](#variables-de-entorno)
- [Documentación de la API](#documentacion-de-la-api)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Licencia](#licencia)
- [Autores](#autores)

## Descripción del Proyecto

ConnectYourCoach Backend permite a los entrenadores registrar rutinas de entrenamiento, asignarlas a clientes, gestionar perfiles y llevar un seguimiento detallado del progreso de cada usuario. Incluye autenticación segura, gestión de roles y endpoints para ejercicios, rutinas.

## Características

- Autenticación con JWT
  - Registro, inicio de sesión, renovación de tokens.
  - Protección de rutas con decoradores personalizados.

- Gestión de Usuarios y Roles
  - Roles de entrenador y cliente.
  - CRUD completo para usuarios (admin).

- Gestión de Rutinas y Ejercicios
  - Crear y asignar rutinas.
  - Añadir ejercicios con parámetros personalizados.
  - Visualización del progreso por usuario.

- API RESTful organizada
  - Rutas claras y organizadas por módulo.
  - Separación lógica entre controladores y servicios.

- Validaciones de entrada
  - Uso de marshmallow para validar esquemas y datos recibidos.

- Documentación Swagger/OpenAPI integrada
  - Explora los endpoints desde /docs en local.

## Arquitectura y Tecnologías

- Lenguaje y Entorno:
  - Python 3.10+
  - Flask como microframework web

- Librerías y Herramientas:
  - Flask-JWT-Extended (auth)
  - Flask-Marshmallow (validaciones)
  - SQLAlchemy (ORM)
  - Marshmallow (serialización)
  - PostgreSQL o SQLite como base de datos
  - dotenv para configuración

## Instalación y Configuración

1. Clona el repositorio:
   git clone https://github.com/LaSalleGracia-Projectes/projecte-aplicaci-web-servidor-g3jonyive.git
   cd projecte-aplicaci-web-servidor-g3jonyive

2. Crea un entorno virtual:
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instala dependencias:
   pip install -r requirements.txt

4. Configura las variables de entorno:
   FLASK_ENV=development
   SECRET_KEY=clave_supersecreta
   JWT_SECRET_KEY=otra_clave_supersecreta
   DATABASE_URL=sqlite:///db.sqlite3  # O usa PostgreSQL

5. Inicializa la base de datos:
   flask db init
   flask db migrate
   flask db upgrade

6. Ejecuta el servidor:
   flask run

## Variables de Entorno

- FLASK_ENV: Modo de entorno (development o production).
- SECRET_KEY: Clave secreta de Flask.
- JWT_SECRET_KEY: Clave usada para firmar los tokens JWT.
- DATABASE_URL: URI de la base de datos (SQLite, PostgreSQL, etc.).

## Documentación de la API

La documentación Swagger está disponible en la ruta /docs.

### Endpoints Principales

- /auth/register: Registro de usuarios
- /auth/login: Inicio de sesión
- /users: Gestión de usuarios (GET, PUT, DELETE)
- /routines: Crear, listar y asignar rutinas
- /exercises: Crear y listar ejercicios
- /progress: Ver el progreso del cliente

## Estructura del Proyecto

/connectyourcoach
  ├── app.py                # Entrada principal del servidor Flask
  ├── config.py             # Configuración de entorno y Flask
  ├── models/               # Modelos de SQLAlchemy
  ├── routes/               # Blueprints y rutas organizadas
  ├── schemas/              # Esquemas Marshmallow
  ├── services/             # Lógica de negocio
  ├── utils/                # Utilidades (decoradores, JWT, etc.)
  └── migrations/           # Archivos de Alembic para DB

## Licencia

MIT License

Distribuido bajo la Licencia MIT. Ver LICENSE para más información.

## Autores

- https://github.com/LaSalleGracia-Projectes/projecte-aplicaci-web-servidor-g3jonyive
