from loguru import logger
logger.add("kafka.log", rotation="1 MB")
