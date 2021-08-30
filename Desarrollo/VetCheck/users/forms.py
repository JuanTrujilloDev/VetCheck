from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


##--> Formulario login
class LoginCaptcha(AuthenticationForm):
    captcha = ReCaptchaField(required = True, widget= ReCaptchaV2Checkbox(attrs={'data-size':'normal', 'required':True}))

    class Meta:
        model = User
        fields = ['username', 'password', 'captcha']


##--> Creacion de usuarios.
class CUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField(required = True, widget= ReCaptchaV2Checkbox(attrs={'data-size':'normal', 'required':True}))
    class Meta:
        model = User
        fields = ['username','password1', 'password2', 'email', 'captcha']
        help_texts = {'username':mark_safe('<small>El usuario debe contener letras, numeros o @/./+/-_ unicamente.</small>'), 'email':mark_safe('<small>Digita tu correo electronico.</small>')}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            email2 = User.objects.get(email__iexact = email)
        except User.DoesNotExist:
            email2 = None
        finally:
            if email2 == None:
                return email
            else:
                raise forms.ValidationError("El correo electronico ya esta vinculado con otra cuenta!")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            username2 = User.objects.get(username__iexact = username)
        except User.DoesNotExist:
            username2 = None
        finally:
            if username2 == None:
                return username
            else:
                raise forms.ValidationError("El usuario ya se encuentra registrado")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = mark_safe("<ul><li><small>Digita una contraseña minimo de 8 caracteres</small></li><li><small>Añade mayusculas y caracteres especiales para hacerla mas fuerte.</small></li>")
        self.fields['password2'].help_text = mark_safe("<small>Repite la contraseña anterior.</small>")
        

