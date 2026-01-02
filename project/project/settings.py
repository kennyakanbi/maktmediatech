import os
from pathlib import Path
from decouple import config
from django.contrib.messages import constants as messages
import dj_database_url
from django.core.management.utils import get_random_secret_key

SECRET_KEY = os.environ.get("SECRET_KEY")


# =====================
# BASE DIR
# =====================
BASE_DIR = Path(__file__).resolve().parent.parent

# =====================
# SECURITY
# =====================
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
        "maktmediatech.onrender.com",
    "127.0.0.1",
    "localhost",
]

CSRF_TRUSTED_ORIGINS = [
    "https://maktmediatech.onrender.com",
]

# HTTPS behind Render proxy
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = None
CSRF_COOKIE_SAMESITE = None

# Optional: for subdomain support
# SESSION_COOKIE_DOMAIN = ".maktmediatech.onrender.com"
# CSRF_COOKIE_DOMAIN = ".maktmediatech.onrender.com"

# =====================
# DATABASE
# =====================
BASE_DIR = Path(__file__).resolve().parent.parent

if os.environ.get("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ.get("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True,
        )
    }
else:
    # Local development with SQLite
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }



# =====================
# APPLICATIONS
# =====================
INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "cloudinary",
    "cloudinary_storage",

    # Local apps
    "myapp.apps.MyappConfig",
    "main",
]

# =====================
# MIDDLEWARE
# =====================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# =====================
# URLS / WSGI
# =====================
ROOT_URLCONF = "project.urls"
WSGI_APPLICATION = "project.wsgi.application"

# =====================
# TEMPLATES
# =====================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# =====================
# PASSWORD VALIDATION
# =====================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =====================
# INTERNATIONALIZATION
# =====================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =====================
# STATIC FILES
# =====================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Whitenoise for production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =====================
# MEDIA FILES (Cloudinary)
# =====================
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": config("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": config("CLOUDINARY_API_KEY"),
    "API_SECRET": config("CLOUDINARY_API_SECRET"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
MEDIA_URL = "/media/"

# =====================
# DEFAULT PK
# =====================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =====================
# MESSAGES
# =====================
MESSAGES_TAGS = {messages.ERROR: "danger"}

LOGIN_REDIRECT_URL = "/admin/"
LOGOUT_REDIRECT_URL = "/admin/login/"
