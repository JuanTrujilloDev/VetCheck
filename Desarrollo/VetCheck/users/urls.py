from django.forms.forms import Form
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import CLoginView, CUserCreationView, socialSuccess
from .views import activate_email
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', CLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', CUserCreationView.as_view(), name="register"),
    path('', include('social_django.urls', namespace="social")),
    path('activate/<uidb64>/<token>/', activate_email, name='activate'),
    path('social/success', socialSuccess, name="social-success")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
