from django.contrib.auth.models import User, Group
from .models import PerfilCliente
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed, sender=User.groups.through)
def manejoPerfiles(action, model, instance, **kwargs):
    if action == "post_add":
        grupo_cliente = Group.objects.get(name="Cliente")
        grupo_vet = Group.objects.get(name="Veterinario")
        grupo_admin = Group.objects.get(name="Administrativo")

        if instance.groups.filter(name = grupo_cliente.name).exists():
            PerfilCliente.objects.create(usuario = instance)

        elif instance.groups.filter(name = grupo_vet.name).exists():
            #Se crearia el perfil del cliente
            print("Se crearia el perfil del cliente")

        elif instance.groups.filter(name = grupo_admin.name).exists():
            #Se crearia el perfil administrador
            print("Se crearia el perfil administrador")

    ### action == PRE_REMOVE --> 
    if action == "pre_remove":
        grupo_cliente = Group.objects.get(name="Cliente")
        grupo_vet = Group.objects.get(name="Veterinario")
        grupo_admin = Group.objects.get(name="Administrativo")

        if instance.groups.filter(name = grupo_cliente.name).exists():
            perfil = PerfilCliente.objects.get(usuario = instance)
            PerfilCliente.delete(perfil)

        elif instance.groups.filter(name = grupo_vet.name).exists():
            #Se eliminaria el perfil del cliente
            print("Se eliminaria el perfil del cliente")

        elif instance.groups.filter(name = grupo_admin.name).exists():
            #Se eliminaria el perfil administrador
            print("Se eliminaria el perfil administrador")

            



