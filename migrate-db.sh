#!/bin/bash

clear

# Kiểm tra và xử lý thư mục migrations
if docker-compose exec flask-backend [ -d "migrations" ]; then
    echo "Folder 'migrations' exists. Removing it..."
    docker-compose exec flask-backend rm -rf migrations
fi

echo "Initializing database migrations..."
docker-compose exec flask-backend flask db init

# Tiến hành migration và upgrade
docker-compose exec flask-backend flask db migrate -m "Initial migration"
docker-compose exec flask-backend flask db upgrade
