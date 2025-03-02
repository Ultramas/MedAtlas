import os
import sys

# 1. Add your project’s path (the folder containing manage.py) to sys.path
project_path = '/home/PokeTrove/PokeTrove-Official-Website'
if project_path not in sys.path:
    sys.path.append(project_path)

# 2. Tell Django where to find your settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# 3. Let Django handle the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
