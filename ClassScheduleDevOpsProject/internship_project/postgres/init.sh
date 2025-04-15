#!/bin/bash
set -e

until pg_isready -U "$POSTGRES_USER"; do
  echo "Waiting for postgres..."
  sleep 1
done

echo "Restoring database from SQL dump..."
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /docker-entrypoint-initdb.d/class_schedule.dump

echo "✅ Database restored successfully!"
