import pika
from settings import Settings


class RabbitMQConsumer:
    def __init__(self, callback):
        self.__host = Settings.rabbit_host
        self.__port = Settings.rabbit_port
        self.__username = Settings.rabbit_user
        self.__password = Settings.rabbit_pasword
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(username=self.__username, password=self.__password)
        )

        channel = pika.BlockingConnection(connection_parameters).channel()

        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )

        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        )

        return channel
    
    def start(self):
        print('Listen RabbitMQ on Port 5672')
        self.__channel.start_consuming()

def callback(ch,method,properties,body):
    print(body)


rabbitmq_consumer = RabbitMQConsumer(callback=callback)
rabbitmq_consumer.start()