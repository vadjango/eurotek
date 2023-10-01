"""
Django settings for CoreEurotek project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import string
from datetime import timedelta
from pathlib import Path
from configurations import Configuration
from configurations import values
from django.utils.translation import gettext_lazy as _


class Dev(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-e%)8efgb1uji_5)f7y6gqt^k*9$yq@12lrji8g!gca-hlxi9b_'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ["*"]

    CORS_ALLOW_ALL_ORIGINS = True

    # CORS_ALLOW_ALL_ORIGINS = True
    # Application definition

    INSTALLED_APPS = [
        'daphne',
        'corsheaders',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_extensions',
        'rest_framework',
        'report',
        'report.auth.user',
        'report.auth',
        'report.comment',
        'notifications'
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'CoreEurotek.urls'

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

    WSGI_APPLICATION = 'CoreEurotek.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'postgres',
            'NAME': 'eurotek',
            'PASSWORD': os.environ.get('POSTGRESQL_PASSWORD'),
            'HOST': 'localhost',
            'PORT': 5432
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.2/howto/static-files/

    STATIC_URL = 'static/'
    MEDIA_ROOT = "media/"
    MEDIA_URL = "media/"

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    AUTH_USER_MODEL = "report_user.User"
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 15
    }

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "report_formatter": {
                "format": "{levelname} {asctime} {module} {process} {thread} {message}",
                "style": "{",
                "datefmt": "%d.%m.%Y"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "report_formatter",
                "stream": "ext://sys.stdout"
            }
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG"
        }
    }

    TRENCH_AUTH = {
        'MFA_METHODS': {
            'sms_twilio': {
                "VERBOSE_NAME": _("sms_twilio"),
                "VALIDITY_PERIOD": 100000000000,
                "HANDLER": "report.auth.backends.TwoFactorMessageDispatcher",
                "SOURCE_FIELD": "phone_number",
                "TWILIO_VERIFIED_FROM_NUMBER": "+380978476990"
            }
        }
    }

    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(weeks=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(weeks=100),
        "TOKEN_OBTAIN_SERIALIZER": "report.auth.login.serializers.AuthTokenSerializer",
        "USER_ID_FIELD": "employee_id"
    }
    ASGI_APPLICATION = "CoreEurotek.asgi.application"

    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("127.0.0.1", 6379)],
            },
        },
    }


class Prod(Dev):
    DATABASES = {}
    DEBUG = False

    CORS_ALLOW_ALL_ORIGINS = False
