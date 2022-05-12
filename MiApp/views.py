
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


def inicio(request):
    if request.method == 'POST':
        miFormulario1 = PreAdopcionFormulario(request.POST)
        if miFormulario1.is_valid():
            informacion = miFormulario1.cleaned_data
            preadopcion=Adoptante(nombreAdoptante=informacion['nombreAdoptante'],apellidoAdoptante=informacion['apellidoAdoptante'],preferenciaAnimal=informacion['preferenciaAnimal'],emailAdoptante = informacion['emailAdoptante'])  
            preadopcion.save()
            return render(request, 'MiApp/inicio.html')
    else:
        miFormulario1=PreAdopcionFormulario()
    return render(request, 'MiApp/preadopcionFormulario.html',{'formulario1':miFormulario1})

def buscar(request):
    #if request.GET['nombre']:
    tipoAnimal = request.GET['tipoAnimal']
    animales = Animal.objects.filter(tipoAnimal = tipoAnimal)
    return render(request,'MiApp/busqueda.html',{'animales':animales,'animal':tipoAnimal})


def contacto(request):
    if request.method == 'POST':
        miFormulario = ConsultaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            consulta=Consulta(nombreConsultante=informacion['nombreConsultante'],emailConsultante=informacion['emailConsultante'],telefonoConsultante=informacion['telefonoConsultante'],mensajeConsultante=informacion['mensajeConsultante'])
            consulta.save()
            return render(request, 'MiApp/contacto.html')
    else:
        miFormulario=ConsultaFormulario()
    return render(request, 'MiApp/consultaEnviada.html', {'formulario':miFormulario})   
