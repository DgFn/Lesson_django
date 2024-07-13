from rest_framework import routers


from subscription.api.views.subscription import SubscriptionListView

api_router = routers.DefaultRouter()
api_router.register(r'subscriptions', SubscriptionListView)

