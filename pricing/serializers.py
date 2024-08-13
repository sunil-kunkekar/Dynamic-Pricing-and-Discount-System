from rest_framework import serializers
from .models import Product, SeasonalProduct, BulkProduct, Discount, PercentageDiscount, FixedAmountDiscount, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'base_price')