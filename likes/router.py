from rest_framework import routers

from likes.api.views.likes import LikeViewSet, LikeCommentViewSet

api_router = routers.DefaultRouter()
api_router.register('likes', LikeViewSet)
api_router.register('likes_comment', LikeCommentViewSet)

