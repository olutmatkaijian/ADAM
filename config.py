import os

ADAM_PSK = "dev1234"


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    broker_url = 'amqp://guest@localhost'
