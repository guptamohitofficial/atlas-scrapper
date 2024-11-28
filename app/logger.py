import logging
import config as settings


def setup_logging():
    log_level = logging.DEBUG
    if settings.LOGGER_LEVEL == "info":
        log_level = logging.INFO
    elif settings.LOGGER_LEVEL == "error":
        log_level = logging.ERROR
    elif settings.LOGGER_LEVEL == "warning":
        log_level = logging.WARNING
    elif settings.LOGGER_LEVEL == "debug":
        log_level = logging.DEBUG

    logger = logging.getLogger("atlas-scrapper")
    logger.setLevel(log_level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    file_handler = logging.FileHandler("atlas-scrapper.log")
    file_handler.setLevel(log_level)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


log = setup_logging()
