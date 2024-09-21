from django.urls import path

from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("student/<int:id>", views.student_detail, name="student_details"),
    path("stu/", views.stu_list, name="stulist"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
