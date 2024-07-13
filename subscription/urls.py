from django.urls import path, include

from .api.views.subscription import SubscriptionPostListView
from .router import api_router
urlpatterns = [
    path('api/', include(api_router.urls)),
    path('api/friend_posts/', SubscriptionPostListView.as_view())
]