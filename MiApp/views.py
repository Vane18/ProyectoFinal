from django.shortcuts import render
from django.http import HttpResponse

from MiApp.forms import formularioAdopcion
from MiApp.models import Adoptante, Animal

def inicio(request):
    return render(request,'MiApp/inicio.html')

def contacto(request):
    return render(request,'MiApp/contacto.html')

def donaciones(request):
    return render(request,'MiApp/donaciones.html')
    
def requisitos(request):
    if request.method == 'POST':
        miFormulario = formularioAdopcion(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            requisito = Animal(nombreAnimal=informacion['nombreAnimal'],edadAnimal=informacion['nombreAnimal'])
            requisito.save()
            return render(request,'MiApp/inicio.html')
    else:
        miFormulario=formularioAdopcion()
    return render(request,'MiApp/requisitos.html', {'formulario':miFormulario})



