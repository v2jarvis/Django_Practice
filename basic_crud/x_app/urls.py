from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.home, name="start"),
    path("add", views.std_info, name="add"),
    path("data", views.show, name="show"),
    path("del/<int:id>", views.del_data, name="del"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("update/<int:id>/", views.update, name="update"),
    path("loginn", views.loginn, name="loginn"),
    path("register", views.register, name="register"),
    path("logout/", views.logoutt, name="logout"),
    path("set_cookie", views.set_cookie, name="set_cookie"),
    path("get_cookie", views.get_cookie, name="get_cookie"),
    path("get_sess", views.get_sess, name="get_sess"),
    path("activate/<str:uidb64>/<str:token>/", views.activate, name="activate"),
    path("forget", views.forget, name="forget"),
    # re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate, name='activate'),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="pass_reset.html"),
        name="password_reset",
    ),
    path(
        "reset_password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("contact", views.contact, name="contact"),
]
