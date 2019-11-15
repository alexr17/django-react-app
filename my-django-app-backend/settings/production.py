# SECURITY WARNING: don't run with debug turned on in production!
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [] # put your url here

SECURE_SSL_REDIRECT = True

# database configuration for heroku. if not using heroku see development.py for database config example
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)