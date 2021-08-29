from django.contrib.auth.models import User, Group
from .models import PerfilCliente
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed, sender=User.groups.through)
def addPerfilCliente(action, model, instance, **kwargs):
    if action == "post_add":
        grupo_cliente = Group.objects.get(name="Cliente")
        if instance.groups.filter(name = grupo_cliente.name).exists():
            PerfilCliente.objects.create(usuario = instance)

    ### action == POST_REMOVE --> 
            



