from django.urls import url
from . import views

urlpatterns = [
    url(r'^register$',views.registration,name='register'),
]