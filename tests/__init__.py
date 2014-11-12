import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')
from django.conf import settings
from django.apps import apps

apps.populate(settings.INSTALLED_APPS)
from . import *
