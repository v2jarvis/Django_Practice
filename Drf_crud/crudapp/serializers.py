from rest_framework import serializers
from .models import Student

# class stu_serializers(serializers.Serializer):
#     name=serializers.CharField(max_length=10,default=None)
#     mob=serializers.IntegerField()
#     address=serializers.CharField(max_length=50,default=None)

class stu_serializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = '__all__'