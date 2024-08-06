# mysite/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import ChangeLog
from .utils import get_current_user, get_changes  # Ensure these are implemented correctly

# mysite/signals.py

@receiver(post_save)
def log_model_save(sender, instance, created, **kwargs):
    print(f"Signal received for {sender} with instance {instance.pk}")
    if sender == ChangeLog:
        return

    action = 'create' if created else 'update'
    user = get_current_user()
    model_name = ContentType.objects.get_for_model(sender).model
    changes = get_changes(instance) if not created else None

    ChangeLog.objects.create(
        user=user,
        action=action,
        model=model_name,
        object_id=instance.pk,
        changes=changes
    )

@receiver(post_delete)
def log_model_delete(sender, instance, **kwargs):
    print(f"Signal received for {sender} with instance {instance.pk}")
    if sender == ChangeLog:
        return

    user = get_current_user()
    model_name = ContentType.objects.get_for_model(sender).model

    ChangeLog.objects.create(
        user=user,
        action='delete',
        model=model_name,
        object_id=instance.pk
    )
