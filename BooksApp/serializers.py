from rest_framework import serializers
from BooksApp.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('BookId',
                  'BookTitle',
                  'BookAuthor',
                  'BookCover',
                  'Synopsis',
                  'Rating')
