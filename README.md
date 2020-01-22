vue-spa-flask

------------------------------------------------------------------------------

The project consists of a backend written in Flask (Python3)
and a frontend (VueJS, SPA). It is intended to ease starting your 
own web development project.

The project was created thanks to these sources: 

https://stackabuse.com/single-page-apps-with-vue-js-and-flask-setting-up-vue-js/

https://codepen.io/roman-koptev/pen/OoGgBz

Python: 3.6.9
Vue: 2.6.11
Vuex: 3.1.2
Vue-router: 3.1.3
Buefy: 0.8.9
PostgreSQL: 12.1 
redis: 1.2.0
etc.

------------------------------------------------------------------------------

Frontend:

1. Install nvm. See the official documentation on how to do that.

2. Using nvm set the node version to 10.*:

    nvm use node 10.*

    Note: if you update and then source the backend/scripts/activate_dev_env.sh script
    then required version of node will already be activated.

3. cd into somewebapp/frontend and run:

    npm install

4. Run the frontend spa:

    npm run dev

------------------------------------------------------------------------------

Backend:

1. cd into backend and run the following:

    . scripts/activate_dev_env.sh

    The script will:

      1. Activate virtualenv.
      2. Install all requirements.

         Note: If you have problems installing psycopg2, then it is quite likely that
         you are missing libpq-dev library (on Linux). Install in rou system
         separately using your package manager.

      3. Run docker containers for postgresql (localhost:5432), pgadmin4 (localhost:80) 
      and redis (localhost:6379) for  queueing tasks. If there are no docker images, it will pull them
      automatically from the docker hub.
      4. Create directories in $HOME for keeping the state of the docker containers.
      5. If you use xfce4 you can uncomment the corresponding lines (you will see them) 
        and insert absolute path to your project directory 
        in the backend/scripts/activate_dev_env.sh script
        for automatically openning up 4 other terminals:
      
         1. For launching backend server:
            
                python appserver.py (virtualenv already activated)
         
         2. Running and showing output of redis.
         3. For opening editor (vim in my case) inside of the frontend
         directory with the required nodejs activated
         4. Launching the frontend:
            npm run dev (required nodejs already activated).
         
        Otherwise update the backend/scripts/activate_dev_env.sh script
        for your desktop environment (Gnome, KDE etc) or 
        open the terminals and run the required services manually.

    Note:

    If you decide to run the services manually you need to run:

        . backend/scripts/utils/run_redis.sh (with python virtualenv activated)

    Then in another terminal:

        cd frontend
        nvm use 10.* (10.16.3 in my case, if your default node is different)

    And then launch frontend spa as usually:

        npm run dev

2.   To deactivate virtualenv and stop the docker containers run:

        . scripts/deactivate_dev_env.sh

3. To populate db run:

    ./populate_db.sh

    Note: This script will drop the database somewebapp and user swa 
    and then recreate them again. Afterwars tables will be created
    according to the backend/somewebapp_api/models.py (this is why
    this script can only be run after sourcing activate_dev_env.sh).
    Then it populates the DB somewebapp with initial data.

4. When you make changes to the models run migrations:

    python manage.py db migrate
    python manage.py db upgrade

------------------------------------------------------------------------------

Testing:

    Backend:
        1. All tests are located in the test directory.
        2. In order to launch tests inside of the backend/test directory
        having activated virtualenv and launched application server run:
            
            python -m unittest

    Frontend:

        Unit tests:

            npm run unit 

            Note: Currently the only unit test fails because a key 'app_title" gets
            returned instead of text 'Some Web App'.

        e2e tests:

            npm run e2e

        All tests:

            npm test
