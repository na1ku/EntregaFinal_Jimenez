# Blog Application

Este proyecto es una aplicación web similar a un blog, creada con Django. La aplicación permite a los usuarios registrarse, iniciar sesión, ver perfiles, enviar mensajes y gestionar blogs.

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

## Casos de Prueba

1. **Registro de Usuario**
   - **Descripción**: Verificar que un usuario puede registrarse correctamente.
   - **Pasos**:
     1. Navegar a `/reg-usuario`.
     2. Rellenar el formulario de registro.
     3. Enviar el formulario.
   - **Resultado Esperado**: El usuario se registra y se redirige a la página de inicio.

2. **Inicio de Sesión**
   - **Descripción**: Verificar que un usuario puede iniciar sesión correctamente.
   - **Pasos**:
     1. Navegar a `login`.
     2. Rellenar el formulario de inicio de sesión.
     3. Enviar el formulario.
   - **Resultado Esperado**: El usuario inicia sesión y se redirige a la página de inicio.

3. **CRUD de Blog**
   - **Descripción**: Verificar que un administrador puede crear, editar y eliminar un blog.
   - **Pasos**:
     1. Iniciar sesión como administrador.
     2. Navegar a `/admin` y crear un nuevo blog.
     3. Editar el blog creado.
     4. Eliminar el blog.
   - **Resultado Esperado**: El blog se crea, edita y elimina correctamente.

## Contribución

1. Hace un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y commitea (`git commit -am 'Añade nueva característica'`).
4. Sube tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
``
