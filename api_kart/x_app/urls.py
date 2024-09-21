# import the necessary modules
from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.list_products, name="products"),
    path("products/add/", views.add_product, name="addproduct"),
    path("cart/add/", views.add_to_cart, name="addcart"),
    path("cart/remove/", views.remove_from_cart, name="removecart"),
    path('cart/view/', views.view_cart, name='viewcart'),
    path("cart/all/",views.product_cart,name="allcart"),
    path("cart/order/", views.place_order, name="placeorder"),
    path("cart/getorder/", views.get_order, name="getorder"),
]
#  end the url add if needed 