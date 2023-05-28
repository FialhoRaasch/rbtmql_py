import json
from typing import Dict

from settings import Settings

import pika


class RabbitMQPublisher:
    def __init__(self):
        self.__host = Settings.rabbit_host
        self.__port = Settings.rabbit_port
        self.__username = Settings.rabbit_user
        self.__password = Settings.rabbit_pasword
        self.__exchange = "data_exchange" 
        self.__routing_key = ""
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(username=self.__username, password=self.__password)
        )

        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel
    
    def send_message(self, body:Dict):
        self.__channel.basic_publish(
            exchange = self.__exchange,
            routing_key = self.__routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )


name = ""

def send():
    message = str(input("mensagem: "))
    rabbitmq_publisher = RabbitMQPublisher()
    rabbitmq_publisher.send_message({name: message})

value = True

while value == True:
    if name == "":
        name = str(input("Nome: "))
    send()