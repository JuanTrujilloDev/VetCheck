from django.contrib import admin
from .models import PerfilAdmin, PerfilCliente, PerfilVeterinario, User

# Register your models here.

admin.site.register(PerfilCliente)
admin.site.register(PerfilVeterinario)
admin.site.register(PerfilAdmin)
admin.site.register(User)

