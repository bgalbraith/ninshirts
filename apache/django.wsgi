### This is a template for the WSGI application needed by mod_wsgi.
### Copy this file to django.wsgi, then change the path and myproject values to the 
### approriate local settings.
import os
import sys

### We need to make sure the Python path contains references to both the application
### and its components. To do that, we add the directory the project directory is in
### and the project directory itself.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

path = BASE_DIR
project = '/ninshirts'
if path not in sys.path:
    sys.path.append(path)
    sys.path.append(path+project)

### Next we have to let the Python environment know where the Django settings are.
os.environ['DJANGO_SETTINGS_MODULE'] = 'ninshirts.settings'

### Finally we import Django's WSGI handler and instantiate.
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

