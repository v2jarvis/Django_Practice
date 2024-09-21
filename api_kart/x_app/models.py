# import necessary modules
from django.db import models

# Create your models here.


class Product(models.Model):
    """
    Model for Product
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    """
    Model for Cart
    """
    products = models.ManyToManyField(Product, through="CartItem")


class CartItem(models.Model):
    """
    Model for CartItem
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        """
        Meta class for CartItem
        """
        unique_together = ("cart", "product")

class Order(models.Model):
    """
    Model for Order the cart product
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default="pending")

class OrderItem(models.Model):
    """
    Model for items in an Order
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    