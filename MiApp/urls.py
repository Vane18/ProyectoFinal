from .views import *
from django.urls import path

urlpatterns = [
     path('',inicio,name='inicio'),
     path('donaciones',donaciones,name='donaciones'),
     path('contacto',contacto,name='contacto'),
     path('requisitos',requisitos,name='requisitos')

]