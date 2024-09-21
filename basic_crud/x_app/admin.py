from django.contrib import admin

from .models import Contact, Students

# Register your models here.
admin.site.register(Students)
admin.site.register(Contact)
# admin.site.register(User)  # This is the default User model from Django
