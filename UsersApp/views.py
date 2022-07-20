from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from BookShelvesApp.serializers import BookShelfSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Account


# from UsersApp.serializer import AccountSerializer
# from .models import Account

from django.views.generic import ListView
from rest_framework import viewsets


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # token['account'] = user.account
        # token['book'] = user.objects.book
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# class AccountViewset(viewsets.ModelViewSet):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)

# @permission_classes([IsAuthenticated])


@api_view(['GET'])
def getUser(request):
    users = list(Account.objects.values())
    return JsonResponse(users, safe=False)
