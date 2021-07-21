from django.urls import url
from . import views
urlpatterns = [
   url(r'^registartion$', views.register, name='register')
]