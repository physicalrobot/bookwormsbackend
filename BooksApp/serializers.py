from rest_framework import serializers
from BooksApp.models import Book
from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre',)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('BookId',
                  'BookGenre',
                  'BookTitle',
                  'BookAuthor',
                  'BookCover',
                  'Synopsis',
                  'Rating')
