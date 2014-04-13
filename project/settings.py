"""
Django settings for derzhanski project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^nb-m=j69krhowe2l&+eah*0_0wv=h8adkt=g8lg^*oiq=%a1*'


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'base',
	'users',
	'problems',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

# Added Later
ADMINS = (
	('Pavel', 'pavelsof@gmail.com'),
)
AUTH_USER_MODEL = 'users.User'

# Location-specific Settings
if 'DYNO' in os.environ:
	import dj_database_url
	DEBUG = True
	TEMPLATE_DEBUG = True
	ALLOWED_HOSTS = ['*']
	DATABASES = {
		'default': dj_database_url.config()
	}
else:
	DEBUG = True
	TEMPLATE_DEBUG = True
	ALLOWED_HOSTS = []
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'development/db.sqlite3'),
		}
	}

