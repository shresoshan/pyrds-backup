''' This modules setup the script configuration. '''
from os import environ, path

#dry_run = environ.get('DRY_RUN') or ''

config = {
    'stage': environ.get('STAGE'),
    'database': environ.get('DATABASE'),
    'server': environ.get('SERVER'),
    'port': environ.get('PORT'),
    'username': environ.get('USERNAME'),
    'password': environ.get('PASSWORD'),
    'bucket': environ.get('BUCKET'),
    'driver_version': environ.get('DRIVER_VERSION'),
    'temp_bucket': environ.get('TEMP_BUCKET')
}
