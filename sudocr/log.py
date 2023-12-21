import sys

import loguru


class _Logger:

    def __init__(self, level='INFO', format='{message}', save_log=False, file='sudocr'):
        self.logger = loguru.logger
        self.level = level
        self.format = format
        loguru.logger.add(sys.stdout, level=self.level, format=self.format)
        if save_log:
            self.save(file=file)

    @staticmethod
    def save(file):
        loguru.logger.add(f"../logs/{file}.log", rotation="1 week", compression="zip")


log_level = 'INFO'
logger = _Logger(log_level).logger
