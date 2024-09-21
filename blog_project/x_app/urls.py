# import necessary modules
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<str:slug>", views.detail, name="detail"),
    path("editblog/<slug:slug>/", views.edit_blog, name="editblog"),
    path("updateblog/<slug:slug>/", views.update, name="updateblog"),
    path("post/", views.blog_post, name="blogpost"),
    path("delete/<slug:slug>/", views.del_blog, name="delblog"),
    path("post/<slug:slug>/comment/", views.add_comment, name="add_comment"),
    path("post/<slug:slug>/like/", views.like_post, name="like_post"),
    path("post/<slug:slug>/dislike/", views.dislike_post, name="dislike_post"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logoutt"),
    path("search/", views.search_posts, name="search_posts"),

]
