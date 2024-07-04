from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.CharField(max_length=2000, blank=False, null=False)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title





class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=2000, blank=False, null=False)
    is_published = models.BooleanField(default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


