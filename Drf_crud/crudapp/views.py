from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import stu_serializers

@api_view(['GET','POST'])
def stu_data(request):
    if request.method=='GET':
        stu=Student.objects.all()
        serializer=stu_serializers(stu,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=stu_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def stu_test(request, pk):
    try:
        data=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=stu_serializers(data)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=stu_serializers(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
