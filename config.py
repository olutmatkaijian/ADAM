import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    broker_url = 'amqp://guest@localhost'
