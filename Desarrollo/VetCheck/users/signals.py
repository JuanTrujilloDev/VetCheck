from django.contrib.auth.models import Group
from .models import PerfilAdmin, PerfilCliente, PerfilVeterinario, User
from django.db.models.signals import post_save
from django.dispatch import receiver


##PERFIL POR FORMULARIO
@receiver(post_save, sender = User)
def agregarPerfil(instance, sender, created, **kwargs):
    grupo_cliente = Group.objects.get(name = "Cliente")
    grupo_vet = Group.objects.get(name = "Veterinario")
    grupo_admin = Group.objects.get(name = "Administrador")
    


    if created:
        instance.groups = grupo_cliente
        PerfilCliente.objects.get_or_create(usuario = instance)
        instance.save()
    

    else:

        if instance.groups == grupo_cliente:
            if PerfilVeterinario.objects.filter(usuario = instance):
                perfil = PerfilVeterinario.objects.get(usuario = instance)
                perfil.delete()

            elif PerfilAdmin.objects.filter(usuario = instance):
                perfil = PerfilAdmin.objects.get(usuario = instance)
                perfil.delete()
            
            PerfilCliente.objects.get_or_create(usuario = instance)

        elif instance.groups == grupo_vet:

            if PerfilCliente.objects.filter(usuario = instance):
                perfil = PerfilCliente.objects.get(usuario = instance)
                perfil.delete()

            elif PerfilAdmin.objects.filter(usuario = instance):
                perfil = PerfilAdmin.objects.get(usuario = instance)
                perfil.delete()
            
            perfil = PerfilVeterinario.objects.get_or_create(usuario = instance)[0]

        elif instance.groups == grupo_admin:

            if PerfilCliente.objects.filter(usuario = instance):
                perfil = PerfilCliente.objects.get(usuario = instance)
                perfil.delete()

            elif PerfilVeterinario.objects.filter(usuario = instance):
                perfil = PerfilVeterinario.objects.get(usuario = instance)
                perfil.delete()
                
            
            PerfilAdmin.objects.get_or_create(usuario = instance)









