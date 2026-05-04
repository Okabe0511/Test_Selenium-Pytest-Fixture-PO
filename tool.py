import logging
import os
from datetime import datetime
from config import LOG_DIR, SCREENSHOT_DIR


class Logger:
    _instance = None

    def __new__(cls, name='WebAutoTest'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, name='WebAutoTest'):
        if self._initialized:
            return
        self._initialized = True

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        log_file = os.path.join(
            LOG_DIR,
            f'test_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        )

        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


def take_screenshot(driver, name=None):
    if name is None:
        name = datetime.now().strftime('%Y%m%d_%H%M%S')
    filepath = os.path.join(SCREENSHOT_DIR, f'{name}.png')
    driver.save_screenshot(filepath)
    return filepath
