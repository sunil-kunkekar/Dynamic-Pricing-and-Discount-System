from django.contrib import admin
from pricing.models import Product, SeasonalProduct, BulkProduct, Discount, PercentageDiscount, FixedAmountDiscount, Order, OrderItem

# Admin class for Product to handle common settings
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_price')
    search_fields = ('name',)
    ordering = ('name',)

 
admin.site.register(Product, ProductAdmin)

class SeasonalProductAdmin(ProductAdmin):
    list_display = ProductAdmin.list_display + ('season_discount_percentage',)
    search_fields = ProductAdmin.search_fields + ('season_discount_percentage',)
    
admin.site.register(SeasonalProduct, SeasonalProductAdmin)