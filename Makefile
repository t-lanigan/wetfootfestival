IGNORE := $(shell bash -c "source setup.sh; env | sed 's/=/:=/' | sed 's/^/export /' > makeenv")                         
include makeenv 

DB_NAME := wetfootfestival

deps:
	pip3 install -r requirements.txt

run:
	FLASK_APP=app.py FLASK_ENV=development flask run

reset-db:
	dropdb $(DB_NAME) && createdb $(DB_NAME)
	flask db upgrade

start-db-server:
	pg_ctl -D /usr/local/var/postgres start

stop-db-server:
	pg_ctl -D /usr/local/var/postgres stop

connect-to-db:
	psql $(DB_NAME)

init-db:
	python manage.py db init

migrate-db:
	python manage.py db migrate

upgrade-db:
	python manage.py db upgrade

deploy:
	git push heroku master