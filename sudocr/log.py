from loguru import logger


class Logger:

    def __init__(self):
        logger.add(sink="stdout", level="INFO", format="{message}")

    @staticmethod
    def save(file='sudocr'):
        logger.add(f"../log/{file}.log", level="DEBUG", rotation="1 week", compression="zip")
