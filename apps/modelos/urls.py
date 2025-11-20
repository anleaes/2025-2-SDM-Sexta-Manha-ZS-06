from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'modelos'

router = routers.DefaultRouter()
router.register('', views.ModeloViewSet, basename='Modelos')

urlpatterns = [
    path('', include(router.urls))
]