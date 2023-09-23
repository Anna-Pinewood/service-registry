import logging
import sys
from pathlib import Path

def get_logger(
        logger_name: str | None = None,
        path: Path | None = None,
        level: int = logging.DEBUG,
        add_stdout: bool = False) -> logging.Logger:
    """
    Get logger with file handler
    Parameters
    ----------
    logger_name: str|None
        Name of logger
    path: Path|None
        Path to log file
    level: int
        Level of logger
    add_stdout: bool
        if true logger will print to stdout too
    """
    logger_name = "logs" if logger_name is None else logger_name
    path_to_logs = Path("logs") if path is None else Path(path)
    path_to_logs.mkdir(parents=True, exist_ok=True)
    filename = path_to_logs / f"{logger_name}.log"
    print(f'Log file path: {filename.absolute()}')

    # create formatter with level name, module, line number, time and message
    formatter = logging.Formatter(
        "%(levelname)-8s [%(asctime)s] %(name)s:%(lineno)d: %(message)s"
    )

    # create file handler
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # create logger
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.setLevel(level)
    if add_stdout:
        # create stdout handler
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(level)
        stdout_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)
    return logger