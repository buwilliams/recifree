from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    photo_url = models.URLField()
    video_url = models.URLField()
    instructions = models.TextField()
    ingredients = models.TextField()

    def __str__(self):
        return self.title
