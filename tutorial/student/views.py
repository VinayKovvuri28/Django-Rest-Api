from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentModelSerializers
from rest_framework import status, viewsets
from rest_framework.response import Response
# Local Authentications and Permissions import
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated 

# Create your views here.
class Studentviewset(viewsets.ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class = StudentModelSerializers
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]