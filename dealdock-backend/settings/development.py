# SECURITY WARNING: don't run with debug turned on in production!
import os

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True


# Database -- development
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'dealdock',
    'USER': os.environ['DATABASE_USER'],
    'PASSWORD': os.environ['DATABASE_PSWD'],
    'HOST': os.environ['DATABASE_URL'],
    'PORT': '5432'
  }
}