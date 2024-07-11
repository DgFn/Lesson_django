from django.urls import path, include

from .api.views.likes import LikePostViewSet, UserLikeCommentViewSet
from .router import api_router
urlpatterns = [
    path('api/', include(api_router.urls)),
    path('api/likes_post_user/<int:post_id>', LikePostViewSet.as_view()),
    path('api/comment_likes/<int:comment_id>', UserLikeCommentViewSet.as_view())
]