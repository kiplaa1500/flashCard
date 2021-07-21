from django.urls import url
from . import views
urlpatterns = [
   url(r'^', views.register, name='register')
]