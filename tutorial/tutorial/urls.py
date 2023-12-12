"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from staff import views
from student import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('Staffviewsets', views.Staffviewsets, basename='Staffviewsets')
# router.register('StaffModelViewSet', views.StaffModelViewSet, basename='StaffModelViewSet')
router.register('Studentviewset', views.Studentviewset, basename='Studentviewset')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('quickstart.urls')),
    path('books/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('staff/Stafflistcreate/', views.Stafflistcreate.as_view()),
    # path('staff/retrieveupdatedelete/<int:pk>/', views.Staffretrieveupdatedelete.as_view()),
    # path('staff/staffCreateAPIView/', views.staffCreateAPIView.as_view()),
    # path('staff/staffListAPIView/', views.staffListAPIView.as_view()),
    # path('staff/staffListCreateAPIView/', views.staffListCreateAPIView.as_view()),
    # path('staff/staffRetrieveAPIView/<int:pk>/', views.staffRetrieveAPIView.as_view()),
    # path('staff/staffDestroyAPIView/<int:pk>/', views.staffDestroyAPIView.as_view()),
    # path('staff/staffUpdateAPIView/<int:pk>/', views.staffUpdateAPIView.as_view()),
    # path('staff/staffRetrieveUpdateAPIView/<int:pk>/', views.staffRetrieveUpdateAPIView.as_view()),
    # path('staff/staffRetrieveDestroyAPIView/<int:pk>/', views.staffRetrieveDestroyAPIView.as_view()),
    # path('staff/staffRetrieveUpdateDestroyAPIView/<int:pk>/', views.staffRetrieveUpdateDestroyAPIView.as_view()),
    path('',include(router.urls))
]
