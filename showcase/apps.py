from django.apps import AppConfig

from showcase.middleware import logger


class ShowcaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'showcase'

    def ready(self):
        import showcase.signals  # Ensure this line is correctly included and executed
        logger.debug("ShowcaseConfig ready method called, signals.py imported")

class ProductsConfig(AppConfig):
    name = 'products'
        
class CitiesConfig(AppConfig):
    name = 'cities'
       
class Core(AppConfig):
    name = 'core'

class BlogConfig(AppConfig):
    name = 'blog'


class UsersConfig(AppConfig):
    name = 'users'

    # add this function
    def ready(self):
        from . import signals
    
# users/__init__.py 
default_app_config = 'users.apps.UsersConfig'

class ChatConfig(AppConfig):
    name = 'chat'

    
class RegistrationsystemConfig(AppConfig):
    name = 'registrationsystem'
