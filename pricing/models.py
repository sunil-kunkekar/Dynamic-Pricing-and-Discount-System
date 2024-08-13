from django.db import models

class Product(models.Model):
    name       = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_price(self):
        return self.base_price

    def __str__(self):
        return self.name


class SeasonalProduct(Product):
    season_discount_percentage = models.FloatField()

    def get_price(self):
        return self.base_price * (1 - self.season_discount_percentage / 100)



class BulkProduct(Product):
    bulk_discount_threshold  = models.IntegerField()
    bulk_discount_percentage = models.FloatField()

    def get_price(self, quantity=1):  # Default argument for quantity
        if quantity >= self.bulk_discount_threshold:
            return self.base_price * (1 - self.bulk_discount_percentage / 100)
        return self.base_price

# class BulkProduct(Product):
#     bulk_discount_threshold  = models.IntegerField()
#     bulk_discount_percentage = models.FloatField()
    
#     def get_price(self, quantity):  # Default quantity to 1 if not provided
#         if quantity >= self.bulk_discount_threshold:
#             return self.base_price * (1 - self.bulk_discount_percentage / 100)
#         return self.base_price

    # def get_price(self, quantity):
    #     if quantity >= self.bulk_discount_threshold:
    #         return self.base_price * (1 - self.bulk_discount_percentage / 100)
    #     return self.base_price


class Discount(models.Model):
    name = models.CharField(max_length=255)

    def apply_discount(self, price):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return self.name





class PercentageDiscount(Discount):
    percentage = models.FloatField()

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)

class FixedAmountDiscount(Discount):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def apply_discount(self, price):
        return max(0, price - self.amount)




class Order(models.Model):
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount  = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    quantity  = models.IntegerField(default=1)

    def calculate_total(self):
        if isinstance(self.product, BulkProduct):
            base_price = self.product.get_price(self.quantity)  # Pass quantity
        else:
            base_price = self.product.get_price()  # No quantity needed
        if self.discount:
            total_price = self.discount.apply_discount(base_price)
        else:
            total_price = base_price
        return total_price

    def __str__(self):
        return f"Order of {self.quantity} x {self.product.name}"





class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.product.get_price(self.quantity)
