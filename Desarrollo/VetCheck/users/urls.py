from django.forms.forms import Form
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import CLoginView


urlpatterns = [
    path('login/', CLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', include('social_django.urls', namespace="social"))
]
