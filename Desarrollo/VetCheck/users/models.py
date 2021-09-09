from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.base import Model
# Create your models here.

class Departamento(models.Model):
    pass


class Ciudad(models.Model):
    pass

class PerfilCliente (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(verbose_name= "Nombres", max_length= 40)
    apellidos = models.CharField(verbose_name="Apellidos", max_length= 75)
    phone_regex = RegexValidator(regex='^(3)([0-9]){9}$', message = "Por favor escribe el numero en el formato aceptado sin codigo de area ej: 3123456789")
    phone = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Telefono")
    direccion = models.CharField(verbose_name= "Direccion", max_length = 60)
    #slug
    #Mascotas Asociadas


    def __str__(self):
        return self.usuario.username

    #save method para creacion del slug

    #get_absolute_url para el perfil











#Perfil Vet


















#Perfil Admin




