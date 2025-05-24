#!/bin/bash

clear
case $1 in
    dev)
      
        echo "Starting the service..."
        
        cat docker-compose.dev.yml > docker-compose.yml
        docker compose  up -d --build
        ;;
    prod)
        echo "Checking the service status..."
        # Place your status command here, e.g., docker-compose ps
        ;;
    *)
        echo "Invalid command. enter r dev or r prod" 
        ;;
esac
