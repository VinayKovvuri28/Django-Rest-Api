from django.shortcuts import render
from .models import StaffModel
from .serializers import StaffModelSerializers
from rest_framework import status, viewsets
from rest_framework.response import Response 
# from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import *
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# Create your views here.

# Mixins:
# -------
# The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. This allows for more flexible composition of behavior.
# The mixin classes can be imported from rest_framework.mixins.
# ListModelMixin:
# Provides a .list(request, *args, **kwargs) method, that implements listing a queryset.
# If the queryset is populated, this returns a 200 OK response, with a serialized representation of the queryset as the body of the response. The response data may optionally be paginated.
# CreateModelMixin:
# Provides a .create(request, *args, **kwargs) method, that implements creating and saving a new model instance.
# If an object is created this returns a 201 Created response, with a serialized representation of the object as the body of the response. If the representation contains a key named url, then the Location header of the response will be populated with that value.
# If the request data provided for creating the object was invalid, a 400 Bad Request response will be returned, with the error details as the body of the response.
# RetrieveModelMixin:
# Provides a .retrieve(request, *args, **kwargs) method, that implements returning an existing model instance in a response.
# If an object can be retrieved this returns a 200 OK response, with a serialized representation of the object as the body of the response. Otherwise, it will return a 404 Not Found.
# UpdateModelMixin:
# Provides a .update(request, *args, **kwargs) method, that implements updating and saving an existing model instance.
# Also provides a .partial_update(request, *args, **kwargs) method, which is similar to the update method, except that all fields for the update will be optional. This allows support for HTTP PATCH requests.
# If an object is updated this returns a 200 OK response, with a serialized representation of the object as the body of the response.
# If the request data provided for updating the object was invalid, a 400 Bad Request response will be returned, with the error details as the body of the response.
# DestroyModelMixin:
# Provides a .destroy(request, *args, **kwargs) method, that implements deletion of an existing model instance.
# If an object is deleted this returns a 204 No Content response, otherwise it will return a 404 Not Found.

class Stafflistcreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class Staffretrieveupdatedelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)

# Concrete View Classes(Concrete Generic Api view Django Rest Api:):
# ---------------------
# The following classes are the concrete generic views. If you're using generic views this is normally the level you'll be working at unless you need heavily customized behavior.
# The view classes can be imported from rest_framework.generics.
# ListAPIView : 
# Used for read-only endpoints to represent a collection of model instances.
# Provides a 'get' method handler.
# Extends: GenericAPIView, ListModelMixin
# CreateAPIView : 
# Used for create-only endpoints.
# Provides a 'post' method handler.
# Extends: GenericAPIView, CreateModelMixin
# ListCreateAPIView:
# Used for read-write endpoints to represent a collection of model instances.
# Provides get and post method handlers.
# Extends: GenericAPIView, ListModelMixin, CreateModelMixin
# RetrieveAPIView : 
# Used for read-only endpoints to represent a single model instance.
# Provides a 'get' method handler.
# Extends: GenericAPIView, RetrieveModelMixin
# UpdateModelMixin : 
# Used for update-only endpoints for a single model instance.
# Provides 'put' and 'patch' method handlers.
# Extends: GenericAPIView, UpdateModelMixin
# DestroyModelMixin : 
# Used for delete-only endpoints for a single model instance.
# Provides a 'delete' method handler.
# Extends: GenericAPIView, DestroyModelMixin
# RetrieveUpdateAPIView:
# Used for read or update endpoints to represent a single model instance.
# Provides get, put and patch method handlers.
# Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin
# RetrieveDestroyAPIView:
# Used for read or delete endpoints to represent a single model instance.
# Provides get and delete method handlers.
# Extends: GenericAPIView, RetrieveModelMixin, DestroyModelMixin
# RetrieveUpdateDestroyAPIView:
# Used for read-write-delete endpoints to represent a single model instance.
# Provides get, put, patch and delete method handlers.
# Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class staffCreateAPIView(CreateAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

class staffListAPIView(ListAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

class staffRetrieveAPIView(RetrieveAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

class staffDestroyAPIView(DestroyAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

class staffUpdateAPIView(UpdateAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

class staffListCreateAPIView(ListCreateAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

class staffRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

class staffRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

class staffRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers

# Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. In other frameworks you may also find conceptually similar implementations named something like 'Resources' or 'Controllers'.

# A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create().

# The method handlers for a ViewSet are only bound to the corresponding actions at the point of finalizing the view, using the .as_view() method.

# Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.

class Staffviewsets(viewsets.ViewSet):
    def list(self, request):
        queryset = StaffModel.objects.all()
        serializer = StaffModelSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if id is not None:
            queryset = StaffModel.objects.get(roll = pk)
            serializer = StaffModelSerializers(queryset)
            return Response(serializer.data)
    
    def update(self, request, pk):
        id=pk
        queryset = StaffModel.objects.get(pk = id)
        serializer = StaffModelSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully record updated'})
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request):
        id=pk
        queryset = StaffModel.objects.get(pk = id)
        queryset.delete()
        return Response({'msg':'Successfully record deleted'})
        
    def create(self, request):
        serializer = StaffModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer_class.save()
            return Response({'msg':'Successfully record created'})
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# ModelViewSet
# The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, by mixing in the behavior of the various mixin classes.

# The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().

class StaffModelViewSet(viewsets.ModelViewSet):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializers