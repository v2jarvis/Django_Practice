# import necessary modules
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cart, CartItem, Product, Order, OrderItem
from .serializers import CartSerializer, ProductSerializer, OrderSerializer


@api_view(["POST"])
def add_product(request):
    """
    Add a product to the cart.
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_products(request):
    """
    List all products
    """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_to_cart(request):
    """
    Add a product to the cart.
    """
    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity", 1)
    cart_id = request.data.get("cart_id")

    try:
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(id=cart_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        return Response(
            {"status": "Product added to cart"}, status=status.HTTP_201_CREATED
        )
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

@api_view(['GET'])
def product_cart(request):
    """
    Get the products in the cart.
    """
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def view_cart(request):
    """
    Retrieve the contents of a cart.
    """
    cart_id = request.query_params.get('cart_id')

    try:
        cart = Cart.objects.get(id=cart_id)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["DELETE"])
def remove_from_cart(request):
    """
    Remove a product from a cart.
    """
    product_id = request.data.get("product_id")
    cart_id = request.data.get("cart_id")

    try:
        cart = Cart.objects.get(id=cart_id)
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
        cart_item.delete()
        return Response(
            {"status": "Product removed from cart"}, status=status.HTTP_204_NO_CONTENT
        )
    except CartItem.DoesNotExist:
        return Response(
            {"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def place_order(request):
    """
    Place an order for the products in the cart and save them in the OrderItem model
    """
    cart_id = request.data.get("cart_id")
    
    try:
        cart = Cart.objects.get(id=cart_id)
        order = Order.objects.create(cart=cart)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.delete()
        return Response({"status": "Order placed successfully"}, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_order(request):
    """
    Get the order details including the products ordered.
    """
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)