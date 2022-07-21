from django.db import models
from django.contrib.auth.models import User
from BooksApp.models import Book

# Create your models here.


class Review(models.Model):
    # id = models.AutoField(primary_key=True)
    reviewtitle = models.CharField(max_length=500)
    body = models.TextField(max_length=1000)
    rating = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
