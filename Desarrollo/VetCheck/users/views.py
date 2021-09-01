from typing import Type
from django.core import mail
from django.http import request
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from .forms import LoginCaptcha
from django.contrib.auth.models import User
from django.views import generic
from .forms import CUserCreationForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

class CLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    authentication_form = LoginCaptcha

    ##ALERTA USUARIO NO VERIFICADO


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
        current_site = get_current_site(self.request)
        mail_subject = 'Confirma tu cuenta VetCheck'
        message = render_to_string('email_activation.html', {
            'domain': current_site.domain,
            'user': user,
            'uid':  urlsafe_base64_encode(force_bytes(user.pk)),
            'token':   default_token_generator.make_token(user),},
            )
        to_email = form.cleaned_data.get('email')
        send_mail(
            mail_subject, message, 'vetcheck@gmail.com', [to_email]
        )

        messages.success(self.request, 'Por favor confirma tu email para ingresar.')
        return HttpResponseRedirect(reverse('login'))

def activate_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email confirmado correctamente, ahora puedes ingresar.')
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponse('Link de activacion invalido!')

@login_required(login_url="/login")
def socialSuccess(request):
    defaultgroup = Group.objects.get(name = 'Cliente')
    user = request.user
    user.groups.add(defaultgroup)

    return redirect('login')


    
        


