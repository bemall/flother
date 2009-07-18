import os
import sys


SITE_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = False
DATE_FORMAT = 'l, jS F Y'
TIME_FORMAT = 'P'
DATETIME_FORMAT = ', '.join([TIME_FORMAT, DATE_FORMAT])
MONTH_DAY_FORMAT = 'j F'

ROOT_URLCONF = 'flother.urls'

COMMENTS_HIDE_REMOVED = False

SOUTH_AUTO_FREEZE_APP = True

COMPRESS_VERSION = True
COMPRESS_AUTO = False
COMPRESS_CSS = {
    'flother': {
        'source_filenames': ('css/reset.css', 'css/structure.css',
            'css/typography.css', 'css/sections.css'),
        'output_filename': 'css/flother.r?.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}
COMPRESS_JS = {}
CSSTIDY_ARGUMENTS = '--remove_last_\;=true --lowercase_s=true --sort_properties=true --template=highest'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'flother.utils.context_processors.section',
    'flother.utils.context_processors.current_year',
)
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)
 
MIDDLEWARE_CLASSES = (
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.SetRemoteAddrFromForwardedFor',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.redirects',

    'tagging',
    'south',
    'compress',

    'flother.apps.blog',
    'flother.apps.contact',
)
