from django.contrib import admin
from pricing.models import Product, SeasonalProduct, BulkProduct, Discount, PercentageDiscount, FixedAmountDiscount, Order, OrderItem

# Admin class for Product to handle common settings
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_price')
    search_fields = ('name',)
    ordering = ('name',)

 
admin.site.register(Product, ProductAdmin)

