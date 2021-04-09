from django.shortcuts import render, HttpResponse
from Servicios.models import Servicio
# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")

def Servicios(request):
    
    Servicios=Servicio.objects.all()
    return render(request, "ProyectoWebApp/servicios.html", {"Servicios":Servicios})

def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")

def contactos(request):
    return render(request, "ProyectoWebApp/contacto.html")