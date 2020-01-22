#!/bin/bash
source $HOME/github/private/vue-spa-flask/backend/venv/bin/activate
# source ../../backend/venv/bin/activate
rq worker
