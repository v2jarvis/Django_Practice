from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=10,default=None)
    mob=models.BigIntegerField()
    address=models.CharField(max_length=50,default=None)
