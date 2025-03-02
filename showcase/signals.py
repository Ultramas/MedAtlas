# users/signals.py
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver

from .models import Outcome, Achievements, ProfileDetails
from .models import User, Profile, AdministrationChangeLog, Battle, Room, Message, Notification, Game
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


@receiver(post_save, sender=Outcome)
def update_achievement_counters(sender, instance, **kwargs):
    user = instance.user
    if not user:
        return  # If there's no associated user, exit

    # Retrieve all achievements associated with the curren user
    achievements = Achievements.objects.filter(user=user)

    # Iterate over each achievement in the queryset and update its counters
    for achievement in achievements:
        achievement.green_counter += instance.green_counter
        achievement.yellow_counter += instance.yellow_counter
        achievement.orange_counter += instance.orange_counter
        achievement.red_counter += instance.red_counter
        achievement.black_counter += instance.black_counter
        achievement.gold_counter += instance.gold_counter
        achievement.redgold_counter += instance.redgold_counter
        achievement.save()  # Save each achievement after updating

def update_currencies_for_profile(instance):
    """
    Update the 'other_currencies_amount' for the given profile instance.
    """
    # Example logic to populate other currencies
    currencies = Currency.objects.exclude(pk=instance.currency.pk)  # Exclude the primary currency
    for currency in currencies:
        ProfileCurrency.objects.get_or_create(profile=instance, currency=currency)

def populate_other_currencies(sender, instance, **kwargs):
    update_currencies_for_profile(instance)

@receiver(m2m_changed, sender=Battle.participants.through)
def update_participant_battle(sender, instance, action, **kwargs):
    if action == "post_add":
        for participant in instance.participants.all():
            if participant.battle != instance:
                participant.battle = instance
                print('participant saved')  # Should now appear
                participant.save()

from django.contrib.auth.signals import user_logged_out
from .models import SettingsModel

@receiver(user_logged_out)
def set_notifications_off(sender, request, user, **kwargs):
    try:
        settings = SettingsModel.objects.get(user=user)
        if settings.notifications_status == 'ON':
            settings.notifications_status = 'OFF'
            settings.save()
    except SettingsModel.DoesNotExist:
        pass


@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    """
    Signal to create a SettingsModel instance when a new user is created.
    """
    if created:
        SettingsModel.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email if hasattr(instance, 'email') else None
        )

@receiver(post_save, sender=Message)
def create_notification_on_message(sender, instance, created, **kwargs):
    """
    Signal to create notifications for users in a room when a new message is posted.
    """
    if created:  # Trigger for newly created messages
        message = instance
        try:
            room = Room.objects.get(name=message.room)
            members_to_notify = room.members.exclude(id=message.signed_in_user.id)

            # Get all users in the room except the sender
            for member in members_to_notify:
                # Check if the member's current_room matches the message's room
                if getattr(member, 'current_room', None) != room.name:
                    # Check notification settings
                    user_settings = SettingsModel.objects.filter(user=member).first()
                    if user_settings and user_settings.notifications_status == "ON":
                        notification = Notification.objects.create(
                            content_type=ContentType.objects.get_for_model(Message),
                            object_id=message.id,
                            related_object=message,
                            message=f"{message.signed_in_user.username} sent a message in {room.name}: {message.value}"
                        )
                        # Add the member to the notification
                        notification.user.add(member)
                        notification.save()

        except Room.DoesNotExist:
            print(f"Room '{message.room}' does not exist.")
