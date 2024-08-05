# users/signals.py
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import User, Profile

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

# signals.py
import json
import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from showcase.models import AdministrationChangeLog
from showcase.middleware import get_current_user


logger = logging.getLogger(__name__)

def create_log_entry(instance, change_type):
    model = instance.__class__
    changed_data = json.dumps(instance.__dict__, default=str)
    user = get_current_user()
    logger.debug(f"Creating log entry for {model} with change type {change_type} by user {user}")
    AdministrationChangeLog.objects.create(
        model_name=ContentType.objects.get_for_model(model).model,
        object_id=instance.pk,
        change_type=change_type,
        changed_data=changed_data,
        user=user
    )

@receiver(post_save)
def model_post_save(sender, instance, created, **kwargs):
    if sender == AdministrationChangeLog:
        return
    change_type = 'created' if created else 'updated'
    logger.debug(f"Post save signal received for {sender} with change type {change_type}")
    create_log_entry(instance, change_type)

@receiver(post_delete)
def model_post_delete(sender, instance, **kwargs):
    if sender == AdministrationChangeLog:
        return
    logger.debug(f"Post delete signal received for {sender}")
    create_log_entry(instance, 'deleted')