from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")


def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")

def contactos(request):
    return render(request, "ProyectoWebApp/contacto.html")