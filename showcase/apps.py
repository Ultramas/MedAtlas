from django.apps import AppConfig


class Showcase(AppConfig):
    name = 'showcase'

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
