#!/usr/bin/env python
import pika, sys, os
# import socket
# import docker

# client = docker.from_env()
# network_name = "rmq_network"
# atp_container = client.containers.get(socket.gethostname())
# client.networks.get(network_name).connect(container=atp_container.id)

rmqhost='rmq_host'
port = 5672
user_name = 'qamcom'
password = 'abc123'
queue_name = 'hello'
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host= rmqhost,port= port, virtual_host='/', credentials=pika.PlainCredentials(user_name, password)))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)