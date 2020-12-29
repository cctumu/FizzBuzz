#!/bin/bash

docker ps -aq --no-trunc | xargs docker rm
docker rmi "$(docker images -f "dangling=true" -q)"

