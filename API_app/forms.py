from django import forms

class Cursoform(forms.Form):
    curso = forms.CharField()
    id_curso = forms.IntegerField()

class Profesorform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)

class Estudiantesform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class Entregablesform(forms.Form):
    titulo = forms.CharField(max_length=40)
    fecha_de_entrega = forms.DateField()
    estado_entregado = forms.BooleanField()
