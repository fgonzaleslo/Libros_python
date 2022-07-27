from dataclasses import fields
from operator import mod
from pyexpat import model
from django import forms
from .models import Autor, Libro

#Declaramos el formulario
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        #model = Autor
        fields ='__all__'


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        #model = Autor
        fields ='__all__'