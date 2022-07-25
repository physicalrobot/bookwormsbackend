from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import viewsets


from BooksApp.models import Book
from BooksApp.serializers import BookSerializer, GenreSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import default_storage
from .models import Genre


class GenreViewSet(viewsets.ModelViewSet):
    # user = request.user
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    # user = request.user
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        bookcover = request.data['BookCover']
        title = request.data['BookTitle']

        Book.objects.create(BookTitle=title, BookCover=bookcover)

        return HttpResponse({'message': 'Book created'},  status=200)


# @csrf_exempt
# def bookApi(request, id=0):
#     if request.method =='GET':
#         books = Book.objects.all()
#         books_serializer =  BookSerializer(books, many=True)
#         return JsonResponse(books_serializer.data, safe=False)

#     elif  request.method =='POST':
#         book_data=JSONParser().parse(request)
#         book_serializer = BookSerializer(data = book_data)
#         if book_serializer.is_valid():
#             book_serializer.save()
#             return JsonResponse("Added Successfully!!",  safe=False)
#         return JsonResponse("Failed to Add",  safe=False)

#     elif request.method=='PUT':
#         book_data=JSONParser().parse(request)
#         book = Book.objects.get(BookId=book_data['BookId'])
#         book_serializer=BookSerializer(book,data=book_data)
#         if  book_serializer.is_valid():
#             book_serializer.save()
#             return JsonResponse('Updated Successfully!!', safe=False)
#         return JsonResponse('Failed to update', safe=False)

#     elif request.method == 'DELETE':
#         book = Book.objects.get(BookId=id)
#         book.delete()
#         return JsonResponse('deleted', safe=False)

# @csrf_exempt
# def BookCoverUpload(request,id=0):
#     if request.method == 'POST':
#        book = Book.objects.get(BookId=id)


#     file  = request.FILES['BookCover']
#     file_name =  default_storage.save(file.name,file)
#     return  JsonResponse(file_name,safe=False)
