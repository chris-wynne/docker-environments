# Docker PostgresSQL Local Database Environment

This project sets up a local database environment with PostgreSQL using Docker. This database uses the Postgis extension for handling geospatial data.

## Prerequisites

1. Install Docker or Docker Desktop
2. Clone this repo to your local machine

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

## Connecting Other Docker Projects to This Database

To connect other Docker services to this database, you can include the local_db_network in your other Docker Compose files as an external network. For example:

```yaml
version: '3.8'
services:
  your-service:
    # Your service configuration
    networks:
      - local_db_network

networks:
  local_db_network:
    external: true
```

With this setup, your-service will be able to communicate with the database in the local_db_network.

# Additional Information

## Data Volume

The PostgreSQL data is persisted using a Docker volume named local-db-data.

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
