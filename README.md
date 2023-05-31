# Sistem Data Jemaat GKIS

# How to Install

	install virtualenv package
	create environment
	pip install django
	git clone from github
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser
    python manage.py loaddata data_support/fixtures/data_support.json

	python manage.py loaddata Pendidikan
	python manage.py loaddata Profesi
	python manage.py loaddata Nob
	python manage.py loaddata Etnik
	python manage.py loaddata Wilayah
    python manage.py loaddata Pelayanan


# Git pull force
    git reset --hard HEAD
    git pull

# Load Data
	python manage.py loaddata Keluarga
	python manage.py loaddata Anggota

# Load Data Using script
	python manage.py shell < ./scripts/import_data_anggota.py