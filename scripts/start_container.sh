#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull hamid1972/simple-python-flask-app:latest

# Run the Docker image as a container
docker run -d -p 5000:5000 hamid1972/simple-python-flask-app:latest
