from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers

# Create your views here.

@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializers(student_obj, many=True)
    return Response({'status':200,
                     'payload': serializer.data
                     })

def post_student(request):
    pass