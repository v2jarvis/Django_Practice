# import the modules
import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View

from .forms import CustomerProfileForm, CustomerRegistrationForm, LoginForm
from .models import Cart, Customer, OrderPlaced, Product


class ProductView(View):
    """
    This class is used to display all the products in the database
    """

    def get(self, request):
        """
        This method is used to display all the products in the database
        """
        totalitem = 0
        mobiles = Product.objects.filter(category="M")
        laptops = Product.objects.filter(category="L")
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(
            request,
            "x_app/home.html",
            {"mobiles": mobiles, "laptops": laptops, "totalitem": totalitem},
        )


class ProductDetailView(View):
    """
    This class is used to display the details of the product
    """

    def get(self, request, id):
        """
        This method is used to display the details of the product
        """
        totalitem = 0
        product = Product.objects.get(id=id)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)
            ).exists()
        return render(
            request,
            "x_app/productdetail.html",
            {
                "product": product,
                "item_already_in_cart": item_already_in_cart,
                "totalitem": totalitem,
            },
        )


def search(request):
    """
    This function is used to search the product
    """
    query = request.GET.get("search1")
    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, "x_app/search.html", {"products": products})


def add_to_cart(request):
    """
    This function is used to add the product to the cart
    """
    product_id = request.GET.get("prod_id")
    product = get_object_or_404(Product, id=product_id)

    # if not request.user.is_authenticated:
    #     product_id=request.GET.get('prod_id')
    #     product = get_object_or_404(Product, id=product_id)
    #     Cart(product=product).save()
    #     return redirect('/cart')

    if not request.user.is_authenticated:
        cart = request.cart
        if str(product_id) in cart:
            cart[str(product_id)] += 1
        else:
            cart[str(product_id)] = 1
        response = redirect("/cart")
        response.set_cookie("cart", json.dumps(cart), max_age=3600)
        return response
    else:
        user = request.user
        cart_item, created = Cart.objects.get_or_create(user=user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        messages.success(request, "Product added to cart")
        return redirect("/cart")


def show_cart(request):
    """
    This function is used to display the cart
    """
    totalitem = 0
    amount = 0.0
    shipping_amount = 50.0
    total_amount = 0.0

    if request.user.is_authenticated:
        user = request.user
        totalitem = Cart.objects.filter(user=user).count()
        cart_items = Cart.objects.filter(user=user)

        for item in cart_items:
            tempamount = item.quantity * item.product.discounted_price
            amount += tempamount
    else:
        cart = request.cart
        cart_items = []
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, id=product_id)
            cart_items.append({"product": product, "quantity": quantity})

        for item in cart_items:
            tempamount = item["quantity"] * item["product"].discounted_price
            amount += tempamount

    total_amount = amount + shipping_amount
    return render(
        request,
        "x_app/addtocart.html",
        {
            "carts": cart_items,
            "totalamount": total_amount,
            "amount": amount,
            "totalitem": totalitem,
        },
    )


@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    """
    This class is used to display the profile of the user
    """

    def get(self, request):
        """
        This function is used to display the profile of the user
        """
        form = CustomerProfileForm()
        return render(
            request, "x_app/profile.html", {"form": form, "active": "btn-primary"}
        )

    def post(self, request):
        """
        This function is used to update the profile of the user
        """
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            locality = form.cleaned_data["locality"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            pincode = form.cleaned_data["pincode"]
            reg = Customer(
                user=user,
                name=name,
                locality=locality,
                city=city,
                state=state,
                pincode=pincode,
            )
            reg.save()
            messages.success(request, "Congratulations!! Profile Update Successfully")
            return render(request, "x_app/profile.html", {"form": form})


def plus_cart(request):
    """
    This function is used to add the quantity of the product in the cart
    """
    if request.method == "GET":
        prod_id = request.GET.get("id")
        print(prod_id)

        if request.user.is_authenticated:
            cart_item, created = Cart.objects.get_or_create(
                user=request.user, product_id=prod_id
            )
            cart_item.quantity += 1
            cart_item.save()
            quantity = cart_item.quantity
        else:
            cart = request.session.get("cart", {})
            cart[prod_id] = cart.get(prod_id, 0) + 1
            request.session["cart"] = cart
            request.session.modified = True
            quantity = cart[prod_id]

        amount = 0.0
        shipping_amount = 50.0

        if request.user.is_authenticated:
            cart_items = Cart.objects.filter(user=request.user)
        else:
            cart_items = [
                {"product": get_object_or_404(Product, id=pid), "quantity": qty}
                for pid, qty in cart.items()
            ]

        for item in cart_items:
            if request.user.is_authenticated:
                amount += item.quantity * item.product.discounted_price
            else:
                amount += item["quantity"] * item["product"].discounted_price

        total_amount = amount + shipping_amount

        data = {"quantity": quantity, "amount": amount, "total_amount": total_amount}
        return JsonResponse(data)


def minus_cart(request):
    """
    Decrease the quantity of a product in the cart
    """
    if request.method == "GET":
        prod_id = request.GET.get("id")

        if request.user.is_authenticated:
            cart_item = Cart.objects.get(user=request.user, product_id=prod_id)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                quantity = cart_item.quantity
            else:
                cart_item.delete()
                quantity = 0
        else:
            cart = request.session.get("cart", {})
            if cart.get(prod_id):
                cart[prod_id] -= 1
                if cart[prod_id] <= 0:
                    del cart[prod_id]
                request.session["cart"] = cart
                request.session.modified = True
            quantity = cart.get(prod_id, 0)

        amount = 0.0
        shipping_amount = 50.0

        if request.user.is_authenticated:
            cart_items = Cart.objects.filter(user=request.user)
        else:
            cart_items = [
                {"product": get_object_or_404(Product, id=pid), "quantity": qty}
                for pid, qty in cart.items()
            ]

        for item in cart_items:
            if request.user.is_authenticated:
                amount += item.quantity * item.product.discounted_price
            else:
                amount += item["quantity"] * item["product"].discounted_price

        total_amount = amount + shipping_amount

        data = {"quantity": quantity, "amount": amount, "total_amount": total_amount}
        return JsonResponse(data)


@login_required
def remove_cart(request):
    """
    Remove a product from the cart
    """
    if request.method == "GET":
        prod_id = request.GET.get("id")

        if request.user.is_authenticated:
            Cart.objects.filter(user=request.user, product_id=prod_id).delete()
        else:
            cart = request.session.get("cart", {})
            if cart.get(prod_id):
                del cart[prod_id]
                request.session["cart"] = cart
                request.session.modified = True

        amount = 0.0
        shipping_amount = 50.0

        if request.user.is_authenticated:
            cart_items = Cart.objects.filter(user=request.user)
        else:
            cart = request.session.get("cart", {})
            cart_items = [
                {"product": get_object_or_404(Product, id=pid), "quantity": qty}
                for pid, qty in cart.items()
            ]

        for item in cart_items:
            if request.user.is_authenticated:
                amount += item.quantity * item.product.discounted_price
            else:
                amount += item["quantity"] * item["product"].discounted_price

        total_amount = amount + shipping_amount

        data = {"amount": amount, "total_amount": total_amount}
        return JsonResponse(data)


@login_required
def address(request):
    """
    Get the user's address
    """
    add = Customer.objects.filter(user=request.user)
    return render(request, "x_app/address.html", {"add": add, "active": "btn-primary"})


@login_required
def orders(request):
    """
    View all orders
    """
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, "x_app/orders.html", {"op": op})


