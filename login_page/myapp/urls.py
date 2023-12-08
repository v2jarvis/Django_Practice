from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.loginn,name="login"),
    path('about/',views.about,name="about"),
    path('logout/',views.logoutt,name="logout"),
    path('analyze/',views.analyze,name='analyze'),
    path('user/',views.user,name='user')
]