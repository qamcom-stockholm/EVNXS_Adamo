#!/usr/bin/env python
import pika, sys, os

rmqhost='rmq_host'
port = 5672
user_name = 'guest'
password = 'guest'
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