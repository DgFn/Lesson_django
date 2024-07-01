from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.CharField(max_length=2000, blank=False, null=False)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    username = models.CharField(max_length=256, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=256, blank=False, null=False)
    last_name = models.CharField(max_length=256, blank=False, null=False)
    bio = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.username


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=2000, blank=False, null=False)
    is_published = models.BooleanField(default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


