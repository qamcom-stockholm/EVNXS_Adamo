producer    --->     RabbitMQ broker      ---> consumer

producer.py     RabbitMQ producer in Python
consumer.py     RabbitMQ consumer in Python
Dockerfile.consumer     Dockerfile for creating an image with Python client for RabbitMQ
Dockerfile.producer     Dockerfile for creating an image with Python client for RabbitMQ
build_all.sh            shell commands for building docker images (consumer, producer)
run_all.sh              shell commands for running all docker images (broker, consumer, producer)