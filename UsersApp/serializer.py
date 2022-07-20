from rest_framework import serializers
from UsersApp.models import Account
from django.contrib.auth.models import User
from BookClubsApp.models import BookClub


class BookClubsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = 'GroupName', 'BookCover', 'GroupComment', 'Comment'
        model = BookClub


class AccountSerializer(serializers.ModelSerializer):
    bookclubs = BookClubsSerializer(read_only=True, many=True)

    class Meta:
        model = Account
        fields = ('user', 'bookshelf', 'book', 'bookclubs')
