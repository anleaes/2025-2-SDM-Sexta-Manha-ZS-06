from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'marca'

router = routers.DefaultRouter()
router.register('', views.MarcaViewSet, basename='Marcas')

urlpatterns = [
    path('', include(router.urls) )
]
