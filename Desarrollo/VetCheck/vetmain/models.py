from django.db import models
from users.models import PerfilCliente

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=25)
    dueño = models.ForeignKey(PerfilCliente, null=False, blank=False, on_delete=models.CASCADE)
    peso = models.FloatField()
    edad = models.DateField(auto_now=False, auto_now_add=False)
    class Sexo(models.IntegerChoices):
        M = 1, 'Macho',
        H = 2, 'Hembra'
    sexo = models.IntegerField(choices = Sexo.choices)
    descripcion = models.TextField(max_length=60, verbose_name="Descripcion de la mascota")


class HistoriaClinica(models.Model):

    class Meta:
        abstract = True

class Cita(HistoriaClinica):
    pass


