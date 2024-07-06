from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.CharField(max_length=2000, blank=False, null=False)
    is_published = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    image = models.ImageField(null=False, blank=False,  )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='images',)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(null=True, blank=True)
    phone_number = models.CharField(
        validators=[RegexValidator(regex=r'\+?1?\d{9,15}')],
        max_length=20,
        null=True,
        blank=True)
    github_link = models.URLField(null=True, blank=True)


