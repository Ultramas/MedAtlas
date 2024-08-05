# middleware.py
import threading
import logging

thread_local = threading.local()
logger = logging.getLogger(__name__)

class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.debug(f"CurrentUserMiddleware called for user: {request.user}")
        thread_local.current_user = request.user
        response = self.get_response(request)
        return response

def get_current_user():
    return getattr(thread_local, 'current_user', None)
