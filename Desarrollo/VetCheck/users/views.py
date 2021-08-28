from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from .forms import LoginCaptcha
from django.contrib.auth.models import User
from django.views import generic
from .forms import CUserCreationForm
# Create your views here.

class CLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    authentication_form = LoginCaptcha


class CUserCreationView(generic.CreateView):
    model = User
    form_class = CUserCreationForm
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(CUserCreationView, self).get(request, args, **kwargs)


