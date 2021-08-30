from django.forms.forms import Form
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import CLoginView, CUserCreationView
from .views import activate_email


urlpatterns = [
    path('login/', CLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', CUserCreationView.as_view(), name="register"),
    path('', include('social_django.urls', namespace="social")),
    path('activate/<uidb64>/<token>/', activate_email, name='activate'),
]
