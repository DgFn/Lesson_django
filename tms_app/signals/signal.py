from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from tms_app.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    profile = Profile.objects.create(user=instance)
    profile.save()
