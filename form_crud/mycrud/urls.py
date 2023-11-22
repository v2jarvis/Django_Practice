from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name="add"),
    path('show',views.myshow,name="show"),
    path('del/<int:id>/',views.delete,name="del"),
    path('edit/<int:id>/',views.edit,name="edit")
]
