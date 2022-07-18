from BookShelvesApp.models import BookShelf
from BookShelvesApp.serializers import BookShelfSerializer
from django.http import HttpResponse
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from django.core.files.storage import default_storage
from rest_framework import viewsets
# Create your views here.


class BookShelfViewSet(viewsets.ModelViewSet):
    queryset = BookShelf.objects.all()
    serializer_class = BookShelfSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBookShelves(request):
    user = request.user
    bookshelves = user.bookshelf.all()
    serializer = BookShelfSerializer(bookshelves, many=True)
    return Response(serializer.data)

    return Response(routes)
    # def post(self,request, *args,**kwargs):
    #     rating  =  request.data['ReviewRating']
    #     body = request.data['ReviewBody']
    #     title  =  request.data['ReviewBook']

    #     Review.objects.create(ReviewBody=body, ReviewBook=title,ReviewRating= rating)

    #     return  HttpResponse({'message':'Review created'},  status=200)
