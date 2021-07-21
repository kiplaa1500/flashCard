# type:ignore
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('flash.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('logout/', views.LogoutView.as_view(), {"next_page": '/'}) ,
    path('api-token-auth/', obtain_auth_token)
]
