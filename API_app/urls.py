from django.urls import path
from API_app import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='Profesores'),
    path('entregables/', views.entregables, name='entregables'),
    path('buscar/', views.buscar),
]
