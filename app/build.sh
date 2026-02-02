#!/bin/bash
set -e

# Default configuration - can be overridden by env vars
# Example: REGISTRY=ghcr.io/myuser ./build.sh v1.0.1
REGISTRY="${REGISTRY:-docker.io/devlopesbernardo}"
IMAGE_NAME="${IMAGE_NAME:-version-demo}"
TAG="${1:-latest}"

FULL_IMAGE="${REGISTRY}/${IMAGE_NAME}:${TAG}"

echo "🚀 Starting build process..."
echo "📦 Image: ${FULL_IMAGE}"

# Build the image
echo "🔨 Building Docker image..."
docker build -t "${FULL_IMAGE}" app/

# Push the image
echo "⬆️  Pushing to registry..."
# Note: Ensure you are logged in to the registry first (docker login)
docker push "${FULL_IMAGE}"

echo "✅ Successfully built and pushed: ${FULL_IMAGE}"