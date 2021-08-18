# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3)vy^86nc+6tisju+s--=k+0kz(z!lsrb9gwff1hbpz4*oli7)'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone_database',
        'USER': 'root',
        'PASSWORD': 'MySQLPassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
