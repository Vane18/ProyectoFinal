
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import *
from .models import *

def inicio(request):
    return render(request,'MiApp/inicio.html')

def contacto(request):
    return render(request,'MiApp/contacto.html')

def donaciones(request):
    return render(request,'MiApp/donaciones.html')
def requisitos(request):
    return render(request,'MiApp/requisitos.html')

def donaciones(request):
    if request.method == 'POST':
        miFormulario = DonacionFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            donacion=Donacion(nombreDonante=informacion['nombreDonante'],apellidoDonante=informacion['apellidoDonante'],valorDonacion=informacion['valorDonacion'])  
            donacion.save()
            return render(request, 'MiApp/donaciones.html')
    else:
        miFormulario=DonacionFormulario()
    return render(request, 'MiApp/donacionesFormulario.html', {'formulario':miFormulario})


