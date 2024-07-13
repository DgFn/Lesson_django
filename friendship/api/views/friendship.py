from rest_framework import viewsets, permissions
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from friendship.api.serializers.friendship import FriendSerializer, FriendShipSerializer, FriendShipResponseSerializer
from friendship.models import Friend, FriendShip


class FriendViewSet(
    GenericViewSet,
    ListModelMixin,
):
    serializer_class = FriendSerializer
    queryset = Friend.objects


class FriendShipViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin
):
    serializer_class = FriendShipSerializer
    queryset = FriendShip.objects


class FriendShipResponseViewSet(
    GenericViewSet,
    ListModelMixin,
    DestroyModelMixin,
    UpdateModelMixin
):
    serializer_class = FriendShipResponseSerializer
    queryset = FriendShip.objects

    permission_classes = [permissions.IsAuthenticated]

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #
    #     serializer.is_valid(raise_exception=True)
    #     user = request.user
    #     serializer.validated_data['user'] = user
    #     self.perform_update(serializer)
    #     return Response(serializer.data)



