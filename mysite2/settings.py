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
from readJson import readJson
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
if hostname != 'darlin.local':
    IS_LOCAL = False
    USER_SESSION_EXPIRE = 10 * 60
    DEBUG = False
else:
    IS_LOCAL = True
    USER_SESSION_EXPIRE = None
    DEBUG = True

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
    'app.link',
)

THIRD_APPS = (
    'rest_framework',
    'corsheaders',
    'django_markdown',
    'django_mysql',
)

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
)

ROOT_URLCONF = 'mysite2.urls'

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
    MYSQL = readJson('./config/mysql/api.json')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': MYSQL.get('NAME'),
            'USER': MYSQL.get('USER'),
            'PASSWORD': MYSQL.get('PASSWORD'),
            'HOST': MYSQL.get('HOST'),
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
            'PORT': MYSQL.get('PORT'),
            'OPTIONS': {
                # Tell MySQLdb to connect with 'utf8mb4' character set
                'charset': 'utf8mb4',
            },
            # Tell Django to build the test database with the 'utf8mb4' character set
            'TEST': {
                'CHARSET': 'utf8mb4',
                'COLLATION': 'utf8mb4_unicode_ci',
            },
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGE_SIZE': 20
}

SESSION_COOKIE_DOMAIN = '.darlin.me'
CSRF_COOKIE_DOMAIN = '.darlin.me'

if IS_LOCAL:
    SESSION_COOKIE_DOMAIN = 'localhost'
    CSRF_COOKIE_DOMAIN = 'localhost'

# CORS_ORIGIN_WHITELIST = (
#     'local.darlin.me',
#     'darlin.me',
#     'www.darlin.me',
#     'spider.darlin.me',
#     'new.darlin.me',
#     'http.darlin.me',
# )
CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?(\w+\.)?darlin\.me$', )

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'user-agent',
    'accept-encoding',
    'x-aestoken',
)

AUTH_USER_MODEL = 'account.Profile'

QINIU = readJson('./config/qiniu.json')
QINIU_ACCESS_KEY = QINIU.get('ACCESS_KEY')
QINIU_SECRET_KEY = QINIU.get('SECRET_KEY')
QINIU_BUCKET_DEFAULT = 'qiniu-darlin-me'
QINIU_MEDIA_SRC = 'media/'

ALIYUN = readJson('./config/aliyun.json')
ALIYUN_KEY_ID = ALIYUN.get('KEY_ID')
ALIYUN_KEY_SECRET = ALIYUN.get('KEY_SECRET')
ALIYUN_BUCKET_ENDPOIONTS = 'http://oss-cn-shanghai.aliyuncs.com'
ALIYUN_BUCKET = 'darlin-me'
ALIYUN_MEDIA_SRC = 'media/'

GITHUB = readJson('./config/github/darlin.me.json')
GITHUB_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_CLIENT_ID = GITHUB.get('CLIENT_ID')
GITHUB_CLIENT_SECRET = GITHUB.get('CLIENT_SECRET')
GITHUB_CALLBACK = 'http://darlin.me'

QQ = readJson('./config/qq/darlin.me.json')
QQ_AUTHORIZE_URL = 'https://graph.qq.com/oauth2.0/authorize'
QQ_CLIENT_ID = QQ.get('CLIENT_ID')
QQ_CLIENT_SECRET = QQ.get('CLIENT_SECRET')

API_URL = ''
