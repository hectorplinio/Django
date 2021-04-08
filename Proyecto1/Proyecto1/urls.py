"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
#Tenemos que importar la funcion para usarla
from Proyecto1.views import saludo, despedida, dameFecha, calculaEdad, cursoC, Curso
urlpatterns = [
    path('admin/', admin.site.urls),
    #Tenemos que llamar la funciuon y darle el nombre que queramos dentro de las comillas
    #Cuando queramos usar el servidor tenemos que poner en el cmd python manage.py runserver
    path('saludo/', saludo), #http://localhost:8000/saludo/
    path('nosveremos/',despedida),#http://localhost:8000/nosveremos/
    path('fecha/', dameFecha),#http://localhost:8000/fecha/
    #Asi es para pasarle valores atraves de la url
    path('edades/<int:edad>/<int:agno>',calculaEdad),#http://localhost:8000/edades/20/55
    path('cursoC/', cursoC),
    path('cursoCSS/', Curso),
    
]
