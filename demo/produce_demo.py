from kafkalibs.producer import KafkaJSONProducer
import time

producer = KafkaJSONProducer("demo-topic")

for i in range(5000):
    producer.send({"event": f"hello {i}"})
    time.sleep(1)

producer.close()
