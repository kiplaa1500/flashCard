# type:ignore
from posixpath import basename
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import flashCardViewSet


router = DefaultRouter()
router.register('flashcard',flashCardViewSet,basename='flashcard')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:id>',include(router.urls)),

]