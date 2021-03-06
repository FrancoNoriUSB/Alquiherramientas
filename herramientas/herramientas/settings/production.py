"""
Django settings for herramientas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = os.path.realpath(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm792z$9!^#xkz+hx)w!e)-za1cr=l4*r5o&s^d=gu_xmj8^7=0'

# MailChimp
MAILCHIMP_API_KEY = 'fd428d20a860e9521a2f9f1dc6968ba5-us10'

# Mailchimp WebHookKey
MAILCHIMP_WEBHOOK_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'www.alquiherramientas.com',
    'alquiherramientas.com',
]

# Application definition
INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'herramientas.apps.administrador',
    'herramientas.apps.main',
    'widget_tweaks',
    'bootstrap3',
    'mailchimp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR, '../templates'),
)

ROOT_URLCONF = 'herramientas.urls'

WSGI_APPLICATION = 'herramientas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'herramientas',                      # Or path to database file if using sqlite3.
        #The following settings are not used with sqlite3:
        'USER': 'herramientas_user',
        'PASSWORD': '@123456#',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
TIME_ZONE = 'America/Caracas'

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = (
    '%d/%m/%Y',
    )

DATETIME_FORMAT = 'N j, Y, P'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/franconori/webapps/static_herramientas'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = (os.path.join(BASE_DIR, '../media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, '../static/fixtures'),
)

# For Sidebar Menu (List of apps and models) (RECOMMENDED)
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

#Configuracion de envio de correos
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'herramientas_mail'
EMAIL_HOST_PASSWORD = '@Alqui2112#'
DEFAULT_FROM_EMAIL = 'contacto@alquiherramientas.com'
SERVER_EMAIL = 'contacto@alquiherramientas.com'

AUTH_USER_MODEL = 'administrador.User'