from typing import Any
import jsonpickle
import pika
from pika import channel
from configuration import configuration

configs: Any = configuration.get_configs()


class Publisher:
    @staticmethod
    def publish(routing_key, message):
        global configs
        connection = Publisher.__create_connection()
        # Create a new channel with the next available channel number or pass in a channel number to use channel =
        connection.channel()
        # Creates an exchange if it does not already exist, and if the exchange exists,
        # verifies that it is of the correct and expected class.
        channel.exchange_declare(exchange=configs['rabbit']['exchange'], exchange_type='topic')
        # Publishes message to the exchange with the given routing key
        channel.basic_publish(exchange=configs['rabbit']['exchange'], routing_key=routing_key,
                              body=jsonpickle.encode(message))
        # Create new connection
        # print("[x] Sent message %r for %r" % (message,routing_key))

    @staticmethod
    def __create_connection():
        global configs
        param = pika.ConnectionParameters(host=configs['rabbit']['host'], port=int(configs['rabbit']['port']))
        return pika.BlockingConnection(param)
