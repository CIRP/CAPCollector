# -*- coding: utf-8 -*-
"""Django settings for CAPCollector project test environment."""

__author__ = "arcadiy@google.com (Arkadii Yakovets)"

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# CREDENTIALS_DIR = os.path.join(BASE_DIR, "testdata/credentials")
#
# SITE_SCHEME = "http"
# SITE_DOMAIN = "localhost"
# SITE_PORT = "8081"
# SITE_URL = SITE_SCHEME + "://" + SITE_DOMAIN + ":" + SITE_PORT
#
# ALLOWED_HOSTS = ["localhost", SITE_DOMAIN]

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'dev.db.sqlite3'),
  }
}

# https://code.djangoproject.com/wiki/Fixtures
FIXTURE_DIRS = (
     os.path.join(BASE_DIR, "tests/fixtures"),
)

LANGUAGES = (
    ("en-us", "English"),
    ("hi", "Hindi"),
    ("pt-br", "Portugues"),
)
