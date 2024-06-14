"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from . import vars # container environment specific vars
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

SITE_URL = vars.vars["SITE_URL"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = envs = vars.vars["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = vars.vars["DEBUG"]

LANGUAGE_CODE = 'de'
TIME_ZONE = 'CET'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = ( os.path.join(BASE_DIR, 'locale'), )
# Languages available
LANGUAGES = (
    ('de', 'Deutsch'),
    # ('en', 'English'),
)

ALLOWED_HOSTS = vars.vars["ALLOWED_HOSTS"]

INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition
CELERY_BROKER_URL = 'redis://localhost:6379/0'

# a better shell
SHELL_PLUS = "ipython"

INSTALLED_APPS = [
    # Live Reload
    #'livereload',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    # Admin Interface
    #'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'pagedown',
    'django_filters',
    #'debug_toolbar',

    # Assets
    'pipeline',
    'pwa',

    # Pages
    'app',
    'core',
    'quiz',
    'casetraining',
    'tandem_exams',
    'pages',
    #'news',
    'emails',
    'profiles',
    #'leaflet',
    'feedback',
    'dashboard',
    'flashcards',

    # Wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.routable_page',
    'wagtail.contrib.table_block',
    # not available in wagtail 2.13
    # 'wagtail.contrib.typed_table_block',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtailmodelchooser',
    'wagtailcolumnblocks',
    'wagtail_color_panel',
    'wagtailfontawesome',
    'wagtailautocomplete',
    'wagtailmarkdown',

    'modelcluster',
    'taggit',

    # Wiki
    'django.contrib.sites.apps.SitesConfig',
    'django.contrib.humanize.apps.HumanizeConfig',
    'django_nyt.apps.DjangoNytConfig',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki.apps.WikiConfig',
    # 'wiki.plugins.attachments.apps.AttachmentsConfig',
    # not used
    # 'wiki.plugins.notifications.apps.NotificationsConfig',
    # 'wiki.plugins.images.apps.ImagesConfig',
    # 'wiki.plugins.macros.apps.MacrosConfig',

    # this is buggy
    # 'wiki.plugins.editsection.apps.EditSectionConfig',
    'wiki.plugins.help.apps.HelpConfig',
    'wiki.plugins.links.apps.LinksConfig',
    'wiki.plugins.globalhistory.apps.GlobalHistoryConfig',
    'editors',
    'markdownify',

    # Chatter
    #'django_chatter',

    # User Profile
    'avatar',

    # Comments
    'django_comments_xtd',
    'django_comments',
    'comments_wagtail_xtd',

    # Wagtail News
    'wagtailnews',

    # Wagtail Menus
    'wagtailmenus',

    # Wagtail Newsletter
    'mjml',
    'birdsong',

    # Link Checker
    #'wagtaillinkchecker',

    # Wagtail Polls
    'wagtailpolls',
    'wagtail.contrib.modeladmin',
    'wagtailstreamforms',
    'treemodeladmin',

    # DRF
    'rest_framework',
    'rest_framework.authtoken',

    # cors-headers
    'corsheaders',

    # django channels
    # 'channels',
] + vars.vars.get("DEV_APPS", [])

MIDDLEWARE = [
    'app.middleware.XForwardedForMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    #'livereload.middleware.LiveReloadScript',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'wagtailmenus.context_processors.wagtailmenus',
            ],
        },
    },
]

#WSGI_APPLICATION = 'wsgi.application'
ASGI_APPLICATION = 'app.routing.application'

ADMINS = vars.vars["ADMINS"]
SERVER_EMAIL = vars.vars["SERVER_EMAIL"]
DEFAULT_FROM_EMAIL = vars.vars["DEFAULT_FROM_EMAIL"]
BIRDSONG_FROM_EMAIL = vars.vars["BIRDSONG_FROM_EMAIL"]

if DEBUG:
    # use mailcatcher for development
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = "localhost"
    EMAIL_PORT = "1025"
