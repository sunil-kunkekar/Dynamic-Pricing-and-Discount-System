from django.contrib import admin
from pricing.models import Product, SeasonalProduct, BulkProduct, Discount, PercentageDiscount, FixedAmountDiscount, Order, OrderItem

# Admin class for Product to handle common settings
class ProductAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'base_price')
    search_fields = ('name',)
    ordering      = ('name',)

admin.site.register(Product, ProductAdmin)

class SeasonalProductAdmin(ProductAdmin):
    list_display  = ProductAdmin.list_display + ('season_discount_percentage',)
    search_fields = ProductAdmin.search_fields + ('season_discount_percentage',)

admin.site.register(SeasonalProduct, SeasonalProductAdmin)

class BulkProductAdmin(ProductAdmin):
    list_display  = ProductAdmin.list_display + ('bulk_discount_threshold', 'bulk_discount_percentage')
    search_fields = ProductAdmin.search_fields + ('bulk_discount_threshold', 'bulk_discount_percentage')

admin.site.register(BulkProduct, BulkProductAdmin)

class DiscountAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name',)
    search_fields = ('name',)

admin.site.register(Discount, DiscountAdmin)

class PercentageDiscountAdmin(DiscountAdmin):
    list_display  = DiscountAdmin.list_display + ('percentage',)
    search_fields = DiscountAdmin.search_fields + ('percentage',)

admin.site.register(PercentageDiscount, PercentageDiscountAdmin)

class FixedAmountDiscountAdmin(DiscountAdmin):
    list_display  = DiscountAdmin.list_display + ('amount',)
    search_fields = DiscountAdmin.search_fields + ('amount',)

admin.site.register(FixedAmountDiscount, FixedAmountDiscountAdmin)


admin.site.register(Order)
admin.site.register(OrderItem)

