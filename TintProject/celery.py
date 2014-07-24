from __future__ import absolute_import
import os
from celery import Celery
from celery import chord
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TintProject.settings')


app = Celery('TintProject',
             broker='amqp',
             backend='amqp://',
             include=['TintProject.tasks']
             )
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)
app.config_from_object('django.conf:settings')

 