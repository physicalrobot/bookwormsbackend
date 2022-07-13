from django.db import models
from UsersApp.models import User
from BooksApp.models import Book

# Create your models here.
class BookShelf(models.Model):
    BookShelfId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    books = models.ManyToManyField(Book)