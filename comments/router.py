from rest_framework import routers

from comments.api.views.comment import CommentViewSet

api_router = routers.DefaultRouter()
api_router.register('comments', CommentViewSet)