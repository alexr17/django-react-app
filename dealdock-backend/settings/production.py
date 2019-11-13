# SECURITY WARNING: don't run with debug turned on in production!
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['dealdock.herokuapp.com']

# heroku uses a dynamically changing environment variable that this package uses
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)