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

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AdministrationChangeLog
from .utils import get_current_user, get_changes



@receiver(post_save)
def log_model_save(sender, instance, created, **kwargs):
    if sender == AdministrationChangeLog:
        return

    user = get_current_user()
    if not user or not isinstance(user, get_user_model()):  # Check if there is no valid user
        return

    action = 'create' if created else 'update'
    model_name = ContentType.objects.get_for_model(sender).model
    changes = get_changes(instance) if not created else None

    try:
        AdministrationChangeLog.objects.create(
            user=user,
            action=action,
            model=model_name,
            object_id=instance.pk,
            changes=changes
        )
    except ValueError as e:
        # Log the error or handle it appropriately
        print(f"Error creating AdministrationChangeLog: {e}")

@receiver(post_delete)
def log_model_delete(sender, instance, **kwargs):
    if sender == AdministrationChangeLog:
        return

    user = get_current_user()
    if not user or not isinstance(user, get_user_model()):  # Check if there is no valid user
        return

    model_name = ContentType.objects.get_for_model(sender).model

    try:
        AdministrationChangeLog.objects.create(
            user=user,
            action='delete',
            model=model_name,
            object_id=instance.pk
        )
    except ValueError as e:
        # Log the error or handle it appropriately
        print(f"Error creating AdministrationChangeLog: {e}")