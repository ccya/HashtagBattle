"""
Django settings for TintProject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
from datetime import timedelta
# from TintProject.tasks import display

djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    '/home/ccya/workplace/TintProject/templates',
)
# CELERYBEAT_SCHEDULE = {
#     'add-every-60-seconds': {
#         'task': 'TintProject.tasks.display',
#         'schedule': timedelta(seconds=5),
#         # 'args': ('league of legends','bike')
#     },
# }

CELERY_TIMEZONE = 'UTC'
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# CELERY_RESULT_BACKEND = "amqp"
# CELERY_IMPORTS = ("tasks", )
# CELERY_ALWAYS_EAGER = True

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_PASSWORD = "mypassword"
BROKER_USER = "myuser"
BROKER_VHOST = "myvhost"
BROKER_URL = "amqp://myuser:mypassword@localhost:5672/myvhost"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yxg7-i+szkqvyu-j5!99=*6w@by6w$qd9$al)qg$odx*zt#s8*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Hashtag',
    'TintProject',
    'TintProject.tasks',
    'djcelery',
    'bootstrap3',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'TintProject.urls'

WSGI_APPLICATION = 'TintProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mydatabase.db',                    # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join('static'),
)
BOOTSTRAP3 = {

    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.2.0/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',

    # Field class to use in horiozntal forms
    'horizontal_field_class': 'col-md-4',

    # Set HTML required attribute on required fields
    'set_required': True,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'form_required_class': '',

    # Class to indicate error (better to set this in your Django form)
    'form_error_class': '',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers':{
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}
