from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='friend_user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE,related_name='friend_with_user')


class FriendShip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='friendship')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_with')
    friend_ship = models.BooleanField(default=False)
