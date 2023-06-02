from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import StreamingHttpResponse
from .models import *
from .serializers import BookSerializer
import time


class BookList(APIView):
    def get(self, request):
        start_time = time.time()
        
        titles = ['The Great Gatsby', 'To Kill a Mockingbird', 'Pride and Prejudice', '1984', 'The Catcher in the Rye', 'Adventures in AI', 'Beyond the Stars', 'Calamity of Clouds', 'Dances with Data',
                  'Elevation of Eagles', 'Fantastic Futures', 'Guardians of the Galaxy', 'Heralds of Hope',
                  'Incredible Ideas', 'Journey to Joy', 'Kingdom of Knowledge', 'Legends of Light',
                  'Mystery of the Mind', 'Nexus of Nature', 'Oceans of Opportunity', 'Palace of Possibilities', 'Quest for Quantum', 'Riddles of the Rainforest', 'Seeds of the Sky', 'Tales of Tomorrow']

        authors = ['F. Scott Fitzgerald', 'Harper Lee', 'Jane Austen', 'George Orwell', 'J.D. Salinger', 'Author One', 'Author Two', 'Author Three', 'Author Four',
                   'Author Five', 'Author Six', 'Author Seven', 'Author Eight',
                   'Author Nine', 'Author Ten', 'Author Eleven', 'Author Twelve',
                   'Author Thirteen', 'Author Fourteen', 'Author Fifteen', 'Author Sixteen',
                   'Author Seventeen', 'Author Eighteen', 'Author Nineteen', 'Author Twenty']
        publication_dates = ['2005-03-15', '1998-11-01', '1813-01-28', '1949-06-08', '1951-07-16', '2000-01-01', '2000-02-02', '2000-03-03', '2000-04-04',
                       '2000-05-05', '2000-06-06', '2000-07-07', '2000-08-08',
                       '2000-09-09', '2000-10-10', '2000-11-11', '2000-12-12',
                       '2001-01-01', '2001-02-02', '2001-03-03', '2001-04-04',
                       '2001-05-05', '2001-06-06', '2001-07-07', '2001-08-08']
        for title, author, date in zip(titles, authors, publication_dates):
            Book.objects.create(title=title, author=author,publication_date=date)
            books = Book.objects.all()
            list = []
        for book in books:
            take = BookSerializer(book)
            list.append(take)
            
            end_time = time.time()
            elapsed_time = end_time - start_time  # calculate elapsed time
        print(f"The operation took {elapsed_time} seconds to complete.")
        return Response(list)

def socket_view(request):
    # Retrieve the socket packet
    socket_packet = request.body.decode('utf-8')
    print(socket_packet)
    # Process the socket packet as needed
    # ...

    # Send a response back to the client if needed
    response = "Socket packet received."
    return HttpResponse(response)