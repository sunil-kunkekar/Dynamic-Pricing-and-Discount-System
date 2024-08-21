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
        

# class OrderSerializer(serializers.ModelSerializer):
#     product     = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
#     discount    = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all(), allow_null=True)
#     total_price = serializers.SerializerMethodField()

#     class Meta:
#         model = Order
#         fields = ['id', 'product', 'discount', 'quantity', 'total_price']

#     def validate_discount(self, value):
#         if value and not isinstance(value, (PercentageDiscount, FixedAmountDiscount)):
#             raise serializers.ValidationError("Invalid discount type. Only PercentageDiscount or FixedAmountDiscount are allowed.")
#         return value

#     def get_total_price(self, obj):
#         return obj.calculate_total()


from rest_framework import serializers
from pricing.models import Product, Discount, PercentageDiscount, FixedAmountDiscount, Order

from decimal import Decimal, InvalidOperation
from rest_framework import serializers
from pricing.models import Order, Product, Discount, PercentageDiscount, FixedAmountDiscount

class OrderSerializer(serializers.ModelSerializer):
    product = serializers.CharField()  # Handle product as a string
    discount = serializers.CharField(allow_null=True)  # Handle discount as a string
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'product', 'discount', 'quantity', 'total_price']

    def validate_product(self, value):
        try:
            product = Product.objects.get(name=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Invalid product name.")
        return product

    def validate_discount(self, value):
        if value is not None:
            try:
                # Attempt to treat discount as a fixed amount first
                discount_value = Decimal(value)
                if discount_value > 1:  # Assuming discounts above 1 are fixed amounts
                    discount = FixedAmountDiscount.objects.filter(amount=discount_value).first()
                else:
                    discount = PercentageDiscount.objects.filter(percentage=discount_value * 100).first()
            except InvalidOperation:
                raise serializers.ValidationError("Invalid discount value format.")
            
            if not discount:
                raise serializers.ValidationError("No matching discount found.")
            
            return discount
        return None

    def get_total_price(self, obj):
        return obj.calculate_total()

    def create(self, validated_data):
        product = validated_data.pop('product')
        discount = validated_data.pop('discount')
        order = Order.objects.create(product=product, discount=discount, **validated_data)
        return order




# class OrderSerializer(serializers.ModelSerializer):
#     product     = serializers.CharField()
#     discount    = serializers.CharField(allow_null=True, required=False)
#     total_price = serializers.SerializerMethodField()

#     class Meta:
#         model = Order
#         fields = ['id', 'product', 'discount', 'quantity', 'total_price']

#     def validate_discount(self, value):
#         if value:
#             try:
#                 discount = Discount.objects.get(pk=value)
#                 if not isinstance(discount, (PercentageDiscount, FixedAmountDiscount)):
#                     raise serializers.ValidationError("Invalid discount type. Only PercentageDiscount or FixedAmountDiscount are allowed.")
#             except Discount.DoesNotExist:
#                 raise serializers.ValidationError("Invalid discount ID.")
#         return value

#     def to_internal_value(self, data):
#         # Convert product and discount to their respective instances
#         if 'product' in data:
#             try:
#                 data['product'] = Product.objects.get(pk=data['product'])
#             except Product.DoesNotExist:
#                 raise serializers.ValidationError({"product": "Invalid product ID."})

#         if 'discount' in data and data['discount'] is not None:
#             try:
#                 data['discount'] = Discount.objects.get(pk=data['discount'])
#             except Discount.DoesNotExist:
#                 raise serializers.ValidationError({"discount": "Invalid discount ID."})

#         return super().to_internal_value(data)

#     def get_total_price(self, obj):
#         return obj.calculate_total()


from rest_framework import serializers
from pricing.models import OrderItem, Product, Order

class OrderItemSerializer(serializers.ModelSerializer):
    product         = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    order           = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    get_total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'get_total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()



# class OrderSerializer(serializers.ModelSerializer):
#     product     = ProductSerializer()
#     discount    = DiscountSerializer(allow_null=True)
#     total_price = serializers.SerializerMethodField()

#     class Meta:
#         model = Order
#         fields = ['id', 'product', 'discount', 'quantity', 'total_price']

#     def get_total_price(self, obj):
#         return obj.calculate_total()

# class OrderItemSerializer(serializers.ModelSerializer):
#     product  = ProductSerializer()
#     order    = OrderSerializer()

#     class Meta:
#         model = OrderItem
#         fields = ['id', 'order', 'product', 'quantity', 'get_total_price']

#     def get_total_price(self, obj):
#         return obj.get_total_price()

# class OrderSerializer(serializers.ModelSerializer):
#     total_price = serializers.SerializerMethodField()

#     class Meta:
#         model = Order
#         fields = ['id','product', 'discount', 'quantity', 'total_price']

#     def get_total_price(self, obj):
#         return obj.calculate_total()

#     def validate_discount(self, value):
#         if value is not None and not isinstance(value, (PercentageDiscount, FixedAmountDiscount)):
#             raise serializers.ValidationError("Discount must be a valid subclass like PercentageDiscount or FixedAmountDiscount.")
#         return value




# class OrderItemSerializer(serializers.ModelSerializer):
#     order     = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
#     product   = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
#     quantity  = serializers.IntegerField()

#     class Meta:
#         model = OrderItem
#         fields = ('id', 'order', 'product', 'quantity', 'get_total_price')

#     def get_get_total_price(self, obj):
#         return obj.get_total_price()