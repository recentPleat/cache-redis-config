import redis
import logging

class RedisConfig:
    def __init__(self, host, port, password, db):
        self.host = host
        self.port = port
        self.password = password
        self.db = db

    def get_redis_connection(self):
        try:
            return redis.Redis(
                host=self.host,
                port=self.port,
                password=self.password,
                db=self.db
            )
        except redis.ConnectionError as e:
            logging.error(f"Failed to connect to Redis: {e}")
            return None

def get_config_from_env():
    host = os.environ.get('REDIS_HOST')
    port = os.environ.get('REDIS_PORT')
    password = os.environ.get('REDIS_PASSWORD')
    db = os.environ.get('REDIS_DB')

    if not all([host, port, password, db]):
        raise ValueError("Missing required environment variables")

    return RedisConfig(host, int(port), password, int(db))

import os