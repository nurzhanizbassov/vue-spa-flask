-- The script is run by postgres user

CREATE USER swa WITH
	PASSWORD 'swa';

CREATE DATABASE somewebapp WITH
    OWNER = swa
    ENCODING = 'UTF8';
