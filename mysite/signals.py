# mysite/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import ChangeLog
from .utils import get_current_user, get_changes
from django.db import transaction

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



@receiver(post_save, sender=InventoryTradeOffer)
def notify_initiator_on_status_change(sender, instance, created, **kwargs):
    if not created:  # Skip notifications for new objects
        content_type = ContentType.objects.get_for_model(InventoryTradeOffer)
        Notification.objects.create(
            message=f"Your trade offer (ID: {instance.id}) has been {instance.status}.",
            content_type=content_type,
            object_id=instance.id,
            user=instance.initiator,

        )


def calculate_final_cost(offer):
    return sum(item.value or 0 for item in offer.offered_items.all())

import queue
from .models import InventoryObject

inventory_sse_queue = queue.Queue()

@receiver([post_save, post_delete], sender=InventoryObject)
def inventory_object_changed(sender, instance, **kwargs):
    inventory_sse_queue.put("changed")

@receiver(post_save, sender=Outcome)
def increment_card_counter(sender, instance, created, **kwargs):
    print('started profile card counter')
    if created and instance.user and not getattr(instance, "demonstration", False):
        try:
            profile = instance.user.profiledetails
            profile.cards_counter = (profile.cards_counter or 0) + 1
            profile.save()
            print('profile card counter updated')
        except ProfileDetails.DoesNotExist:
            pass