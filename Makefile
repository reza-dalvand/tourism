run-server:
	python manage.py runserver

user:
	python manage.py createsuperuser --database=custom_db

check:
	python manage.py check

migrate:
	python manage.py makemigrations
	python manage.py migrate --database=custom_db


translate:
	django-admin compilemessages --ignore=venv
	django-admin makemessages -l fa --ignore=venv


tests:
	pytest -s apps/tests --verbosity=1
