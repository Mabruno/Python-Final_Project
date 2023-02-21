# Tercera-pre-entrega-Bruno-Mauro
Proyecto Final Python

Desarrollo de pagina web intermedia hecha con Django.

Funcionalidades:

Cargar el proyecto mediante el comando "python manage.py runserver". Acceder al link presentado, y una vez allí colocar el "path" al link deseado.

Accediendo a la dirección "/API" podemos ver las siguientes funciones:

  -Vista de inicio con mensaje del desarrollador
  -Vista Curso, haciendo click en la barra de direcciones de la parte superior, donde se puede registrar un curso ingresando el nombre del curso en el campo "curso" como asi tambien el ID del curso en el campo "ID_curso" y pulsando el boton "enviar".
  -Vista de Profesores, haciendo click en la barra de direcciones de la parte superior, donde se puede registrar un un objeto "Profesores" ingresando el nombre, apellido, email y profesion en los distintos campos y pulsando el boton "enviar".
  -Vista de Estudiantes, haciendo click en la barra de direcciones de la parte superior, donde se puede registrar un un objeto "Estudiantes" ingresando el nombre, apellido, email en los distintos campos y pulsando el boton "enviar".
  -Vista de Entregables, haciendo click en la barra de direcciones de la parte superior, donde se puede registrar un un objeto "Estudiantes" ingresando el titulo, fecha de entrega y estado de entrega en los distintos campos y pulsando el boton "enviar".

Todas estas cargas de datos, de cada funcion usada, quedan registradas en la base de datos del proyecto "db.sqlite3" y puede ser consultada y editada a travez de la interfaz "admin" provista por django.

Para acceder al entorno "/admin" utilizar "user: Mauro" y "password: Mauro". Esto dara acceso de superusuario a la base de datos. Alli se pueden consultar los registros agregados y/o pre-existentes.
  
  
