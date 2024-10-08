from rest_framework import viewsets
from .models import *
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer
    
class SeasonalProductViewSet(viewsets.ModelViewSet):
    queryset         = SeasonalProduct.objects.all()
    serializer_class = SeasonalProductSerializer

class BulkProductViewSet(viewsets.ModelViewSet):
    queryset         = BulkProduct.objects.all()
    serializer_class = BulkProductSerializer
    
    
class DiscountViewSet(viewsets.ModelViewSet):
    queryset         = Discount.objects.all()
    serializer_class = DiscountSerializer

class PercentageDiscountViewSet(viewsets.ModelViewSet):
    queryset         = PercentageDiscount.objects.all()
    serializer_class = PercentageDiscountSerializer
    
    
class FixedAmountDiscountViewSet(viewsets.ModelViewSet):
    queryset         = FixedAmountDiscount.objects.all()
    serializer_class = FixedAmountDiscountSerializer
    
    
#ORDER
class OrderViewSet(viewsets.ModelViewSet):
    queryset         = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset         = OrderItem.objects.all()
    serializer_class = OrderItemSerializer