# Geospatial Development Environment

## Running Database

To connect to the database, use the following credentials:

```
Host: localhost \
Port: 5432 \
Database: \
User:  \
Password: 
```

## Set up

Below are the details of what each set up file is doing.

### geo-postgres.Dockerfile

This file is used by Docker to create an image for your PostgreSQL container with PostGIS extension.

### docker-compose.yml

Docker Compose is a tool for defining and running multi-container Docker applications. It uses YAML files to configure the application's services.

### initdb-postgis.sh

This script is run after the database is initialized but before it is started. The script uses psql to connect to the database and runs SQL commands to create the PostGIS and PostGIS_topology extensions if they do not already exist.

## Editing the shell script

The "initdb-postgis.sh" script has been designed to run on unix-like systems. If you edit it in windows you will need to convert the files format with this command in bash:

```bash
dos2unix initdb-postgis.sh
```
