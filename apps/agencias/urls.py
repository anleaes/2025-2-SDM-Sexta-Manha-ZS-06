from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'agencia'

router = routers.DefaultRouter()
router.register('', views.AgenciaViewSet, basename='agencia')

urlpatterns = [
    path('', include(router.urls)),
]
