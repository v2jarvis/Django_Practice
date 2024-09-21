# import necessory module
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contact, Student
from .serializers import ContactSerializer, StudentSerializer

@api_view(["GET", "POST"])
def student_list(request):
    """
    List all students or create a new student.
    """
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return None

@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, id):
    """
    Retrieve, update, or delete a specific student.
    """
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return None

@api_view(["GET"])
def stu_list(request):
    """
    This function is perform the search and pagination on the student data.
    """
    students = Student.objects.all()

    search = request.GET.get("search", None)
    if search:
        stu = students.filter(Q(name__startswith=search) | Q(email__startswith=search))
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    sort = request.GET.get("sort", None)
    if sort:
        stu = students.order_by(sort)
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    try:
        page = request.GET.get("page", None)
        paginator = Paginator(students, 5)
        if page:
            try:
                stu = paginator.page(page)
            except PageNotAnInteger:
                stu = paginator.page(1)
            except EmptyPage:
                stu = paginator.page(paginator.num_pages)
        else:
            stu = paginator.page(1)

        serializer = StudentSerializer(stu, many=True)
        context = {
            "count": paginator.count,
            "next": stu.next_page_number(),
            "previous": stu.previous_page_number(),
            "results": serializer.data,
        }
        return Response(context, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ContactView(APIView):
    """
    This function is perform the post and get the contact data.
    """

    def post(self, request):
        """
        This function is perform the post request and save the contact data.
        """
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        This function is perform the get request and return the contact data.
        """
        data = Contact.objects.all()
        serializer = ContactSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
