# Dockerfile
FROM postgres:13

# Add PostGIS extension
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-13-postgis-3 \
    && rm -rf /var/lib/apt/lists/*

# Initialize the database with PostGIS extension
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/initdb-postgis.sh