from django.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView 
from . import views

urlpatterns = [
    url(r'^accounts/register$',views.registration,name='register'),
    url(r'^accounts/login$',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^accounts/logout$',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout')
]