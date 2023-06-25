from django.urls import path

from Book.consumer import SocketConsumer

urlpatterns = [
    
    path('ws/socket/', SocketConsumer.as_asgi()),
]
