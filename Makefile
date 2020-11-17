dev:
	python manage.py runserver 0.0.0.0:9999

migrate:
	python manage.py makemigration && python manage.py migrate

db:
	docker-compose up