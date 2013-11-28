from django.conf import global_settings

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cms',
    'cms.stacks',
    'mptt',
    'menus',
    'south',
    'sekizai',

    'djangocms_admin_style',
    'django.contrib.admin',

    'cms.plugins.link',
    'cms.plugins.picture',

    'app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

CMS_TEMPLATES = (
    ('template1.html', 'Template One'),
)

ROOT_URLCONF = 'bug.urls'

WSGI_APPLICATION = 'bug.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}


LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('it', 'Italiano')
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'var', 'www')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SITE_ID = 1
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)
