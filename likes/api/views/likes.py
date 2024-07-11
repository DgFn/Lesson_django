from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from likes.api.serializers.likes import LikeSerializer, LikeCommentSerializer, UserSerializer
from likes.models import Like, LikeComment
from tms_app.models import Post


class LikeViewSet(
    GenericViewSet,
    ListModelMixin,
    DestroyModelMixin,
    CreateModelMixin
):
    serializer_class = LikeSerializer
    queryset = Like.objects


class LikeCommentViewSet(
    GenericViewSet,
    ListModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
):
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects


class LikePostViewSet(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return User.objects.filter(likes__liker_id=post_id)


class UserLikeCommentViewSet(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        comment_id = self.kwargs['comment_id']
        return User.objects.filter(comment_likes__comment_id=comment_id)
