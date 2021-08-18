# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)3cjyh5)7ppsm%%e8pm(%0l1$z&yiy=#_!%3@t3yz%l7mg*e!@'

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
