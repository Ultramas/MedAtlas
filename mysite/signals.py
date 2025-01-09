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

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProfileDetails, Experience, Level

@receiver(post_save, sender=ProfileDetails)
def check_rubies_spent(sender, instance, **kwargs):
    if instance.rubies_spent:
        profile_exp, created = Experience.objects.get_or_create(profile=instance, user=instance.user)
        for level in Level.objects.all():
            if instance.rubies_spent >= level.experience:
                profile_exp.level.add(level)

@receiver(post_save, sender=ProfileDetails)
def update_profile_level_on_save(sender, instance, **kwargs):
    print(f"Signal triggered for profile: {instance}")
    print(f"Rubies spent: {instance.rubies_spent}")
    update_profile_level(instance)


@receiver(user_logged_out)
def set_notifications_off(sender, request, user, **kwargs):
    """Set notification status to 'OFF' when the user logs out."""
    if user.is_authenticated:  # Ensure the user is logged in
        try:
            settings = SettingsModel.objects.get(user=request.user)
            if settings.notifications_status == 'ON':
                settings.notifications_status = 'OFF'
                settings.save()
        except SettingsModel.DoesNotExist:
            pass


# Signal to handle status change

@receiver(post_save, sender=InventoryTradeOffer)
def notify_initiator_on_status_change(sender, instance, created, **kwargs):
    if not created:  # Skip notifications for new objects
        content_type = ContentType.objects.get_for_model(InventoryTradeOffer)
        Notification.objects.create(
            message=f"Your trade offer (ID: {instance.id}) has been {instance.status}.",
            content_type=content_type,
            object_id=instance.id,
            user=instance.initiator
            from django.db import transaction

def calculate_final_cost(offer):
    # Sum the fees or values of all offered items
    return sum(item.value or 0 for item in offer.offered_items.all())

