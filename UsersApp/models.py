from BookShelvesApp.models import BookShelf
from BooksApp.models import Book
from django.contrib.auth.models import AbstractUser


from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    bookshelf = models.OneToOneField(
        BookShelf, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username
