from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="start"),
    path('add',views.std_info,name="add"),
    path('data',views.show,name="show"),
    path('del/<int:sid>',views.del_data,name="del"),
    path('edit/<int:sid>/',views.edit,name='edit'),
    path('update/<int:sid>/',views.update,name='update'),
    path('loginn',views.loginn,name="loginn"),
    path('register',views.register,name='register'),
    path('logout/',views.logoutt,name="logout")
]