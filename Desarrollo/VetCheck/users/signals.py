from django.contrib.auth.models import User, Group
from .models import PerfilCliente
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from .models import PerfilCliente

@receiver(m2m_changed, sender = User.groups.through)
def agregarPerfil(instance, action, reverse, *args, **kwargs):
    grupo_cliente = Group.objects.get(name = "Cliente")
    grupo_veterinario = Group.objects.get(name = "Veterinario")
    grupo_administrativo = Group.objects.get(name = "Administrativo")
    
    
    if action == "post_add":
        


        if  grupo_cliente in instance.groups.all():
            try:
                perfil = PerfilCliente.objects.get(usuario = instance)
            except:
                perfil = None

            finally:
                if perfil == None:
                    PerfilCliente.objects.create(usuario = instance)

        elif grupo_veterinario in instance.groups.all():
            '''
            SE TRAE EL PERFIL Veterinario
            try:
                perfil = PerfilEmpresa.objects.get(usuario = instance)
            except:
                perfil = None

            finally:
                if perfil == None:
                    PerfilEmpresa.objects.create(usuario = instance)'''

        elif grupo_administrativo in instance.groups.all():
            '''
            SE TRAE EL PERFIL administrativo
            try:
                perfil = PerfilModerador.objects.get(usuario = instance)
            except:
                perfil = None

            finally:
                if perfil == None:
                    PerfilModerador.objects.create(usuario = instance)'''

    if action == "pre_remove":

        if  grupo_cliente in instance.groups.all():
            try:
                perfil = PerfilCliente.objects.get(usuario = instance)
            except:
                perfil = None

            finally:
                if perfil != None:
                    perfil.delete()

        elif grupo_veterinario in instance.groups.all():
            '''
            SE TRAE EL PERFIL Veterinario
             try:
                perfil = PerfilCliente.objects.get(usuario = instance)
            except:
                perfil = None

            finally:
                if perfil != None:
                    perfil.delete()'''

        elif grupo_administrativo in instance.groups.all():
            '''
            SE TRAE EL PERFIL administrativo
             try:
                perfil = PerfilCliente.objects.get(usuario = instance)
            except:
                perfil = None

            finally:
                if perfil != None:
                    perfil.delete()'''








