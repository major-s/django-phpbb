from django.conf import settings

PHPBB_TABLE_PREFIX = getattr(settings, 'PHPBB_TABLE_PREFIX', 'phpbb_')
