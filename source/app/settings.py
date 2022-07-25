import os

IS_PRODUCTION = os.environ.get('IS_PRODUCTION')

if IS_PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *
import django_on_heroku
django_on_heroku.settings(locals())
