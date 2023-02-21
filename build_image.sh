#!/bin/sh

if [[ $(uname -m) == *"arm"* ]]; then
  BUILD_PLATFORM="--platform linux/amd64"
fi

docker build $BUILD_PLATFORM -t python-api .

echo "cleaning up old docker images..."
docker system prune -f
