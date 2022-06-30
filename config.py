import os


class Config(object):
    workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
    threads = int(os.environ.get('GUNICORN_THREADS', '1'))

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://bgqwlnlitcvzfh:0f6771392b7c3b7313eb522e48323a2b3ca1fa2700ed99755b5ef7b47c2c637f@ec2-54-211-255-161.compute-1.amazonaws.com:5432/d45siv70th8lb1')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_POOL_TIMEOUT = 30  # 30 seconds
    SQLALCHEMY_POOL_RECYCLE = 10  # max connection idle
    SQLALCHEMY_MAX_OVERFLOW = 50  # max in queue
    JSON_SORT_KEYS = False
    JWT_SECRET_KEY = "super-secret"