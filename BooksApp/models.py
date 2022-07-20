from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


fs = FileSystemStorage(location='/media/bookcovers')


def upload_path(instance, filename):
    return '/'.join(['bookcovers', str(instance.BookTitle), filename])


class Book(models.Model):
    BookId = models.AutoField(primary_key=True)
    BookTitle = models.CharField(max_length=500)
    BookCover = models.ImageField(null=True, blank=True, upload_to=upload_path)
