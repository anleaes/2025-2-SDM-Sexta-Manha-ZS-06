from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MotoristaViewSet

app_name = "motorista"

router = DefaultRouter()
router.register(r'', MotoristaViewSet, basename='motorista')

urlpatterns = [
    path('', include(router.urls)),
]