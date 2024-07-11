from django.db import models
from django.db.models import ForeignKey

from tms_app.models import Post


# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    post = ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
