run-server:
	python manage.py runserver

user:
	python manage.py createsuperuser --database=users_db

migrate:
	python manage.py makemigrations
	python manage.py migrate --database=users_db


translate:
	django-admin compilemessages --ignore=venv
	django-admin makemessages -l fa --ignore=venv


run-tests:
	python manage.py test --pattern="test_*.py" apps/tests --verbosity=1
