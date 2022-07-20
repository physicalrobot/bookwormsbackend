from rest_framework import serializers
from UsersApp.models import Account
from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user', 'bookshelf', 'book')
