from django.urls import path
from .views import *

urlpatterns = [
    path('', view=bookslist, name='bookslist'),
    path('add/', view=post_books, name='post_books'),
    path('update/<int:book_id>/', view=update_books, name='update_books'),
    path('delete/<int:book_id>/', view=delete_books, name='delete_books'),
]
