#create multiple model here
from django.db import models

class Employee(models.Model):
    sid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,null=False)
    mobile=models.BigIntegerField()
    email=models.EmailField()

def __str___(self):
    return self.name
