# coding: utf-8
"""
Django settings for mysite2 project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&zpmk=@&vz!a(y0e$v#@sczt^pisebm@82mzyhyg&g@!vldf)o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

import socket
hostname = socket.gethostname()
if hostname == 'iZ94zbdp1q5Z':
    IS_LOCAL = False
    USER_SESSION_EXPIRE = 10 * 60
    DEBUG = False
    EMPLATE_DEBUG = False
else:
    IS_LOCAL = True
    USER_SESSION_EXPIRE = None
    DEBUG = True
    TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'app.article',
    'app.account',
    'app.comments',
)

THIRD_APPS = (
    'DjangoUeditor',
    'rest_framework',
    'corsheaders',
)

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

ROOT_URLCONF = 'mysite2.urls'

CORS_ORIGIN_WHITELIST = (
    'local.darlin.me',
    'static.darlin.me',
    'darlin.me',
)
CORS_ALLOW_CREDENTIALS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if IS_LOCAL:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mysite2',
            'USER': 'root',
            'PASSWORD': 'Shiwei122',
            'HOST': '',
            'CHARSET': 'utf8',
            'PORT': '',
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '//dn-darlin.qbox.me/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'dist'),
)
STATIC_ROOT = os.path.join(BASE_DIR, "")

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGE_SIZE': 10
}

SESSION_COOKIE_DOMAIN = '.darlin.me'
CSRF_COOKIE_DOMAIN = '.darlin.me'
# SESSION_COOKIE_DOMAIN = '.localhost:3000'

AUTH_USER_MODEL = 'account.Profile'