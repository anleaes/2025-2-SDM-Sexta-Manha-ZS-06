from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocacaoViewSet

app_name = 'locacao'

router = DefaultRouter()
router.register('', LocacaoViewSet, basename='locacao')

urlpatterns = [
    path('', include(router.urls)),
]
