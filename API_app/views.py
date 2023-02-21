from django.shortcuts import render
from API_app.models import Curso, Profesores, Estudiantes, Entregables
from django.http import HttpResponse
from API_app.forms import Cursoform, Profesorform, Estudiantesform, Entregablesform
from django.http.request import QueryDict


def curso(request):
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)



def inicio(request):
    return render(request, 'API_app/inicio.html')

def entregables(request):

    if request.method == 'POST':
        formulario_entregables = Entregablesform(request.POST)


        if formulario_entregables.is_valid():
            informacion = formulario_entregables.cleaned_data
            entrega = Entregables(titulo=informacion['titulo'], fecha_de_entrega=informacion['fecha_de_entrega'], estado_entregado=informacion['estado_entregado'])
            entrega.save()

            return render(request, 'API_app/inicio.html')

    else:
        formulario_entregables = Entregablesform()

    return render(request, 'API_app/entregables.html', {'formulario_entregables':formulario_entregables})


def estudiantes(request):

    if request.method == 'POST':
        formulario_estudiantes = Estudiantesform(request.POST)

        if formulario_estudiantes.is_valid():
            informacion = formulario_estudiantes.cleaned_data
            estudiante = Estudiantes(nombre=informacion['nombre'],
                                  apellido=informacion['apellido'],
                                  email=informacion['email'],
                                  )
            estudiante.save()

            return render(request, 'API_app/inicio.html')

    else:
        formulario_estudiantes = Estudiantesform()

    return render(request, 'API_app/estudiantes.html', {'formulario_estudiantes':formulario_estudiantes})


def profesores(request):

    if request.method == 'POST':
        formulario_profesores = Profesorform(request.POST)

        if formulario_profesores.is_valid():
            informacion = formulario_profesores.cleaned_data
            profesor = Profesores(nombre=informacion['nombre'],
                                  apellido=informacion['apellido'],
                                  email=informacion['email'],
                                  profesion=informacion['profesion']
                                  )
            profesor.save()

            return render(request, 'API_app/inicio.html')

    else:
        formulario_profesores = Profesorform()

    return render(request, 'API_app/profesores.html', {'formulario_profesores':formulario_profesores})

def cursos(request):

    if request.method == 'POST':
        formulario_curso = Cursoform(request.POST)


        if formulario_curso.is_valid():
            informacion = formulario_curso.cleaned_data
            curso = Curso(curso=informacion['curso'], id_curso=informacion['id_curso'] )
            curso.save()

            return render(request, 'API_app/inicio.html')

    else:
        formulario_curso = Cursoform()

    return render(request, 'API_app/cursos.html', {'formulario_curso':formulario_curso})


def buscar(request):
    if request.GET["id_curso"]:


        id_curso = request.GET['id_curso']
        cursos = Curso.objects.filter(id_curso__icontains=id_curso)

        return render(request, "API_app/cursos.html", {"cursos": cursos, "id_curso": id_curso})

    else:

        respuesta = "No enviaste datos"

    # No olvidar from django.http import HttpResponse
    # return HttpResponse(respuesta)
    return render(request, "API_app/cursos.html", {"respuesta": respuesta})


