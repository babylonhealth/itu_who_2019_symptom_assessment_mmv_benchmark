"""
Django settings for mmvb_backend project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

IS_TRUE = lambda value: str(value).lower() in ["1", "true", "yes"]  # noqa

ENABLE_TOY_AIS = IS_TRUE(os.environ.get("ENABLE_CASE_SYNTHESIZER", "true"))

ENABLE_CASE_SYNTHESIZER = IS_TRUE(
    os.environ.get("ENABLE_CASE_SYNTHESIZER", "true")
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "7ik*d943xjsg6+yc!fj+sd!xf6l2qculn-ufn@3%tlse2p5rd)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TODO: properly configure it for dev/prod environments in the future
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_mysql",
    "rest_framework",
    "corsheaders",
    "common",
    "ai_implementations",
    "benchmarking_sessions",
    "cases",
]

if ENABLE_TOY_AIS:
    INSTALLED_APPS.append("toy_ais")

if ENABLE_CASE_SYNTHESIZER:
    INSTALLED_APPS.append("case_synthesizer")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mmvb_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "mmvb_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME", "mmvb"),
        "USER": os.environ.get("DB_USER", "system"),
        "PASSWORD": os.environ.get("DB_PWD", "systemsecret"),
        "HOST": os.environ.get(
            "DB_HOST", "127.0.0.1"
        ),  # Or an IP Address that your DB is hosted on
        "PORT": os.environ.get("DB_PORT", "3306"),
        "OPTIONS": {"charset": "utf8mb4",},
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

AUTH_USER_MODEL = "common.User"

APPEND_SLASH = False

# DRF settings

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ],
}

# CELERY configs

CELERY_BROKER_URL = "redis://" + os.environ.get("REDIS_HOST", "localhost")
CELERY_RESULT_BACKEND = "redis://" + os.environ.get("REDIS_HOST", "localhost")

# CORS settings

CORS_ORIGIN_WHITELIST = [
    "https://localhost:3000",
    "http://localhost:3000",
    "https://127.0.0.1:3000",
    "http://127.0.0.1:3000",
    "https://localhost:8000",
    "http://localhost:8000",
    "https://127.0.0.1:8000",
    "http://127.0.0.1:8000",
    "https://fgai4h-tg-symptom-benchmarking-frontend-omne4kyxzq-ez.a.run.app",
    "http://fgai4h-tg-symptom-benchmarking-frontend-omne4kyxzq-ez.a.run.app",
    "https://demo-who2019.air.babylontech.co.uk:8000",
    "http://demo-who2019.air.babylontech.co.uk:8000",
    os.environ.get("WEBAPP_HOST_URL") or "http://localhost:8080",
]

# Project and Apps Configurations
BENCHMARKING_SESSION_TIMEOUT = int(
    os.environ.get("BENCHMARKING_SESSION_TIMEOUT", 10)
)

SERVER_URL = os.environ.get("MMVB_SERVER_URL", "http://localhost")
SERVER_PORT = os.environ.get("MMVB_SERVER_PORT", "8000")
DEFAULT_TIMEOUT = int(os.environ.get("DEFAULT_TIMEOUT", 2))
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", 3))
