"""
URL configuration for noticias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sitio import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('noticias', views.NoticiaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('ejemplo_forms/', views.ejemplo_forms),
    path('ejemplo_forms_django/', views.ejemplo_forms_django),
    path('ejemplo_forms_django_mas_copado/', views.ejemplo_forms_django_mas_copado),
    path('ejemplo_ajax/', views.ejemplo_ajax),
    path('api/ultimo_titulo/', views.api_ultimo_titulo),
    path('api/lista_noticias/', views.api_lista_noticias),
    path('api/', include(router.urls)),
]
