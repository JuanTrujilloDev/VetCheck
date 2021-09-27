from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator
from PIL import Image
from django.utils.text import slugify
from django.urls import reverse


class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete= models.CASCADE, default = 1)

class PerfilCliente (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(verbose_name= "Nombres", max_length= 40)
    apellidos = models.CharField(verbose_name="Apellidos", max_length= 75)
    phone_regex = RegexValidator(regex='^(3)([0-9]){9}$', message = "Por favor escribe el numero en el formato aceptado sin codigo de area ej: 3123456789")
    phone = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Telefono")
    direccion = models.CharField(verbose_name= "Direccion", max_length = 60)
    slug = models.SlugField(null=True, blank = True)
    class Ciudades(models.IntegerChoices):
     BOGOTA=   1, 'Bogota'
     MEDELLIN =   2, 'Medellin'
     CALI =    3, 'Cali'
     BARRANQUILLA =   4, 'Barranquilla'
     CARTAGENA =    5, 'Cartagena'
     CUCUTA =    6, 'Cucuta'
     BUCARAMANGA =    7, 'Bucaramanga'
     VILLAVICENCIO =   8, 'Villavicencio'
     IBAGUE =    9, 'Ibague'
     SANTAMARTA =    10, 'Santa Marta'
     MANIZALES=    11, 'Manizales'
     PEREIRA=    12, 'Pereira'
     NEIVA=    13, 'Neiva'
     PASTO=    14, 'Pasto'
     ARMENIA=    15, 'Armenia'

    ciudad = models.IntegerField(choices = Ciudades.choices , default = Ciudades.BOGOTA)


    def __str__(self):
        return self.usuario.username

    #save method para creacion del slug
    def save(self, *args, **kwargs):
        slug = slugify(self.usuario.username)
        super().save(*args, **kwargs)

   #get_absolute_url para el perfil
    def get_absolute_url(self):
        return reverse('profile-cliente')
    











#Perfil Veterinario

class PerfilVeterinario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(verbose_name= "Nombres", max_length= 40)
    apellidos = models.CharField(verbose_name="Apellidos", max_length= 75)
    phone_regex = RegexValidator(regex='^(3)([0-9]){9}$', message = "Por favor escribe el numero en el formato aceptado sin codigo de area ej: 3123456789")
    phone = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Telefono")
    direccion = models.CharField(verbose_name= "Direccion", max_length = 60)
    slug = models.SlugField(null=True, blank = True)
    class Ciudades(models.IntegerChoices):
     BOGOTA=   1, 'Bogota'
     MEDELLIN =   2, 'Medellin'
     CALI =    3, 'Cali'
     BARRANQUILLA =   4, 'Barranquilla'
     CARTAGENA =    5, 'Cartagena'
     CUCUTA =    6, 'Cucuta'
     BUCARAMANGA =    7, 'Bucaramanga'
     VILLAVICENCIO =   8, 'Villavicencio'
     IBAGUE =    9, 'Ibague'
     SANTAMARTA =    10, 'Santa Marta'
     MANIZALES=    11, 'Manizales'
     PEREIRA=    12, 'Pereira'
     NEIVA=    13, 'Neiva'
     PASTO=    14, 'Pasto'
     ARMENIA=    15, 'Armenia'

    ciudad = models.IntegerField(choices = Ciudades.choices , default = Ciudades.BOGOTA)
    class Cargos(models.IntegerChoices):
      ESTILISTA=  1, 'Estilista'
      VETGENERAL =  2, 'Veterinario General'
      VETESPECIALISTA =  3, 'Veterinario Especialista'
    cargo = models.IntegerField(choices = Cargos.choices, default = Cargos.VETGENERAL)
    class Animales(models.IntegerChoices):
        CONVENCIONALES = 1, 'Convencionales'
        NOCONVENCIONALES = 2, 'No Convencionales'

    animales = models.IntegerField(choices = Animales.choices, default = Animales.CONVENCIONALES)


















#Perfil Admin

class PerfilAdmin (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(verbose_name= "Nombres", max_length= 40)
    apellidos = models.CharField(verbose_name="Apellidos", max_length= 75)
    phone_regex = RegexValidator(regex='^(3)([0-9]){9}$', message = "Por favor escribe el numero en el formato aceptado sin codigo de area ej: 3123456789")
    phone = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Telefono")
    direccion = models.CharField(verbose_name= "Direccion", max_length = 60)
    slug = models.SlugField(null=True, blank = True)
    class Ciudades(models.IntegerChoices):
     BOGOTA=   1, 'Bogota'
     MEDELLIN =   2, 'Medellin'
     CALI =    3, 'Cali'
     BARRANQUILLA =   4, 'Barranquilla'
     CARTAGENA =    5, 'Cartagena'
     CUCUTA =    6, 'Cucuta'
     BUCARAMANGA =    7, 'Bucaramanga'
     VILLAVICENCIO =   8, 'Villavicencio'
     IBAGUE =    9, 'Ibague'
     SANTAMARTA =    10, 'Santa Marta'
     MANIZALES=    11, 'Manizales'
     PEREIRA=    12, 'Pereira'
     NEIVA=    13, 'Neiva'
     PASTO=    14, 'Pasto'
     ARMENIA=    15, 'Armenia'

    ciudad = models.IntegerField(choices = Ciudades.choices , default = Ciudades.BOGOTA)


    def __str__(self):
        return self.usuario.username

    #save method para creacion del slug
    def save(self, *args, **kwargs):
        slug = slugify(self.usuario.username)
        super().save(*args, **kwargs)

 


