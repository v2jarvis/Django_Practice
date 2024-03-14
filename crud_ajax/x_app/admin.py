from django.contrib import admin
from .models import Student

admin.site.register(Student)




# @admin.register(Student)
# class Student(admin.ModelAdmin):
#     pass
