
import logging

import db_redis
import redis
from flask_apscheduler import APScheduler

import service_discover
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


def init_scheduler(service_name: str):
    discover_func = service_discover.discover(service_name=service_name)
    discover_func.__call__()
    scheduler = APScheduler()
    scheduler.add_job(id=service_name+'_discover',
                      func=service_discover.discover(
                          service_name=service_name),
                      trigger='interval',
                      seconds=10)
    return scheduler
