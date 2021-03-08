from django.db import models
from django.utils import timezone
from recipe_user.models import RecipeUser

class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    blog_author = models.ForeignKey(RecipeUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
