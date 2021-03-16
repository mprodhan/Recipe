from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class RecipeUser(AbstractUser):
    display_name = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.display_name
