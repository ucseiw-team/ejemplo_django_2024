from django import forms
from sitio.models import Noticia


class FormNoticia(forms.Form):
    titulo = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=200)
    archivada = forms.BooleanField()


class FormNoticiaMasCopado(forms.ModelForm):
    class Meta:
         model = Noticia
         fields = ["titulo", "texto", "fecha", "archivada"]
