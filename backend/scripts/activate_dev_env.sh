#!/bin/bash

# This script sets development environment: activates python virtual environment,
# launches docker containers for postgresql db, redis and pgadmin4. 

# It can also open up one additional terminal for the python backend
# with python virtualenv activated, one terminal for redis output 
# and two terminals for the frontend part with the required nodejs activated. 
# Currently the opening of terminals works for XFCE Desktop Environment only and
# if you indicate absolute path to tour project directory in 
# the corresponding lines below. 
# The lines for opening the terminals are currently commented out.
# Opening the terminals might help if you use an editor like vim 
# and need to open several terminals with required directories and
# everything activated at once.

# Activate virtualenv

# Check if directory exists since it is used for activating python virtualenv
VENV_DIR="${BASH_SOURCE[0]%/*}/../venv"
# VENV_DIR="$HOME/github/private/vue-spa-flask/backend/venv"
if [ ! -d "$VENV_DIR" ]; then
  # mkdir -p $HOME/github/private/vue-spa-flask/backend/venv
  mkdir -p ${BASH_SOURCE[0]%/*}/../venv
  virtualenv -p python3 ${BASH_SOURCE[0]%/*}/../venv
fi

. venv/bin/activate

pip install -r requirements.txt

# Check if directory exists since it is used for saving state of the container
POSTGRES_DIR="$HOME/docker/volumes/postgres/"
if [ ! -d "$POSTGRES_DIR" ]; then
  mkdir -p $HOME/docker/volumes/postgres
fi

# Run then postgresql docker container
docker container run --rm --name somewebapp-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data -d postgres

# Check if directory exists since it is used for saving state of the container
PGADMIN_DIR="$HOME/docker/volumes/pgadmin4/"
if [ ! -d "$PGADMIN_DIR" ]; then
  mkdir -p $HOME/docker/volumes/pgadmin4
  chmod -R 777 $HOME/docker/volumes/pgadmin4
fi

# Run the pgadmin4 docker container
docker container run --rm --name somewebapp-pgadmin4 -e PGADMIN_DEFAULT_EMAIL='admin@somewebapp.kz' -e PGADMIN_DEFAULT_PASSWORD='admin' -p 80:80 -v $HOME/docker/volumes/pgadmin4:/var/lib/pgadmin -d dpage/pgadmin4

# Run the redis docker container
docker container run --rm --name somewebapp-redis -p 6379:6379 -d redis

# Uncomment the lines below and put absolute path 
# to your project if you need to open up 4 other terminals. 
# One for the backend, one for redis output 
# and two for the frontend.

# if [ "$XDG_CURRENT_DESKTOP" == "XFCE" ]; then
# 
#   xfce4-terminal --working-directory=$HOME/github/private/vue-spa-flask/backend --maximize \
#   -e 'bash -c "source $HOME/github/private/vue-spa-flask/backend/venv/bin/activate; bash"'
#   xfce4-terminal --working-directory=$HOME/github/private/vue-spa-flask/backend --maximize \
#   -e 'bash -c "source $HOME/github/private/vue-spa-flask/backend/scripts/utils/run_redis.sh; bash"'
#   xfce4-terminal --working-directory=$HOME/github/private/vue-spa-flask/frontend \
#   --maximize -e 'bash -c "source $HOME/github/private/vue-spa-flask/backend/scripts/utils/run_nvm.sh; bash"'
#   xfce4-terminal --working-directory=$HOME/github/private/vue-spa-flask/frontend \
#   --maximize -e 'bash -c "source $HOME/github/private/vue-spa-flask/backend/scripts/utils/run_nvm.sh; bash"'
# 
# else
#   echo "XFCE Desktop Environment has not been found. 
#         Add your Desktop Environment to the activate_dev_env.sh script
#         located in the vue-spa-flask/backend/scripts directory"
# fi
