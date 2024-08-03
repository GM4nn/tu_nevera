"""
Django settings for pruebasubir project.

Generated by 'django-admin startproject' using Django 2.0.4.

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
SECRET_KEY = 'cz8k+2b!+nmquyks%du@^-ndd$z=iyw)v^drtzha3e_ay*t2t5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    'subir',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    #'social_django',
    'usuario'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'pruebasubir.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'social_django.context_processors.backends',  
                #'social_django.context_processors.login_redirect',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    ##'social_core.backends.open_id.OpenIdAuth',
    #'social_core.backends.github.GithubOAuth2',
    #'social_core.backends.twitter.TwitterOAuth',
    #'social_core.backends.google.GoogleOAuth',
    #'social_core.backends.google.GoogleOpenId',
    #'social_core.backends.google.GoogleOAuth2',
    #'social_core.backends.google.GoogleOAuth',
    #'social_core.backends.facebook.FacebookAppOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '220085619933-rtavo4kf3b0r30tr8ut1tcusolhgvu0p.apps.googleusercontent.com' 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'KYcXotR8Udv2krJnCtZSaH1K' 

SOCIAL_AUTH_GITHUB_KEY = 'a81a38be7e69bf0c5f77'
SOCIAL_AUTH_GITHUB_SECRET = 'c981bdf01c0b01424d5ffd071b8e202024389205'

SOCIAL_AUTH_FACEBOOK_KEY = '2037962326528430'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '81dbac17a9499e651727f170215d44f8' 



WSGI_APPLICATION = 'pruebasubir.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'basededatos',
        'USER': 'root',
        'PASSWORD': 'lomismoxd123',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
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
STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media')
)


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'tunevera.official'
EMAIL_HOST_PASSWORD = 'Tunevera1112'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/indexex/'

LOGOUT_REDIRECT_URL = '/'


SOCIAL_AUTH_LOGIN_ERROR_URL = '/inicia-sesion/'