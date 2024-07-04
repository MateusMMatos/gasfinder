import dj_database_url
from pathlib import Path
import os
import django_heroku


# Configurações do Django
BASE_DIR = Path(__file__).resolve().parent.parent

# Mantendo o secret key seguro
SECRET_KEY = os.getenv('SECRET_KEY', '12d@#4030M')

# Definindo o modo DEBUG para produção
DEBUG = True

# Configurando os hosts permitidos
ALLOWED_HOSTS = ['gasfinderr-b2ff1682b63d.herokuapp.com', 'localhost', '127.0.0.1']

# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
]

# Middlewares configurados
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração do URL Conf
ROOT_URLCONF = 'gasfinder.urls'

# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates' / 'core'],
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

# Configuração do WSGI
WSGI_APPLICATION = 'gasfinder.wsgi.application'

# Configuração do banco de dados
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'GasFinder',
    'USER': 'mateus',
    'PASSWORD': '12d@#4030',
    'HOST': 'localhost',
    'PORT': '5432',
}
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurações de idioma e localização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configurações de arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Definição do campo auto increment padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuração para o Heroku
django_heroku.settings(locals())

# Handlers personalizados para erros
handler404 = 'core.views.custom_404'
handler500 = 'core.views.custom_500'
