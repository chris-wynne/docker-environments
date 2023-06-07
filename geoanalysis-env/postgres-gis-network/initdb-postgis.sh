#!/bin/sh
# initdb-postgis.sh

echo "Running initdb-postgis.sh..."

set -e

# Load PostGIS into the database
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  echo "Creating PostGIS and PostGIS_Topology extensions..."
  CREATE EXTENSION IF NOT EXISTS postgis;
  CREATE EXTENSION IF NOT EXISTS postgis_topology;
EOSQL

echo "Finished running initdb-postgis.sh."