def mobile(request, data=None):
    """
    This function is used to display the mobiles in the database
    """
    if data == None:
        mobiles = Product.objects.filter(category="M")
    elif data == "MI" or data == "Samsung" or data == "Apple":
        mobiles = Product.objects.filter(category="M").filter(brand=data)
    elif data == "bellow":
        mobiles = Product.objects.filter(category="M").filter(
            discounted_price__lt=20000
        )
    elif data == "above":
        mobiles = Product.objects.filter(category="M").filter(
            discounted_price__gt=20000
        )
    return render(request, "x_app/mobile.html", {"mobiles": mobiles})


def laptop(request, data=None):
    """
    This function is used to display the laptop
    """
    if data == None:
        laptops = Product.objects.filter(category="L")
    elif data == "HP" or data == "Apple":
        laptops = Product.objects.filter(category="L").filter(brand=data)
    elif data == "bellow":
        laptops = Product.objects.filter(category="L").filter(
            discounted_price__lt=50000
        )
    elif data == "above":
        laptops = Product.objects.filter(category="L").filter(
            discounted_price__gt=50000
        )
    return render(request, "x_app/laptop.html", {"laptops": laptops})


def forget(request):
    """
    This function is used to forget the password using sending the registered email
    """
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            UserModel = get_user_model()
            email = form.cleaned_data["email"]
            associated_users = UserModel.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "x_app/pass_reset_email.html"
                    c = {
                        "email": user.email,
                        "domain": request.META["HTTP_HOST"],
                        "site_name": "your site",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            settings.EMAIL_HOST_USER,
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    # return HttpResponse("password reset link send")
                    return redirect("password_reset_done")
    form = PasswordResetForm()
    return render(request, "x_app/pass_reset.html", {"password_reset_form": form})


class CustomerRegistrationView(View):
    """
    This function is used to register the customer
    """

    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "x_app/customerregistration.html", {"form": form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations!! Registered Successfully")
            form.save()
        return render(request, "x_app/customerregistration.html", {"form": form})


def customer_login(request):
    """
    This function is used to login the customer
    """
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                cart_cookie = request.COOKIES.get("cart", "{}")
                cart_data = json.loads(cart_cookie)
                request.session["cart"] = cart_data
                for product_id, quantity in cart_data.items():
                    product = get_object_or_404(Product, id=product_id)
                    cart_item, created = Cart.objects.get_or_create(
                        user=user, product=product
                    )
                    if not created:
                        cart_item.quantity += quantity
                    else:
                        cart_item.quantity = quantity
                    cart_item.save()
                response = redirect("profile")
                response.delete_cookie("cart")
                return response
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "x_app/login.html", {"form": form})


@login_required
def checkout(request):
    """
    This function is used to checkout the product
    """
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 50.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = p.quantity * p.product.selling_price
            amount += tempamount
        total_amount = amount + shipping_amount
    return render(
        request,
        "x_app/checkout.html",
        {"add": add, "totalamount": total_amount, "carts": cart_items},
    )


@login_required
def payment_done(request):
    """
    This function is used to make the payment
    """
    user = request.user
    custid = request.GET.get("custid")
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(
            user=user, customer=customer, product=c.product, quantity=c.quantity
        ).save()
        c.delete()
    return redirect("orders")


def set_cookie(request):
    """
    set cookie function that have the functionality of set the cookie if
    someone perform the cookie set click
    """
    if request.method == "GET":
        try:
            id = request.GET.get("id")
            product = get_object_or_404(Product, id=id)
            title = product.title
            response = HttpResponse()
            response.set_cookie(
                "title",
                title,
                max_age=1000,
                secure=True,
                httponly=True,
                samesite="Strict",
            )
            return response
        except Product.DoesNotExist:
            return HttpResponse(status=404)
        except Exception:
            return HttpResponse(status=500)
    else:
        return HttpResponse(status=405)
