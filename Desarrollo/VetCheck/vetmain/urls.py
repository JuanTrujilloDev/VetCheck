from django.urls import path
from .views import *
urlpatterns = [
    path('home/cliente/', HomeClienteView.as_view(), name="home-cliente"),
    path('create-mascota/', CreateMascota.as_view(), name="create-mascota"),
    path('list-mascotas', ListMascota.as_view(), name="lista-mascotas"),
    path('actualizar/cliente', ProfileCliente.as_view(), name="profile-cliente"),
    path('perfil-mascota/<int:pk>', ProfileMascota.as_view(), name="profile-mascota"),
    path('lista-citas/', ListaCitas.as_view(), name = 'lista-citas'),
    path('detalle-cita/<int:pk>', DetalleCita.as_view(), name="detalle-cita")
]
