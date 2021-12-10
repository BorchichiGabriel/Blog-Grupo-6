# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogDB',
        'USER':'postgres',
        'PASSWORD':'226997',
        'HOST':'localhost',
        'PORT':'5432'
    }
}