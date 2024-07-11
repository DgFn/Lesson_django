from django.urls import path, include

from .api.views.comment import CommentListViewSet
from .router import api_router
urlpatterns = [
    path('api/', include(api_router.urls)),
    path('api/post_comments/<int:post_id>', CommentListViewSet.as_view()),
]