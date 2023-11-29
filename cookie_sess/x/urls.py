from django.urls import path
from . import views

urlpatterns = [
    path('',views.set_session,name="set"),
    path('get',views.get_session,name="get")
]
