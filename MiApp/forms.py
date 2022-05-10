from django import forms

class DonacionFormulario(forms.Form):
    nombreDonante = forms.CharField(max_length=50)
    apellidoDonante = forms.CharField(max_length=50)
    valorDonacion = forms.IntegerField()