import os
from pathlib import Path
import subprocess
import ast
import dotenv
from dotenv import load_dotenv
import json

DEBUG = False # i.e. Run locally or not
BASE_DIR = Path(__file__).resolve().parent.parent

if DEBUG:
    load_dotenv()

    SECRET_KEY = os.environ.get('SECRET_KEY')

    ALLOWED_HOSTS = ['127.0.0.1']

    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('LOCAL_ENGINE'),
            'NAME': os.environ.get('LOCAL_NAME'),
            'USER': os.environ.get('LOCAL_USER'),
            'PASSWORD': os.environ.get('LOCAL_PASSWORD'),
            'HOST': os.environ.get('LOCAL_HOST'),
            'PORT': os.environ.get('LOCAL_PORT'),
        }
    }



else:
    # If DEBUG=False use production settings - wll only ever be on AWS if in
    # prod
    # Parse the JSON file and retrieve our settings.
    SETTINGS = None
    with open(BASE_DIR.parent.parent.parent.parent / 'tmp/folio-env-app-config.json') as f:
        SETTINGS = json.load(f)


    SECRET_KEY = SETTINGS['SECRET_KEY']

    # Use the settings to connect to our DB:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql',
            'NAME':     SETTINGS['RDS_DB_NAME'],
            'USER':     SETTINGS['RDS_USERNAME'],
            'PASSWORD': SETTINGS['RDS_PASSWORD'],
            'HOST':     SETTINGS['RDS_HOSTNAME'],
            'PORT':     SETTINGS['RDS_PORT'],
        }
    }

    ALLOWED_HOSTS = [
            SETTINGS['AWS_HOST_NAME']
        ]

        # Using centralised credentials for production environment as this is
        # not committed and also for immutability.

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation'
                    '.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation'
                    '.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation'
                    '.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation'
                    '.NumericPasswordValidator',
        },
    ]

INSTALLED_APPS = [
    'folio_aws.apps.basic.apps.HomeConfig',
    'folio_aws.apps.projects.apps.ProjectsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'folio_aws.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'folio_aws.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-ie'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images]
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'static'

# Temporarily put the static dir into a temp folder and adjust the dirs below
# accordingly to fre up scope for static compilation

STATICFILES_DIRS = [
    BASE_DIR / "static_temp/static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
