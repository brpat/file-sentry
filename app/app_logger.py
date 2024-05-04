import os
import re
import logging
from logging.handlers import TimedRotatingFileHandler

class AppLogger:
    def __init__(self, log_path: str):
        self.log_path = log_path
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        self.make_log_directory()
        handler = logging.FileHandler(self.log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger

    def log_event(self, message: str) -> None:
        self.logger.info(message)
        
    def log_eror(self, message: str) -> None:
        self.logger.error(message)

    def make_log_directory(self) -> None:
        if not os.path.exists(os.path.dirname(self.log_path)):
            os.makedirs(os.path.dirname(self.log_path))

    @staticmethod
    def rotate_logs(path: str):
        handler = TimedRotatingFileHandler(path, when="midnight", interval=1)
        handler.suffix = "%Y-%m-%d"
        handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}$")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger = logging.getLogger(__name__)
        logger.addHandler(handler)
