#!/bin/bash
docker rm -f safesteval
docker build -t safesteval .
docker run --name=safesteval --rm -p3333:3333 -it safesteval

