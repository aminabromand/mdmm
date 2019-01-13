import datetime
import os

AWS_ON = True

AWS_GROUPNAME = os.environ.get('AWS_GROUPNAME', 'DEFAULT')
AWS_USERNAME = os.environ.get('AWS_USERNAME', 'DEFAULT')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'DEFAULT')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', 'DEFAULT')

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'mdmm.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'mdmm.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'mdmm-bucket'

AWS_S3_REGION_NAME = 'eu-central-1'
AWS_S3_HOST = 's3.eu-central-1.amazonaws.com'
AWS_S3_SIGNATURE_VERSION = 's3v4'

S3DIRECT_REGION = 'eu-central-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL + 'media/'
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
	'Expires': expires,
	'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

PROTECTED_DIR_NAME = 'protected'
PROTECTED_MEDIA_URL = '//%s.s3.amazonaws.com/%s/' %( AWS_STORAGE_BUCKET_NAME, PROTECTED_DIR_NAME)

AWS_DOWNLOAD_EXPIRE = 5000 #(0ptional, in milliseconds)