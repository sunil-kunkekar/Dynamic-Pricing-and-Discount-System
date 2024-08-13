from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import ProductViewSet, SeasonalProductViewSet,BulkProductViewSet,DiscountViewSet,PercentageDiscountViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'seasonal-products', SeasonalProductViewSet)
router.register(r'bulk-products', BulkProductViewSet)

router.register(r'discounts', DiscountViewSet)
router.register(r'percentage-discounts', PercentageDiscountViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
