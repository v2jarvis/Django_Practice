# import necessary module
from django.urls import path
# from django.conf.urls import handler404

from . import views

urlpatterns = [
    path("", views.contact, name="contact")
    ]

# handler404 = views.custom_404