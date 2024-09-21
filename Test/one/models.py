from django.db import models

# Create your models here.
class Student(models.Model):
    user=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)