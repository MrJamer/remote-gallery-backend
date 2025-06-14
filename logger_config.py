import logging
import json
import os
from logging.handlers import RotatingFileHandler

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "message": record.getMessage(),
            "timestamp": self.formatTime(record, "%Y-%m-%d %H:%M:%S"),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        return json.dumps(log_record, ensure_ascii=False, indent=2)

def setup_logger(log_file='logs/app.log'):
    logger = logging.getLogger("image-gallery")
    logger.setLevel(logging.INFO)

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    if logger.hasHandlers():
        logger.handlers.clear()

    handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
    handler.setFormatter(JsonFormatter())

    logger.addHandler(handler)
    return logger
