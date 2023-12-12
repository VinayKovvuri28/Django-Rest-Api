from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', view=home, name='home'),
    path('student/', view=post_student, name='post_student'),   
]
