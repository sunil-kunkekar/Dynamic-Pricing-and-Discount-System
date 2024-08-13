from rest_framework import serializers
from .models import *
from rest_framework import viewsets

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'base_price')
        
class SeasonalProductSerializer(ProductSerializer):
    season_discount_percentage = serializers.FloatField()

    class Meta(ProductSerializer.Meta):
        model = SeasonalProduct
        fields = ProductSerializer.Meta.fields + ('season_discount_percentage',)
        
        
class SeasonalProductViewSet(viewsets.ModelViewSet):
    queryset         = SeasonalProduct.objects.all()
    serializer_class = SeasonalProductSerializer

class BulkProductSerializer(ProductSerializer):
    bulk_discount_threshold = serializers.IntegerField()
    bulk_discount_percentage = serializers.FloatField()

    class Meta(ProductSerializer.Meta):
        model = BulkProduct
        fields = ProductSerializer.Meta.fields + ('bulk_discount_threshold', 'bulk_discount_percentage')
        

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'name')

class PercentageDiscountSerializer(DiscountSerializer):
    percentage = serializers.FloatField()

    class Meta(DiscountSerializer.Meta):
        model = PercentageDiscount
        fields = DiscountSerializer.Meta.fields + ('percentage',)