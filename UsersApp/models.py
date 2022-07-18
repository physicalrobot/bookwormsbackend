# # from django.contrib.auth.models import User
# from BookShelvesApp.models import BookShelf
# from BooksApp.models import Book
# # from django.contrib.auth.models import AbstractUser

# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.

# def get_model_fields(model):
#     return model._meta.fields


# class User(AbstractUser):

#     book = models.ForeignKey(Book, on_delete=models.CASCADE, null = True)
#     bookshelf =  models.OneToOneField(BookShelf, on_delete=models.CASCADE, null = True)


# class CustomUser(AbstractUser):

#     book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
#     bookshelf = models.OneToOneField(
#         BookShelf, on_delete=models.CASCADE, null=True)
