from django.urls import path, re_path
from Book.views import BookList
from Book.consumer import SocketConsumer

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    re_path(r'ws/socket/$', SocketConsumer.as_asgi()),
]
