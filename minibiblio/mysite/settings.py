import os
from pathlib import Path
import environ

# 1. Rutas Base y Variables de Entorno
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, True), SECRET_KEY=(str, 'fallback-key'))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# 2. Seguridad
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['rromerocarretero3.ieti.site', 'localhost', '127.0.0.1']

# --- CONFIGURACIÓN CRÍTICA PARA HTTPS/PROXY IETI ---
CSRF_TRUSTED_ORIGINS = ['https://rromerocarretero3.ieti.site']
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# --- AÑADIDO PARA SEGURIDAD DE COOKIES EN HTTPS ---
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# --------------------------------------------------

# 3. Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'minibiblio.apps.MinibiblioConfig',
]

# 4. Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 5. URLs y Plantillas
ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# 6. Base de Datos (Forzamos SQLite para evitar errores de MySQL)
DATABASES = {
    'default': env.db(),
}

# 7. Modelo de Usuario Personalizado
AUTH_USER_MODEL = 'minibiblio.Usuari'

# 8. Archivos Estáticos y Media
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 9. Configuración de CORS
CORS_ALLOW_ALL_ORIGINS = True 
# --- AÑADIDO PARA PERMITIR PETICIONES DESDE EL FRONT ---
CORS_ALLOW_CREDENTIALS = True
# ------------------------------------------------------

# 10. Internacionalización
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# nano ~/django_pillow/minibiblio/mysite/settings.py
# Al final de settings.py
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Esto es lo que evita que Django se pierda con los Alias de Apache
FORCE_SCRIPT_NAME = None
