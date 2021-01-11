1. Install ```docker, docker-compose```.
2. cd into the 'dc' directory.
3. Run:
    ```
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
    ```

4. In the api directory create virtual environment:

    ```
    virtualenv -p python3 venv
    ```

5. Activate the virtual environment:

    ```
    [Windows]   . venv/bin/activate
    [Unix]     source venv/bin/activate
    ```

6. Install requirements locally:

    ```
    ~/eksk/api pip install -r requirements.txt
    ```

7. In order to create user and database 'someapp' run:

    ```
    psql -h localhost -U postgres -f api/scripts/db/init_db.sql
    ```
8. In order to populate database with test data run:

    ```
    cd dc

    docker-compose -f docker-compose.yml -f docker-compose.dev.yml exec someapp-api bash

    ./scripts/db/populate_db.sh
    ```

9. Set up db for running tests:

    ```
    psql -h localhost -U postgres -p 5433 -f api/scripts/db/init_db.sql
    ```

10. Run the tests:

    ```
    cd dc

    docker-compose -f docker-compose.yml -f docker-compose.dev.yml exec someapp-api bash

    python manage.py test
    ```

11. Access
    ```
    frontend    localhost:8088
    backend     localhost:5000
    database    localhost:5432
    ```

