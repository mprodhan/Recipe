import os
from django.db import models
from django.utils import timezone
from PIL import Image

from recipe_user.models import RecipeUser


class Blog(models.Model):
    blog_title = models.CharField(max_length=30)
    blog_body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    blog_image = models.ImageField(upload_to='media/')
    blog_author = models.ForeignKey(RecipeUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        upload_img = Image.open(self.blog_image.path)
        if upload_img.height > 300 or upload_img.width > 300:
            output_size = (300,300)
            upload_img.thumbnail(output_size)
            upload_img.save(self.blog_image.path)