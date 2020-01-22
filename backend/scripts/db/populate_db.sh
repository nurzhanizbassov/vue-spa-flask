#!/bin/bash

# This script is needed to dropping, creating and populating the dev db.

rm -rf ./migrations/
psql "postgresql://postgres:postgres@localhost/postgres" -f scripts/db/drop_db_and_user.sql
psql "postgresql://postgres:postgres@localhost/postgres" -f scripts/db/create_user_and_db.sql
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py insert_data
