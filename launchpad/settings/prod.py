from .base import *
import os
import django_heroku

ALLOWED_HOSTS = ["gs-voting.herokuapp.com"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = os.environ.get("SECRET_KEY")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# database
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": os.environ("PDB_NAME"),
#         "USER": os.environ("PDB_USER"),
#         "PASSWORD": os.environ("PDB_PASS"),
#         "HOST": "localhost",
#         "PORT": "",
#     }
# }

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME=os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

django_heroku.settings(locals())