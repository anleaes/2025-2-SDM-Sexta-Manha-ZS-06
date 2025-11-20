from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'veiculo'

router = routers.DefaultRouter()
router.register('', views.VeiculoViewSet, basename='veiculos')

urlpatterns = [
    path('', include(router.urls)),
]