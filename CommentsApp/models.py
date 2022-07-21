from tkinter import CASCADE
from django.db import models
from UsersApp.models import Account
from django.contrib.auth.models import User
from BookClubsApp.models import BookClub

# Create your models here.


class Comment(models.Model):
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookclub = models.ForeignKey(BookClub, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
