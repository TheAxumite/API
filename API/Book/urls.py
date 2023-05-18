from django.urls import path
from Book.views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
