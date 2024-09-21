from django.contrib import admin

from .models import Contact, Student

# Register your models here.

admin.site.register(Student)
admin.site.register(Contact)
