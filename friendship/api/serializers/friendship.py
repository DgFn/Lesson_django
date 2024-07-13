from rest_framework import serializers
from friendship.models import FriendShip, Friend
from rest_framework.exceptions import ValidationError


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user', )


class FriendShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendShip
        exclude = ('friend_ship', 'user')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user', )


class FriendShipResponseSerializer(serializers.ModelSerializer):
    friend = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )

    class Meta:
        model = FriendShip
        fields = '__all__'

    def validate(self, attrs):

        request = self.context['request']
        user = request.user
        instance = self.instance
        if instance and instance.friend != user:
            raise serializers.ValidationError('Так незя')
        return attrs
