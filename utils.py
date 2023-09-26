import logging
from pathlib import Path

def get_logger(logger_name: str,
               level: int = logging.INFO,
               log_file: str = 'log.log'):

    path_to_logs = Path("logs")
    path_to_logs.mkdir(parents=True, exist_ok=True)
    filename = path_to_logs / f"{log_file}.log"

    logger = logging.getLogger(name=logger_name)
    logger.setLevel(level=level)
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        fmt="%(levelname)-8s [%(asctime)s] %(name)s:%(lineno)d: %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(filename=filename)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
