from django.db import models
from django.db.models.enums import IntegerChoices
from users.models import PerfilCliente, PerfilVeterinario
from django_resized import ResizedImageField
from django.urls import reverse
from datetime import datetime, timedelta

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=25)
    dueño = models.ForeignKey(PerfilCliente, null=False, blank=False, on_delete=models.CASCADE)
    peso = models.FloatField()
    edad = models.DateField(auto_now=False, auto_now_add=False)
    class Tipo(models.IntegerChoices):
        C = 1, 'Convencional',
        NC = 2, 'No Convencional'
    tipo = models.IntegerField(choices = Tipo.choices)
    class Grupo(models.IntegerChoices):
        C = 1, 'Canino',
        F = 2, 'Felino',
        R = 3, 'Roedor',
        L = 4, 'Lagomorfo',
        A = 5, 'Ave',
        ANF = 6, 'Anfibio',
        REP = 7, 'Reptil'
    grupo = models.IntegerField(choices = Grupo.choices)


    class Sexo(models.IntegerChoices):
        M = 1, 'Macho',
        H = 2, 'Hembra'
    sexo = models.IntegerField(choices = Sexo.choices)
    descripcion = models.TextField(max_length=60, verbose_name="Descripcion de la mascota")
    imagen = ResizedImageField(upload_to = 'mascotas', size=[500, 300], default = 'default-image.png')

    def get_absolute_url(self):
        return reverse("profile-mascota", kwargs={"pk": self.pk})

    def get_edad(self):
        edad = datetime.now().date() - self.edad
        edad = "%.2f" % round(edad.days / 365.25, 1)
        return edad
    


class HistoriaClinica(models.Model):
    motivo = models.TextField(max_length= 150, verbose_name= "Motivo de consulta", blank = True, null = True)
    class Esp(models.IntegerChoices):
        GEN = 1 , 'Cita General'
        CIR = 2 , 'Cirugia'
        EXM = 3 , 'Examenes'
    subespecialidad = models.IntegerField(choices = Esp.choices, default = Esp.GEN, blank = False, null = False)
    #Examen Fisico:
    examen_fisico = models.TextField(max_length= 350, blank = True, null = True)
    vacunas = models.CharField(max_length= 40, blank = True, null = True)
    antiparacito = models.CharField(max_length= 40, blank = True, null = True)
    examenes = models.FileField(upload_to = 'archivos', blank = True, null = True)
    diagnostico = models.TextField(max_length= 350, blank = True, null = True)
    receta = models.TextField(max_length=350, blank = True, null = True)

    class Meta:
        abstract = True

class Cita(HistoriaClinica):
    paciente = models.ForeignKey(Mascota, on_delete=models.CASCADE, blank = True, null = True)
    usuario = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE, blank = True, null = True)
    fecha = models.DateTimeField(auto_now= False, auto_now_add= False, blank = False)
    veterinario = models.ForeignKey(PerfilVeterinario, null = False, blank = False, on_delete= models.CASCADE)
    confirmacion = models.BooleanField(null = False, default = False)

    def get_hora_final(self):
        hora_final = self.fecha + timedelta(hours = 1)
        return hora_final

    def get_absolute_url(self):
        return reverse("detalle-cita", kwargs={"pk": self.pk})
    





