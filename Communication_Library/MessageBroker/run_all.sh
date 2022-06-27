#!/bin/bash
network_name=rmq_net  
host_name=rmq_host
user_name=guest
password=guest

docker network create $network_name
docker run -d --hostname $host_name --name $host_name -p 15672:15672 -p 5672:5672 --network $network_name \
            -e RABBITMQ_DEFAULT_USER=$user_name \
            -e RABBITMQ_DEFAULT_PASS=$password rabbitmq:3-management
docker run -it --network $network_name consumer
#docker run -it --network $network_name producer
