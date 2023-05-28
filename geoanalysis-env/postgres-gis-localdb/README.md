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