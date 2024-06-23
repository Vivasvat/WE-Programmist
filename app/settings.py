"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-eq&h!wvvc9+d#f8+05u3k5vuuxmq*s8$q+)fc-h1$0$8=^8x&*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'mysite.com',
    "*",
    "enjoyed-maggot-moral.ngrok-free.app",
    "localhost",
    "127.0.0.1",
]  # '*',

# Для того, чтобы работала админка на удаленном сервере
CSRF_TRUSTED_ORIGINS = ["https://enjoyed-maggot-moral.ngrok-free.app"]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',

    # 'social_core.backends.steam.SteamOpenId',
]
# Steam login
SOCIAL_AUTH_STEAM_EXTRA_DATA = ['player']
# Steam web-key
SOCIAL_AUTH_STEAM_API_KEY = '32F3511A43799D68278EE99A1F138508'

LOGIN_REDIRECT_URL= '/acc/'

# Для "удаления" промежуточных страниц в django-allauth
# Не рекомендовано по соображениям безопастности
# Лучше использовать POST запрос в формах
SOCIALACCOUNT_LOGIN_ON_GET = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    'main.apps.MainConfig',
    'users.apps.UsersConfig',
    'acc.apps.AccountConfig',

    'allauth',

    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.steam',
    'allauth.socialaccount.providers.openid',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

# ROOT_URLCONF = 'social_auth.urls'
ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]# 

# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'github': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': 'Ov23ctC6p7mAJPLaSdVM',
#             'secret': 'e40ca2a3ec3495a9fdf9250d418a32f78f8ddb22',
#             'key': ''
#         }
#     },
#     'vk': {
#         'APP': {
#             'client_id': '158255944209-7busq4pca3ibulnadc4q7udpobsokvgh.apps.googleusercontent.com',
#             'secret': 'your-vk-client-secret',
#             'key': ''
#         }
#     },
#     'google': {
#         'APP': {
#             'client_id': '51929642',
#             'secret': 'GXRCWyLuA6ni2MeL1qNR',
#             'key': ''
#         }
#     }
# }

# WSGI_APPLICATION = 'social_auth.wsgi.application'
WSGI_APPLICATION = "app.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ru"  # en-us

TIME_ZONE = "UTC" # UTC Europe/Moscow

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'users.User'
