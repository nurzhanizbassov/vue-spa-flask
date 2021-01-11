-- The script is run by postgres user
DROP DATABASE someapp;
DROP USER someapp;

CREATE USER someapp WITH
	PASSWORD 'someapp';

CREATE DATABASE someapp WITH
    OWNER = someapp
    ENCODING = 'UTF8';
