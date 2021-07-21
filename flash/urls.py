# type:ignore
from posixpath import basename
from django.urls import path,include
from rest_frameworks.routers import DefaultRauter
from .views import flashCardViewSet


rauter = DefaultRauter
router.register('flashcard',flashCardViewSet,basename=flashcard)

urlpatterns = [
    path('viewset/',include('router.urls')),
    path('viewset/<int:id>',include('router.urls')),

]