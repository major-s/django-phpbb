from django.conf import settings

# These defaults can be overriden in project's settings.py

PHPBB_TABLE_PREFIX = getattr(settings, 'PHPBB_TABLE_PREFIX', 'phpbb_')
PHPBB_BLOCKED_FORUMS = getattr(settings, 'PHPBB_BLOCKED_FORUMS', [])
