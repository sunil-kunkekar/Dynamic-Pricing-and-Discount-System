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
        
        
class FixedAmountDiscountSerializer(DiscountSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta(DiscountSerializer.Meta):
        model  = FixedAmountDiscount
        fields = DiscountSerializer.Meta.fields + ('amount',)
        


#oRDER
# class OrderSerializer(serializers.ModelSerializer):
#     product  = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
#     discount = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all(), required=False, allow_null=True)
#     quantity = serializers.IntegerField()

#     class Meta:
#         model = Order
#         fields = ('id', 'product', 'discount', 'quantity', 'calculate_total')

#     def get_calculate_total(self, obj):
#         return obj.calculate_total()



class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id','product', 'discount', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.calculate_total()

    def validate_discount(self, value):
        if value is not None and not isinstance(value, (PercentageDiscount, FixedAmountDiscount)):
            raise serializers.ValidationError("Discount must be a valid subclass like PercentageDiscount or FixedAmountDiscount.")
        return value




class OrderItemSerializer(serializers.ModelSerializer):
    order     = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    product   = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity  = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity', 'get_total_price')

    def get_get_total_price(self, obj):
        return obj.get_total_price()