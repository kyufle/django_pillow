"""
Django settings for mysite project.
"""

from pathlib import Path
import os
import environ

# 1. Configuración de Rutas
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Inicializar environ con valores por defecto de seguridad
env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, 'django-insecure-fallback-key-12345'),
)

# 3. Lógica de búsqueda del archivo .env
# Intentamos buscarlo en BASE_DIR (minibiblio) o en el padre (django_pillow)
env_file = os.path.join(BASE_DIR, '.env')
if not os.path.exists(env_file):
    env_file = os.path.join(BASE_DIR.parent, '.env')

# Cargar el archivo si existe
if os.path.exists(env_file):
    environ.Env.read_env(env_file)

# 4. Asignación de variables (ahora con defaults para evitar el KeyError)
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=['*'])

# 5. Configuración de Usuario
AUTH_USER_MODEL = 'minibiblio.Usuari'

# 6. Aplicaciones
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

# 7. Middleware
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# 8. Base de Datos
# Si env.db() falla porque no hay DATABASE_URL, usamos un sqlite local por defecto
DATABASES = {
    'default': env.db(default=f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}')
}

# 9. Validadores y Localización
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 10. Estáticos y Media
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 11. CORS
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
])