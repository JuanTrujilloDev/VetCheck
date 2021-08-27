from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from .forms import LoginCaptcha
# Create your views here.

class CLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    authentication_form = LoginCaptcha


