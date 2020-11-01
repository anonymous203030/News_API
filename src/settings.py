
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '^8zln(b3lvgulb@0l2hc3v9(df5t6v3s534&^mm^e!$1%_x)0u'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',

    #apps
    'posts',
    'users',
    'comments',
    'subscription',
    #3-rd party
    'rest_framework',
    'drf_yasg',

]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #new ! Django-debug-toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
# DJANGO DEBUG TOOLBAR FORCE!
MIDDLEWARE += (
    'debug_toolbar_force.middleware.ForceDebugToolbarMiddleware',
)



ROOT_URLCONF = 'src.urls'

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
#new !
WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# new!
AUTH_USER_MODEL = "users.User"

STATIC_ROOT = os.path.join(BASE_DIR, "src", "static")
#For Image
MEDIA_ROOT = os.path.join(BASE_DIR, "src", "media")
MEDIA_URL = "/media/"
#
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS":"rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE":20,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
   'rest_framework.permissions.AllowAny',
]

}
#DRF_YASG LOGIN LOGOUT
LOGIN_URL = 'admin/login/'
LOGOUT_URL = 'admin/logout/'

INTERNAL_IPS = [
    '127.0.0.1',
]


