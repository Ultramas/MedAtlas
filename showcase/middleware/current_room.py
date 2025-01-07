from django.utils.deprecation import MiddlewareMixin

class CurrentRoomMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Dynamically set the 'current_room' attribute for authenticated users.
        """
        if request.user.is_authenticated:
            # Extract the room name from the URL kwargs
            room_name = view_kwargs.get('room', None)
            request.user.current_room = room_name  # Dynamically set the attribute
        return None
