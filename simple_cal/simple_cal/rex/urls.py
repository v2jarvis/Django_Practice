#import simple urls
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name="home")
]
