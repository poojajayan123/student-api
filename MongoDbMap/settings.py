import os
from six.moves import urllib
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = 'z2m_c5vlb4*gn9rvi(chtc(g2ionuyts$+#cuj$3i15f_)q1kc'

DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1']
APPEND_SLASH=False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'Student',
    'polls',
    'users',
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

ROOT_URLCONF = 'MongoDbMap.urls'

AUTH_USER_MODEL = "Student.StudentUser"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'MongoDbMap.wsgi.application'

MONGODB_DATABASES = {
    'default' : {
        'NAME' : 'Student',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME'  : 'Student',
           'CLIENT': {
              'host': 'mongodb+srv://root:' + urllib.parse.quote_plus('root') + '@iti.dbmyx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
              'port': 27017,                                                        
              'username': 'root',
              'password': 'root',
            }
    }
}

AUTHENTICATION_BACKENDS = (
   ['django.contrib.auth.backends.ModelBackend']
)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    ),
}
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

# LOGIN_REDIRECT_URL = '/users/home/'
# LOGIN_URL = '/users/login/'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_FILE_ROOT = 'D:\python\MongoDbMap\MongoDbMap\static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    'D:\python\MongoDbMap\MongoDbMap\static',
)
