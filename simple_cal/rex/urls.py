#import simple urls
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dis,name="dis")
]
