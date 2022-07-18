from django.db import models
from BooksApp.models import Book
from django.contrib.auth.models import User


# Create your models here.


class BookShelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    books = models.ManyToManyField(Book)
