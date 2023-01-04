run: 
	python manage.py runserver --settings=settings.local

run-prod: 
	python manage.py runserver --settings=settings.prod

migrate: 
	python manage.py migrate --settings=settings.prod

makemigrations: 
	python manage.py makemigrations --settings=settings.prod

