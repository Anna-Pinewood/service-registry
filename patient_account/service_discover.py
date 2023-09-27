import logging
import os
import random
import socket
from itertools import cycle

from flask import request

import patient_account.db_redis as db_redis
from patient_account.consts import SERVICE_HOST, SERVICE_PORT
import patient_account.load_balancing as load_balancing
from utils import get_logger

logger = get_logger(logger_name=__name__,
                    level=logging.INFO)


def discover(service_name: str):
    def wrapped_discover():
        replicas_pool = []
        logger.info('Service name: %s', service_name)
        service_replicas: list = db_redis.redis_connection.lrange(
            service_name, 0, -1)
        for replica in service_replicas:
            host, port = db_redis.redis_connection.hmget(
                replica, keys=['host', 'port'])
            if (host is None) and (port is None):
                # Реплика недоступна
                db_redis.redis_connection.lrem(
                    service_name, count=0, value=replica)
                continue
            elif (host is not None) and (port is not None):
                # Реплика доступна. Добавим его в пул
                replicas_pool.append(tuple([replica, host, port]))
            else:
                raise RuntimeError
        load_balancing.replicas_pool = cycle(replicas_pool)
        logger.info('Replicas pool: %s', str(replicas_pool))
    return wrapped_discover


def register(service_name: str):
    redis_client = db_redis.redis_connection
    replica_random_number = random.randint(1, 100)
    replica_name = f"replica_{replica_random_number}"

    while replica_name in redis_client.lrange(service_name, 0, -1):
        replica_random_number = random.randint(1, 100)
        replica_name = f"replica_{replica_random_number}"

    logger.info('Replica_name: %s', replica_name)

    host, port = get_host_ip()

    redis_client.lpush(service_name, replica_name)
    redis_client.hset(replica_name, "host", host)
    redis_client.hset(replica_name, "port", port)


# def get_host_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(('8.8.8.8', 53))
#     host_ip, host_port = s.getsockname()
#     s.close()
#     return host_ip, host_port

def get_host_ip():
    return SERVICE_HOST, SERVICE_PORT
