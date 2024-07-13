from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from subscription.models import Subscription
from .models import FriendShip, Friend



@receiver(post_save, sender=FriendShip)
def update_friendship(sender, instance, created, **kwargs):
    if not created and instance.friend_ship:
        Friend.objects.get_or_create(user=instance.user, friend=instance.friend)
        Friend.objects.get_or_create(user=instance.friend, friend=instance.user)
        Subscription.objects.get_or_create(user=instance.user,subscriber=instance.friend, subscription=True)
        Subscription.objects.get_or_create(user=instance.friend,subscriber=instance.user, subscription=True)


@receiver(post_delete, sender=FriendShip)
def delete_friendship(sender, instance, **kwargs):
    Friend.objects.filter(user=instance.user, friend=instance.friend).delete()
    Friend.objects.filter(user=instance.friend, friend=instance.user).delete()
    Subscription.objects.filter(user=instance.friend, friend=instance.user).delete()
