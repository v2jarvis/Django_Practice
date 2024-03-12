from django.db import models

class info(models.Model):
    name=models.CharField(max_lenght=20)
    mob=models.BigIntegerField()
    add=models.CharField(max_lenght=30)
