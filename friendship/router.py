from rest_framework import routers
from friendship.api.views.friendship import FriendViewSet, FriendShipViewSet, FriendShipResponseViewSet

api_router = routers.DefaultRouter()
api_router.register(r'friends', FriendViewSet, basename='friends')
api_router.register(r'friends_ship', FriendShipViewSet, basename='friends_ship')
api_router.register(r'friends_response', FriendShipResponseViewSet, basename='friends_response')
