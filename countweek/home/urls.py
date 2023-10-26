#this is app urls here we import some neccessory files and path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dis,name="display"),
   
]