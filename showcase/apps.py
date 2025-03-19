# showcase/apps.py
from django.apps import AppConfig

class ShowcaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'showcase'

    def ready(self):
        import showcase.signals  # Ensure this line is correctly included and executed
        # logger.debug("ShowcaseConfig ready method called, signals.py imported")
