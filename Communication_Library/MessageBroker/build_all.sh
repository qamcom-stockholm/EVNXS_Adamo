#!/bin/bash
docker build --pull --rm -f "Dockerfile.consumer" -t consumer .
docker build --pull --rm -f "Dockerfile.producer" -t producer .
