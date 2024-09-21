# import necessary module
from django.urls import path

from . import views
from .views import CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.register, name="register"),
    # path(
    #     "password-reset/", views.password_reset_request, name="password_reset_request"
    # ),
    # path(
    #     "password-reset-confirm/",
    #     views.password_reset_confirm,
    #     name="password_reset_confirm",
    # ),
]
