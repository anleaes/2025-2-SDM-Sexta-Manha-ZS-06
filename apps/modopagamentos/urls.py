from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModoPagamentoViewSet

app_name = 'modopagamento'

router = DefaultRouter()
router.register('', ModoPagamentoViewSet, basename='modopagamento')

urlpatterns = [
    path('', include(router.urls)),
]