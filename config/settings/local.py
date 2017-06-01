
from .base import *

#loading the local environment variables
env_file = str(ROOT_DIR.path('.env.local'))
print('Loading : {}'.format(env_file))
env.read_env(env_file)
print('The .env.local file has been loaded.')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='fr+si28x_^u5pu3-75699-ih_z%rlb^e1jb8w&!%1w^7pyzh=(')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST', default='localhost'),
        'PORT': env('DATABASE_PORT', default='5432'),
    }
}
