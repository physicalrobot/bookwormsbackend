from django.db import models
from BooksApp.models import Book
from django.contrib.auth.models import User


# Create your models here.


class BookShelf(models.Model):
    books = models.ManyToManyField(Book)
