from django.urls import path
from Book.views import BookList
from Book.consumer import SocketConsumer

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('ws/socket/', SocketConsumer.as_asgi()),
]
