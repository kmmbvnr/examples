# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from __future__ import absolute_import
from .celery import app as celery_app  # NOQA

from . import modules

website = modules.Website()
form = modules.Viewform()