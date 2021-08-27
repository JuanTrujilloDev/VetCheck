from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class LoginCaptcha(AuthenticationForm):
    captcha = ReCaptchaField(required = True, widget= ReCaptchaV2Checkbox(attrs={'data-size':'normal', 'required':True}))

    class Meta:
        model = User
        fields = ['username', 'password', 'captcha']

