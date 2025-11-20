from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'cliente'

router = routers.DefaultRouter()
router.register('', views.ClienteViewSet, basename='Clientes')

urlpatterns = [
    path('', include(router.urls)),
]