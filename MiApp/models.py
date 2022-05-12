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
    emailAdoptante = models.EmailField()
    preferenciaAnimal = models.CharField(max_length=10)
    def __str__(self):
        return f'Nombre: {self.nombreAdoptante} Apellido: {self.apellidoAdoptante} Email: {self.emailAdoptante} Preferencia: {self.preferenciaAnimal}'

class Animal(models.Model):
    nombreAnimal = models.CharField(max_length=50)
    edadAnimal = models.IntegerField()
    tipoAnimal = models.CharField(max_length=50)
    def __str__(self):
        return f'Nombre: {self.nombreAnimal} Edad: {self.edadAnimal} Tipo: {self.tipoAnimal}'

class Consulta(models.Model):
    nombreConsultante = models.CharField(max_length=50)
    emailConsultante = models.EmailField()
    telefonoConsultante = models.IntegerField()
    mensajeConsultante = models.CharField(max_length=350)