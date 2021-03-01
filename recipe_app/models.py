from django.db import models
from django.utils import timezone

class Food(models.Model):
    title = models.CharField(max_length=30)
    ingredients = models.TextField()
    directions = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



