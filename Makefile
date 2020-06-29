IGNORE := $(shell bash -c "source setup.sh; env | sed 's/=/:=/' | sed 's/^/export /' > makeenv")                         
include makeenv 

DB_NAME := wetfootfestival

deps:
	pip3 install -r requirements.txt

test:
	python test_app.py

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

add-volunteer:
	curl --header "Content-Type: application/json" \
	--request POST \
	--data '{"name":"xyz","phone_number":"xyz", "email":"12345", "event":"1"}' \
	http://localhost:5000/volunteers

patch-volunteer:
	curl --header "Content-Type: application/json" \
	--request PATCH \
	--data '{"name":"patch-xyz"}' \
	http://localhost:5000/volunteers/1

delete-volunteer:
	curl --request DELETE http://localhost:5000/volunteers/1