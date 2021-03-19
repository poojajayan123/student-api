"""
WSGI config for MongoDbMap project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from django.conf import settings

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MongoDbMap.settings')

# export DJANGO_SETTINGS_MODULE=MongoDbMap.settings


application = get_wsgi_application()