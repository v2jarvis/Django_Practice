#create multiple model here
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20,null=False)
    course=models.CharField(max_length=10,default=None)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=20,default=None)

def __str___(self):
    return self.name
