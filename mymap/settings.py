# mymap/settings.py

from dotenv import load_dotenv

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv( BASE_DIR / '.env', )

# settings for Windows 10 with GDAL
if os.name == 'nt':
  VENV_BASE = os.environ['VIRTUAL_ENV']
  os.environ['PATH']     = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
  os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

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
  'django.contrib.gis',
  # packages
  'rest_framework',
  'rest_framework_gis',
  'gisserver',
  'leaflet',
  'djgeojson',
  'slippers',
  # apps
  'site_basis.apps.SiteBasisConfig',
  'markers.apps.MarkersConfig',
  'stations.apps.StationsConfig',
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

ROOT_URLCONF = 'mymap.urls'

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

WSGI_APPLICATION = 'mymap.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': os.getenv('PG_DATABASE'),
    'USER': os.getenv('PG_USER'),
    'PASSWORD': os.getenv('PG_PASSWORD'),
    'PORT': 5432,
    'HOST': 'localhost'
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
TIME_ZONE     = 'Europe/Amsterdam'
USE_I18N      = True
USE_TZ        = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles" # The absolute filesystem path to the directory where collectstatic will collect static files for deployment.
STATIC_URL  = "/static/"               # URL to use when referring to static files located in STATIC_ROOT.

MEDIA_ROOT = BASE_DIR / "mediafiles"   # The absolute filesystem path to the directory that will hold user-stored files.
MEDIA_URL  = "/media/"                 # URL that handles the media served from MEDIA_ROOT, used for managing stored files.

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LEAFLET_CONFIG = {
  #'SPATIAL_EXTENT'     : (5.0, 44.0, 7.5, 46),
  'SPATIAL_EXTENT'     : (4.5, 51.0, 6.0, 53.5),
  'DEFAULT_CENTER'     : (52.5, 4.95),
  'DEFAULT_ZOOM'       : 16,
  'MIN_ZOOM'           : 3,
  'MAX_ZOOM'           : 18,
  'DEFAULT_PRECISION'  : 6,
  'ATTRIBUTION_PREFIX' : 'Powered by datalab',
  'SCALE'              : 'metric',
  #'MINIMAP'            : True,
  'PLUGINS': {
    'draw': {
      'css': ['https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/1.0.4/leaflet.draw.css',],
      'js': 'https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/1.0.4/leaflet.draw.js',
      'auto-include': True,
    },
  },
  #'TILES'              : 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
}