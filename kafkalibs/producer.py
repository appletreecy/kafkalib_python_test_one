from kafka import KafkaProducer
import json
from .config import KAFKA_BROKER_URL
from .logger import logger
from .metrics import producer_success_counter, producer_failure_counter

class KafkaJSONProducer:
    def __init__(self, topic):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER_URL,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def send(self, message: dict):
        try:
            future = self.producer.send(self.topic, value=message)
            future.get(timeout=10)
            logger.info(f"Produced message: {message}")
            producer_success_counter.inc()
        except Exception as e:
            logger.error(f"Error producing message: {e}")
            producer_failure_counter.inc()

    def close(self):
        self.producer.flush()
        self.producer.close()
