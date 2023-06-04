from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import StreamingHttpResponse, HttpResponse

from .serializers import BookSerializer
import time




def socket_view(request):
    # Retrieve the socket packet
    socket_packet = request.body.decode('utf-8')
    print(socket_packet)
    # Process the socket packet as needed
    # ...

    # Send a response back to the client if needed
    response = "Socket packet received."
    return HttpResponse(response)