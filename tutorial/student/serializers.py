from rest_framework import serializers
from .models import *

class StudentModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields='__all__'