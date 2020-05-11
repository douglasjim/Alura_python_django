"""
Django settings for alurareceita project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pmeop740z0+%-3j^glpi!e_t)6m%_&hp500+^(f!zjqwo5u8c%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

#registramento
INSTALLED_APPS = [
    'receitas',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'alurareceita.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'receitas/templates')], #aqui temos que especificar onde esta o arquivo da WEB
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

WSGI_APPLICATION = 'alurareceita.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



#temos que realizar dowload de arquivos(ferramentas) que possamos fazer essa tal ponte entre o django e o nosso Banco de dados que no caso é o postGre o icone do elefante
#OBS !! PRECISAMOS COLOCAR TODAS ESSAS INFORMACOES ABAIXO PARA QUE POSSAMOS CONECTAR NO BANCO DE DADOS !!!!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', #nesse caso estamos usando o postgresql se fosse outro iamos colocar o nome do outro
        'NAME': 'alura_receita', #nome do banco de dados que criamos
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


#tudo isso nas linhas de baixo serve para dizer que temos arquios estaticos e queremos usar
STATOC_ROOT = os.path.join(BASE_DIR,'static') # aqui serve para relatar que temos arquivos estaticos que no caso sao javascript e css
STATIC_URL = '/static/'
#aqui estamos dizendo onde esta nossos arquivos estaticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'alurareceita/static')
]
#

django_heroku.settings(locals())