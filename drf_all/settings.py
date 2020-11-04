"""
Django settings for drf project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0a!r)m1qvf)b-^&vrj8-xq_@^$$=&qr&ljht+xeg(xkopn9-5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_day2',
    'drf_day1',
    'drf_day3',
    'drf_day4',
    'drf_day5',
    'drf_day6',
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

ROOT_URLCONF = 'drf_all.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'drf_all.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# 静态资源目录
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "media/"
AUTH_USER_MODEL = "drf_day5.User5"
# DRF的全局配置
REST_FRAMEWORK = {
    # DRF渲染器默认配置
    'DEFAULT_RENDERER_CLASSES': [
        # json格式的渲染器
        'rest_framework.renderers.JSONRenderer',
        # # 浏览器渲染
        'rest_framework.renderers.BrowsableAPIRenderer',
        # 'rest_framework.renderers.TemplateHTMLRenderer',
    ],
    # DRF默认的解析器的配置
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',  # 解析json数据
        'rest_framework.parsers.FormParser',  # 解析不带文件的form数据
        'rest_framework.parsers.MultiPartParser'  # 解析带文件的form数据
    ],

    # DRF配置的全局异常处理的方法
    'EXCEPTION_HANDLER': 'drf_day2.exceptions.exception_handler',



    # DRF默认的权限认证类
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 默认的认证器
        'rest_framework.authentication.SessionAuthentication',  # 基于session
        'rest_framework.authentication.BasicAuthentication',  # Basic
        # 'api.authentications.MyAuth',
    ],
    # DRF默认的权限配置
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    # DRF频率配置
    'DEFAULT_THROTTLE_CLASSES': [
        # 'rest_framework.throttling.UserRateThrottle',
        'drf_day5.throttle.SendMessageRate',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/m',
        'user': '10/day',
        'send': '1/m',
    }
}
