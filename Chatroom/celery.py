from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chatroom.settings')

app = Celery('Chatroom')
app.loader.override_backends['django-db'] = 'django_celery_results.backends.database:DatabaseBackend'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
    broker_connection_retry_on_startup=True,
)


app.autodiscover_tasks()