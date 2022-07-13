from django.db import models
from BooksApp.models import Book
from django.contrib.auth.models import AbstractUser

# Create your models here.

def get_model_fields(model):
    return model._meta.fields



class User(AbstractUser):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, null = True)

