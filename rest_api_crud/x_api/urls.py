from .views import StudentView  
from django.urls import path  
  
urlpatterns = [  
    path('', StudentView.as_view())  
] 