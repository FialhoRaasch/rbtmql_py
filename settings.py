from decouple import config

class Settings:
    rabbit_host = config("RABBITMQ_DEFAULT_HOST")
    rabbit_port = int(config("RABBITMQ_DEFAULT_PORT"))
    rabbit_user = config("RABBITMQ_DEFAULT_USER")
    rabbit_pasword = config("RABBITMQ_DEFAULT_PASS")