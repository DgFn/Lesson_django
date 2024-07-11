from django.contrib.auth.models import User
from django.db import models

from comments.models import Comment
from tms_app.models import Post


# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='likes')
    liker = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name='likes')


class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='comment_likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=False, related_name='like_comment')
