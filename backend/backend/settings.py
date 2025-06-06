"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG")))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    "import_export",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "administration",
    "material",
    "note",
    "part",
    "project",
    "task",
    "corsheaders",
    "django_filters",
    "dbbackup",
    "ninja",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")

CORS_ORIGIN_WHITELIST = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")

CORS_ALLOW_ALL_ORIGINS = True

DBBACKUP_STORAGE = "django.core.files.storage.FileSystemStorage"
DBBACKUP_STORAGE_OPTIONS = {"location": "/backups/"}
DBBACKUP_CLEANUP_KEEP = 2
DBBACKUP_CLEANUP_KEEP_MEDIA = 2

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}

JAZZMIN_SETTINGS = {
    "show_ui_builder": bool(int(os.environ.get("DEBUG"))),
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Admin",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Admin",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "logov2.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-fluid",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "favicon.ico",
    # Welcome text on the login screen
    "welcome_sign": "Please log in",
    # Copyright on the footer
    "copyright": "John Adams",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # external url that opens in a new window (Permissions can be added)
        {
            "name": "Back to Site",
            "url": "/",
            "new_window": False,
        },
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {
            "name": "Back to Site",
            "url": "/",
            "new_window": False,
        },
    ],
    "icons": {
        "project": "fas fa-wrench",
        "project.Project": "fas fa-wrench",
        "project.ProjectStatus": "fas fa-wrench",
        "project.ProjectPhase": "fas fa-wrench",
        "task.Task": "fas fa-hammer",
        "task.TaskStatus": "fas fa-hammer",
        "part.Part": "fas fa-screwdriver",
        "part.PartStatus": "fas fa-screwdriver",
        "administration.Version": "fas fa-circle-info",
        "material.Material": "fas fa-ruler",
        "material.MaterialObject": "fas fa-ruler",
        "material.MaterialStatus": "fas fa-ruler",
        "material.Store": "fas fa-ruler",
        "material.WoodSpecies": "fas fa-ruler",
        "note.Note": "fas fa-pencil",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-chevron-right",
    "order_with_respect_to": [
        "project",
        "project.Project",
        "project.ProjectStatus",
        "project.ProjectPhase",
        "task",
        "task.Task",
        "task.TaskStatus",
        "part",
        "part.Part",
        "part.PartStatus",
        "material",
        "material.Material",
        "material.MaterialObject",
        "material.MaterialStatus",
        "material.Store",
        "material.WoodSpecies",
        "note",
        "note.Note",
        "adminstration",
    ],
    "changeform_format": "collapsible",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": True,
    "brand_colour": "navbar-teal",
    "accent": "accent-success",
    "navbar": "navbar-teal navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-teal",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "minty",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": False,
}
