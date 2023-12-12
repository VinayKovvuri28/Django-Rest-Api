from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BooksModel
from .serializers import BooksModelSerializers

# Create your views here.
# Read
@api_view(['GET'])
def bookslist(request):
    books_obj = BooksModel.objects.all()
    serializer = BooksModelSerializers(books_obj, many=True)
    return Response(serializer.data)

# Create
@api_view(['POST'])
def post_books(request):
    books_obj = BooksModel.objects.all()
    serializer = BooksModelSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Update
@api_view(['POST'])
def update_books(request,book_id):
    books_obj = BooksModel.objects.get(id=book_id)
    serializer = BooksModelSerializers(instance=books_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete
@api_view(['Delete'])
def delete_books(request,book_id):
    books_obj = BooksModel.objects.get(id=book_id)
    books_obj.delete()
    return Response("Book Record is deleted successfully")