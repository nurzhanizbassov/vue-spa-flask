#!/bin/bash

# This scripts unsets the development environment: deactivates
# the python virtual environment, stops dockers containers
# for postgresql db, redis and pgadmin4.


# Deactivate virtualenv
deactivate
# Stop postgresql docker container
docker container stop somewebapp-postgres
# Stop pgadmin4 docker container
docker container stop somewebapp-pgadmin4
# Stop redis docker container
docker container stop somewebapp-redis
