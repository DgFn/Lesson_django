from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription_user')
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription_subscriber')
    subscription = models.BooleanField(default=False)
