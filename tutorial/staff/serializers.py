from rest_framework import serializers
from .models import *

class StaffModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        fields='__all__'