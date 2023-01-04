from .base import *
import pymysql

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


pymysql.version_info = (1, 4, 2, 'final', 0)

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cities',
        'USER': 'root',
        'PASSWORD': 'RealMadrid97!',
        'HOST': 'localhost',
        'PORT': '',
    }
}