#!/bin/sh

echo "Database host: ${DATABASE_HOST}"

postgres_ready() {
python << END
import sys
import os
import psycopg2
try:
    conn = psycopg2.connect(
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"))

except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 2
done

pytest tests --cov --cov-report=xml --cov-report=term
