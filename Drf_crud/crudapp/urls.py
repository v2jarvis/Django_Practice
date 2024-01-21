from django.urls import path
from . import views
urlpatterns=[
    path('',views.stu_data,name='studata'),
    path('<int:pk>/', views.stu_test,name='stutest')
]