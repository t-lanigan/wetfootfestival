IGNORE := $(shell bash -c "source setup.sh; env | sed 's/=/:=/' | sed 's/^/export /' > makeenv")                         
include makeenv 

DB_NAME := wetfootfestival

deps:
	pip3 install -r requirements.txt

run:
	FLASK_APP=app.py FLASK_ENV=development flask run

reset-db:
	dropdb $(DB_NAME) && createdb $(DB_NAME)
	python3 manage.py db upgrade
	python3 add_fake_data.py

start-db-server:
	pg_ctl -D /usr/local/var/postgres start

stop-db-server:
	pg_ctl -D /usr/local/var/postgres stop

connect-to-db:
	psql $(DB_NAME)

init-db:
	python3 manage.py db init

migrate-db:
	python3 manage.py db migrate

upgrade-db:
	python3 manage.py db upgrade

deploy:
	git push heroku master

add-fake-data:
	python3 add_fake_data.py