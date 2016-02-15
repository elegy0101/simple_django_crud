# simple_django_crud
Crud básico en django para practicar, en este sencillo proyecto se pueden realizar las operaciones basicas de un crud hacia una tabla llamada servers. Antes de comenzar asegurate de tener una base de datos creada con el nombre que gustes, posteriormente puedes proceder a ejecutar la aplicacion.

# Ejecutando el proyecto

   python manage.py makemigrations
   python manage.py migrate

# Migrando tu base de datos

  python manage.py makemigrations "nombre de tu app"
  python manage.py migrate "nombre de tu app"

# Ahora puedes ejecutar el servidor de desarrollo

  python manage.py runserver

Para acceder a la aplicacion ve a la siguiente URL: http://localhost:8000/
