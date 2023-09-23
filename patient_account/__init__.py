
import logging

import db_redis
import redis

from utils import get_logger

logger = get_logger(__name__,
                    level=logging.INFO,
                    add_stdout=True)


def init_redis_connection(host: str,
                          port: str,
                          password: None | str = None):
    if db_redis.redis_connection is None:
        db_redis.redis_connection = redis.Redis(host=host,
                                                port=port,
                                                password=password,
                                                decode_responses=True)
        logger.info('Connection to redis established.')
    return db_redis.redis_connection
