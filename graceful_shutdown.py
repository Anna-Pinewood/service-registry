import logging
import os
import sys
import signal
import threading
import time
from patient_account.consts import SERVICE_NAME
from patient_account.service_discover import unregister

from utils import get_logger

logger = get_logger(__name__,
                    level=logging.INFO)


def exit_app():
    logger.info('Killing %s in 15 sec...', str(os.getpid()))
    time.sleep(15)
    os.kill(os.getpid(), signal.SIGKILL)


def signal_handler(signal, frame):
    """SIGTERM and SIGINT handlers."""
    logger.info('Got signal %s. Graceful shutdown...', str(signal))
    unregister(service_name=SERVICE_NAME)
    thread_exit = threading.Thread(target=exit_app)
    thread_exit.start()
