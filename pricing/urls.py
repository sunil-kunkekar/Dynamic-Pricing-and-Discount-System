from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import ProductViewSet, SeasonalProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'seasonal-products', SeasonalProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
