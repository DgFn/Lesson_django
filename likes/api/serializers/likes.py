from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from likes.models import Like, LikeComment
from tms_app.models import Post


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ('user',)

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user', )


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        exclude = ('user',)

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user', )


# Достать пользователей который лайкнули мой пост или коммент
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


