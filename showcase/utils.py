import threading

_thread_locals = threading.local()

def get_current_user():
    return getattr(_thread_locals, 'user', None)

class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.user = request.user
        response = self.get_response(request)

        return response
def get_changes(instance):
    if not instance.pk:
        return None
    old_instance = instance.__class__.objects.get(pk=instance.pk)
    changes = {}
    for field in instance._meta.fields:
        field_name = field.name
        old_value = getattr(old_instance, field_name)
        new_value = getattr(instance, field_name)
        if old_value != new_value:
            changes[field_name] = {
                'old': old_value,
                'new': new_value
            }
    return changes
