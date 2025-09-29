#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
IMAGE_NAME="localhost/xcloud-mcp"
TAG="latest"
CONTAINER_NAME="xcloud-mcp-server"
SERVICE_NAME="xcloud-mcp.service"
PROJECT_DIR="/path/to/your/project" # TODO: Update with the absolute path to the project on your server

# --- Deployment Steps ---

echo "Changing to project directory: $PROJECT_DIR"
cd $PROJECT_DIR

echo "Pulling latest changes from Git..."
git pull

echo "Building new container image: $IMAGE_NAME:$TAG"
podman build -t $IMAGE_NAME:$TAG .

echo "Restarting systemd service: $SERVICE_NAME"
sudo systemctl restart $SERVICE_NAME

echo "Deployment successful!"

# --- Optional: Clean up old images ---
echo "Cleaning up unused container images..."
podman image prune -f

echo "Done."
