from __future__ import absolute_import

import os
import sys
from celery import Celery

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'karenina'))
sys.path.insert(0, os.path.join(BASE_DIR, 'viewform'))
sys.path.insert(0, os.path.join(BASE_DIR, 'viewflow'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'examples.settings')

app = Celery('examples')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
