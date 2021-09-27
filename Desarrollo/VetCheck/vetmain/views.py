from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, HttpResponseRedirect
from users.models import PerfilCliente
from .models import Cita, Mascota
from django.urls import reverse
from django.db.models import Q
from datetime import datetime
# Create your views here.

class HomeClienteView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'homemain.html'


    def get(self, request):
        try:
            if request.user.groups.name == 'Cliente' and PerfilCliente.objects.filter(usuario = request.user).exists():
                return super().get(self, request)
            else:
                ## REDIRECT A 404
                return(redirect('home'))
        
        except:
            return(redirect('home'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mascotas'] = Mascota.objects.filter(dueño = self.request.user.perfilcliente)[0:3]
        return context

class CreateMascota(LoginRequiredMixin, generic.CreateView):
    model = Mascota
    template_name = "create-mascota.html"
    fields = ['nombre','peso', 'edad', 'sexo', 'descripcion', 'imagen']
    success_url = 'home-cliente'

    def get(self, request, *args, **kwargs):
        if request.user.groups.name == "Cliente":
            print(True)
            return super().get(request, *args, **kwargs)
        else:
            print(False)
            return redirect('home')

    def form_valid(self, form, *args, **kwargs):
        if form.is_valid():
            objeto = form.save(commit = False)
            objeto.dueño = self.request.user.perfilcliente
            objeto.save()
            return HttpResponseRedirect(reverse('home-cliente'))
        else:
            return HttpResponseRedirect(reverse('create-mascota'))

class ListMascota(LoginRequiredMixin, generic.ListView):
    model = Mascota
    template_name = "mascota_list.html"

    def get_queryset(self):
        queryset = Mascota.objects.filter(dueño = self.request.user.perfilcliente)
        return queryset

    def get(self, request, *args, **kwargs):
        if self.request.user.groups.name == "Cliente":
            return super().get(request, *args, **kwargs)
        else:
            return(redirect('home'))


class ProfileCliente(LoginRequiredMixin, generic.UpdateView):
    model = PerfilCliente
    template_name = "profile-cliente.html"
    fields = ['nombres', 'apellidos', 'phone', 'direccion', 'ciudad']

    def get(self, request, *args, **kwargs):
        if self.request.user.groups.name == "Cliente":
            return super().get(request, *args, **kwargs)
        else:
            return(redirect('home'))

    def get_object(self):
        return PerfilCliente.objects.get(pk=self.request.user.perfilcliente.pk)

class ProfileMascota(LoginRequiredMixin, generic.UpdateView):
    model = Mascota
    template_name = "perfil-mascota.html"
    fields = ['nombre','peso', 'sexo', 'descripcion', 'imagen']


    def get(self, request, *args, **kwargs):
        if self.request.user == self.get_object().dueño.usuario:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')

class ListaCitas(LoginRequiredMixin, generic.ListView):
    model = Cita
    template_name = "lista-citas.html"

    def get_queryset(self):
        queryset = Cita.objects.filter(Q(paciente__isnull = True ) & Q(fecha__gte = datetime.now()))
        return queryset

    def get(self, request, *args, **kwargs):
        if self.request.user.groups.name == "Cliente":
            return super().get(request, *args, **kwargs)
        else:
            return(redirect('home'))


class DetalleCita(LoginRequiredMixin, generic.DetailView):
    model = Cita
    template_name = "detalle-cita.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.groups.name == "Cliente":
            return super().get(request, *args, **kwargs)
        else:
            return(redirect('home'))

class ReservarCita(LoginRequiredMixin, generic.UpdateView):
    model = Cita
    template_name = "reservar-cita.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.groups.name == "Cliente" and Cita.objects.filter( Q(pk = self.get_object().pk) & Q(paciente_isnull = True) & Q(fecha_gte = datetime.now())):
            return super().get(request, *args, *kwargs)
        else:
            if self.request.user.groups.name == "Cliente":
                return redirect('home-cliente')
            else:
                return redirect('home')
    




        
        
