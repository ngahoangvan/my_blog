#!/bin/bash

docker-compose -f docker-compose.db.yml up -d --force-recreate db
