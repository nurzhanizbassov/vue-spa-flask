#!/bin/bash

# This script populates the dev db with test data.

rm -rf ./migrations/
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py insert_data
