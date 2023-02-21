from django.contrib import admin
from .models import Curso, Profesores, Estudiantes, Entregables

admin.site.register(Curso)
admin.site.register(Profesores)
admin.site.register(Estudiantes)
admin.site.register(Entregables)


