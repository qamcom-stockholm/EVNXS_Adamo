import pika

# Step #3
def on_open(connection):
    connection.channel(on_open_callback=on_channel_open)

# Step #4
def on_channel_open(channel):
    channel.basic_publish('exchange_name',
                          'routing_key',
                          'Test Message',
                          pika.BasicProperties(content_type='text/plain',
                                               type='example'))

# Step #1: Connect to RabbitMQ
connection = pika.SelectConnection(on_open_callback=on_open)

try:
    # Step #2 - Block on the IOLoop
    connection.ioloop.start()

# Catch a Keyboard Interrupt to make sure that the connection is closed cleanly
except KeyboardInterrupt:

    # Gracefully close the connection
    connection.close()

    # Start the IOLoop again so Pika can communicate, it will stop on its own when the connection is closed
    connection.ioloop.start()