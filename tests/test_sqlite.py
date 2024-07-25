# This is an example test settings file for use with the Django test suite.
#
# The 'sqlite3' backend requires only the ENGINE setting (an in-
# memory database will be used). All other backends will require a
# NAME and potentially authentication information. See the
# following section in the docs for more information:
#
# https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/
#
# The different databases that Django supports behave differently in certain
# situations, so it is recommended to run the test suite against as many
# database backends as possible.  You may want to create a separate settings
# file for each of the backends you test against.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'HOST': 'localhost',
        'NAME': 'django_test2',
        'USER': 'mohammad3',
        'PASSWORD': '1m2m3m4M5M',
        'PORT': '5432'
    },
    "other": {
        "ENGINE": "django.db.backends.postgresql",
        'HOST': 'localhost',
        'NAME': 'django_test3',
        'USER': 'mohammad3',
        'PASSWORD': '1m2m3m4M5M',
        'PORT': '5432'
    },
}


# settings.py

WORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

USE_TZ = False

#SECRET_KEY= 'eSWaAIMt2B3TBog9D8qKHSCJ-R_yZl21FMdNLOl22KXUow0Ph5y_9SesYCh-X5Yah9o'
SECRET_KEY = "django_tests_secret_key"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://default:1m2m3m4M5M@127.0.0.1:6379",
    }
}

#SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_ENGINE = 'django.contrib.sessions.backends.db' # New

SESSION_CACHE_ALIAS = 'default'
