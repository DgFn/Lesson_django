from django.contrib.auth.models import User
from rest_framework import permissions, status, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from subscription.api.serializers.subscriptions import SubscriptionSerializer, SubscriptionPostSerializer
from subscription.models import Subscription
from tms_app.models import Post


class SubscriptionListView(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin
):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class SubscriptionPostListView(generics.ListAPIView):
    serializer_class = SubscriptionPostSerializer

    def get_queryset(self):
        followed_users = Subscription.objects.filter(subscriber=self.request.user).values_list('user', flat=True)
        return Post.objects.filter(user__in=followed_users)
