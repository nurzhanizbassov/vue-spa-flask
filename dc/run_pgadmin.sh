#!/bin/bash
docker run --rm --name someapp-pgadmin -d -e 'PGADMIN_DEFAULT_EMAIL=admin@someapp.kz' -e 'PGADMIN_DEFAULT_PASSWORD=admin' -p 5050:80 -v $HOME/docker_volumes/someapp-pgadmin:/var/lib/pgadmin dpage/pgadmin4
