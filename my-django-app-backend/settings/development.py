# SECURITY WARNING: don't run with debug turned on in production!
import os

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True


# Database -- development
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

try:
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': os.environ['DATABASE_NAME'],
      'USER': os.environ['DATABASE_USER'],
      'PASSWORD': os.environ['DATABASE_PSWD'],
      'HOST': os.environ['DATABASE_URL'],
      'PORT': '5432'
    }
  }
except:
  print("Database environment variables not set up properly")