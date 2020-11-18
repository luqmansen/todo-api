dev:
	python manage.py runserver 0.0.0.0:9999

migrate:
	python manage.py makemigration && python manage.py migrate

db:
	docker-compose

guni:
	SECRET_KEY=123 gunicorn todo_api.wsgi -c gunicorn.conf.py --log-file -