#Siempre se crea un primer archivo con el nombre de views
#Primero importarmos la biblioteca
from django.http import HttpResponse
import datetime
from django.template import Template, Context
#Asi se cargan los cargadores de plantillas
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):#Primera vista
    #Esto es para abrir la plantilla y despues leerla
    p1=Persona("Héctor", "Navarro")
    #nombre="Héctor"
    #apellido ="Navarro"
    #Esto sirve para meter las listas en diccionarios
    temas_curso=["Plantillas", "Modelos", "Formularios","Vistas", "Despliegue"]
    ahora=datetime.datetime.now()
    #doc_externo=open("C:/Users/Hector/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #Para usar los cargdores hay que irse a settings y alli pegar la ruta donde estan las plantillas en dirs
    #doc_externo=loader.get_template("miplantilla.html")
    #Para pasarle valores al contexto con un diccionario
    #ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido, "hora":ahora})
    #Esto es para pasarle valores con clases
    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora":ahora, "temas":temas_curso})
    #documento=plt.render(ctx)
    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora":ahora, "temas":temas_curso})
    return render(request,"miplantilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora":ahora, "temas":temas_curso})

def cursoC(request):
    ahora=datetime.datetime.now()
    return render(request, "CursoC.html", {"dameFecha":ahora})

def Curso(request):
    ahora=datetime.datetime.now()
    return render(request, "cursoCSS.html", {"dameFecha":ahora})

def despedida(request):
    return  HttpResponse("Hasta luego mundo de Django")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()
    documento="<html><body><h1>Fecha y hora actuales %s </html></body></h1>" %fecha_actual
    return HttpResponse(documento)


def calculaEdad(request, edad, agno):#se ponemos el valor asi, sale luego en la url

    #edadActual =18
    periodo=agno-2019
    edadFutura=edad+periodo
    documento=documento="<html><body><h1>En el año %s tendrás %s años. </html></body></h1>"%(agno, edadFutura)
    return HttpResponse(documento)