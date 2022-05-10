from django.db import models

class Donacion(models.Model):
    nombreDonante = models.CharField(max_length=50)
    apellidoDonante = models.CharField(max_length=50)
    valorDonacion = models.IntegerField()
    def __str__(self):
        return f'Nombre: {self.nombreDonante} Apellido: {self.apellidoDonante} Valor: {self.valorDonacion}'

class Adoptante(models.Model):
    nombreAdoptante = models.CharField(max_length=50)
    apellidoAdoptante = models.CharField(max_length=50)

class Animal(models.Model):
    nombreAnimal = models.CharField(max_length=50)
    edadAnimal = models.IntegerField()

class Consulta(models.Model):
    nombreConsultante = models.CharField(max_length=50)
    emailConsultante = models.EmailField()
    telefonoConsultante = models.IntegerField()
    mensajeConsultante = models.CharField(max_length=350)