release: python manage.py migrate --no-input
web: gunicorn todo_api.wsgi -c gunicorn.conf.py --log-file -
