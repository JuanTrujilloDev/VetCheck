from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import LoginCaptcha
from django.contrib.auth.models import User
from django.views import generic
from .forms import CUserCreationForm
from django.contrib.auth.models import Group
# Create your views here.

class CLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    authentication_form = LoginCaptcha


class CUserCreationView(generic.CreateView):
    model = User
    form_class = CUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(CUserCreationView, self).get(request, args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        group = Group.objects.get(name = 'Cliente')
        user.groups.add(group)

        return super().form_valid(form)

    
        


