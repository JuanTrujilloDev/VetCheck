from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from users.models import PerfilCliente
# Create your views here.

class HomeClienteView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'homemain.html'


    def get(self, request):
        try:
            if request.user.groups.filter(name = 'Cliente').exists() and PerfilCliente.objects.filter(usuario = request.user).exists():
                return super().get(self, request)
            else:
                return(redirect('home'))
        
        except:
            return(redirect('home'))

        
        
