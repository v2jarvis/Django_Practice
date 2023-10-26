#this is app urls here we import some neccessory files and path
# In your urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<str:key>/', views.week, name='week'),  # Use the correct view function name 'week'
]
