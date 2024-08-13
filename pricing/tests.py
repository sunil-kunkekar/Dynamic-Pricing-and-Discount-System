from django.test import TestCase
from .models import Product, SeasonalProduct, BulkProduct, PercentageDiscount, FixedAmountDiscount, Order, OrderItem

class ProductTestCase(TestCase):
    
    def setUp(self):
        self.product = Product.objects.create(name="Basic Product", base_price=100.00)
        self.seasonal_product = SeasonalProduct.objects.create(
            name="Seasonal Product", base_price=200.00, season_discount_percentage=10.0
        )
        self.bulk_product = BulkProduct.objects.create(
            name="Bulk Product", base_price=150.00, bulk_discount_threshold=5, bulk_discount_percentage=20.0
        )
    
    def test_product_price(self):
        self.assertEqual(self.product.get_price(), 100.00)

    def test_seasonal_product_price(self):
        self.assertEqual(self.seasonal_product.get_price(), 180.00)  # 200 - 10% discount

    def test_bulk_product_price_without_discount(self):
        self.assertEqual(self.bulk_product.get_price(quantity=4), 150.00)  # No discount applied

    def test_bulk_product_price_with_discount(self):
        self.assertEqual(self.bulk_product.get_price(quantity=6), 120.00)  # 20% discount applied


class DiscountTestCase(TestCase):
    
    def setUp(self):
        self.percentage_discount   = PercentageDiscount.objects.create(name="10% Off", percentage=10.0)
        self.fixed_amount_discount = FixedAmountDiscount.objects.create(name="50 Off", amount=50.00)

    def test_percentage_discount(self):
        discounted_price = self.percentage_discount.apply_discount(200.00)
        self.assertEqual(discounted_price, 180.00)  # 200 - 10% discount

    def test_fixed_amount_discount(self):
        discounted_price = self.fixed_amount_discount.apply_discount(200.00)
        self.assertEqual(discounted_price, 150.00)  # 200 - 50



# class OrderTestCase(TestCase):

#     def setUp(self):
#         self.product          = Product.objects.create(name="Basic Product", base_price=100.00)
#         self.seasonal_product = SeasonalProduct.objects.create(
#             name="Seasonal Product", base_price=200.00, season_discount_percentage=10.0
#         )
#         self.bulk_product = BulkProduct.objects.create(
#             name="Bulk Product", base_price=150.00, bulk_discount_threshold=5, bulk_discount_percentage=20.0
#         )
#         self.percentage_discount = PercentageDiscount.objects.create(name="10% Off", percentage=10.0)
#         self.fixed_amount_discount = FixedAmountDiscount.objects.create(name="50 Off", amount=50.00)

#     def test_order_without_discount(self):
#         order = Order.objects.create(product=self.product, quantity=3)
#         self.assertEqual(order.calculate_total(), 300.00)  # No discount applied

#     def test_order_with_percentage_discount(self):
#         order = Order.objects.create(product=self.seasonal_product, discount=self.percentage_discount, quantity=2)
#         self.assertEqual(order.calculate_total(), 360.00)  # 2 x (200 - 10%)

#     def test_order_with_fixed_amount_discount(self):
#         order = Order.objects.create(product=self.seasonal_product, discount=self.fixed_amount_discount, quantity=2)
#         self.assertEqual(order.calculate_total(), 280.00)  # 2 x (200 - 50)

#     def test_order_with_bulk_discount(self):
#         order = Order.objects.create(product=self.bulk_product, quantity=6)
#         self.assertEqual(order.calculate_total(), 720.00)  # 6 x (150 - 20%)


# class OrderItemTestCase(TestCase):

#     def setUp(self):
#         self.product    = Product.objects.create(name="Basic Product", base_price=100.00)
#         self.order      = Order.objects.create(product=self.product, quantity=1)
#         self.order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2)

#     def test_order_item_total_price(self):
#         self.assertEqual(self.order_item.get_total_price(), 200.00)  # 2 x 100