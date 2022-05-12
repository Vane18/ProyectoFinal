from django import forms

class DonacionFormulario(forms.Form):
    nombreDonante = forms.CharField(max_length=50)
    apellidoDonante = forms.CharField(max_length=50)
    valorDonacion = forms.IntegerField()

class PreAdopcionFormulario(forms.Form):
    nombreAdoptante = forms.CharField(max_length=50)
    apellidoAdoptante = forms.CharField(max_length=50)
    preferenciaAnimal = forms.CharField(max_length=10)
    emailAdoptante = forms.CharField(max_length=50)

class ConsultaFormulario(forms.Form):
    nombreConsultante = forms.CharField(max_length=50)
    emailConsultante = forms.EmailField()
    telefonoConsultante = forms.IntegerField()
    mensajeConsultante = forms.CharField(max_length=350)