from rest_framework import generics
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from comments.api.serializers.comment import CommentSerializer, CommentPostSerializer
from comments.models import Comment


class CommentViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin
):
    serializer_class = CommentSerializer
    queryset = Comment.objects


class CommentListViewSet(generics.ListAPIView):
    serializer_class = CommentPostSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)
