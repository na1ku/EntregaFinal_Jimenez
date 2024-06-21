# Blog Application

Este proyecto es una aplicación web similar a un blog, creada con Django. La aplicación permite a los usuarios registrarse, iniciar sesión, ver perfiles, enviar mensajes y gestionar blogs.

## Link al video explicativo y recorrido por la página

Este es el link al video de explicativo subido a [Youtube](https://youtu.be/iY8PNJHil3o).

## Características

- Registro de usuarios
- Inicio de sesión
- Perfiles de usuario
- Administración de blogs (CRUD completo)
- Envío de mensajes entre usuarios
- Página "Acerca de mí"
- Visualización de páginas de blogs
- Protección de operaciones críticas para administradores

## Requisitos

- Python 3.8+
- Django 3.2+
- SQLite3

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/blog-app.git
   cd blog-app
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```

5. Crea un superusuario para acceder al admin:
   ```bash
   python manage.py createsuperuser
   ```

6. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Uso

- Accede al sitio web en `http://localhost:8000`.
- Regístrate en `/reg-usuario` y luego inicia sesión en `/login`.
- Gestiona tu perfil en `/perfil`.
- Accede a la administración del sitio en `/admin`.
- Envía mensajes a otros usuarios en `/inbox`.
- Visualiza y gestiona blogs en `/foro`.

## Rutas principales

- `/about-me`: Página "Acerca de mí".
- `/foro`: Lista de blogs.
- `/foro/<pageId>`: Detalle de un blog.
- `/reg-usuario`: Registro de usuario.
- `/login`: Inicio de sesión.
- `/perfil`: Perfil de usuario.
- `/admin`: Administración del sitio.
- `/inbox`: Mensajería entre usuarios.

## Modelos

### Blog
- **título**: CharField
- **subtítulo**: CharField
- **cuerpo**: TextField
- **autor**: ForeignKey(User)
- **fecha**: DateTimeField
- **imagen**: ImageField

## Contribución

1. Hace un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y commitea (`git commit -am 'Añade nueva característica'`).
4. Sube tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.
