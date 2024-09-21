# import necessary modules
from rest_framework import serializers

from .models import Cart, CartItem, Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    """
    class Meta:
        """
        This is meta inner class
        """
        model = Product
        fields = ["id", "name", "price"]

class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for CartItem model.
    """
    product = ProductSerializer()
    
    class Meta:
        """
        This is meta inner class
        """
        model = CartItem
        fields = ["id", "product", "quantity"]

class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for Cart model.
    """
    items = CartItemSerializer(source="cartitem_set", many=True)

    class Meta:
        """
        This is meta inner class
        """
        model = Cart
        fields = ["id", "items"]

class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for OrderItem model.
    """
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.
    """
    items = OrderItemSerializer(source="orderitem_set", many=True)

    class Meta:
        model = Order
        fields = ["id", "cart", "order_date", "items"]
