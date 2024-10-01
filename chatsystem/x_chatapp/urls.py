from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logoutt"),
    path("send-message/", views.SendMessageView.as_view(), name="send_message"),
    path("fetch-messages/", views.FetchMessagesView.as_view(), name="fetch_messages"),
    path(
        "unread_message_count/",
        views.UnreadMessageCountView.as_view(),
        name="unread_message_count",
    ),
]
