from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name="home"),
    path('insert',views.insert,name='insert'),
    path('retrive',views.re,name='retrive'),
    path('search1',views.search1,name='search1')
]
