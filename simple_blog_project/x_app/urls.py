from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from  . import views

urlpatterns = [
    path("",views.blogs ,name="blog"),
    path("register/", views.Register ,name="register"),
    path("login/",views.Login, name="login"),
    path('profile/',views.Profile ,name="profile"),
    #path('edit_profile/',views.edit_profile ,name="edit_profile"),
    path('add_blogs/',views.add_blogs ,name="add_blogs"),
    path('blog_comments/<slug:slug>/', views.blogs_comments, name='blog_comments'),
    path('delete_blog/<slug:slug>/', views.delete_blog, name='delete_blog'),
    #path('blog_comments/',views.blogs_comments,name="blog_comments"),
    path("logout/",views.logoutt,name="logout")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)