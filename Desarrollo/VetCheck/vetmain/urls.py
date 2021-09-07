from django.urls import path
from .views import *
urlpatterns = [
    path('home/cliente/', HomeClienteView.as_view(), name="home-cliente")
]
