"""
Django settings for DraftNews project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os #
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o9zg#&9!fvy+$8g%0!(xg*_p_6b_y$3162x3dld#3p$(&m2%w@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', #added
    'django.contrib.flatpages', #added
    'newsportal.apps.NewsportalConfig',
    'django_filters', #filters via pip

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.google',

    'django_apscheduler',


]

SITE_ID =1   #we added this var in advance for .sites and .flatpages

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', ####
    #CACHE MW:
    'django.middleware.locale.LocaleMiddleware',

]

ROOT_URLCONF = 'DraftNews.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], ####
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'DraftNews.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
        "TIMEOUT": 300
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
LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static' ] ##########

LOGIN_REDIRECT_URL = "/newsportal"
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}
#Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию

SITE_URL = 'http://127.0.0.1:8000'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" #-- to console

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "a-re-a@yandex.ru"
EMAIL_HOST_PASSWORD = "beskfjolemjokxbo"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = '[NewsPortal] '

DEFAULT_FROM_EMAIL = "a-re-a@yandex.ru"

SERVER_EMAIL = "a-re-a@yandex.ru"
MANAGERS = (
    ('Me', 'a-re-a@yandex.ru'),
)

ADMINS = (
    ('Me', 'a-re-a@yandex.ru'),
)


APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'

APSCHEDULER_RUN_NOW_TIMEOUT = 25    #кол-во секунд, за кот. ф-ция должна выполниться

#Celery
CELERY_BROKER_URL = f'redis://default:irC9lB8SC8EcQLc2k6lA3QnID2Ys8wch@redis-12366.c304.europe-west1-2.gce.cloud.redislabs.com:12366'
CELERY_RESULT_BACKEND = f'redis://default:irC9lB8SC8EcQLc2k6lA3QnID2Ys8wch@redis-12366.c304.europe-west1-2.gce.cloud.redislabs.com:12366'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ENABLE_UTC = False
#celery -A DraftNews worker -l INFO --pool=solo


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },

    "formatters": {
        "console_format": {
            "format": "{asctime} : {levelname} – {message}",
            "style": "{",
        },
        "warning_format": {
            "format": "{asctime} : {levelname} – {pathname} / {message}",
            "style": "{",
        },
        "error_format": {
            "format": "{asctime} : {levelname} – {pathname} / {exc_info} – {message}",
            "style": "{",
        },
        "info_and_security_format": {
            "format": "{asctime} : {levelname} – {module} – {message}",
            "style": "{",
        },
    },

    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "console_format",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "formatter": "warning_format",
        },
        "general": {
            "level": "INFO",
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "filename": "general.log",
            "formatter": "info_and_security_format",
        },
        "errors": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "errors.log",
            "formatter": "error_format",
        },
        "security": {
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "filename": "security.log",
            "formatter": "info_and_security_format",
        },

    },
    "loggers": {
        "django": {
            "handlers": ["console", "general"],
        },
        "django.server": {
            "handlers": ["errors", "mail_admins"],
            "level": "ERROR",
        },
        "django.request": {
            "handlers": ["errors", "mail_admins"],
            "level": "ERROR",

        },
        "django.template": {
            "handlers": ["errors"],
            "level": "ERROR",
        },
        "django.db.backends": {
            "handlers": ["errors"],
            "level": "ERROR",
        },
        "django.security.*": {
            "handlers": ["security"],
        },
    },
}