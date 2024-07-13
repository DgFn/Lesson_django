from django.urls import path, include


from .router import api_router
urlpatterns = [
    path('api/', include(api_router.urls)),
]