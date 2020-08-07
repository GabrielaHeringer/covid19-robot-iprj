django-static:
	cd djangoapp && ./manage.py collectstatic

django-migrations:
	cd djangoapp && ./manage.py makemigrations

django-migrate:
	cd djangoapp && ./manage.py migrate

scrapy-run-diario:
        # roda de segunda a sabado 
	./spiders_diario.sh
	
scrapy-run-semanal:
	# roda todo domingo
	./spiders_semanal.sh

django-run:
	cd djangoapp && ./manage.py runserver
