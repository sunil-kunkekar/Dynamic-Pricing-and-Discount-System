from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import ProductViewSet, SeasonalProductViewSet,BulkProductViewSet,DiscountViewSet,PercentageDiscountViewSet,FixedAmountDiscountViewSet,OrderItemViewSet,OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'seasonal-products', SeasonalProductViewSet)
router.register(r'bulk-products', BulkProductViewSet)

router.register(r'discounts', DiscountViewSet)
router.register(r'percentage-discounts', PercentageDiscountViewSet)

router.register(r'fixed-amount-discounts', FixedAmountDiscountViewSet)

router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
