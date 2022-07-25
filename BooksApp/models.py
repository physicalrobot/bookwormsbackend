from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


fs = FileSystemStorage(location='/media/bookcovers')


def upload_path(instance, filename):
    return '/'.join(['bookcovers', str(instance.BookTitle), filename])


class Genre(models.Model):
    genre = models.CharField(max_length=500)


class Book(models.Model):
    BookId = models.AutoField(primary_key=True)
    BookGenre = models.ForeignKey(
        Genre, blank=True, null=True, on_delete=models.CASCADE)
    BookTitle = models.CharField(max_length=500)
    BookAuthor = models.CharField(max_length=500)
    BookCover = models.ImageField(null=True, blank=True, upload_to=upload_path)
    Synopsis = models.TextField(max_length=2000)
    Rating = models.IntegerField(null=True, blank=True, default=1,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(1)
                                 ])
