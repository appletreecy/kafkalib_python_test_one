from kafka import KafkaConsumer
import json
from .config import KAFKA_BROKER_URL
from .logger import logger
from .metrics import consumer_success_counter, consumer_failure_counter

class KafkaJSONConsumer:
    def __init__(self, topic, group_id):
        self.topic = topic
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=KAFKA_BROKER_URL,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )

    def consume(self, process_func):
        logger.info(f"Consuming from {self.topic}...")
        try:
            for msg in self.consumer:
                logger.info(f"Received: {msg.value}")
                try:
                    process_func(msg.value)
                    consumer_success_counter.inc()
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    consumer_failure_counter.inc()
        except Exception as e:
            logger.error(f"Fatal consumer error: {e}")
