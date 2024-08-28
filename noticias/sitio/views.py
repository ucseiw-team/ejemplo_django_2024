from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework import viewsets
from sitio.serializers import NoticiaSerializer

from sitio.models import Noticia
from sitio.forms import FormNoticia, FormNoticiaMasCopado
from datetime import datetime


def inicio(request):
    # nueva = Noticia()
    # nueva.titulo = 'entro alguien!'
    # nueva.texto = 'acaba de entrar alguien al sitio'
    # nueva.fecha = datetime.now()
    # nueva.save()

    noticias = Noticia.objects.filter(archivada=False)

    return render(request, 'inicio.html', {'lista_noticias': noticias})


def ejemplo_forms(request):
    if request.method == "POST":
        print("DEBUG de form:")
        print(request.POST["titulo"])
        # guardar la noticia además

        return redirect("/inicio/")

    return render(request, "ejemplo_forms.html", {})


def ejemplo_forms_django(request):
    if request.method == "POST":
        form = FormNoticia(request.POST)

        if form.is_valid():
            print("DEBUG titulo ingresado en el form:")
            print(form.cleaned_data["titulo"])
            print("DEBUG POST crudo:", request.POST)
            print("DEBUG presionó guardar?", "guardar" in request.POST)
            print("DEBUG presionó guardar y editar?", "guardar_y_editar" in request.POST)
            # guardar la noticia además

            return redirect("/inicio/")
    else:
        form = FormNoticia()

    return render(request, "ejemplo_forms_django.html", {"form": form})


def ejemplo_forms_django_mas_copado(request):
    if request.method == "POST":
        form = FormNoticiaMasCopado(request.POST)

        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = "desconocido"
            noticia.save()

            return redirect("/inicio/")
    else:
        form = FormNoticiaMasCopado()

    return render(request, "ejemplo_forms_django.html", {"form": form})


def ejemplo_ajax(request):
    return render(request, "ejemplo_ajax.html", {})


def api_ultimo_titulo(request):
    ultima_noticia = Noticia.objects.all().order_by("-fecha").first()
    data = {
        "titulo_ultima_noticia": ultima_noticia.titulo,
    }
    return JsonResponse(data)


def api_lista_noticias(request):
    lista_noticias = Noticia.objects.all().order_by("-fecha")[0:3]
    return render(request, "api_lista_noticias.html", {"lista_noticias": lista_noticias})


class NoticiaViewSet(viewsets.ModelViewSet):
    """
    API de noticias.
    """
    queryset = Noticia.objects.all().order_by('-fecha')
    serializer_class = NoticiaSerializer

