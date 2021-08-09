# Config with hot reload
FROM python:3.9.0-slim-buster

WORKDIR /api

COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# COPY manage.py ./
# COPY appserver.py ./
# COPY someapp.py ./
COPY *.py ./
COPY scripts ./
COPY app ./
COPY manage.py ./

# ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/somewebapp_api/"
# CMD python someapp.py
# CMD python appserver.py
CMD python manage.py run
# CMD ./scripts/db/populate_db.sh

# ENTRYPOINT [ "python" ]
# CMD [ "appserver.py" ]
