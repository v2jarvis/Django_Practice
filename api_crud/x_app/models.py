# import necessary modules
from django.db import models


class Student(models.Model):
    """
    This is a model for a student.
    """

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # add more fields as needed

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    """
    Model for contact information
    """

    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message)
