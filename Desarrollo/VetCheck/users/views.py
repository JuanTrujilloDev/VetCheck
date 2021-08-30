from typing import Type
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import LoginCaptcha
from django.contrib.auth.models import User
from django.views import generic
from .forms import CUserCreationForm
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
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
        current_site = get_current_site(request)
        mail_subject = 'Confirma tu cuenta VetCheck'
        message = render_to_string('email_activation.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':  urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()

        return super().form_valid(form)

def activate_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Tu cuenta ha sido activada ya puedes iniciar sesion!')
    else:
        return HttpResponse('Link de activacion invalido!')

    
        


