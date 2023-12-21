import loguru


class _Logger:

    def __init__(self, level='INFO', format='{message}'):
        self.logger = loguru.logger
        self.level = level
        self.format = format
        loguru.logger.add(sink="stdout", level=self.level, format=self.format)

    @staticmethod
    def save(file='sudocr'):
        loguru.logger.add(f"../logs/{file}.log", rotation="1 week", compression="zip")


log_level = 'INFO'
logger = _Logger(log_level).logger
