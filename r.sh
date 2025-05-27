#!/bin/bash

clear
case $1 in
    dev)
        echo "Starting the service..."
        docker compose  down
        cat docker-compose.dev.yml > docker-compose.yml
        docker compose  up -d --build
        ;;
    prod)
        echo "Checking the service status..."
        docker compose  down
        cat docker-compose.prod.yml > docker-compose.yml
        docker compose  up -d --build
        ;;
    *)
        echo "Invalid command. enter r dev or r prod" 
        ;;
esac
