# Docker PostgresSQL Local Database Environment

This project sets up a local database environment with PostgreSQL using Docker. This database uses the Postgis extension for handling geospatial data.

## Prerequisites

1. Install Docker or Docker Desktop
2. Clone this repo to your local machine

## Services

1. db (PostgreSQL): A PostgreSQL database with the PostGIS extension. Accessible on port 5432.
2. app (Python Application): A Python application service with data analysis packages such as pandas, geopandas, folium, geojson, and openpyxl installed. Accessible on port 5000.
3. portainer (Docker Monitoring): Portainer service for managing and monitoring Docker services. Accessible on port 9000.

# Setup

## User & Password

Create a .env file in the root directory of the project (this is where the docker-compose.yml file is). This file will contain the environment variables for your PostgreSQL database. Here's what you need to include:

```dotenv
POSTGRES_USER=db-admin
POSTGRES_PASSWORD=admin-pass
```

Replace db-admin and admin-pass with the username and password you want to use for your PostgreSQL database. Note: For security reasons, don't commit this file to your repository.

## Running Containers

To build the image run:

```bash
docker compose build
```

To run the container run:

```bash
docker compose up -d
```

## Stopping the Containers

When you're done, you can stop the containers by running:

```bash
docker-compose down
```

This will stop and remove the containers. The data in your PostgreSQL database will persist between runs thanks to Docker volumes.

# Additional Information

## Connect to the container

### Option 1: VS Code

Click the blue icon in the bottom left of VS Code. Select "Attach to Running Container".

### Option 2: Interactive bash session

```(bash)
docker-compose run --rm app bash
```

Replace bash with sh if your container uses sh instead.

## Data Volume

The PostgreSQL data is persisted using a Docker volume named geospatial-data. The Python application can access data files from the local ./datafiles directory, which is mounted as /app/datafiles in the Docker container.

## Monitoring with Portainer

This setup also includes Portainer for monitoring your Docker environment. Once the containers are running, you can access the Portainer UI at http://localhost:9000.

## initdb-postgis.sh

This script is run automatically after the database is initialized but before it is started. The script uses psql to connect to the database and runs SQL commands to create the PostGIS and PostGIS_topology extensions if they do not already exist.

## Backing up your PostgresSQL Database in Docker

This section describes how you can create a backup of your PostgreSQL database running inside a Docker container using the pg_dump tool.

1. Run the following command in your terminal to display a list of all running Docker containers. Note the ID of your Docker container running PostgreSQL. 

```bash
docker ps
```

2. Next, execute the pg_dump command in the Docker container to create a backup of your PostgreSQL database. Make sure to replace YOUR_CONTAINER_ID_OR_NAME with your actual Docker container ID or name, and YOUR_DATABASE_NAME with the name of your database. This command will create a backup of your PostgreSQL database and write it to backup.sql on your local machine.

```bash
docker exec YOUR_CONTAINER_ID_OR_NAME pg_dump -U postgres YOUR_DATABASE_NAME > backup.sql
```

3. If your PostgreSQL database requires a password, you can supply it by using the PGPASSWORD environment variable as follows:

```bash
docker exec -e PGPASSWORD=your_password YOUR_CONTAINER_ID_OR_NAME pg_dump -U postgres YOUR_DATABASE_NAME > backup.sql
```

4. Finally, verify that the backup was successful. You can do this by viewing the contents of the backup.sql file. Use any text editor to open the file, or you can even try to restore it into a new database to check its validity.
