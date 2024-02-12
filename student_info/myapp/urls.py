from django.urls import path
from . import views

urlpatterns = [
    path('',views.std_info,name="home"),
    path('data',views.show,name="show"),
    path('del/<int:sid>',views.del_data,name="del"),
    path('edit/<int:sid>/',views.edit,name='edit'),
    path('update/<int:sid>/',views.update,name='update')
]