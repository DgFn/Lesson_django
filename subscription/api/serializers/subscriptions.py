from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from subscription.models import Subscription
from tms_app.models import Post


class SubscriptionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Subscription
        fields = ('subscriber','subscription')


    # def save(self, **kwargs):
    #     user = kwargs.pop('user', None)
    #     instance = super().save(**kwargs)
    #     if user:
    #         instance.user = user
    #     return instance



class SubscriptionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
