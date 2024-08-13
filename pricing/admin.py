from django.contrib import admin
from pricing.models import Product, SeasonalProduct, BulkProduct, Discount, PercentageDiscount, FixedAmountDiscount, Order, OrderItem

# Admin class for Product to handle common settings
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'base_price')
    search_fields = ('name',)
    ordering = ('name',)

 
admin.site.register(Product, ProductAdmin)

class SeasonalProductAdmin(ProductAdmin):
    list_display = ProductAdmin.list_display + ('season_discount_percentage',)
    search_fields = ProductAdmin.search_fields + ('season_discount_percentage',)
    
admin.site.register(SeasonalProduct, SeasonalProductAdmin)


class BulkProductAdmin(ProductAdmin):
    list_display  = ProductAdmin.list_display + ('bulk_discount_threshold', 'bulk_discount_percentage')
    search_fields = ProductAdmin.search_fields + ('bulk_discount_threshold', 'bulk_discount_percentage')
    
admin.site.register(BulkProduct, BulkProductAdmin)

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Discount, DiscountAdmin)

class PercentageDiscountAdmin(DiscountAdmin):
    list_display = DiscountAdmin.list_display + ('percentage',)
    search_fields = DiscountAdmin.search_fields + ('percentage',)
    
admin.site.register(PercentageDiscount, PercentageDiscountAdmin)

class FixedAmountDiscountAdmin(DiscountAdmin):
    list_display = DiscountAdmin.list_display + ('amount',)
    search_fields = DiscountAdmin.search_fields + ('amount',)

admin.site.register(FixedAmountDiscount, FixedAmountDiscountAdmin)





# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id','product', 'quantity', 'discount', 'calculate_total')
#     search_fields = ('product__name',)
    
#     def get_queryset(self, request):
#         # Customize queryset to include related discount information
#         return super().get_queryset(request).select_related('product', 'discount')

#     def calculate_total(self, obj):
#         return obj.calculate_total()

admin.site.register(Order)


# class OrderItemAdmin(admin.ModelAdmin):
#     list_display  = ('id','order', 'product', 'quantity', 'get_total_price')
#     list_filter   = ('order', 'product')
#     search_fields = ('order__product__name', 'product__name')

#     def get_total_price(self, obj):
#         return obj.get_total_price()
#     get_total_price.short_description = 'Total Price'
    
admin.site.register(OrderItem)