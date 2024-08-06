# users/signals.py
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import User, Profile, AdministrationChangeLog
from .views import get_changes


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#def save_profile(sender, instance, created, **kwargs):
#    user = instance
#    if created:
#        profile = Profile(user=user)
#        profile.save()


from .middleware import get_current_user

import json
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AdministrationChangeLog, Product
from .middleware import get_current_user

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import AdministrationChangeLog
from .utils import get_current_user, get_changes  # Assuming these are defined in utils.py

@receiver(post_save)
def log_model_save(sender, instance, created, **kwargs):
    if sender == AdministrationChangeLog:
        return

    action = 'create' if created else 'update'
    user = get_current_user()
    model_name = ContentType.objects.get_for_model(sender).model
    changes = get_changes(instance) if not created else None

    AdministrationChangeLog.objects.create(
        user=user,
        action=action,
        model=model_name,
        object_id=instance.pk,
        changes=changes
    )

@receiver(post_delete)
def log_model_delete(sender, instance, **kwargs):
    if sender == AdministrationChangeLog:
        return

    user = get_current_user()
    model_name = ContentType.objects.get_for_model(sender).model

    AdministrationChangeLog.objects.create(
        user=user,
        action='delete',
        model=model_name,
        object_id=instance.pk
    )
