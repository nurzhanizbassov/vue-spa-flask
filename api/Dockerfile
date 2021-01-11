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

# Config without hot reload 
# FROM maven:3.6.0-jdk-11-slim as build

# WORKDIR /eokno-api
# COPY pom.xml .
# RUN mvn verify --fail-never
# COPY ./src src
# RUN mvn clean verify

# FROM openjdk:11-slim
# WORKDIR /eokno-api
# COPY --from=build /eokno-api/target/eokno-api.jar eokno-api.jar
# ENTRYPOINT ["java","-Djava.security.egd=image:/dev/./urandom", "-Dspring.profiles.active=docker", "-jar", "/eokno-api/eokno-api.jar"]
