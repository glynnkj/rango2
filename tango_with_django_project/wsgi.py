"""
WSGI configuration for tango_with_django_project project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, please see https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

application = get_wsgi_application()