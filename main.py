import logging

from flask import Flask

import consts
from consts import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT, URL_SECRET_NUMBER
from patient_account import init_redis_connection, init_scheduler, views
from patient_account.service_discover import register
from utils import get_logger

app = Flask(__name__)


logger = get_logger(__name__,
                    level=logging.INFO)

if __name__ == "__main__":
    init_redis_connection(host=REDIS_HOST,
                          port=REDIS_PORT,
                          password=REDIS_PASSWORD)
    service_name = "web_app"
    scheduler = init_scheduler(service_name=service_name)
    scheduler.init_app(app)
    scheduler.start()

    app.register_blueprint(views.bp)
    logger.info(' Getting secret number...')
    secret_number = views.fetch_secret_number(
        source=URL_SECRET_NUMBER)
    logger.info('Got secret number %s', secret_number)
    consts.SECRET_NUMBER = secret_number
    if secret_number is not None:
        app.run()
        register(service_name)
