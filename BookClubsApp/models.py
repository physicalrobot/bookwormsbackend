from django.db import models
# from UsersApp.models import Account
# from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/bookcovers')


def upload_path(instance, filename):
    return '/'.join(['bookcovers', str(instance.GroupName), filename])


class BookClub(models.Model):
    GroupName = models.CharField(max_length=500)
    BookCover = models.ImageField(null=True, blank=True, upload_to=upload_path)
    GroupComment = models.TextField()
    Comment = models.CharField(max_length=500)
