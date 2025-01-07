import threading
import logging

from django.utils.deprecation import MiddlewareMixin

# Thread-local storage for the current user
_thread_locals = threading.local()
logger = logging.getLogger(__name__)

def get_current_user():
    """
    Retrieve the current user from thread-local storage.
    """
    return getattr(_thread_locals, 'user', None)

class CurrentUserMiddleware(MiddlewareMixin):
    """
    Middleware to store the current user in thread-local storage and track the room they are visiting.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.user = request.user
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Dynamically set the 'current_room' attribute for authenticated users.
        """
        if request.user.is_authenticated:
            # Extract the room name from the URL kwargs
            room_name = view_kwargs.get('room', None)
            request.user.current_room = room_name  # Dynamically set the attribute

    def process_request(self, request):
        if request.user.is_authenticated:
            path = request.path
            if path.startswith('/home/') and path.endswith('/'):
                room_name = path.split('/')[-2]
                setattr(request.user, 'current_room', room_name)
            else:
                setattr(request.user, 'current_room', None)

        if path.startswith('/home/') and path.endswith('/'):
            room_name = path.split('/')[-2]  # Assumes the path format is `/home/<room>/`
            request.user.current_room = room_name
            logger.debug(f"User {request.user} is in room: {room_name}")
        else:
            request.user.current_room = None
            logger.debug(f"User {request.user} is not in a specific room.")


from django.utils.timezone import now
from showcase.models import SettingsModel

class NotificationStatusMiddleware:
    """Middleware to update notification status based on user activity."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Update notification status to "ON" when a logged-in user makes a request
        if request.user.is_authenticated:
            try:
                settings = SettingsModel.objects.get(user=request.user)
                if settings.notifications_status == 'OFF':
                    settings.notifications_status = 'ON'
                    settings.save()
            except SettingsModel.DoesNotExist:
                pass

        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        """Optionally handle exceptions."""
        return None
