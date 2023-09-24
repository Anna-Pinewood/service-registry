import logging
from flask import Blueprint, jsonify
import requests
import time
from utils import get_logger

from consts import URL_SECRET_NUMBER

logger = get_logger(__name__,
                    level=logging.INFO,
                    add_stdout=True)

bp = Blueprint(name='patient',
               url_prefix='/',
               import_name=__name__)


def fetch_secret_number(source: str):
    max_retries = 30  # Максимальное количество попыток
    retry_delay = 5  # Задержка между попытками (в секундах)
    timeout = 120  # Таймаут запроса (в секундах)

    secret_number = None
    for i in range(max_retries):
        try:
            response = requests.get(source, timeout=timeout)
            if response.status_code == 200:
                secret_number = response.json().get('secret_number', None)
                return secret_number
        except requests.RequestException:
            pass  # Проигнорировать исключение и повторить попытку

        logger.info('Attempt %s: %s', str(i), response.text)
        time.sleep(retry_delay)

    return secret_number


@bp.route('/return_secret_number')
def secret_number_handler():
    secret_number = fetch_secret_number(
        source=URL_SECRET_NUMBER)
    logger.info('secret number = %s', str(secret_number))
    if secret_number is not None:
        return jsonify({"secret_number": secret_number})
    else:
        return "Failed to fetch the secret number", 500
