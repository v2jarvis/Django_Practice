# import modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from x_app import views

from .forms import LoginForm, MyPasswordChangingForm

# url routing of all
urlpatterns = [
    # product and search related urls
    path("", views.ProductView.as_view(), name="home"),
    path(
        "product-detail/<int:id>",
        views.ProductDetailView.as_view(),
        name="product-detail",
    ),
    path("mobile/", views.mobile, name="mobile"),
    path("mobile/<slug:data>", views.mobile, name="mobiledata"),
    path("laptop/", views.laptop, name="laptop"),
    path("laptop/<slug:data>", views.laptop, name="laptopdata"),
    path("search/", views.search, name="search"),
    # profile and orders related urls
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path("orders/", views.orders, name="orders"),
    # cart related urls
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.show_cart, name="cart"),
    path("pluscart/", views.plus_cart, name="pluscart"),
    path("minuscart/", views.minus_cart, name="minuscart"),
    path("removecart/", views.remove_cart, name="removecart"),
    # cookie and sessions related urls
    path("set_cookie/", views.set_cookie, name="setcookie"),
    # payment done and chechout realted urls
    path("paymentdone/", views.payment_done, name="paymentdone"),
    path("checkout/", views.checkout, name="checkout"),
    # login and registration related urls
    path(
        "passwordchange/",
        auth_views.PasswordChangeView.as_view(
            template_name="x_app/passwordchange.html",
            form_class=MyPasswordChangingForm,
            success_url="/passwordchangedone/",
        ),
        name="passwordchange",
    ),
    path(
        "passwordchangedone/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="x_app/passwordchangedone.html"
        ),
        name="passwordchangedone",
    ),
    path("accounts/login/", views.customer_login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path(
        "registration/",
        views.CustomerRegistrationView.as_view(),
        name="customerregistration",
    ),
    # reset password related urls
    path("forget/", views.forget, name="forget"),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="x_app/pass_reset.html"),
        name="password_reset",
    ),
    path(
        "reset_password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="x_app/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="x_app/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="x_app/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
