from django.shortcuts import render
from Servicios.models import Servicio
# Create your views here.
def Servicios(request):
    
    Servicios=Servicio.objects.all()
    return render(request, "Servicios/servicios.html", {"Servicios":Servicios})
