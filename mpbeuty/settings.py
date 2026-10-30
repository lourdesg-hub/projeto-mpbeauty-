
"""
Django settings for mpbeuty project.
"""

from pathlib import Path

# Caminho principal do projeto
BASE_DIR = Path(__file__).resolve().parent.parent


# Segurança
SECRET_KEY = 'django-insecure-5@kirln+wt-p64qzqz63ilvzzfq(&6l3g4gmj14*d4$j1iyhhc'

DEBUG = True

ALLOWED_HOSTS = []


# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'beauty',
]


# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URLs principais
ROOT_URLCONF = 'mpbeuty.urls'


# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'beauty' / 'templates'],
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


WSGI_APPLICATION = 'mpbeuty.wsgi.application'


# Banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Idioma e fuso horário
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_TZ = True


# Arquivos estáticos (CSS, JavaScript e imagens)
STATIC_URL = '/static/'


# Configurações de login e logout
LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'inicio'

LOGOUT_REDIRECT_URL = 'inicio'


# Chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
