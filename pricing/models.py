from django.db import models

class Product(models.Model):
    name       = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_price(self):
        return self.base_price

    class Meta:
        abstract = True

class SeasonalProduct(Product):
    season_discount_percentage = models.FloatField()

    def get_price(self):
        return self.base_price * (1 - self.season_discount_percentage / 100)

class BulkProduct(Product):
    bulk_discount_threshold  = models.IntegerField()
    bulk_discount_percentage = models.FloatField()

    def get_price(self, quantity):
        if quantity >= self.bulk_discount_threshold:
            return self.base_price * (1 - self.bulk_discount_percentage / 100)
        return self.base_price

class Discount(models.Model):
    name = models.CharField(max_length=255)

    def apply_discount(self, price):
        raise NotImplementedError("Subclasses must implement this method")

    class Meta:
        abstract = True

class PercentageDiscount(Discount):
    percentage = models.FloatField()

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)

class FixedAmountDiscount(Discount):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def apply_discount(self, price):
        return max(0, price - self.amount)