else:
    EMAIL_BACKEND = 'django_ses.SESBackend'
    AWS_ACCESS_KEY_ID = 'AKIAU6GDWNDEJWBRSTFV'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_SES_REGION_NAME = 'eu-central-1'
    AWS_SES_REGION_ENDPOINT = 'email.eu-central-1.amazonaws.com'

    #EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    #EMAIL_HOST = vars.vars["EMAIL"]["host"]
    #EMAIL_PORT = vars.vars["EMAIL"]["port"]
    #EMAIL_HOST_USER = vars.vars["EMAIL"]["login"]
    #EMAIL_HOST_PASSWORD = vars.vars["EMAIL"]["password"]
    #EMAIL_USE_TLS = True
    #EMAIL_USE_SSL = True
    #EMAIL_SSL_VERSION = 'TLSv1_2'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = vars.vars["DATABASES"]

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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CHANNEL_LAYERS = {
  'default': {
      'BACKEND': 'channels_redis.core.RedisChannelLayer',
      'CONFIG': {
        'hosts': [('127.0.0.1', 6379)],
      },
  },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/assets/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'pipeline.storage.PipelineManifestStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build')
]

WAGTAIL_SITE_NAME = 'strafrecht-online'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SITE_ID = 1

PIPELINE = {
    'PIPELINE_ENABLED': not vars.vars["DEBUG"], #not DEBUG
    'COMPILERS': (
        'pipeline.compilers.sass.SASSCompiler',
        'pipeline.compilers.es6.ES6Compiler'
    ),
    'CSS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'BABEL_ARGUMENTS': '', #'--presets es2016',
    'STYLESHEETS': {
    },
    'JAVASCRIPT': {
    }
}

X_FRAME_OPTIONS='SAMEORIGIN'

LOGIN_URL = "/profile/login/"
LOGOUT_URL = "/profile/logout/"

WIKI_ACCOUNT_HANDLING = True
WIKI_ACCOUNT_SIGNUP_ALLOWED = False
WIKI_SIGNUP_URL = "/profile/register/"
WIKI_ANONYMOUS = True
WIKI_ANONYMOUS_CREATE = True
WIKI_ANONYMOUS_WRITE = True
WIKI_EDITOR = 'editors.modern.Modern'
WIKI_CHECK_SLUG_URL_AVAILABLE = False
# we hopefully don't get over this
WIKI_SHOW_MAX_CHILDREN = 500

from .wiki_patch import wiki_can_moderate
WIKI_CAN_MODERATE = wiki_can_moderate
WIKI_CAN_DELETE = wiki_can_moderate

COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 5
COMMENTS_XTD_CONFIRM_EMAIL = True

CHAT_WS_SERVER_HOST = 'localhost'
CHAT_WS_SERVER_PORT = 5002
CHAT_WS_SERVER_PROTOCOL = 'ws'

#import os
#if os.name == 'nt':
#    import platform
#    OSGEO4W = r"C:\OSGeo4W"
#    if '64' in platform.architecture()[0]:
#        OSGEO4W += "64"
#    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
#    os.environ['OSGEO4W_ROOT'] = OSGEO4W
#    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
#    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
#    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']
#else:
#    GDAL_LIBRARY_PATH = '/usr/include/gdal'

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8080",
#     "http://127.0.0.1:8000"
# ]


CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ],
}

PWA_APP_NAME = 'Strafrecht Online'
PWA_APP_DESCRIPTION = "Strafrecht Online"
PWA_APP_THEME_COLOR = 'rgb(255, 226, 0)'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/assets/images/icon.png',
        'size': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/assets/images/icon.png',
        'size': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/assets/images/icon.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

AVATAR_GRAVATAR_DEFAULT = 'identicon'
AVATAR_EXPOSE_USERNAMES = False
AVATAR_MAX_AVATARS_PER_USER = '1'

# CSP_SCRIPT_SRC = ("'self'", "'unsafe-eval'", "'unsafe-inline'",)
COMMENTS_APP = 'django_comments_xtd'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
COMMENTS_XTD_MAX_THREAD_LEVEL = 5

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
CSRF_TRUSTED_ORIGINS = ['https://strafrecht-online.org/']
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': vars.vars["LOGGING"]["level"],
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': vars.vars["LOGGING"]["filename"],
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': vars.vars["LOGGING"]["level"],
            'propagate': True,
        },
    },
}