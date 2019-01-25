from .base import *

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'    #for the pictures/images
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


