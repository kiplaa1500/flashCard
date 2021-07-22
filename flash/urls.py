# type:ignore
from posixpath import basename
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import flashCardViewSet,ProfileViewSet
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


router = DefaultRouter()
router.register('flashcard',flashCardViewSet,basename='flashcard')
router.register('profile',ProfileViewSet,basename='profile')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:id>',include(router.urls)),
    path('flascard/<int:id>',views.flashcard,name='flashcard_item'),
    path('',views.default,name='home'),
    path('search/', views.search_results, name='search_results'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^project/(\d+)',views.flashcard,name='flascard_item'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)