from django.urls import path
from . import views

urlpatterns = [
    path('',views.std_info,name="home"),
    path('data',views.show,name="show"),
    path('del/<int:sid>',views.del_data,name="del")
    #path('delshow',views.del_data,name="show")
]