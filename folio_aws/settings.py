import os
from pathlib import Path
import subprocess
import ast


# Unfortunately EB won't access variables stored in environment so must do the
# below
def get_environ_vars():
    completed_process = subprocess.run(
        ['/opt/elasticbeanstalk/bin/get-config', 'environment'],
        stdout=subprocess.PIPE,
        text=True,
        check=True
    )
    return ast.literal_eval(completed_process.stdout)


BASE_DIR = Path(__file__).resolve().parent.parent
env_vars = get_environ_vars()
SECRET_KEY = env_vars['SECRET_KEY']

DEBUG = env_vars['DJANGO_DEBUG']

if DEBUG == '1':
    ALLOWED_HOSTS = ['127.0.0.1']

    DATABASES = {
        'default': {
            'ENGINE': env_vars['LOCAL_ENGINE'],
            'NAME': env_vars['LOCAL_NAME'],
            'USER': env_vars['LOCAL_USER'],
            'PASSWORD': env_vars['LOCAL_PASSWORD'],
            'HOST': env_vars['LOCAL_HOST'],
            'PORT': env_vars['LOCAL_PORT'],
        }
    }

else:
    ALLOWED_HOSTS = [
        env_vars['AWS_HOST_NAME']
    ]

    # Using centralised credentials for production environment as this is
    # not committed and also for immutability.

    if 'RDS_HOSTNAME' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAME'],
                'PORT': os.environ['RDS_PORT'],
            }
        }

    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': env_vars['RDS_DB_NAME'],
                'USER': env_vars['RDS_USERNAME'],
                'PASSWORD': env_vars['RDS_PASSWORD'],
                'HOST': env_vars['RDS_HOSTNAME'],
                'PORT': env_vars['RDS_PORT'],
            }
        }

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
