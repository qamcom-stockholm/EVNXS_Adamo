#!/usr/bin/env python
import pika

# import docker
# import socket
# client = docker.from_env()
# network_name = "rmq_network"
# atp_container = client.containers.get(socket.gethostname())
# client.networks.get(network_name).connect(container=atp_container.id)

rmqhost='rmq_host'
port = 5672
user_name = 'qamcom'
password = 'abc123'
queue_name = 'hello'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host= rmqhost, port=port  , virtual_host='/', credentials=pika.PlainCredentials(user_name, password)))
channel = connection.channel()

channel.queue_declare(queue=queue_name)

channel.basic_publish(exchange='', routing_key=queue_name, body='Hello World! again and again')
print(" [x] Sent 'Hello World!'")
connection.close()