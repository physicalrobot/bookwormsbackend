from django.db import models

# Create your models here.
class Review(models.Model):
    ReviewId = models.AutoField(primary_key=True)
    ReviewBook = models.CharField(max_length = 500)
    ReviewBody = models.CharField(max_length = 500)
    ReviewRating = models.CharField(max_length = 500)