from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name="add"),
    path('show',views.myshow,name="show")
]
